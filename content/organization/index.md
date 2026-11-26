---
title: Advancing computing education, together
layout: home
permalink: /index.html
---
<section class="home-hero">
<div><p class="eyebrow">ACM Special Interest Group on Computer Science Education</p>
<h1>Advancing computing education,<br><em>together.</em></h1>
<p class="lead">A global community of professionals, researchers, educators, teachers, and students interested in understanding and improving computing education.</p>
<div class="actions"><a class="button" href="{{ '/membership/join.html' | relative_url }}">Become a member <span aria-hidden="true">↗</span></a><a class="text-link" href="{{ '/about/profile.html' | relative_url }}">Get to know SIGCSE <span aria-hidden="true">→</span></a></div></div>
<aside class="hero-aside"><p class="eyebrow">Find your next step</p><a href="{{ '/conferences/' | relative_url }}">Connect at a conference <span aria-hidden="true">↗</span></a><a href="{{ '/programs/special/' | relative_url }}">Develop a new idea <span aria-hidden="true">↗</span></a><a href="{{ '/get-involved/' | relative_url }}">Contribute to the community <span aria-hidden="true">↗</span></a><p>Research. Teaching. Practice.</p></aside>
</section>
<section class="home-section"><div class="section-heading"><div><p class="eyebrow">Opportunities & support</p><h2>Make your next move.</h2></div><a href="{{ '/get-involved/' | relative_url }}">Ways to get involved →</a></div>
<div class="task-grid">
<a href="{{ '/programs/awards/' | relative_url }}"><span class="task-number">01</span><h3>Awards & nominations</h3><p>Recognize contributions to computing education and explore previous recipients.</p><span aria-hidden="true">→</span></a>
<a href="{{ '/programs/special/' | relative_url }}"><span class="task-number">02</span><h3>Special Projects</h3><p>Find grant guidance for ideas that benefit the computing education community.</p><span aria-hidden="true">→</span></a>
<a href="{{ '/programs/travel-grants/' | relative_url }}"><span class="task-number">03</span><h3>Travel grants</h3><p>Explore support for attending SIGCSE-sponsored conferences.</p><span aria-hidden="true">→</span></a>
</div></section>
<section class="home-section community-band"><div><p class="eyebrow">Meet. Share. Learn.</p><h2>Find your computing<br>education community.</h2><p>Explore SIGCSE conferences and connect with their own websites for event information.</p><a class="button" href="{{ '/conferences/' | relative_url }}">Explore conferences →</a></div><ul class="conference-shortlist">{% for conf in site.data.conferences %}<li><a href="{{ '/conferences/#' | append: conf.id | relative_url }}">{{ conf.abbreviation }} <span aria-hidden="true">↗</span></a></li>{% endfor %}</ul></section>
<section class="home-section"><div class="section-heading"><div><p class="eyebrow">From the community</p><h2>Latest news</h2></div><a href="{{ '/news/' | relative_url }}">All news →</a></div><div class="news-list">{% for post in site.posts limit:4 %}<article><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%d %b %Y' }}</time><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><span aria-hidden="true">↗</span></article>{% endfor %}</div></section>
<section class="organization-strip"><div><h2>Your organization, in the open.</h2><p>Find the people, records and policies behind SIGCSE.</p></div><div><a href="{{ '/about/board.html' | relative_url }}">Board & contacts →</a><a href="{{ '/about/reports/' | relative_url }}">Minutes & reports →</a><a href="{{ '/policies/' | relative_url }}">Policies →</a><a href="{{ '/resources/' | relative_url }}">Community resources →</a></div></section>
