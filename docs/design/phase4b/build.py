"""Render isolated Phase 4B HTML concepts; never changes the working Jekyll site."""
import html
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = Path(__file__).resolve().parent
OUT = ROOT / 'artifacts/phase4b'
LIVE = 'http://127.0.0.1:8765'
PHOTO = 'assets/teaching%20copy.jpg'
GROUP = 'assets/exhibits%20copy.jpg'
LOGO = 'assets/SIGCSE-logo_horiz_color_no-back.png'
NAMES = {'a': 'Editorial association', 'b': 'Professional community', 'c': 'Compact SIGCSE portal'}
NAV = [('Conferences', '/conferences/'), ('Membership', '/membership/'),
       ('Awards', '/programs/awards/'), ('Funding', '/funding/'), ('Resources', '/resources/'),
       ('Governance', '/governance/'), ('Policies', '/policies/')]
TASKS = [('Conferences', '/conferences/', 'Find SIGCSE events and their websites.'),
         ('Awards & nominations', '/programs/awards/', 'Recognize contributions to computing education.'),
         ('Special Projects', '/programs/special/', 'Support new ideas in learning and teaching.'),
         ('Travel grants', '/programs/travel-grants/', 'Find support for conference participation.'),
         ('Community resources', '/resources/', 'Publications and resources for educators.'),
         ('Get involved', '/get-involved/', 'Committees, task forces and volunteering.')]


def link(text, path, cls=''):
    return f'<a class="{cls}" href="{LIVE}{path}">{html.escape(text)}</a>'


def news():
    result = []
    for p in sorted((ROOT / '_posts').glob('*'), reverse=True)[:3]:
        raw = p.read_text(encoding='utf-8-sig')
        title = re.search(r'^title:\s*(.+)', raw, re.M).group(1).strip('"\'')
        # Link to the real news archive rather than guessing Jekyll post slugs.
        date = datetime.strptime(p.name[:10], '%Y-%m-%d').strftime('%d %b %Y')
        result.append(f'<li><time>{date}</time>{link(title,"/news/")}</li>')
    return '<ul class="news">' + ''.join(result) + '</ul>'


def header(concept, interior):
    items = []
    for name, path in NAV:
        target = f'{concept}-special-projects.html' if name == 'Funding' else LIVE + path
        current = ' aria-current="location"' if interior and name == 'Funding' else ''
        items.append(f'<a href="{target}"{current}>{name}</a>')
    return f'''<div class="concept-toolbar"><div>Concept {concept.upper()} · {NAMES[concept]}</div><div><a href="{concept}-home.html">Homepage</a> · <a href="{concept}-special-projects.html">Special Projects</a> · <a href="index.html">Compare concepts</a></div></div>
<header class="masthead wrap"><a href="{concept}-home.html"><img class="logo" src="{LOGO}" alt="ACM SIGCSE" width="235"></a><div class="brand-description">Special Interest Group on<br>Computer Science Education</div><div class="utility">{link('About SIGCSE','/about/profile.html')}{link('News','/news/')}{link('Join SIGCSE','/membership/join.html','button')}</div></header>
<nav class="primary" aria-label="Main navigation"><div class="wrap">{''.join(items)}</div></nav>'''


def footer():
    return f'''<footer><div class="wrap"><strong>ACM SIGCSE</strong><span>Research, teaching and practice in computing education.</span>{link('Board & contacts','/about/board.html')} · {link('Policies','/policies/')} · {link('Conference archives','/archives/')}</div></footer>'''


def task_list(concept):
    return '<div class="task-links">' + ''.join(
        f'<div><h3><a href="{concept}-special-projects.html">{name}</a></h3><p>{desc}</p></div>' if name == 'Special Projects'
        else f'<div><h3>{link(name,path)}</h3><p>{desc}</p></div>' for name, path, desc in TASKS) + '</div>'


