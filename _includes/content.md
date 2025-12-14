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

## Web Clients

<ul>
{% for entry in site.data['web-clients'] %}
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

## CLI Clients

<ul>
{% for entry in site.data['cli-clients'] %}
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

## Windows Clients

<ul>
{% for entry in site.data['windows-clients'] %}
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

## Relay Implementations

<ul>
{% for entry in site.data['relay-implementations'] %}
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

## Tools

<ul>
{% for entry in site.data.tools %}
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

## Bots

<ul>
{% for entry in site.data.bots %}
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

## Libraries

<ul>
{% for entry in site.data.libraries %}
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

## Books/Articles

<ul>
{% for entry in site.data['books-articles'] %}
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

## Blog Entries

<ul>
{% for entry in site.data['blog-entries'] %}
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

## Slides

<ul>
{% for entry in site.data.slides %}
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

## Videos

<ul>
{% for entry in site.data.videos %}
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

## Events

<ul>
{% for entry in site.data.events %}
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
