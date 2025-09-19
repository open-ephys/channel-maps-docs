..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_main.jpg
    :align: center
    :width: 60%

    {{ sku }}

..   csv-table::
    :widths: 15, 50

    "**Acquisition System**", "{{ hs_data[sku]['acquisition_system'] }}"
    "**Dimensions**", "{{ hs_data[sku]['dimensions'] }}"
    "**Weight**", "{{ hs_data[sku]['mass'] }}"
    "**Probe connector**", "{{ hs_data[sku]['probe_connector'] }}"
    "**Tether connector**", "{{ hs_data[sku]['tether_connector'] }}"
    "**REF and GND**", "{{ hs_data[sku]['ref_gnd'] }}"
    {%- if hs_data[sku]['mounting_hole'] %}
    "**Structural Opening**", "{{ hs_data[sku]['mounting_hole'] }}"
    {%- endif %}
    "**Source Files**", "{{ hs_data[sku]['src_repo'] }}"
    "**Release**", "{{ hs_data[sku]['release'] }}"

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_channel_map.jpg
    :align: center
    :width: 70%

    Channel map. For Open Ephys GUI channel numbers, add 1.

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_axes.jpg
    :align: center
    :width: 70%

    {% if sku == 'OEPS-6570' %}
    {{ sku }} Accelerometer axes
    {% else %}
    {{ sku }} IMU axes
    {% endif %}

EIB Combination
-----------------------------

..  csv-table::
    :widths: 15, 50

    "**Compatible EIB**", "ShuttleDrive 64-ch Hirose EIB (OEPS-6813)"

..  figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6813_mounting.jpg
    :align: center
    :width: 100%

    EIB combination mounting

..  figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6813_channel_map.jpg
    :align: center
    :width: 70%

    EIB combination channel map

Adapter Combination
-----------------------------

..  csv-table::
    :widths: 15, 50

    "**Compatible Adapter**", "Adapter Hirose to Omnetics 64ch (OEPS-7200)"

..  figure:: /_static/images/{{ sku }}/adp/{{ sku }}_OEPS-7200_mounting.jpg
    :align: center
    :width: 100%

    EIB combination mounting

..  figure:: /_static/images/{{ sku }}/adp/{{ sku }}_OEPS-7200_channel_map.jpg
    :align: center
    :width: 70%

    Adapter combination channel map


Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/1WYDymxNqGRtFPxn69H9JzeMgePpXcFSPHiWJYBE0lu4/edit?gid=0#gid=0"></iframe></div></center>
