<li>
  <a href="{{ entry.address }}" target="_blank">{{ entry.name }}</a>

  {% if entry.description[lang] %}
    - {{ entry.description[lang] }}
  {% endif %}

  {% if entry.authors %}
    {% include authors.md authors=entry.authors %}
  {% endif %}
</li>
