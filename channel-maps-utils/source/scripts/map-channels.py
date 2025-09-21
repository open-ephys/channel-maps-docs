import os, json, pathlib
from collections import defaultdict, namedtuple
from itertools import combinations
import pandas as pd

# Data structures
CSVInfo = namedtuple('CSVInfo', ['name', 'type', 'df', 'connectors'])
Connection = namedtuple('Connection', ['source', 'target', 'connector_pair'])
IntermediaryConnection = namedtuple('IntermediaryConnection', ['source', 'adapter', 'target', 'path'])

class ConnectorGraph:
    """Graph representing connector relationships."""
    
    def __init__(self, connector_pairs):
        self.pairs = set()
        self.adjacency = defaultdict(set)
        
        for pair_group in connector_pairs:
            if len(pair_group) == 2:
                conn1, conn2 = [list(info.keys())[0] for info in pair_group]
                self.pairs.add((conn1, conn2))
                self.adjacency[conn1].add(conn2)
                self.adjacency[conn2].add(conn1)
    
    def can_pair(self, conn1, conn2):
        return (conn1, conn2) in self.pairs or (conn2, conn1) in self.pairs
    
    def get_partners(self, connector):
        return self.adjacency[connector]

class CSVManager:
    """Manages CSV files and their metadata."""
    
    VALID_COMBINATIONS = {
        ('headstage', 'eib'),
        ('headstage', 'adapter'), 
        ('adapter', 'eib'),
        ('headstage', 'adapter', 'eib')
    }
    
    def __init__(self, directories):
        self.csvs = {}
        self.by_type = defaultdict(dict)
        self._load_csvs(directories)
    
    def _load_csvs(self, directories):
        for csv_type, directory in directories.items():
            path = pathlib.Path(directory)
            if not path.exists():
                continue
                
            for csv_file in path.glob("*.csv"):
                try:
                    df = pd.read_csv(csv_file, dtype="string")
                    df.columns = df.columns.str.strip()
                    
                    csv_info = CSVInfo(
                        name=csv_file.stem,
                        type=csv_type.rstrip('s'),  # remove plural
                        df=df,
                        connectors=set(df.columns)
                    )
                    
                    self.csvs[csv_info.name] = csv_info
                    self.by_type[csv_info.type][csv_info.name] = csv_info
                    
                except Exception as e:
                    print(f"Error reading {csv_file}: {e}")
    
    def is_valid_combination(self, *types):
        return tuple(types) in self.VALID_COMBINATIONS

class ConnectionFinder:
    """Finds valid connections between CSVs."""
    
    def __init__(self, csv_manager, connector_graph):
        self.csvs = csv_manager
        self.graph = connector_graph
    
    def find_direct_connections(self):
        """Find direct connections between CSV pairs."""
        connections = []
        
        for conn1, conn2 in self.graph.pairs:
            # Find CSVs containing each connector
            csvs_with_conn1 = {name: csv for name, csv in self.csvs.csvs.items() if conn1 in csv.connectors}
            csvs_with_conn2 = {name: csv for name, csv in self.csvs.csvs.items() if conn2 in csv.connectors}
            
            # Create valid connections
            for csv1 in csvs_with_conn1.values():
                for csv2 in csvs_with_conn2.values():
                    if (csv1.name != csv2.name and self.csvs.is_valid_combination(csv1.type, csv2.type)):
                        connections.append(Connection(
                            source=(csv1, conn1),
                            target=(csv2, conn2),
                            connector_pair=(conn1, conn2)
                        ))
        
        return connections
    
    def find_intermediary_connections(self):
        """Find connections through adapter CSVs."""
        connections = []
        
        for adapter in self.csvs.by_type['adapter'].values():
            # Get all connector pairs on this adapter
            adapter_connectors = adapter.connectors & set(self.graph.adjacency.keys())
            
            for conn1, conn2 in combinations(adapter_connectors, 2):
                # Find headstages and EIBs that can connect to these connectors
                headstage_partners = self._find_partners('headstage', conn1, conn2)
                eib_partners = self._find_partners('eib', conn1, conn2)
                
                # Create connections in both directions
                for direction in [(conn1, conn2), (conn2, conn1)]:
                    ac1, ac2 = direction
                    
                    for hs_csv, hs_conn in headstage_partners.get(ac1, []):
                        for eib_csv, eib_conn in eib_partners.get(ac2, []):
                            if hs_csv.name != eib_csv.name:
                                connections.append(IntermediaryConnection(
                                    source=(hs_csv, hs_conn),
                                    adapter=(adapter, ac1, ac2),
                                    target=(eib_csv, eib_conn),
                                    path=f"{hs_csv.name}({hs_conn}) → {adapter.name}({ac1}-{ac2}) → {eib_csv.name}({eib_conn})"
                                ))
        
        return connections
    
    def _find_partners(self, csv_type, conn1, conn2):
        """Find CSVs of given type that can pair with connector."""
        partners = defaultdict(list)
        
        for csv in self.csvs.by_type[csv_type].values():
            for connector in csv.connectors:
                if connector in self.graph.get_partners(conn1):
                    partners[conn1].append((csv, connector))
                if connector in self.graph.get_partners(conn2):
                    partners[conn2].append((csv, connector))
        
        return partners

