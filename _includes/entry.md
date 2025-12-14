<li>
  <a href="{{ entry.address }}" target="_blank">{%- include t.md content=entry.name -%}</a>

  {% if entry.description %}
    - {%- include t.md content=entry.description -%}
  {% endif %}

  {% if entry.authors %}
    {%- include authors.md authors=entry.authors -%}
  {% endif %}
</li>
