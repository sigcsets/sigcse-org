{% assign n1 = page.path | split: "/" | last %}
{% assign year = n1 | split: "." | first %}

{% assign prev = false %}
{% assign next = false %}
{% assign looking = true %}
{% assign onemore = false %}
{% assign first_yr = 0 %}
{% assign last_yr = 0 %}

{% assign conf = site.data.virtual.conferences | where: "year", year | first %}
{% assign items = site.data.virtual.conferences | sort: 'year' %}
{% for c in items %}
  {% comment %}They can both be true, first and last when the
  conference has only 1 instance... so this is true until 2026
  once Virtual has 2{% endcomment %}
  {% if forloop.first == true %}
    {% assign first_yr = c.year %}
  {%endif%}
  {% if forloop.last == true %}
    {% assign last_yr = c.year %}
  {%endif%}

  {% if looking %}
    {% if c.year == conf.year %}
      {% assign looking = false %}
      {% assign onemore = true %}
    {% else %}
      {% assign prev = c.year %}
    {% endif %}
  {% elsif onemore %}
    {% assign next = c.year %}
    {% assign onemore = false %}
  {% endif %}
{% endfor %}


> <a name="top" id="top"></a> {% if conf.year <= first_yr %}{% else %} <a href="{{prev}}.html">← Previous</a> &#124; {% endif %}<a href="conferences.html">SIGCSE Virtual Index</a> {% if conf.year == last_yr %}{% else %} &#124; <a href="{{next}}.html">Next →</a>{% endif %}

<table class="table table-sm">
  <tbody>
    <tr><th scope="row">Proceedings</th>
    <td colspan="2">
      {% if conf.proceedings.size > 1 %}
      <ul>{% for p in conf.proceedings -%}
      <li><a href="{{p.doi}}">{{p.title}}</a></li>
      {% endfor -%}</ul>
      {% else %}
      {% for p in conf.proceedings -%}
      <a href="{{p.doi}}">{{p.title}}</a><br>
      {% endfor -%}
      {% endif %}
    </td></tr>

{% capture proc_cover_path %}/events/virtual/images/covers/virtual{{conf.year}}.png{% endcapture %}
{% assign cover_exists = site.static_files | find: "path", proc_cover_path %}
{% if cover_exists %}
{% assign image_path = proc_cover_path %}
{% else %}
{% assign image_path = "/assets/images/default-proceeding.png" %}
{% endif %}
<tr><th scope="row">Dates</th><td>{{conf.dates}}</td><td rowspan="4" style="text-align:right"><img width="131" style="border: 5px solid #ddd;" src="{{image_path}}" alt="Proceedings cover for {{ conf.title | escape }}">&nbsp;

</td></tr>
{% if conf.theme %}
<tr><th scope="row">Theme</th><td colspan="2">{{conf.theme}}</td></tr>{%endif%}
{% if conf.venue %}
<tr><th scope="row">Venue</th><td>{{conf.venue}}</td></tr>{%endif%}
{% if conf.location %}
<tr><th scope="row">Location</th><td>{{conf.location}}</td></tr>{%endif%}
{% if conf.attendance %}
<tr><th scope="row">Attendance</th><td>{{conf.attendance}}</td></tr>{%endif%}
{% if conf.acceptance %}
<tr><th scope="row">Acceptance</th><td colspan="2">{{conf.acceptance}}</td></tr>{%endif%}
{% if conf.website %}
<tr><th scope="row">Website</th><td colspan="2"><a href="{{conf.website}}" target="_blank">{{conf.website}}</a></td></tr>{%endif%}
  </tbody>
</table>


{% comment %} AWARDS {% endcomment %}
{% include awards.md event="VIRTUAL" %}


{% if conf.logo %}&nbsp;<img src="images/logos/{{conf.logo}}" alt="Conference logo for {{ conf.title | escape }}">{%endif%}
