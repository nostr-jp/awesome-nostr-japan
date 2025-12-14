## Relays

<ul>
{% for entry in site.data.relays %}
  <li>
    <code>{{ entry.address }}</code>

    {% if entry.description[include.lang] %}
     - {{ entry.description[include.lang] }}
    {% endif %}

    {% if entry.authors %}
      {% include authors.md authors=entry.authors %}
    {% endif %}
  </li>
{% endfor %}
</ul>

## Web Services

<ul>
{% for entry in site.data['web-services'] %}
  <li>
    <a href="{{ entry.address }}" target="_blank">{{ entry.name }}</a>

    {% if entry.description[include.lang] %}
     - {{ entry.description[include.lang] }}
    {% endif %}

    {% if entry.authors %}
      {% include authors.md authors=entry.authors %}
    {% endif %}
  </li>
{% endfor %}
</ul>
