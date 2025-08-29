
{{ sku }}
=========

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_main.jpg
    :align: center
    :width: 60%

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

    {{ sku }} Channel map. For Open Ephys GUI channel numbers, add 1.

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_axes.jpg
    :align: center
    :width: 70%

    {% if sku == 'OEPS-6574' %}
    {{ sku }} Accelerometer axes
    {% else %}
    {{ sku }} IMU axes
    {% endif %}


Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/1WYDymxNqGRtFPxn69H9JzeMgePpXcFSPHiWJYBE0lu4/edit?gid=0#gid=0"></iframe></div></center>
