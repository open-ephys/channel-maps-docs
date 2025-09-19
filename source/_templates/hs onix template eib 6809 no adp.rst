
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
    "**Operating voltage**", "{{ hs_data[sku ]['operating_voltage'] }}"
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

.. Add this section when pictures and channel maps are done

.. {{ sku }} EIB Combination
.. -----------------------------
..
.. .. csv-table::)
..     :widths: 15, 50
..
..     "**Compatible EIB**", "OEPS-6809 ShuttleDrive 32-ch Omnetics EIB"
..
.. .. figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6809_mounting.jpg
..     :align: center
..     :width: 100%
..
..     {{ sku }} EIB combination mounting
..
.. .. figure:: /_static/images/{{ sku }}/eib/{{ sku }}_OEPS-6809_channel_map.jpg
..     :align: center
..     :width: 70%
..
..     {{ sku }} EIB combination channel map

Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSxEZVG5xytX9CU5a87evB-YSvePfsPWiUGv_nH_SoK7Be4nRgFMId30PxKsUkr2QmLoIl2BF-KabnA/pubhtml?widget=true&amp;headers=false&amp;chrome=false"></iframe></div></center>