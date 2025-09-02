
===================================================================================================
{{ hs.Name }} ({{ hs.SKU }})
===================================================================================================

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_main.jpg
    :align: center
    :width: 60%

..  csv-table::
    :widths: 15, 50
    {% for key, value in hs.Chart.items() %}
    "**{{ key }}**", "{{ value }}"{% endfor %}

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_channel_map.jpg
    :align: center
    :width: 70%

    {{ hs.SKU }} Channel map. For Open Ephys GUI channel numbers, add 1.

{% if sku == 'OEPS-7741' %}
.. dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    .. figure:: /_static/images/OEPS-7741/main/OEPS-7741_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        {{ hs.SKU }} Channel map. For Open Ephys GUI channel number, add 1.
{% endif %}

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_axes.jpg
    :align: center
    :width: 70%

    {{ hs['3D'] }} axes

.. Add this section when pictures and channel maps are done

{% if hs.EIBs is defined and hs.EIBs|length > 0 %}

{{ hs.SKU }} EIB Combinations
------------------------------------------------------------------------

Compatible EIBs:
{% for eib in hs.EIBs %} {% for eib_sku, eib_name in eib.items() %}
-   {{ eib_name }} ({{ eib_sku }}) {% endfor %} {% endfor %}

{% for eib in hs.EIBs %} {% for eib_sku, eib_name in eib.items() %}

{{ eib_name }} ({{ eib_sku }})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_{{ eib_sku }}_mounting.jpg
    :align: center
    :width: 100%

    {{ hs.SKU }} {{ eib_sku }} combination mounting 

..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_{{ eib_sku }}_channel_map.jpg
    :align: center
    :width: 70%

    {{ hs.SKU }} {{ eib_sku }} combination channel map

{% endfor %} {% endfor %}

{% if sku == 'OEPS-7741' %}
.. dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/eib/OEPS-7741_OEPS-6813_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        {{ hs.SKU }} {{ eib_sku }} combination channel map
{% endif %}

{% endif %}

{% if hs.Adapters is defined and hs.Adapters|length > 0 %}

{{ hs.SKU }} Adapter Combination
--------------------------------------------------------------------------------------

Compatible Adapters:
{% for adapter in hs.Adapters %} {% for adapter_sku, adapter_name in adapter.items() %}
-   {{ adapter_name }} ({{ adapter_sku }}) {% endfor %} {% endfor %}

{% for adapter in hs.Adapters %} {% for adapter_sku, adapter_name in adapter.items() %}

{{ adapter_name }} ({{ adapter_sku }})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  figure:: /_static/images/{{ hs.SKU }}/adapter/{{ hs.SKU }}_{{ adapter_sku }}_mounting.jpg
    :align: center
    :width: 100%

    {{ hs.SKU }} {{ adapter_sku }} combination mounting 

..  figure:: /_static/images/{{ hs.SKU }}/adapter/{{ hs.SKU }}_{{ adapter_sku }}_channel_map.jpg
    :align: center
    :width: 70%

    {{ hs.SKU }} {{ adapter_sku }} combination channel map

{% endfor %} {% endfor %}

{% if sku == 'OEPS-7741' %}
..  dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/adp/OEPS-7741_OEPS-7200_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        {{ hs.SKU }} Adapter combination channel map
{% endif %}

{% endif %}

Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/1WYDymxNqGRtFPxn69H9JzeMgePpXcFSPHiWJYBE0lu4/edit?gid=0#gid=0"></iframe></div></center>
