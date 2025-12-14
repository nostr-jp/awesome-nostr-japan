{% for section in site.data._sections %}
  <h2>{{ section.title[lang] }}</h2>

  <ul>
    {% for entry in site.data[section.entries] %}
      {% case section['entry-template'] %}
        {% when 'entry-relay.md' %}
          {% include entry-relay.md  entry=entry %}
        {% else %}
          {% include entry.md        entry=entry %}
      {% endcase %}
    {% endfor %}
  </ul>
{% endfor %}
