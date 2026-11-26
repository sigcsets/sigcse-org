---
title: ACM SIGCSE — Computing education community
layout: home
permalink: /index.html
---
<section class="community-introduction">
{% include photo.html id='attendees' eager=true %}
<div><h1>The computing education community</h1><p>A global community of professionals, researchers, educators, teachers, and students interested in understanding and improving computing education.</p><a class="button" href="{{ '/membership/' | relative_url }}">Membership information</a><p class="secondary-action"><a href="{{ '/about/profile.html' | relative_url }}">About SIGCSE</a></p></div>
</section>
<section class="explore-section"><h2>Explore SIGCSE</h2><div class="task-grid">
<div><h3><a href="{{ '/conferences/' | relative_url }}">Conferences</a></h3><p>Find SIGCSE events and their websites.</p></div>
<div><h3><a href="{{ '/programs/awards/' | relative_url }}">Awards & nominations</a></h3><p>Nomination information and recipient histories.</p></div>
<div><h3><a href="{{ '/programs/special/' | relative_url }}">Special Projects</a></h3><p>Grants for new ideas in computing education.</p></div>
<div><h3><a href="{{ '/programs/travel-grants/' | relative_url }}">Travel grants</a></h3><p>Support for conference participation.</p></div>
<div><h3><a href="{{ '/resources/' | relative_url }}">Community resources</a></h3><p>Publications and resources for educators.</p></div>
<div><h3><a href="{{ '/get-involved/' | relative_url }}">Volunteer & participate</a></h3><p>Committees, task forces, and community activities.</p></div>
</div></section>
{% include upcoming-conferences.html %}
<div class="home-columns"><section><div class="section-heading"><h2>News from SIGCSE</h2><a href="{{ '/news/' | relative_url }}">All news</a></div><div class="news-list">{% for post in site.posts limit:3 %}<article><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%d %b %Y' }}</time><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3></article>{% endfor %}</div></section>
<aside class="governance-links"><h2>Board & governance</h2><ul><li><a href="{{ '/about/board.html' | relative_url }}">Board members & contacts</a></li><li><a href="{{ '/about/reports/board.html' | relative_url }}">Board minutes</a></li><li><a href="{{ '/about/reports/chair.html' | relative_url }}">Chair’s reports</a></li><li><a href="{{ '/policies/' | relative_url }}">Policies & bylaws</a></li></ul></aside></div>