class DataJoiner:
    """Handles joining operations."""
    
    @staticmethod
    def join_direct(connection):
        """Perform direct join between two CSVs."""
        (csv1, conn1), (csv2, conn2) = connection.source, connection.target
        
        try:
            result = pd.merge(
                csv1.df, csv2.df,
                left_on=conn1, right_on=conn2,
                how='outer',
                suffixes=(f'_{csv1.name}', f'_{csv2.name}')
            ).drop(columns=[conn1, conn2]).T.reset_index(drop=True)
            
            return {
                'type': 'direct',
                'sources': [csv1.name, csv2.name],
                'types': [csv1.type, csv2.type],
                'connectors': [conn1, conn2],
                'data': result
            }
        except Exception as e:
            print(f"Error in direct join: {e}")
            return None
    
    @staticmethod
    def join_intermediary(connection):
        """Perform intermediary join through adapter."""
        (hs_csv, hs_conn) = connection.source
        (adapter, ac1, ac2) = connection.adapter  
        (eib_csv, eib_conn) = connection.target
        
        try:
            # Two-step join
            temp = pd.merge(
                hs_csv.df, adapter.df,
                left_on=hs_conn, right_on=ac1,
                how='inner'
            ).drop(columns=[hs_conn, ac1])
            
            if len(temp) == 0:
                return None
            
            result = pd.merge(
                temp, eib_csv.df,
                left_on=ac2, right_on=eib_conn,
                how='inner'
            ).drop(columns=[ac2, eib_conn]).T.reset_index(drop=True)
            
            if len(result) == 0:
                return None
            
            return {
                'type': 'intermediary',
                'sources': [hs_csv.name, adapter.name, eib_csv.name],
                'types': [hs_csv.type, adapter.type, eib_csv.type],
                'path': connection.path,
                'data': result
            }
        except Exception as e:
            print(f"Error in intermediary join: {e}")
            return None

def main():
    """Main execution function."""
    print("=== CSV Connector Pairing Tool ===\n")
    
    script_dir = pathlib.Path(__file__).parent.resolve()
    directories = {
        'adapters': script_dir / "../assets/adapters",
        'eibs': script_dir / "../assets/eibs",
        'headstages': script_dir / "../assets/headstages"
    }
    
    # Load connector pairs
    try:
        with open(script_dir / "../assets/connector-pairs.json") as f:
            connector_pairs = json.load(f)
    except Exception as e:
        print(f"Error loading connector pairs: {e}")
        return
    
    # Initialize components
    csv_manager = CSVManager(directories)
    connector_graph = ConnectorGraph(connector_pairs)
    finder = ConnectionFinder(csv_manager, connector_graph)
    
    print(f"Loaded {len(csv_manager.csvs)} CSVs")
    print(f"Built connector graph with {len(connector_graph.pairs)} pairs")
    
    # Find connections
    direct_connections = finder.find_direct_connections()
    intermediary_connections = finder.find_intermediary_connections()
    
    print(f"Found {len(direct_connections)} direct connections")
    print(f"Found {len(intermediary_connections)} intermediary connections")
    
    if not (direct_connections or intermediary_connections):
        print("No valid connections found!")
        return
    
    # Process connections
    results = []
    
    # Process direct connections
    for conn in direct_connections:
        result = DataJoiner.join_direct(conn)
        if result:
            results.append(result)
    
    # Process intermediary connections
    for conn in intermediary_connections:
        result = DataJoiner.join_intermediary(conn)
        if result:
            results.append(result)
    
    # Save results
    output_dir = script_dir / "../../output"
    output_dir.mkdir(exist_ok=True)
    
    for result in results:
        if result['type'] == 'direct':
            filename = f"{result['sources'][0]}_{result['sources'][1]}.csv"
            print(f"DIRECT ({'+'.join(result['types'])}): {result['data'].shape}")
        else:
            filename = f"{result['sources'][0]}_{result['sources'][1]}_{result['sources'][2]}.csv"
            print(f"INTERMEDIARY: {result['path']} - {result['data'].shape}")
        
        result['data'].to_csv(output_dir / filename, index=False, header=False)
    
    print(f"\nProcessed {len(results)} connections successfully")

if __name__ == "__main__":
    main()