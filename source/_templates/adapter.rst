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

{% if adapter.Pinout is defined %}
..  figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}_connector_map.jpg
    :align: center
    :width: 70%

    Connector mapping.
{% endif %}

{% if adapter.Pinout is defined %}
..  figure:: /_static/images/{{ adapter.SKU }}/adapter/{{ adapter.SKU }}_connector_pinout.jpg
    :align: center
    :width: 70%

    Connector pinout.
{% endif %}

{% if adapter.Headstages is defined and adapter.Headstages|length > 0 %}

Compatible Headstages
-------------------------
{% for hs in adapter.Headstages %}
-   {{ hs.Name }} ({{ hs.SKU }})
{% endfor %}
{% endif %}