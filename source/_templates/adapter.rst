===================================================================================================
{{ adapter.Name }}
===================================================================================================

..  figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}.jpg
    :align: center
    :width: 60%

    {{ adapter.SKU }}

..  csv-table::
    :widths: 15, 50
    {% for key, value in adapter.Chart.items() %}
    "**{{ key }}**", "{{ value }}"{% endfor %}

{% for eib in adapter.EIBs %} 

{{ eib.Name }}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}_{{ eib.SKU }}_mounting.jpg
    :align: center
    :width: 100%

    EIB combination mounting
{% endfor%}

{% if adapter.SKU == 'OEPS-6820' %}
.. figure:: /_static/images/OEPS-6820/adapter/OEPS-6820_connector_map.jpg
        :align: center
        :width: 70%

        EIB combination channel map on Nanoz GUI
{% endif %}

{% if adapter.Pinout is defined %}
..  figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}_connector_pinout.jpg
    :align: center
    :width: 70%

    Connector pinout (pins)
{% endif %}

{% if adapter.Pinout is defined and adapter.SKU != 'OEPS-6820' %}
.. figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}_connector_map.jpg
    :align: center
    :width: 70%

    Connector pinout (vias)
{% endif %}

{% if adapter.Headstages is defined and adapter.Headstages|length > 0 %}

Compatible Headstages
-------------------------
{% for hs in adapter.Headstages %}
-   {{ hs.Name }} ({{ hs.SKU }})
{% endfor %}
{% endif %}