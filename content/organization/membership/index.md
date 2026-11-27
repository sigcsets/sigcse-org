---
title: Membership
layout: community
permalink: /membership/index.html
heading: A community for computing educators
introduction: Connect with colleagues, share teaching and research, and help shape computing education through SIGCSE.
actions:
  - {name: Join SIGCSE, link: /membership/join.html}
  - {name: Renew through ACM, link: 'https://www.acm.org/renew'}
---

{% include membership-benefits.html %}

<section class="participation-band"><div><h2>Take part in SIGCSE</h2><p>Review conference submissions, join a committee, contribute a resource, or volunteer to help organize a conference.</p></div><a class="button" href="{{ '/get-involved/' | relative_url }}">Find ways to get involved</a></section>

<section class="membership-snapshot" aria-labelledby="global-community"><div><h2 id="global-community">A global community</h2><p>Membership snapshot · {{ site.data.membership.date }}</p></div><div><strong>{{ site.data.membership.members }}</strong><span>members</span></div><div><strong>{{ site.data.membership.countries }}</strong><span>countries represented</span></div></section>

## Membership profile



As of {{site.data.membership.date}}, SIGCSE has a total of {{site.data.membership.members}} members representing {{site.data.membership.countries}} countries. The membership is divided into several categories:



{%- for k in site.data.membership.categories -%}
{%- if forloop.first -%}
{{k.name}} ({{k.percent}}),
{%- elsif forloop.last %}
 and {{k.name}} ({{k.percent}})
{%- else %}
{{k.name}} ({{k.percent}}),
{%- endif -%}
{%- endfor -%}. The pie chart below shows these groups.
{% capture path %}{{"/assets/images/"|absolute_url}}{{site.data.membership.image}}{% endcapture %}

<img class="membership-chart" src='{{path}}' alt="Membership:
{% for cat in site.data.membership.categories -%} {{cat.name}} ({{cat.percent}}); {%- endfor -%}">

<span id="interested-in-joining"></span>

## More ways to connect

-   [Benefits](benefits.html) - If you are a member these are
    your outstanding benefits
-   [How to Join](join.html) - If you are not a member, think
    about joining
-   [Get Involved](get-involved.html) - Ways for members to
    become more involved with SIGCSE
-   [Mailing Lists](mailing-lists.html) - Three informative
    mailing lists are available for all members
-   [ACM Membership Grades](grades.html) - Information on
    ACM’s advanced membership grades.


## Questions about your membership?


-   Contact ACM member services help desk at <acmhelp@acm.org>
-   For questions about SIGCSE member benefits, contact us at
    <membership@sigcse.org>
