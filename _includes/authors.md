by
{% for author in include.authors %}
  <a href="{{ author.url }}" target="_blank">
    {{ author.name }}
  </a>
  {% unless forloop.last %}, {% endunless %}
{% endfor %}
