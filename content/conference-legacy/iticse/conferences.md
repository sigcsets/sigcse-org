---
title: All ITiCSE Conference
layout: page
permalink: /events/iticse/conferences.html
content_type: conference-legacy
conference: iticse
---

Follow the links below to each Technical Symposium summary page which includes links to the proceedings in the ACM DL. The ACM DL also includes a <a href="{{site.data.iticse.acmdl}}">Conference Series</a> page where all of the proceedings are linked.

{% assign items = site.data.iticse.conferences | sort: 'year' | reverse %}
{% for c in items -%}
    {% assign fn = '/events/iticse/' | append: c.year | append: '.html' -%}
    {% include item.md path=fn %}
{% endfor %}
