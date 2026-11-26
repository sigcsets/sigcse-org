---
title: SIGCSE Board
layout: page
image-path: "/assets/images/board/current/"
permalink: /about/board.html
---
<h2>{{ site.data.board.current-board.year }} Board</h2>
<div class="board-grid">{% for member in site.data.board.current-board.members %}<section class="board-person"><img src="{{ page.image-path | append: member.image | relative_url }}" alt="{{ member.name }}" width="85" height="85"><div><h3>{{ member.name }}</h3><p class="role">{{ member.position }}</p><p>{{ member.affiliation }}<br>{{ member.country }}</p><p><a href="mailto:{{ member.email }}">{{ member.email }}</a></p></div></section>{% endfor %}</div>
<h2>Board history</h2><p>A list of <a href="{{ '/about/board-history/' | relative_url }}">former Board members</a> is available online.</p>
