#!/usr/bin/env python3
"""
CSV Connector Mapping Graph Generator and Data Joiner (Functional Version)
"""

import argparse
import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import pandas as pd
from pathlib import Path

DIRS = ("headstages", "adapters", "eibs")
COLORS = {"headstages": "#ef4444", "adapters": "#3b82f6", "eibs": "#10b981"}
VALID_CONNECTIONS = {("headstages", "adapters"),
                     ("headstages", "eibs"),
                     ("adapters", "eibs")}

def load_csv_files(mappings_dir: Path):
    csv_files = []
    for subdir in DIRS:
        for csv in (mappings_dir / subdir).glob("*.csv"):
            try:
                df = pd.read_csv(csv, dtype=str)
                if df.shape[1] >= 2:
                    csv_files.append({
                        "id": f"{subdir}-{csv.stem}",
                        "filename": csv.name,
                        "directory": subdir,
                        "connectors": df.columns[:2].str.strip().tolist(),
                        "df": df,
                    })
            except Exception as e:
                print(f"Error loading {csv}: {e}")
    print(f"Loaded {len(csv_files)} CSV files")
    return csv_files

def can_connect(f1, f2, connector_pairs):
    dirs = (f1["directory"], f2["directory"])
    if dirs not in VALID_CONNECTIONS and dirs[::-1] not in VALID_CONNECTIONS:
        return None
    for c1 in f1["connectors"]:
        for c2 in f2["connectors"]:
            if any(c1 in d1 and c2 in d2
                for pair in connector_pairs if len(pair) >= 2
                for i, d1 in enumerate(pair) for j, d2 in enumerate(pair) if i != j):
                    return {"conn1": c1, "conn2": c2}
    return None

def build_graph(csv_files, connector_pairs):
    g = nx.Graph()
    for f in csv_files:
        g.add_node(f["id"], **f, color=COLORS[f["directory"]])
    for i, f1 in enumerate(csv_files):
        for f2 in csv_files[i + 1:]:
            if conn := can_connect(f1, f2, connector_pairs):
                g.add_edge(f1["id"], f2["id"], **conn)
    print(f"Graph built: {g.number_of_nodes()} nodes, {g.number_of_edges()} edges")
    return g

def find_paths(g):
    paths = [{"type": "direct", "nodes": [u, v], "connectors": [d["conn1"], d["conn2"]]}
             for u, v, d in g.edges(data=True)]

    for node, data in g.nodes(data=True):
        if data["directory"] != "adapters":
            continue
        neighbors = list(g.neighbors(node))
        for i, n1 in enumerate(neighbors):
            for n2 in neighbors[i + 1:]:
                dirs = {g.nodes[n1]["directory"], g.nodes[n2]["directory"]}
                if dirs == {"headstages", "eibs"}:
                    e1, e2 = g.edges[n1, node], g.edges[node, n2]
                    paths.append({
                        "type": "intermediary",
                        "nodes": [n1, node, n2],
                        "connectors": [e1["conn1"], e1["conn2"], e2["conn1"], e2["conn2"]],
                    })
    return paths

def join_path(g, path):
    try:
        if path["type"] == "direct":
            n1, n2 = path["nodes"]
            c1, c2 = path["connectors"]
            df = pd.merge(g.nodes[n1]["df"], g.nodes[n2]["df"],
                          left_on=c1, right_on=c2, how="outer",
                          suffixes=(f"_{g.nodes[n1]['filename'][:-4]}",
                                    f"_{g.nodes[n2]['filename'][:-4]}"))
            df.drop(columns=[c for c in (c1, c2) if c in df], inplace=True)
            return {"type": "direct",
                    "sources": [g.nodes[n1]["filename"][:-4], g.nodes[n2]["filename"][:-4]],
                    "data": df}

        n1, mid, n2 = path["nodes"]
        c1, mc1, mc2, c2 = path["connectors"]
        tmp = pd.merge(g.nodes[n1]["df"], g.nodes[mid]["df"],
                       left_on=c1, right_on=mc1, how="inner")
        df = pd.merge(tmp, g.nodes[n2]["df"], left_on=mc2, right_on=c2, how="inner")
        df.drop(columns=[c1, mc1, mc2, c2], inplace=True, errors="ignore")
        return {"type": "intermediary",
                "sources": [g.nodes[n1]["filename"][:-4],
                            g.nodes[mid]["filename"][:-4],
                            g.nodes[n2]["filename"][:-4]],
                "data": df}
    except Exception as e:
        print(f"Join error: {e}")
        return None

def perform_joins(g, out_dir="output"):
    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    results = []
    for path in find_paths(g):
        if (res := join_path(g, path)) is not None:
            fname = f"{'_'.join(res['sources'])}.csv"
            res["data"].T.reset_index(drop=True).to_csv(out / fname, index=False, header=False)
            results.append(res)
            print(f"Created: {fname} ({res['data'].shape[0]} rows, {res['data'].shape[1]} cols)")
    return results

def layout(g):
    y = {"headstages": 2.0, "adapters": 0.0, "eibs": -2.0}
    pos = {}
    for d in DIRS:
        nodes = [n for n, data in g.nodes(data=True) if data["directory"] == d]
        xs = [i * 3.0 - (len(nodes) - 1) * 1.5 for i in range(len(nodes))]
        for node, x in zip(nodes, xs):
            pos[node] = (x, y[d])
    return pos

def visualize(g, save=None):
    pos = layout(g)
    plt.figure(figsize=(12, 10))
    for d, color in COLORS.items():
        nx.draw_networkx_nodes(g, pos,
                               nodelist=[n for n, data in g.nodes(data=True) if data["directory"] == d],
                               node_color=color, node_size=6000, alpha=0.8)
    nx.draw_networkx_edges(g, pos, edge_color="#64748b", width=2, alpha=0.6)
    nx.draw_networkx_labels(g, pos,
                            labels={n: data["filename"][:-4] for n, data in g.nodes(data=True)},
                            font_size=11, font_weight="bold", font_color="white")
    for d, y in {"headstages": 2, "adapters": 0, "eibs": -2}.items():
        plt.text(-0.5, y, d.title(), fontsize=12, fontweight="bold",
                 ha="right", va="center", color=COLORS[d])
    legend_elements = [mpatches.Patch(color=c, label=d.title()) for d, c in COLORS.items()]
    plt.legend(handles=legend_elements, loc="upper right")
    plt.title("CSV Connector Mapping Graph", fontsize=16, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    if save:
        plt.savefig(save, dpi=300, bbox_inches="tight")
        print(f"Graph saved to {save}")
    plt.show()

def main():
    p = argparse.ArgumentParser(description="Generate CSV connector mapping graph and perform data joins")
    p.add_argument("--mappings_dir", required=True)
    p.add_argument("--pairs_file", required=True)
    p.add_argument("--output_image")
    p.add_argument("--output_dir", default="output")
    p.add_argument("--skip_viz", action="store_true")
    args = p.parse_args()

    try:
        connector_pairs = json.loads(Path(args.pairs_file).read_text())
        print(f"Loaded {len(connector_pairs)} connector pairs")
        csv_files = load_csv_files(Path(args.mappings_dir))
        g = build_graph(csv_files, connector_pairs)
        if not args.skip_viz:
            visualize(g, args.output_image)
        print("\nPerforming data joins...")
        results = perform_joins(g, args.output_dir)
        print(f"\nCompleted: {len(results)} CSVs → {args.output_dir}")
        print(f"  - {sum(r['type']=='direct' for r in results)} direct")
        print(f"  - {sum(r['type']=='intermediary' for r in results)} intermediary")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
