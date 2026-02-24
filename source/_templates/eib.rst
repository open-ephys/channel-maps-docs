===================================================================================================
{{ eib.Name }}
===================================================================================================

..  figure:: /_static/images/{{ eib.SKU }}/eib/{{ eib.SKU }}.jpg
    :align: center
    :width: 60%

    {{ eib.SKU }}

..  csv-table::
    :widths: 15, 50
    {% for key, value in eib.Chart.items() %}
    "**{{ key }}**", "{{ value }}"{% endfor %}

{% if eib.Pinout is defined %}
..  figure:: /_static/images/{{ eib.SKU }}/eib/{{ eib.SKU }}_connector_pinout.jpg
    :align: center
    :width: 70%

    Connector pinout (pins).
{% endif %}

{% if eib.Pinout is defined %}
..  figure:: /_static/images/{{ eib.SKU }}/eib/{{ eib.SKU }}_connector_map.jpg
    :align: center
    :width: 70%

    Connector pinout (vias).
{% endif %}

{% if eib.Headstages is defined and eib.Headstages|length > 0 %}

Compatible Headstages
-------------------------
{% for hs in eib.Headstages %}
-   {{ hs.Name }} ({{ hs.SKU }})
{% endfor %}
{% endif %}