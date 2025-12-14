<li>
  <code>{{ include.entry.address }}</code>

  {% if include.entry.description[lang] %}
    - {{ include.entry.description[lang] }}
  {% endif %}

  {% if include.entry.authors %}
    {% include authors.md authors=include.entry.authors %}
  {% endif %}
</li>
