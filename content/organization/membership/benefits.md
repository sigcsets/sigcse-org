---
title: Benefits of Membership
layout: page
permalink: /membership/benefits.html
benefits:
  - {"group": "Community and Recognition", "text": "Voting rights in SIGCSE Board elections."}
  - {"group": "Community and Recognition", "text": "Four issues of [ACM Inroads](https://inroads.acm.org/), a magazine dedicated to advancing computing education worldwide. Members receive electronic access, and physical-copy members also receive printed issues.", "featured": true, "label": "Publications", "link": "/resources/"}
  - {"group": "Community and Recognition", "text": "Access to the quarterly SIGCSE Bulletin newsletter."}
  - {"group": "Community and Recognition", "text": "Free access to SIGCSE publication archives through the ACM Digital Library, including proceedings from selected in-cooperation conferences."}
  - {"group": "Community and Recognition", "text": "Access to the SIGCSE-ANNOUNCE, SIGCSE-MEMBERS, SIGCSE-JOBS, and SIGCSE-VOLUNTEERS mailing lists."}
  - {"group": "Community and Recognition", "text": "Eligibility to nominate candidates for SIGCSE awards, including the Outstanding Contribution to Computer Science Education, Distinguished Service to the Computer Science Education Community, Broadening Participation in Computing Education, Early Career Researcher, and Test of Time awards.", "featured": true, "label": "Recognize colleagues", "link": "/programs/awards/"}
  - {"group": "Leadership Opportunities", "text": "Opportunity to participate in SIGCSE committees and task forces on topics of current interest.", "featured": true, "label": "Shape the community", "link": "/programs/committees-task-forces/"}
  - {"group": "Leadership Opportunities", "text": "Eligibility to serve on steering committees that help shape SIGCSE conferences and doctoral consortia."}
  - {"group": "Leadership Opportunities", "text": "Eligibility to stand as a candidate in SIGCSE Board elections."}
  - {"group": "Financial Benefits", "text": "Reduced registration rates for all SIGCSE conferences.", "featured": true, "label": "Meet at conferences", "link": "/conferences/"}
  - {"group": "Financial Benefits", "text": "Eligibility to apply for SIGCSE Special Projects grants supporting innovative ideas in computing education.", "featured": true, "label": "Develop new ideas", "link": "/programs/special/"}
  - {"group": "Financial Benefits", "text": "Eligibility to apply for the Henry Walker Travel Grant Program to support attendance at SIGCSE-sponsored conferences.", "featured": true, "label": "Travel support", "link": "/programs/travel-grants/"}
  - {"group": "Financial Benefits", "text": "Access to SIGCSE-supported Financial Hardship Waivers for eligible corresponding authors who cannot otherwise cover ACM Open Article Processing Charges."}
---

SIGCSE membership supports programs and initiatives that benefit the global computing education community, including:

- Maintaining access to high-quality research and teaching practice through SIGCSE-affiliated conference proceedings and the SIGCSE website.

- Supporting the growth of computing education worldwide through SIGCSE conferences, local and regional SIG chapters, and numerous in-cooperation conferences.

- Sponsoring mentoring and professional development opportunities, including the biennial New and Aspiring Educator Workshop and the Department Chairs Roundtable, typically held in conjunction with the SIGCSE Technical Symposium.

- Publishing reports from SIGCSE committees on topics of broad interest to the computing education community.

- Sponsoring doctoral consortia at SIGCSE conferences to support the next generation of computing education researchers through mentoring and partial travel support.

- Contributing to major computing curriculum task forces and serving as a thought leader for computing education.

Membership in SIGCSE provides the following direct benefits:

{% assign groups = page.benefits | group_by: 'group' %}
{% for group in groups %}
## {{ group.name }}

{% for benefit in group.items %}
- {{ benefit.text }}
{% endfor %}
{% endfor %}

[Join SIGCSE](join.html).