def home(concept):
    mission = 'A global community of professionals, researchers, educators, teachers, and students interested in understanding and improving computing education.'
    caption = 'SIGCSE attendees · photograph from the existing website archive'
    photo = f'<figure><img src="{PHOTO}" alt="Two SIGCSE attendees together at a community event"><figcaption>{caption}</figcaption></figure>'
    group = f'<figure><img src="{GROUP}" alt="A group gathered for the SIGCSE 50th celebration in 2019"><figcaption>SIGCSE 50th celebration, 2019 · archive photograph</figcaption></figure>'
    if concept == 'a':
        body = f'''<main class="wrap editorial-home"><div class="editorial-lead"><div><h1>A global forum for<br>computing education</h1><p class="intro">{mission}</p><p>{link('About our community','/about/profile.html')} &nbsp; {link('Become a member','/membership/join.html','button')}</p></div>{photo}</div>
<div class="editorial-columns"><section><h2>Participate in SIGCSE</h2>{task_list(concept)}</section><aside><h2>Community news</h2>{news()}{link('All news','/news/')}<div class="governance-note"><h3>Your organization</h3>{link('Board and contacts','/about/board.html')}<br>{link('Minutes and reports','/about/reports/')}</div></aside></div></main>'''
    elif concept == 'b':
        body = f'''<main class="wrap community-home"><section class="community-lead">{photo}<div><h1>The computing<br>education community</h1><p>{mission}</p>{link('Join SIGCSE','/membership/join.html','button')}<p class="secondary-action">{link('Find a conference','/conferences/')}</p></div></section>
<section class="community-opportunities"><h2>Share ideas. Support each other. Take part.</h2>{task_list(concept)}</section><div class="community-bottom"><section><h2>News from SIGCSE</h2>{news()}</section><aside>{group}<p>{link('Meet the Board','/about/board.html')} · {link('Get involved','/get-involved/')}</p></aside></div></main>'''
    else:
        body = f'''<main class="wrap compact-home"><div class="compact-intro"><h1>Your SIGCSE community</h1><p>{mission}</p></div><div class="portal-columns"><aside class="quick-nav"><h2>Find what you need</h2>{''.join(link(n,p) for n,p,d in TASKS)}{link('Join SIGCSE','/membership/join.html')}{link('Board minutes','/about/reports/board.html')}</aside>
<div><section class="portal-section"><h2>Opportunities & support</h2><dl><dt><a href="{concept}-special-projects.html">Special Projects grants</a></dt><dd>Application guidance, eligibility and previous awards.</dd><dt>{link('Travel grants','/programs/travel-grants/')}</dt><dd>Henry Walker Travel Grant Program information.</dd><dt>{link('Awards & nominations','/programs/awards/')}</dt><dd>Nomination processes and recipient histories.</dd></dl></section><section class="portal-section"><h2>SIGCSE conferences</h2><div class="conference-links">{link('Technical Symposium','/conferences/#symposia')}{link('ITiCSE','/conferences/#iticse')}{link('ICER','/conferences/#icer')}{link('CompEd','/conferences/#comped')}{link('RESPECT','/conferences/#respect')}{link('SIGCSE Virtual','/conferences/#virtual')}</div>{link('Conference directory and event websites','/conferences/')}</section><section class="portal-section"><h2>Governance & records</h2><p>{link('Board contacts','/about/board.html')} · {link('Minutes and reports','/about/reports/')} · {link('Policies and bylaws','/policies/')} · {link('Committees','/programs/committees-task-forces/')}</p></section></div>
<aside class="portal-news"><h2>Latest news</h2>{news()}{link('All news','/news/')}{photo}</aside></div></main>'''
    return header(concept, False) + body + footer()


def funding_nav(concept):
    return f'''<nav class="funding-nav" aria-label="Funding section"><h2>Funding & support</h2>{link('Funding overview','/funding/')}<a href="{concept}-special-projects.html" aria-current="page">Special Projects grants</a>{link('Travel grants','/programs/travel-grants/')}{link('Speaker’s Fund','/programs/speakers/')}<a href="#previous">Previous awards</a></nav>'''


def facts():
    return '''<div class="facts"><div><span>Submission deadlines</span><strong>May 15 & November 15</strong></div><div><span>Maximum award</span><strong>$5,000 USD</strong></div><div><span>Eligibility</span><strong>SIGCSE members</strong></div></div>'''


def application():
    return '''<section class="application"><h2>Applying for a grant</h2><p>Complete the <a href="https://forms.gle/Gq7QSbjCA6GjTNaU6">Special Projects Application</a> by the May 15 or November 15 deadline.</p><h3>Your proposal should explain</h3><ul><li>The purpose, approach and expected outcome of the project.</li><li>The start date, duration and benefit to the wider community.</li><li>How results will be shared and adopted by others.</li><li>A budget with a brief justification.</li></ul><h3>Who can apply?</h3><p>You must be a SIGCSE member. SIGCSE Board members are not eligible. Smaller bids are encouraged.</p><p>No person or group can receive more than $10,000 during any four-year period. Other conditions apply; read the <a href="http://127.0.0.1:8765/programs/special/">full published guidance</a>.</p></section>'''


