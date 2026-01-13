
===================================================================================================
{{ hs.Name }}
===================================================================================================

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_main.jpg
    :align: center
    :width: 60%

    {{ hs.SKU }}

..  csv-table::
    :widths: 15, 50
    {% for key, value in hs.Chart.items() %}
    "**{{ key }}**", "{{ value }}"{% endfor %}

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_channel_map.jpg
    :align: center
    :width: 70%

    Channel map. For Open Ephys GUI channel numbers, add 1.

{% if hs.SKU == 'OEPS-7741' %}
.. dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    .. figure:: /_static/images/OEPS-7741/main/OEPS-7741_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        Channel map. For Open Ephys GUI channel number, add 1.
{% endif %}

..  figure:: /_static/images/{{ hs.SKU }}/main/{{ hs.SKU }}_axes.jpg
    :align: center
    :width: 70%

    {{ hs['3D'] }} axes

.. Add this section when pictures and channel maps are done

{% if hs.EIBs is defined and hs.EIBs|length > 0 %}

Compatible EIBs
------------------------------------------------------------------------

{% for eib in hs.EIBs %} 
-   {{ eib.Name }} ({{ eib.SKU }}) {% endfor %}

{% for eib in hs.EIBs %} 

{{ eib.Name }}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_{{ eib.SKU }}_mounting.jpg
    :align: center
    :width: 100%

    EIB combination mounting 

..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_{{ eib.SKU }}_channel_map.jpg
    :align: center
    :width: 70%

    EIB combination channel map

{% endfor %}

{% if sku == 'OEPS-7741' %}
.. dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/eib/OEPS-7741_OEPS-6813_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        EIB combination channel map
{% endif %}

{% endif %}

{% if hs.Adapters is defined and hs.Adapters|length > 0 %}

Adapter Combinations
--------------------------------------------------------------------------------------

Compatible Adapters:
{% for adapter in hs.Adapters %} 
-   {{ adapter.Name }} {% endfor %} 

{% for adapter in hs.Adapters %} 

{{ adapter.Name }}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  figure:: /_static/images/{{ hs.SKU }}/adapter/{{ hs.SKU }}_{{ adapter.SKU }}_mounting.jpg
    :align: center
    :width: 100%

    Adapter combination mounting 

..  figure:: /_static/images/{{ hs.SKU }}/adapter/{{ hs.SKU }}_{{ adapter.SKU }}_channel_map.jpg
    :align: center
    :width: 70%

    Adapter combination channel map

{% endfor %} 

{% if sku == 'OEPS-7741' %}
..  dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/adp/OEPS-7741_OEPS-7200_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        Adapter combination channel map
{% endif %}

{% endif %}

Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/1WYDymxNqGRtFPxn69H9JzeMgePpXcFSPHiWJYBE0lu4/edit?gid=0#gid=0"></iframe></div></center>
