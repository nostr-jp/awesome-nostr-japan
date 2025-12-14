<li>
  <code>{{ include.entry.url }}</code>

  {% if entry.description %}
    - {%- include t.md content=entry.description -%}
  {% endif %}

  {% if entry.authors %}
    {%- include authors.md authors=entry.authors -%}
  {% endif %}
</li>
