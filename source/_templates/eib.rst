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

    Connector pinout.
{% endif %}