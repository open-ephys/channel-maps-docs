{% if template_type == 'headstage' %} 
    {% include 'hs.rst' %} 
{% endif %}

{% if template_type == 'adapter' %} 
    {% include 'adapter.rst' %} 
{% endif %}

{% if template_type == 'eib' %} 
    {% include 'eib.rst' %} 
{% endif %}