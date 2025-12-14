{% if include.content contains "" %} <!-- if include.content is string -->
  {% assign text=include.content %}
{% else %}
  {% assign text=include.content[page.lang] | default: include.content.en | default: include.content.ja %}
{% endif %}

{% if include['disable-markdown'] %}
  {{ text }}
{% else %}
  {{ text | markdownify | remove: '<p>' | remove: '</p>' }}
{% endif %}