def support():
    years = range(2025, 2016, -1)
    return f'''<aside class="application-support"><h2>Start your application</h2><a class="button" href="https://forms.gle/Gq7QSbjCA6GjTNaU6">Application form</a><p>Proposals are considered twice each year.</p><h3>Questions?</h3><a href="mailto:apply@sigcse.org">apply@sigcse.org</a><h3 id="previous">Previous Special Projects</h3><p>Explore the work supported by SIGCSE.</p><div class="year-links">{''.join(link(str(y),f'/programs/special/{y}.html') for y in years)}</div>{link('All previous awards','/programs/special/')}</aside>'''


def interior(concept):
    breadcrumbs = f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{concept}-home.html">Home</a><span>/</span>{link("Funding & support","/funding/")}<span>/</span><span aria-current="page">Special Project Grants</span></nav>'
    intro = 'SIGCSE Special Projects Grants help members investigate and introduce new ideas in the learning and teaching of computing. Projects must benefit the wider disciplinary community.'
    if concept == 'a':
        body = f'''<main class="wrap interior">{breadcrumbs}<div class="interior-heading"><h1>Special Project Grants</h1><p>{intro}</p></div><div class="funding-layout">{funding_nav(concept)}<div>{facts()}{application()}</div>{support()}</div></main>'''
    elif concept == 'b':
        body = f'''<main class="wrap interior">{breadcrumbs}<div class="community-funding-heading"><div><h1>Special Project Grants</h1><p>{intro}</p></div><a href="https://forms.gle/Gq7QSbjCA6GjTNaU6" class="button">Apply for a grant</a></div>{facts()}<div class="community-funding-body"><div>{application()}<section class="obligations"><h2>Sharing the results</h2><p>Successful proposers agree to report to the SIGCSE Board and publish results for the community.</p></section></div><div>{support()}{funding_nav(concept)}</div></div></main>'''
    else:
        body = f'''<main class="wrap interior">{breadcrumbs}<div class="compact-funding">{funding_nav(concept)}<div><h1>Special Project Grants</h1><p>{intro}</p><table><caption>Application at a glance</caption><tbody><tr><th scope="row">Deadlines</th><td>May 15 and November 15</td></tr><tr><th scope="row">Maximum award</th><td>$5,000 USD; smaller bids encouraged</td></tr><tr><th scope="row">Eligibility</th><td>SIGCSE members; Board members excluded</td></tr></tbody></table>{application()}</div>{support()}</div></main>'''
    return header(concept, True) + body + footer()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'assets').mkdir(exist_ok=True)
    for file in ['assets/images/home/teaching copy.jpg', 'assets/images/home/exhibits copy.jpg',
                 'assets/images/logo/SIGCSE-logo_horiz_color_no-back.png']:
        shutil.copyfile(ROOT / file, OUT / 'assets' / Path(file).name)
    shutil.copyfile(SOURCE / 'concepts.css', OUT / 'concepts.css')
    cards = []
    for concept, label in NAMES.items():
        for kind, render in [('home', home), ('special-projects', interior)]:
            body = render(concept)
            body = body.replace('<main ', '<main id="content" tabindex="-1" ', 1)
            title = 'Homepage' if kind == 'home' else 'Special Project Grants'
            page = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Concept {concept.upper()} · {title} · SIGCSE</title><link rel="stylesheet" href="concepts.css"></head><body class="concept-{concept}"><a class="skip" href="#content">Skip to main content</a>{body}</body></html>'
            (OUT / f'{concept}-{kind}.html').write_text(page, encoding='utf-8')
        cards.append(f'<section><h2>{concept.upper()}. {label}</h2><p><a href="{concept}-home.html">Open homepage</a> · <a href="{concept}-special-projects.html">Open Special Projects</a></p><a href="screenshots/{concept}-home.jpg"><img src="screenshots/{concept}-home.jpg" alt="Concept {concept.upper()} homepage"></a><a href="screenshots/{concept}-special-projects.jpg"><img src="screenshots/{concept}-special-projects.jpg" alt="Concept {concept.upper()} Special Projects page"></a></section>')
    (OUT / 'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SIGCSE visual concepts</title><style>body{font:16px/1.5 system-ui;max-width:1240px;margin:2rem auto;padding:0 1rem;color:#20394e}h1{font-size:30px}section{border-top:2px solid #4b86b5;padding:1rem 0}img{max-width:48%;margin-right:1%;vertical-align:top;border:1px solid #ddd}a{color:#1763a0}</style><h1>SIGCSE · Three visual directions</h1><p>Isolated exploration. The working Jekyll website is unchanged. Each concept includes a homepage and the same Special Projects content. Desktop screenshots use 1440 × 1000.</p>'+''.join(cards)+'</html>', encoding='utf-8')
    print(f'Rendered six isolated concepts in {OUT}')


if __name__ == '__main__':
    main()
