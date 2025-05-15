
{{ sku }}
=============================================================

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_main.jpg
    :align: center
    :width: 60%
    :alt: {{ sku }} ONIX Headstage Ephys 64ch (opto and curr. stim)

..   csv-table::
    :widths: 20, 80

    {% if hs_data[sku]['acquisition_system'] %}
        "*Acquisition System*", "{{ hs_data[sku]['acquisition_system'] }}"
    {% endif %}
    "*Dimensions*", "{{ hs_data[sku]['dimensions'] }}"
    "*Weight*", "{{ hs_data[sku]['mass'] }}"
    "*Connector*", "{{ hs_data[sku]['probe_connector'] }}"
    "*Operating voltage*", "{{ hs_data[sku]['operating_voltage'] }}"
    "*REF and GND*", "{{ hs_data[sku]['ref_gnd'] }}"
    "*Source Files*", "{{ hs_data[sku]['src_repo'] }}"
    "*Release*", "{{ hs_data[sku]['release'] }}"

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_channel_map.jpg
    :align: center
    :width: 70%
    :alt: {{ sku }} Channel map

    {{ sku }} Channel map. For Open Ephys GUI channel numbers, add 1.

..  figure:: /_static/images/{{ sku }}/main/{{ sku }}_axes.jpg
    :align: center
    :width: 70%
    :alt: {{ sku }} IMU axes

    {{ sku }} IMU axes

{{ sku }} EIB Combination
-----------------------------

..  csv-table::
    :widths: 18, 80

    "*Compatible EIB*", "OEPS-6813 ShuttleDrive 64-ch Hirose EIB"

..  figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6813_mounting.jpg
    :align: center
    :width: 100%
    :alt: {{ sku }} EIB combination mounting

    {{ sku }} EIB combination mounting

..  figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6813_channel_map.jpg
    :align: center
    :width: 70%
    :alt: {{ sku }} EIB combination channel map

    {{ sku }} EIB combination channel map

    {{ sku }} Channel Mapping Tables and Connector Pinout
----------------------------------------------------------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSxEZVG5xytX9CU5a87evB-YSvePfsPWiUGv_nH_SoK7Be4nRgFMId30PxKsUkr2QmLoIl2BF-KabnA/pubhtml?gid=0&single=true"></iframe></center>
