## Relays

<ul>
{% for relay in site.data.relays %}
  <li>
    <code>{{ relay.address }}</code>

    {% if relay.description[lang] %}
     - {{ relay.description[lang] }}
    {% endif %}

    {% if relay.authors %}
      by
      {% for author in relay.authors %}
        <a href="{{ author.url }}">{{ author.name }}</a>{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    {% endif %}
  </li>
{% endfor %}
</ul>
