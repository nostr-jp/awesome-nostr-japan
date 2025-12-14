{% if include.content contains "" %} <!-- if include.content is string -->
  {{ include.content }}
{% else %}
  {{ include.content[page.lang] }}
{% endif %}
