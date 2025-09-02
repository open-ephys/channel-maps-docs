
===================================================================================================
{{ hs.Name }}
===================================================================================================

..  rubric:: {{ hs.SKU }}
    :class: sku-rubric
    :heading-level: 4

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

    {% if sku == 'OEPS-6573' %}
    {{ hs.SKU }} Accelerometer axes
    {% else %}
    {{ hs.SKU }} IMU axes
    {% endif %}

.. Add this section when pictures and channel maps are done

.. {{ hs.SKU }} EIB Combination
.. -----------------------------

.. (..  csv-table::)
    :widths: 15, 50

    "**Compatible EIB**", "OEPS-6809 ShuttleDrive 32-ch Omnetics EIB"

.. ..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_OEPS-6809_mounting.jpg
    :align: center
    :width: 100%

    {{ hs.SKU }} EIB combination mounting

.. ..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_OEPS-6809_channel_map.jpg
    :align: center
    :width: 70%

    {{ hs.SKU }} EIB combination channel map

{{ hs.SKU }} EIB Combination
-----------------------------

.. ..  csv-table::
..     :widths: 15, 50

..     "**Compatible EIB**", "OEPS-6813 ShuttleDrive 64-ch Hirose EIB"

.. ..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_OEPS-6813_mounting.jpg
..     :align: center
..     :width: 100%

..     {{ hs.SKU }} EIB combination mounting

.. ..  figure:: /_static/images/{{ hs.SKU }}/eib/{{ hs.SKU }}_OEPS-6813_channel_map.jpg
..     :align: center
..     :width: 70%

..     {{ hs.SKU }} EIB combination channel map

{% if sku == 'OEPS-7741' %}
.. dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/eib/OEPS-7741_OEPS-6813_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        {{ hs.SKU }} EIB combination channel map

{% endif %}


{{ hs.SKU }} Adapter Combination
-----------------------------

.. ..  csv-table::
..     :widths: 15, 50

..     "**Compatible Adapter**", "OEPS-7200 Adapter Hirose to Omnetics 64ch"

.. ..  figure:: /_static/images/{{ hs.SKU }}/adp/{{ hs.SKU }}_OEPS-7200_mounting.jpg
..     :align: center
..     :width: 100%

..     {{ hs.SKU }} EIB combination mounting

.. ..  figure:: /_static/images/{{ hs.SKU }}/adp/{{ hs.SKU }}_OEPS-7200_channel_map.jpg
..     :align: center
..     :width: 70%

..     {{ hs.SKU }} Adapter combination channel map

{% if sku == 'OEPS-7741' %}
..  dropdown:: Channel map if your data were acquired using up to version 0.4.5 of the OpenEphys.Onix1 library

    ..  figure:: /_static/images/OEPS-7741/adp/OEPS-7741_OEPS-7200_channel_map_v0.4.5.jpg
        :align: center
        :width: 70%

        {{ hs.SKU }} Adapter combination channel map

{% endif %}

Other combinations
------------------

To construct other channel maps, take a look at the channel mapping table and connector pinout.

..  raw:: html

    <center><div style="margin-top: 50px;"><iframe width="800" height="1200" scrolling='yes' src="https://docs.google.com/spreadsheets/d/1WYDymxNqGRtFPxn69H9JzeMgePpXcFSPHiWJYBE0lu4/edit?gid=0#gid=0"></iframe></div></center>
