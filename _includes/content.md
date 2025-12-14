{% for section in site.data._sections %}
  <h2>{% include t.md content=section.title %}</h2>

  <ul>
    {% for entry in site.data[section.entries] %}
      {% case section.entry_template %}
        {% when 'entry-relay.md' %}
          {% include entry-relay.md  entry=entry %}
        {% else %}
          {% include entry.md        entry=entry %}
      {% endcase %}
    {% endfor %}
  </ul>
{% endfor %}
