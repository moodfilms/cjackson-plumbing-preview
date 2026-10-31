"""Builds the C Jackson Plumbing site.

    python3 build.py          preview build: noindex tags + preview note (for the GitHub Pages preview)
    python3 build.py --live   launch build for www.cjacksonplumbing.com: indexable, no preview note
"""
import math, os, html, json, sys
OUT = os.path.dirname(os.path.abspath(__file__)) + '/'
SITE = 'https://www.cjacksonplumbing.com/'
PREVIEW = 'https://moodfilms.github.io/cjackson-plumbing-preview/'
LIVE = '--live' in sys.argv
BASE = SITE if LIVE else PREVIEW
UPDATED = '2026-10-31'
E = html.escape
GSZ = '(max-width: 640px) 46vw, 300px'

LAND = ('01977 309 517', '+441977309517')
MOB = ('07872 584 324', '+447872584324')
EMAIL = 'cjacksonplumbing@hotmail.com'
ADDR = '75 Lower Oxford Street, Castleford WF10 4AF'
MAPS = 'https://www.google.com/maps/search/?api=1&query=75+Lower+Oxford+Street+Castleford+WF10+4AF'

ICON = {
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'quote': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 18v-5.5C4 8.4 6.3 6 10 5.5v2.6C8.2 8.6 7.3 9.8 7.2 11.5H10V18H4Zm10 0v-5.5c0-4.1 2.3-6.5 6-7v2.6c-1.8.5-2.7 1.7-2.8 3.4H20V18h-6Z"/></svg>',
 'years': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
 'person': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
 'clean': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M6 6l2 2M16 16l2 2M6 18l2-2M16 8l2-2"/></svg>',
 'drop': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/></svg>',
 'flame': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c1 3 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5 0 2 1 3 2 3 0-3-1-5 1-8.5Z"/></svg>',
 'tap': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h9a4 4 0 0 1 4 4v1h-4v-1H4z"/><path d="M8 5h3M9.5 5v4"/><path d="M15 18c0 1 .7 2 1.5 2S18 19 18 18c0-1-1.5-2.5-1.5-2.5S15 17 15 18Z"/></svg>',
 'bolt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 5 6v5c0 4.5 3 8.4 7 10 4-1.6 7-5.5 7-10V6l-7-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
 'insured': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h4"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/></svg>',
 'alert': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 2 20h20L12 3Z"/><path d="M12 10v4M12 17h.01"/></svg>',
 'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
}

LOGO = '<img src="img/brand/cjackson-logo.png" alt="C Jackson Plumbing" width="847" height="237">'

# ---------------- Real content ----------------
REVIEWS = [
 dict(id='pat', name='Pat', place='Pontefract', text="Thanks Craig for the brilliant job you did on my bathroom after the previous fitter left it in a mess. Your work was to a high standard, paying great attention to every detail. I'm very happy with it. Everything you did ticked all the boxes, leaving everything clean and tidy each day. I will certainly use you again if I need work doing again and would recommend to anyone. Thank you again for a first class job."),
 dict(id='steve', name='Steve', place='Whitkirk', text="Craig came to my house for a consultation for a new bathroom suite. He was on time (which is hard these days!). He organised electricians, tilers and plasterers and ran the job. He was in touch with me all the time. From start to finish the job was completed within 2 weeks. Extremely happy!"),
 dict(id='richard', name='Richard', place='Kippax', text="Very impressed as this was a very large job: removed joists and did underfloor heating. The efficiency and organisation was 100%. Craig organised everything. Would recommend."),
 dict(id='joanne', name='Joanne', place='Castleford', text="Very pleased with the outcome of our bathroom. Craig was very pleasant and professional and dealt with everything that I asked of him. He did an excellent job and I would highly recommend."),
 dict(id='paul', name='Paul', place='', text="Thanks to Craig and John for all their hard work on our new bathroom. I can't recommend them highly enough. From start to finish they have been extremely professional and the finished bathroom is excellent. Will definitely be using them for our next project."),
 dict(id='jilly', name='Jilly', place='', text="Just wanted to say thank you and place on record how happy we are with the quality of your work on the recent bathroom project you completed for us. We would have no hesitation in recommending you, due to the great service that you and your team provided."),
 dict(id='meg', name='Meg', place='Harrogate', text="A true professional, with attention to detail from start to finish."),
 dict(id='jonathan', name='Jonathan', place='Whitkirk', text="We were extremely impressed by the finish. We would highly recommend!"),
 dict(id='jason', name='Jason', place='Harrogate', text="Thoroughly happy with the job from start to finish."),
]
RV = {r['id']: r for r in REVIEWS}

PROJECTS = [
 dict(id='joanne', title="Joanne's bathroom", kind='Bathroom', place='Castleford',
      desc="A dated corner bath, coloured suite and carpet taken out. A new bath was built in on a timber frame with a mosaic panel and niche, alongside a quadrant shower and large-format grey tiles.",
      stages=[('before','joanne-before','Original bathroom with a green corner bath, matching basin and patterned carpet'),('during','joanne-during','New timber frame built for the bath and boxing, walls boarded'),('after','joanne-after','Finished bathroom with built-in bath, mosaic panel and grey tiles')],
      extras=[('joanne-1','Wall-hung basin with chrome mixer and heated towel rail'),('joanne-2','Built-in bath with mosaic-tiled niche')], quote='joanne'),
 dict(id='dan', title="Dan's bathroom", kind='Bathroom', place='',
      desc="Old tiles stripped and the walls made good, then finished in grey large-format tiles with an L-shaped shower bath and glass screen, a back-lit mirror and a vanity unit.",
      stages=[('before','dan-before','Bathroom stripped back to bare walls with old adhesive showing'),('during','dan-during','Walls freshly plastered and ready for tiling'),('after','dan-after','Finished bathroom with back-lit mirror, vanity unit and shower bath')],
      extras=[('dan-1','L-shaped shower bath with tiled panel and glass screen'),('dan-2','Close-coupled WC and chrome towel radiator on grey tiles')]),
 dict(id='diane', title="Diane's bathroom", kind='Bathroom', place='',
      desc="Red wall tiles and the old pedestal suite removed and the room rebuilt with new studwork. Finished with a quadrant shower, LED mirror, chrome towel rail and a concealed-cistern WC.",
      stages=[('before','diane-before','Original bathroom with red wall tiles and pedestal basin'),('during','diane-during','New studwork framing during the rebuild'),('after','diane-after','Finished room with wall-hung basin and concealed-cistern WC')],
      extras=[('diane-1','Quadrant shower enclosure with mosaic feature tiles'),('diane-2','LED mirror above a chrome towel rail')]),
 dict(id='kaye', title="Kaye's kitchen", kind='Kitchen', place='',
      desc="Taken back to brick and fully re-boarded before fitting a new kitchen with a metro-tile splashback and under-cabinet lighting. A new shower room was added off the kitchen in the same job.",
      stages=[('before','kaye-before','Kitchen stripped back to bare brick'),('during','kaye-during','Walls re-boarded with the room ready for fitting'),('after','kaye-after','Finished kitchen with gloss units, metro-tile splashback and under-cabinet lights')],
      extras=[('kaye-1','Kitchen during fitting with the garden door open'),('kaye-2','New shower room with quadrant enclosure, off the kitchen')]),
 dict(id='barbara', title="Barbara's bathroom", kind='Bathroom', place='',
      desc="Stripped right back to the floorboards, then finished with marble-effect wall tiles, a combination vanity and WC unit, a tall chrome towel radiator and wood-effect flooring.",
      stages=[('before','barbara-before','Bathroom stripped to floorboards with old pipework exposed'),('during','barbara-during','Walls prepared during the rebuild'),('after','barbara-after','Finished bathroom with grey combination vanity unit and marble-effect tiles')],
      extras=[('barbara-1','View into the finished bathroom past the louvred cupboard'),('barbara-2','Bath with marble-effect tiling and chrome mixer')]),
 dict(id='crashley', title="Mr & Mrs Crashley's bathroom", kind='Bathroom', place='',
      desc="Old stone-effect tiles and fittings removed, then a full refit with large-format porcelain, a long combination vanity and WC unit, a designer towel rail and a shower enclosure.",
      stages=[('before','crashley-before','Bathroom with the old tiles removed and walls exposed'),('during','crashley-during','New towel rail fitted while the walls are prepared'),('after','crashley-after','Finished bathroom with long white vanity unit under the window')]),
 dict(id='colin-michelle', title="Colin & Michelle's bathroom", kind='Bathroom', place='',
      desc="Taken back to bare brick and rebuilt as a period bathroom: white metro tiles, a Victorian-pattern floor, column radiator, high-level cistern and a glass-screened walk-in shower.",
      stages=[('before','colin-michelle-before','Room stripped back to bare brick'),('after','colin-michelle-after','Period bathroom with metro tiles, high-level cistern and pedestal basin')],
      extras=[('colin-michelle-1','Pedestal basin with traditional taps on a patterned floor'),('colin-michelle-2','Walk-in shower with glass screen and thermostatic valve'),('colin-michelle-3','Bath and column radiator under the window'),('colin-michelle-4','Traditional heated towel rail')]),
 dict(id='martin', title="Martin's bathroom", kind='Bathroom', place='',
      desc="A tired bathroom stripped out and refitted with full-height white tiling, a shower over the bath with a glass screen, and a wall-hung vanity unit.",
      stages=[('before','martin-before','Original bathroom before work started'),('during','martin-during','Room stripped out during the refit'),('after','martin-after','Finished bathroom with white tiling and shower over the bath')]),
 dict(id='pat', title="Pat's bathroom", kind='Bathroom', place='Pontefract',
      desc="Put right after a previous fitter left it unfinished. Sage-green metro tiles, a patterned floor, a washstand basin with pillar taps and a traditional WC.",
      stages=[('after','pat-after','Washstand basin and traditional WC with sage-green metro tiles and patterned floor')], quote='pat'),
 dict(id='tina', title="Tina's en-suite", kind='En-suite', place='',
      desc="A compact en-suite with a shower enclosure, back-lit mirror, floor-standing vanity unit and a chrome towel rail.",
      stages=[('after','tina-after','En-suite vanity unit under a back-lit mirror')],
      extras=[('tina-1','Shower enclosure and towel rail'),('tina-2','Chrome towel rail on light grey tiles')]),
]
HOME_TABS = ['joanne', 'dan', 'diane', 'kaye', 'barbara', 'crashley']
P = {p['id']: p for p in PROJECTS}
STAGE_NAME = {'before': 'Before', 'during': 'During', 'after': 'Finished'}

# ---------------- To-scale area map ----------------
TOWNS = [
 ('Leeds', 53.7997, -1.5492, 'r'), ('Roundhay', 53.8347, -1.5023, 'r'), ('Whitkirk', 53.7990, -1.4560, 'b'),
 ('Garforth', 53.7920, -1.3820, 'r'), ('Kippax', 53.7670, -1.3700, 'r'), ('Rothwell', 53.7486, -1.4780, 'l'),
 ('Methley', 53.7350, -1.4090, 'l'), ('Castleford', 53.7250, -1.3620, 'r'), ('Pontefract', 53.6910, -1.3120, 'l'),
]
def build_map():
    lat0, lat1, lon0, lon1 = 53.665, 53.855, -1.600, -1.270
    W = 520; pad = 30
    k = math.cos(math.radians((lat0 + lat1) / 2))
    s = (W - 2 * pad) / ((lon1 - lon0) * k)
    H = round((lat1 - lat0) * s + 2 * pad)
    X = lambda lon: pad + (lon - lon0) * k * s
    Y = lambda lat: pad + (lat1 - lat) * s
    km5 = 5 / 111.32 * s  # 5 km in px (latitude degrees)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="map-title map-desc">',
           '<title id="map-title">Service area map</title>',
           '<desc id="map-desc">Towns covered around Leeds and West Yorkshire, drawn to scale, with the Castleford base highlighted.</desc>',
           f'<defs><pattern id="g" width="{km5/2:.2f}" height="{km5/2:.2f}" patternUnits="userSpaceOnUse"><path d="M{km5/2:.2f} 0V{km5/2:.2f}M0 {km5/2:.2f}H{km5/2:.2f}" stroke="#dde0e5" stroke-width="1" fill="none"/></pattern></defs>',
           f'<rect width="{W}" height="{H}" fill="#f2f3f5"/><rect width="{W}" height="{H}" fill="url(#g)"/>']
    bx, by = X(-1.3620), Y(53.7250)
    for r_km in (10, 20):
        out.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{r_km/111.32*s:.1f}" fill="none" stroke="#121418" stroke-opacity=".18" stroke-dasharray="3 5" stroke-width="1.2"/>')
    for name, lat, lon, side in TOWNS:
        x, y = X(lon), Y(lat)
        base = name == 'Castleford'
        if base:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="#f7ce4c" fill-opacity=".35"/><circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#f7ce4c" stroke="#121418" stroke-width="2"/>')
        else:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#121418"/>')
        if side == 'r': tx, ty, anchor = x + (20 if base else 11), y + 4.5, 'start'
        elif side == 'l': tx, ty, anchor = x - 11, y + 4.5, 'end'
        else: tx, ty, anchor = x, y + 20, 'middle'
        weight = 800 if base else 600
        size = 15 if base else 13
        out.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" font-family="Montserrat, sans-serif" font-size="{size}" font-weight="{weight}" fill="#121418" paint-order="stroke" stroke="#f2f3f5" stroke-width="4" stroke-linejoin="round">{name}</text>')
    lx = X(-1.5492)
    out.append(f'<path d="M{lx:.1f} 26V10M{lx-5:.1f} 15l5-5 5 5" stroke="#565d68" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    out.append(f'<text x="{lx+10:.1f}" y="20" font-family="Montserrat, sans-serif" font-weight="700" font-size="9.5" letter-spacing=".08em" fill="#565d68">HARROGATE</text>')
    sx, sy = pad, H - pad + 6
    out.append(f'<path d="M{sx} {sy}h{km5:.1f}M{sx} {sy-5}v5M{sx+km5:.1f} {sy-5}v5" stroke="#121418" stroke-width="1.6" fill="none"/>')
    out.append(f'<text x="{sx + km5 + 8:.1f}" y="{sy+1}" font-family="Montserrat, sans-serif" font-weight="700" font-size="9.5" fill="#565d68">5 km</text>')
    out.append('</svg>')
    return '\n'.join(out)

# ---------------- Shared chrome ----------------
def head(title, desc, path='', extra=''):
    robots = '' if LIVE else '<meta name="robots" content="noindex, nofollow">\n'
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{path}">
{robots}<meta name="theme-color" content="#121418">
<meta name="geo.region" content="GB-WKF">
<meta name="geo.placename" content="Castleford">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Figtree:wght@400;500;600;700&display=swap">
<link rel="icon" type="image/png" sizes="32x32" href="img/brand/favicon-32.png">
<link rel="apple-touch-icon" href="img/brand/icon-180.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="C Jackson Plumbing">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{BASE}img/brand/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>'''

def header(active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{href}"{cur}>{label}</a>'
    pre = '' if active == 'home' else 'index.html'
    return f'''
<div class="topbar">
  <div class="wrap">
    <p class="topbar-msg"><span class="pulse" aria-hidden="true"></span><strong>24-hour</strong>emergency plumbing<span class="hide-sm"> across Leeds &amp; West Yorkshire</span></p>
    <p class="topbar-lines"><span class="hide-sm">Office</span><a class="hide-sm" href="tel:{LAND[1]}">{LAND[0]}</a> <span class="hide-sm">Mobile</span><a href="tel:{MOB[1]}">{MOB[0]}</a></p>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="C Jackson Plumbing, home">{LOGO}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{ICON['menu']}</button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      {link('bathroom-fitters-castleford.html', 'Bathrooms', 'bathrooms')}
      {link('plumbing-heating-castleford.html', 'Plumbing &amp; heating', 'plumbing')}
      {link('work.html', 'Our work', 'work')}
      {link('areas.html', 'Areas', 'areas')}
      <a class="btn btn--brass" href="{pre}#contact">Request a quote</a>
    </nav>
  </div>
</header>'''

def footer(active):
    pre = '' if active == 'home' else 'index.html'
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="logo" href="index.html" aria-label="C Jackson Plumbing, home">{LOGO}</a>
        <p class="footer-tagline">Providing 24 hour plumbing services</p>
        <p>A family-owned plumbing firm in Castleford. Specialists in luxury bathrooms and kitchens, with 24-hour emergency call-outs.</p>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="tel:{LAND[1]}">Office {LAND[0]}</a></li>
          <li><a href="tel:{MOB[1]}">Mobile {MOB[0]}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ADDR}</li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="bathroom-fitters-castleford.html">Bathroom fitting</a></li>
          <li><a href="kitchen-fitters-castleford.html">Kitchen fitting</a></li>
          <li><a href="plumbing-heating-castleford.html">Plumbing &amp; heating</a></li>
          <li><a href="emergency-plumber-castleford.html">24-hour emergency plumber</a></li>
        </ul>
      </div>
      <div>
        <h4>More</h4>
        <ul>
          <li><a href="work.html">Our work</a></li>
          <li><a href="areas.html">Areas we cover</a></li>
          <li><a href="index.html#reviews">Reviews</a></li>
          <li><a href="index.html#faq">Questions</a></li>
          <li><a href="{pre}#contact">Request a quote</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <p>&copy; 2026 C Jackson Plumbing &middot; Fully insured</p>
      {'' if LIVE else '<p>Design preview. Not yet the live cjacksonplumbing.com site.</p>'}
    </div>
  </div>
</footer>
<div class="callbar" aria-label="Quick contact">
  <a class="btn btn--line" href="tel:{MOB[1]}">{ICON['phone']}Call Craig</a>
  <a class="btn btn--brass" href="{pre}#contact">Get a quote</a>
</div>
<script src="site.js"></script>
</body>
</html>
'''

def img(name, alt, cls='', lazy=True, w=None, h=None, sizes='(max-width: 640px) 92vw, 440px', low=False, high=False):
    """Responsive image: phones get the 640px file, larger screens the full one.
    Images inside hidden tab panels must NOT use loading="lazy": iOS Safari never
    fetches them when the panel is revealed by a tap, so they load eagerly at low priority."""
    from PIL import Image
    if w is None:
        w, h = Image.open(OUT + 'img/' + name + '.jpg').size
    l = ' loading="lazy"' if lazy else ''
    l += ' decoding="async"'
    if low: l += ' fetchpriority="low"'
    if high: l += ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ''
    srcset = ''
    if os.path.exists(OUT + 'img/' + name + '-640.jpg'):
        srcset = f' srcset="img/{name}-640.jpg 640w, img/{name}.jpg {w}w" sizes="{sizes}"'
    return f'<img{c} src="img/{name}.jpg"{srcset} alt="{E(alt)}" width="{w}" height="{h}"{l}>'

def review_footer(r):
    place = f', {E(r["place"])}' if r['place'] else ''
    return f'<b>{E(r["name"])}</b>{place}'

# ---------------- Homepage ----------------
def home():
    h = head('Plumber & Bathroom Fitter in Castleford | C Jackson Plumbing',
             'Family-run plumbers and luxury bathroom fitters in Castleford. Fully insured, 15+ years\' experience and 24-hour emergency call-outs across Leeds and West Yorkshire.',
             '', ld(business(), website(), faq_schema(HOME_FAQ)))
    h += header('home')
    steve = RV['steve']
    h += f'''
<main>
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">Castleford &middot; Leeds &middot; West Yorkshire</span>
      <h1>Luxury bathrooms in Castleford, fitted start to finish by a <em>local family firm</em>.</h1>
      <p class="hero-lead">We plan and install bathrooms, en-suites, wet rooms and kitchens, and handle everyday plumbing and heating. Craig runs every job personally: he books the electricians, tilers and plasterers and keeps you updated until the room is finished.</p>
      <div class="hero-actions">
        <a class="btn btn--brass" href="#contact">Request a quote {ICON['arrow']}</a>
        <a class="btn btn--line" href="tel:{LAND[1]}">{ICON['phone']}Call {LAND[0]}</a>
      </div>
      <p class="hero-reassure">Home visit and written price before anything is booked. Small jobs welcome too.</p>
      <figure class="hero-quote">
        {ICON['quote']}
        <blockquote style="margin:0"><p>He was on time (which is hard these days!). He organised electricians, tilers and plasterers. He was in touch with me all the time.</p>
        <cite>Steve, Whitkirk &middot; full bathroom in 2 weeks</cite></blockquote>
      </figure>
    </div>
    <div class="hero-wall">
      <figure class="hero-photo">
        {img('colin-michelle-after', 'Period-style bathroom in West Yorkshire with white metro tiles, high-level cistern, column radiator and patterned floor', lazy=False, high=True)}
        <figcaption><span>Colin &amp; Michelle&rsquo;s bathroom</span><span>Finished</span></figcaption>
      </figure>
      <div class="hero-before">
        {img('colin-michelle-before', 'The same room stripped back to bare brick before work began', lazy=False, sizes='64px')}
        <span><b>Before</b>Stripped back to bare brick</span>
      </div>
    </div>
  </div>
</section>

<section class="trust" aria-label="Accreditations and why customers choose us">
  <div class="wrap">
    <ul>
      <li>{ICON['insured']}<strong>Fully insured</strong><span>cover in place on every job we do</span></li>
      <li>{ICON['years']}<strong>15+ years</strong><span>fitting bathrooms, kitchens and heating</span></li>
      <li>{ICON['home']}<strong>Family owned</strong><span>local firm based in Castleford</span></li>
      <li>{ICON['person']}<strong>One point of contact</strong><span>Craig organises every trade on the job</span></li>
      <li>{ICON['bolt']}<strong>24-hour call-outs</strong><span>day or night, across West Yorkshire</span></li>
    </ul>
  </div>
</section>

<section class="band" id="services">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What we do</span>
      <h2>Bathrooms are our speciality. We look after the rest of the house too.</h2>
      <p>From a complete bathroom rebuild to a dripping tap, the same experienced team does the work, to the same standard.</p>
    </div>
    <div class="services">
      <article class="service service--feature">
        <div class="service-body">
          <span class="tag">Our specialism</span>
          <h3>Luxury bathrooms, en-suites &amp; wet rooms</h3>
          <p>Full design-and-fit projects, from stripping out the old room to the last bead of silicone.</p>
          <ul>
            <li>Strip-out, new pipework and first fix</li>
            <li>Electricians, plasterers and tilers organised for you</li>
            <li>Walk-in showers, wet rooms and built-in baths</li>
            <li>Underfloor heating and towel radiators</li>
          </ul>
          <a class="text-link" href="bathroom-fitters-castleford.html">Bathroom fitting in Castleford {ICON['arrow']}</a>
        </div>
        {img('shower-room', 'Walk-in shower room with glass screen, rainfall shower head and dark textured tiles')}
      </article>
      <article class="service service--photo">
        {img('kaye-after', 'Finished kitchen with gloss units, metro-tile splashback and under-cabinet lighting')}
        <div class="service-body">
          <h3>Kitchens</h3>
          <p>Kitchens planned and installed to the same standard as our bathrooms, including plumbing for sinks and appliances.</p>
          <a class="text-link service-link" href="kitchen-fitters-castleford.html">Kitchen fitting {ICON['arrow']}</a>
        </div>
      </article>
      <article class="service">
        <span class="service-icon">{ICON['flame']}</span>
        <h3>Boilers, radiators &amp; heating</h3>
        <p>Boiler and radiator work, towel rails, underfloor heating and heating repairs.</p>
        <a class="text-link service-link" href="plumbing-heating-castleford.html">Plumbing &amp; heating repairs {ICON['arrow']}</a>
      </article>
      <article class="service">
        <span class="service-icon">{ICON['tap']}</span>
        <h3>Taps, leaks &amp; small jobs</h3>
        <p>Replacement taps, leaking pipes, toilets and showers. No job is too small.</p>
        <a class="text-link service-link" href="plumbing-heating-castleford.html">Small plumbing jobs {ICON['arrow']}</a>
      </article>
      <article class="service service--urgent">
        <span class="service-icon">{ICON['drop']}</span>
        <h3>24-hour emergency call-outs</h3>
        <p>Burst pipe, leak or no water? Ring the mobile, day or night, for a fast response.</p>
        <a class="urgent-number" href="tel:{MOB[1]}">{MOB[0]}</a>
        <a class="text-link service-link urgent-link" href="emergency-plumber-castleford.html">What to do in an emergency {ICON['arrow']}</a>
      </article>
    </div>
  </div>
</section>

<section class="band band--ink" id="work">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our work</span>
      <h2>Every job photographed, from strip-out to finish.</h2>
      <p>Choose a project to see how the room looked before, part-way through and on the day we handed it over.</p>
    </div>
    <div class="viewer-tabs" role="tablist" aria-label="Projects">'''
    for i, pid in enumerate(HOME_TABS):
        p = P[pid]
        sel = 'true' if i == 0 else 'false'
        h += f'\n      <button class="viewer-tab" role="tab" id="tab-{pid}" aria-controls="panel-{pid}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}" type="button">{E(p["title"])}</button>'
    h += '\n    </div>'
    for i, pid in enumerate(HOME_TABS):
        p = P[pid]
        hid = '' if i == 0 else ' hidden'
        meta = p['kind'] + (f' &middot; {E(p["place"])}' if p['place'] else '')
        h += f'\n    <div class="viewer-panel" role="tabpanel" id="panel-{pid}" aria-labelledby="tab-{pid}" tabindex="0"{hid}>\n      <ol class="stages">'
        for st, name, alt in p['stages']:
            sz = '(max-width: 640px) 92vw, 460px' if st == 'after' else '(max-width: 640px) 46vw, 300px'
            h += f'\n        <li class="stage stage--{st}"><figure style="margin:0">{img(name, alt, lazy=False, low=(i > 0), sizes=sz)}<figcaption class="stage-label"><i></i>{STAGE_NAME[st]}</figcaption></figure></li>'
        h += f'\n      </ol>\n      <div class="viewer-notes">\n        <span class="meta">{meta}</span>\n        <h3>{E(p["title"])}</h3>\n        <p>{E(p["desc"])}</p>'
        if p.get('quote'):
            r = RV[p['quote']]
            h += f'\n        <blockquote>{E(r["text"].split(". ")[0])}.<cite>{E(r["name"])}{", " + E(r["place"]) if r["place"] else ""}</cite></blockquote>'
        h += f'\n        <a class="text-link viewer-cta" href="#contact">Plan a room like this {ICON["arrow"]}</a>'
        h += '\n      </div>\n    </div>'
    h += f'''
    <div class="viewer-foot">
      <p>Ten projects photographed in full, including period bathrooms, en-suites and a kitchen.</p>
      <a class="btn btn--line-light" href="work.html">View all our work {ICON['arrow']}</a>
    </div>
  </div>
</section>

<section class="band" id="process">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How a bathroom job runs</span>
      <h2>One person in charge, from first visit to handover.</h2>
      <p>You won&rsquo;t be left chasing separate trades. Craig plans the job and coordinates everyone who works on it.</p>
    </div>
    <ol class="steps">
      <li class="step"><div class="step-num"><b>01</b></div><h3>Home visit</h3><p>Craig comes out at a time that suits you, measures up and talks through layout, products and budget.</p></li>
      <li class="step"><div class="step-num"><b>02</b></div><h3>Plan &amp; quote</h3><p>You get a clear plan for the room and a written price before any work is booked in.</p></li>
      <li class="step"><div class="step-num"><b>03</b></div><h3>Strip-out &amp; build</h3><p>We take the room back, sort the pipework and bring in the electricians, plasterers and tilers in the right order. Craig is your one point of contact throughout.</p></li>
      <li class="step"><div class="step-num"><b>04</b></div><h3>Finish &amp; handover</h3><p>Every detail finished properly, with the house left clean and tidy at the end of each day.</p></li>
    </ol>
    <div class="process-note">
      <p><strong>How long does it take?</strong> It depends on the room. As a guide, Steve in Whitkirk had his full bathroom replaced in two weeks, start to finish.</p>
      <a class="text-link" href="#contact">Book a home visit {ICON['arrow']}</a>
    </div>
  </div>
</section>

<section class="band band--white" id="reviews">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Reviews</span>
      <h2>What our customers say.</h2>
      <p>Written by customers across Castleford, Pontefract, Leeds and beyond.</p>
    </div>
    <div class="reviews">
      <figure class="review-feature" style="margin:0">
        {ICON['quote']}
        <blockquote style="margin:0"><p>{E(RV['pat']['text'])}</p></blockquote>
        <footer>{review_footer(RV['pat'])}</footer>
      </figure>
      <p class="swipe-hint" aria-hidden="true">Swipe for more reviews <span>&rarr;</span></p>
      <div class="review-grid">'''
    for r in REVIEWS[1:]:
        h += f'\n        <figure class="review"><blockquote style="margin:0"><p>{E(r["text"])}</p></blockquote><footer>{review_footer(r)}</footer></figure>'
    h += f'''
      </div>
    </div>
  </div>
</section>

<section class="band band--ink cta-band">
  <div class="wrap">
    <div>
      <h2>Thinking about your own bathroom or kitchen?</h2>
      <p class="cta-sub">Tell us about the room and Craig will arrange a visit at a time that suits you.</p>
    </div>
    <div class="hero-actions">
      <a class="btn btn--brass" href="#contact">Request a quote {ICON['arrow']}</a>
      <a class="btn btn--line-light" href="tel:{MOB[1]}">{ICON['phone']}Call {MOB[0]}</a>
    </div>
  </div>
</section>

<section class="band" id="areas">
  <div class="wrap areas">
    <figure class="map-card" style="margin:0">
      {build_map()}
      <figcaption>Drawn to scale. Dashed rings at 10 km and 20 km from Castleford.</figcaption>
    </figure>
    <div class="areas-copy">
      <span class="eyebrow">Areas we cover</span>
      <h2>Based in Castleford, working across Leeds and West Yorkshire.</h2>
      <p>We cover the towns around Castleford and across Leeds, and have travelled as far as Harrogate for bathroom projects.</p>
      <ul class="chips">
        {area_chips()}
      </ul>
      <div class="base-card">
        {ICON['pin']}
        <address>{ADDR}</address>
        <span>Not sure if we cover you? Call or send your postcode with your enquiry.</span>
        <a class="text-link" href="areas.html">See every area we cover {ICON['arrow']}</a>
      </div>
    </div>
  </div>
</section>

{faq_section(HOME_FAQ, 'Questions customers ask us.', 'Straight answers about cost, timings, call-outs and the areas we cover.')}

<section class="band contact" id="contact">
  <div class="wrap">
    <div class="contact-copy">
      <span class="eyebrow">Request a quote</span>
      <h2>Tell us about your job.</h2>
      <p>Send a few details and Craig will get back to you to arrange a visit. Prefer to talk? Ring either number.</p>
      <ul class="contact-lines">
        <li><span>Office</span><a href="tel:{LAND[1]}">{LAND[0]}</a></li>
        <li><span>Mobile</span><a href="tel:{MOB[1]}">{MOB[0]}</a></li>
        <li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span>Address</span><address>{ADDR}</address></li>
      </ul>
      <div class="urgent-note">{ICON['alert']}<p>Water leaking right now? Don&rsquo;t use the form. Call <a href="tel:{MOB[1]}">{MOB[0]}</a>.</p></div>
    </div>
    <div class="form-card">
      <h3>Request a quote</h3>
      <p>It takes about a minute. We only use your details to reply to you.</p>
      <form id="quote-form" class="form-grid" novalidate>
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
        <div class="field"><label for="f-email">Email <small>(optional)</small></label><input id="f-email" name="email" type="email" autocomplete="email"></div>
        <div class="field"><label for="f-postcode">Postcode</label><input id="f-postcode" name="postcode" autocomplete="postal-code" required placeholder="e.g. WF10 4AF"></div>
        <div class="field field--full"><label for="f-job">Type of job</label>
          <select id="f-job" name="job" required>
            <option value="New bathroom">New bathroom</option>
            <option value="En-suite or wet room">En-suite or wet room</option>
            <option value="Kitchen">Kitchen</option>
            <option value="Heating or radiators">Heating or radiators</option>
            <option value="Taps, leak or small job">Taps, leak or small job</option>
            <option value="Something else">Something else</option>
          </select></div>
        <div class="field field--full"><label for="f-message">Tell us about the job</label><textarea id="f-message" name="message" required placeholder="Room size, what you'd like, and when you're hoping to start"></textarea></div>
        <div class="form-actions">
          <button class="btn btn--brass" type="submit">Send enquiry {ICON['arrow']}</button>
          <p>Or call {LAND[0]} / {MOB[0]}</p>
        </div>
        <p class="form-status" id="form-status" role="status" hidden>Your email app should now open with your details filled in. Press send there to reach us. If nothing opened, email {EMAIL} or call {MOB[0]}.</p>
      </form>
    </div>
  </div>
</section>
</main>'''
    h += footer('home')
    return h

# ---------------- Work page ----------------
def work():
    h = head('Bathroom & Kitchen Projects in Castleford | Our Work',
             'Before, during and after photos of bathrooms, en-suites and kitchens fitted by C Jackson Plumbing in Castleford, Pontefract and West Yorkshire.',
             'work.html', ld(business(), crumbs([('Our work', 'work.html')]), {"@type": "CollectionPage", "@id": SITE + "work.html#page", "name": "Our work", "url": SITE + "work.html", "about": {"@id": SITE + "#business"}}))
    h += header('work')
    h += '''
<main>
<section class="page-head">
  <div class="wrap">
    {crumb_nav([('Our work', 'work.html')])}
    <span class="eyebrow">Our work</span>
    <h1>Bathrooms and kitchens we&rsquo;ve rebuilt in Castleford and West Yorkshire.</h1>
    <p>Every project below was planned and installed by our team. The photos run in order: how the room looked when we arrived, the work in progress, and the finished room. Tap any photo to enlarge it.</p>
    <nav class="jump" aria-label="Jump to a project">'''
    for p in PROJECTS:
        h += f'<a href="#{p["id"]}">{E(p["title"])}</a>'
    h += '</nav>\n  </div>\n</section>\n<div class="projects">'
    for p in PROJECTS:
        meta = p['kind'] + (f' &middot; {E(p["place"])}' if p['place'] else '')
        h += f'''
<article class="project" id="{p['id']}">
  <div class="wrap">
    <div class="project-info">
      <span class="meta">{meta}</span>
      <h2>{E(p['title'])}</h2>
      <p>{E(p['desc'])}</p>'''
        if p.get('quote'):
            r = RV[p['quote']]
            h += f'\n      <blockquote>{E(r["text"])}<cite>{E(r["name"])}{", " + E(r["place"]) if r["place"] else ""}</cite></blockquote>'
        h += '\n    </div>\n    <ul class="gallery">'
        stages = p['stages']; extras = p.get('extras', [])
        kinds = [st for st, _, _ in stages]
        items = []
        for st, n, a in stages:
            # On phones: the main finished photo is full width; a lone before/during photo is too.
            wide = st == 'after' or (st in ('before', 'during') and not ('before' in kinds and 'during' in kinds))
            items.append((st, n, a, wide))
        for k, (n, a) in enumerate(extras):
            items.append(('after', n, a, len(extras) % 2 == 1 and k == len(extras) - 1))
        for st, n, a, wide in items:
            cap = f'{p["title"]}: {STAGE_NAME[st]}'
            wcls = ' is-wide' if wide else ''
            h += f'\n      <li class="stage stage--{st}{wcls}"><button type="button" data-full="img/{n}.jpg" data-caption="{E(cap)}">{img(n, a, sizes=GSZ)}</button><span class="stage-label"><i></i>{STAGE_NAME[st]}</span></li>'
        h += '\n    </ul>\n  </div>\n</article>'
    h += f'''
</div>
<section class="band band--ink cta-band">
  <div class="wrap">
    <div>
      <h2>Planning a new bathroom or kitchen?</h2>
      <p class="cta-sub">Tell us about the room and Craig will arrange a visit at a time that suits you.</p>
    </div>
    <div class="hero-actions">
      <a class="btn btn--brass" href="index.html#contact">Request a quote {ICON['arrow']}</a>
      <a class="btn btn--line-light" href="tel:{LAND[1]}">{ICON['phone']}Call {LAND[0]}</a>
    </div>
  </div>
</section>
</main>
<dialog class="lightbox" id="lightbox" aria-label="Photo viewer">
  <button class="lb-close" type="button" aria-label="Close photo">{ICON['close']}</button>
  <figure><img src="" alt=""><figcaption></figcaption></figure>
</dialog>'''
    h += footer('work')
    return h


# =====================================================================
# SEO: structured data, FAQs, service pages, areas page, crawler files
# =====================================================================
AREA_NAMES = ['Castleford', 'Pontefract', 'Methley', 'Rothwell', 'Garforth', 'Kippax', 'Whitkirk', 'Roundhay', 'Leeds', 'Harrogate', 'West Yorkshire']

def ld(*nodes):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(nodes)}, ensure_ascii=False) + '</script>\n'

def business():
    return {
      "@type": "Plumber", "@id": SITE + "#business", "name": "C Jackson Plumbing",
      "slogan": "Providing 24 hour plumbing services",
      "description": "Family-owned plumbing firm in Castleford, West Yorkshire, specialising in luxury bathrooms, en-suites, wet rooms and kitchens, with 24-hour emergency call-outs. Fully insured with over 15 years of experience.",
      "url": SITE, "telephone": LAND[1], "email": EMAIL,
      "contactPoint": [
        {"@type": "ContactPoint", "telephone": LAND[1], "contactType": "customer service", "areaServed": "GB", "availableLanguage": "English"},
        {"@type": "ContactPoint", "telephone": MOB[1], "contactType": "emergency", "areaServed": "GB", "availableLanguage": "English"}],
      "logo": SITE + "img/brand/cjackson-logo-full.png", "image": SITE + "img/brand/og-image.jpg",
      "address": {"@type": "PostalAddress", "streetAddress": "75 Lower Oxford Street", "addressLocality": "Castleford", "addressRegion": "West Yorkshire", "postalCode": "WF10 4AF", "addressCountry": "GB"},
      "hasMap": MAPS,
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}],
      "areaServed": [{"@type": "Place", "name": n} for n in AREA_NAMES],
      "knowsAbout": ["Bathroom fitting", "En-suite installation", "Wet rooms", "Walk-in showers", "Kitchen fitting", "Emergency plumbing", "Leak repairs", "Radiators", "Underfloor heating", "Heating repairs"],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Plumbing and bathroom services", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE + u}} for n, u in SERVICE_LINKS]},
    }

SERVICE_LINKS = [('Bathroom fitting', 'bathroom-fitters-castleford.html'), ('Kitchen fitting', 'kitchen-fitters-castleford.html'),
                 ('Plumbing and heating repairs', 'plumbing-heating-castleford.html'), ('24-hour emergency plumber', 'emergency-plumber-castleford.html')]

def website():
    return {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "C Jackson Plumbing", "publisher": {"@id": SITE + "#business"}, "inLanguage": "en-GB"}

def crumbs(items):
    lst = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE}]
    for i, (name, path) in enumerate(items, start=2):
        lst.append({"@type": "ListItem", "position": i, "name": name, "item": SITE + path})
    return {"@type": "BreadcrumbList", "itemListElement": lst}

def crumb_nav(items):
    parts = ['<a href="index.html">Home</a>'] + [f'<span aria-current="page">{E(n)}</span>' if i == len(items) - 1 else f'<a href="{u}">{E(n)}</a>' for i, (n, u) in enumerate(items)]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(parts) + '</nav>'

def service_schema(name, path, desc, stype):
    return {"@type": "Service", "@id": SITE + path + "#service", "name": name, "serviceType": stype, "description": desc, "url": SITE + path,
            "provider": {"@id": SITE + "#business"}, "areaServed": [{"@type": "Place", "name": n} for n in AREA_NAMES]}

# ---- FAQ bank: every answer is based on facts confirmed for this business ----
FAQ = {
 'cost': ("How much does a new bathroom cost in Castleford?",
          "Every bathroom is different, so we don't quote a price until we've seen the room. Craig visits, measures up and talks through layout, products and budget, then gives you a written price before anything is booked."),
 'kcost': ("How much does a new kitchen cost?",
          "It depends on the size of the room, the units and how much work the walls and pipework need. Craig visits, measures up and gives you a written price before anything is booked."),
 'duration': ("How long does it take to fit a bathroom?",
          "It depends on the size of the room and how much work is involved. As a guide, Steve in Whitkirk had his full bathroom replaced in two weeks from start to finish."),
 'trades': ("Do you organise the tiler, plasterer and electrician?",
          "Yes. Craig books and coordinates the electricians, plasterers and tilers on every job, so you have one point of contact from the first visit to handover."),
 'wetroom': ("Can you fit walk-in showers and wet rooms?",
          "Yes. Walk-in showers, wet rooms and built-in baths are part of our bathroom work. Richard in Kippax had a large job that involved removing joists and fitting underfloor heating."),
 'emergency': ("Do you offer 24-hour emergency call-outs?",
          "Yes. For burst pipes, serious leaks or no water, call Craig's mobile on 07872 584 324, day or night."),
 'stopcock': ("What should I do while I wait for an emergency plumber?",
          "Turn off the water at your stopcock, which is usually under the kitchen sink or where the water pipe enters the house. If water is near electrics, switch off the electricity at the consumer unit if it is safe to do so. Open the cold taps to drain the pipes, and catch drips in buckets."),
 'small': ("Do you take on small plumbing jobs?",
          "Yes. Replacement taps, leaking pipes, toilets, showers and radiators are all welcome. No job is too small."),
 'heating': ("Do you repair radiators and heating?",
          "Yes. We carry out boiler and radiator work, replace towel rails, fit underfloor heating and repair heating systems."),
 'kitchens': ("Do you fit kitchens as well as bathrooms?",
          "Yes. We plan and install kitchens to the same standard as our bathrooms, including all the plumbing for sinks and appliances."),
 'areas': ("Which areas do you cover?",
          "We're based at 75 Lower Oxford Street in Castleford and cover Pontefract, Methley, Rothwell, Garforth, Kippax, Whitkirk, Roundhay, Leeds and the wider West Yorkshire area. We have also travelled to Harrogate for bathroom projects."),
 'insured': ("Are you insured?",
          "Yes. C Jackson Plumbing is fully insured on every job."),
 'experience': ("How long have you been in business?",
          "C Jackson Plumbing is a family-owned firm with over 15 years of experience fitting bathrooms, kitchens and heating."),
}
HOME_FAQ = ['cost', 'duration', 'trades', 'emergency', 'small', 'areas', 'insured']

def faq_schema(keys):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": FAQ[k][0], "acceptedAnswer": {"@type": "Answer", "text": FAQ[k][1]}} for k in keys]}

def faq_section(keys, title, sub, band='band band--white'):
    items = ''.join(f'\n      <details class="faq-item"{" open" if i == 0 else ""}><summary><h3>{E(FAQ[k][0])}</h3><span class="faq-icon" aria-hidden="true"></span></summary><p>{E(FAQ[k][1])}</p></details>' for i, k in enumerate(keys))
    return f'''<section class="{band}" id="faq">
  <div class="wrap faq-wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>{title}</h2>
      <p>{sub}</p>
    </div>
    <div class="faq">{items}
    </div>
  </div>
</section>'''

def town_slug(n): return n.lower().replace(' ', '-')

def area_chips():
    out = []
    for n in ['Castleford', 'Pontefract', 'Methley', 'Rothwell', 'Garforth', 'Kippax', 'Whitkirk', 'Roundhay', 'Leeds', 'Harrogate']:
        cls = ' class="is-base"' if n == 'Castleford' else ''
        out.append(f'<li{cls}><a href="areas.html#{town_slug(n)}">{n}</a></li>')
    return ''.join(out)

def call_buttons(light=False):
    line = 'btn--line-light' if light else 'btn--line'
    return f'''<div class="hero-actions">
        <a class="btn btn--brass" href="index.html#contact">Request a quote {ICON['arrow']}</a>
        <a class="btn {line}" href="tel:{LAND[1]}">{ICON['phone']}Call {LAND[0]}</a>
      </div>'''

def cta_band(title, sub, emergency=False):
    actions = (f'<div class="hero-actions"><a class="btn btn--brass btn--big" href="tel:{MOB[1]}">{ICON["phone"]}Call {MOB[0]}</a></div>'
               if emergency else call_buttons(light=True))
    return f'''<section class="band band--ink cta-band">
  <div class="wrap">
    <div>
      <h2>{title}</h2>
      <p class="cta-sub">{sub}</p>
    </div>
    {actions}
  </div>
</section>'''

def project_cards(ids):
    cards = []
    for pid in ids:
        p = P[pid]
        name, alt = [(n, a) for st, n, a in p['stages'] if st == 'after'][0]
        meta = p['kind'] + (f' &middot; {E(p["place"])}' if p['place'] else '')
        cards.append(f'''
      <a class="project-card" href="work.html#{pid}">
        {img(name, alt, sizes='(max-width: 640px) 92vw, 380px')}
        <span class="project-card-body"><span class="meta">{meta}</span><strong>{E(p['title'])}</strong><span class="project-card-link">See before &amp; after {ICON['arrow']}</span></span>
      </a>''')
    return '<div class="project-cards">' + ''.join(cards) + '\n    </div>'

def review_row(ids):
    return '<div class="review-row">' + ''.join(f'\n      <figure class="review"><blockquote style="margin:0"><p>{E(RV[r]["text"])}</p></blockquote><footer>{review_footer(RV[r])}</footer></figure>' for r in ids) + '\n    </div>'

def checklist(items):
    return '<ul class="checklist">' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>'

# ---- Service pages ----
SERVICES = [
 dict(path='bathroom-fitters-castleford.html', key='bathrooms', crumb='Bathroom fitting', stype='Bathroom installation',
      title='Bathroom Fitters in Castleford | C Jackson Plumbing',
      desc='Luxury bathroom, en-suite and wet room fitting in Castleford, Pontefract and Leeds. One family firm handles the strip-out, plumbing, tiling and electrics.',
      eyebrow='Bathroom fitting &middot; Castleford',
      h1='Bathroom fitters in Castleford, from strip-out to the last tile.',
      intro='Luxury bathrooms are our speciality. We plan and install complete bathrooms, en-suites and wet rooms across Castleford, Pontefract, Leeds and West Yorkshire. Craig runs every job personally, from the first visit to handover.',
      photo=('colin-michelle-after', 'Period-style bathroom with white metro tiles and a high-level cistern, fitted by C Jackson Plumbing'),
      body_h2='One firm for the whole bathroom.',
      body=['Most bathroom refits need four or five trades: a plumber, an electrician, a plasterer, a tiler and someone to take the old room out. We organise all of them and run the job in the right order, so you have one person to call instead of five.',
            'We fit everything from period-style bathrooms with metro tiles, high-level cisterns and Victorian-pattern floors to modern rooms with large-format porcelain, back-lit mirrors and wall-hung vanity units.',
            'Before any work is booked, Craig visits, measures up and gives you a written price.'],
      included=['Full strip-out and removal of the old suite', 'New pipework and first-fix plumbing', 'Electricians, plasterers and tilers organised for you',
                'Baths, showers, basins, WCs and vanity units', 'Walk-in showers, wet rooms and built-in baths', 'Underfloor heating, towel radiators and LED mirrors'],
      projects=['colin-michelle', 'joanne', 'dan', 'diane', 'barbara', 'crashley'], projects_h2='Bathrooms we&rsquo;ve fitted.',
      reviews=['steve', 'richard', 'joanne'], faq=['cost', 'duration', 'trades', 'wetroom', 'areas', 'insured'],
      cta=('Ready to plan your new bathroom?', 'Tell us about the room and Craig will arrange a home visit at a time that suits you.')),
 dict(path='kitchen-fitters-castleford.html', key='kitchens', crumb='Kitchen fitting', stype='Kitchen installation',
      title='Kitchen Fitters in Castleford | C Jackson Plumbing',
      desc='Kitchen fitting in Castleford, Pontefract and Leeds by a family-run plumbing firm. Units, worktops, splashbacks and all the plumbing for sinks and appliances.',
      eyebrow='Kitchen fitting &middot; Castleford',
      h1='Kitchen fitting in Castleford, planned and plumbed properly.',
      intro='We plan and install kitchens to the same standard as our bathrooms. As plumbers first, we get the sink, appliances and pipework right, and Craig coordinates the other trades so you deal with one person.',
      photo=('kaye-after', 'Fitted kitchen with gloss units, metro-tile splashback and under-cabinet lighting in West Yorkshire'),
      body_h2='Back to brick when it needs it.',
      body=['Some kitchens only need new units. Others need taking right back. On Kaye’s kitchen we stripped the room to bare brick, re-boarded the walls, fitted new units with a metro-tile splashback and under-cabinet lighting, and added a new shower room off the kitchen in the same job.',
            'Every kitchen starts with a home visit and a written price before anything is booked.'],
      included=['Strip-out of the old kitchen', 'Walls re-boarded and made good where needed', 'Units, worktops and splashbacks fitted',
                'Sinks, taps, dishwashers and washing machines plumbed in', 'Lighting and electrics organised with our electrician', 'Shower rooms and utility plumbing in the same job'],
      projects=['kaye'], projects_h2='A kitchen we&rsquo;ve fitted.',
      reviews=['meg', 'jilly', 'jason'], faq=['kcost', 'kitchens', 'trades', 'areas', 'insured'],
      cta=('Planning a new kitchen?', 'Tell us about the room and Craig will arrange a home visit at a time that suits you.')),
 dict(path='plumbing-heating-castleford.html', key='plumbing', crumb='Plumbing & heating', stype='Plumbing and heating repairs',
      title='Local Plumber in Castleford | Plumbing & Heating Repairs',
      desc='Local plumber in Castleford for taps, leaks, toilets, showers, radiators and heating repairs. Small jobs welcome. Fully insured, 15+ years’ experience.',
      eyebrow='Plumbing &amp; heating &middot; Castleford',
      h1='Plumbing and heating repairs in Castleford. No job too small.',
      intro='Alongside full bathroom installs, we take on everyday plumbing and heating work across Castleford, Pontefract and Leeds: dripping taps, leaking pipes, toilets, showers, radiators and heating faults.',
      photo=('tina-2', 'Chrome towel radiator fitted on light grey tiles'),
      body_h2='The same care on a tap as on a full bathroom.',
      body=['Small jobs get the same attention as our bathroom projects. We turn up when we say we will, explain what’s wrong and leave the house clean and tidy.',
            'If water is escaping right now, don’t wait for a reply to a form. Call the mobile on 07872 584 324, day or night.'],
      included=['Replacement taps and mixers', 'Leaking pipes and joints', 'Toilet and cistern repairs and replacements',
                'Shower repairs and replacements', 'Radiators, towel rails and underfloor heating', 'Boiler, radiator and heating repairs'],
      projects=['tina', 'dan'], projects_h2='Recent work.',
      reviews=['paul', 'jonathan', 'meg'], faq=['small', 'heating', 'emergency', 'areas', 'insured', 'experience'],
      cta=('Need a plumber in Castleford?', 'Call the office, or send a few details and we’ll get back to you.')),
]

def service_page(d):
    pg = service_schema(d['crumb'], d['path'], d['desc'], d['stype'])
    h = head(d['title'], d['desc'], d['path'], ld(business(), pg, crumbs([(d['crumb'], d['path'])]), faq_schema(d['faq'])))
    h += header(d['key'])
    photo, alt = d['photo']
    body = ''.join(f'\n        <p>{E(t)}</p>' for t in d['body'])
    h += f'''
<main>
<section class="page-head svc-head">
  <div class="wrap">
    <div class="svc-head-copy">
      {crumb_nav([(d['crumb'], d['path'])])}
      <span class="eyebrow">{d['eyebrow']}</span>
      <h1>{E(d['h1'])}</h1>
      <p>{E(d['intro'])}</p>
      {call_buttons()}
      <p class="hero-reassure">Home visit and written price before anything is booked. Fully insured.</p>
    </div>
    <figure class="svc-photo">{img(photo, alt, lazy=False, high=True, sizes='(max-width: 900px) 92vw, 460px')}</figure>
  </div>
</section>

<section class="band band--white">
  <div class="wrap split">
    <div class="prose">
      <h2>{d['body_h2']}</h2>{body}
    </div>
    <div class="included-card">
      <h3>What&rsquo;s included</h3>
      {checklist(d['included'])}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head section-head--split">
      <div style="display:grid;gap:14px"><span class="eyebrow">Our work</span><h2>{d['projects_h2']}</h2></div>
      <a class="text-link" href="work.html">See all projects {ICON['arrow']}</a>
    </div>
    {project_cards(d['projects'])}
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Reviews</span><h2>What customers say.</h2></div>
    {review_row(d['reviews'])}
  </div>
</section>

{faq_section(d['faq'], 'Common questions.', 'If your question isn&rsquo;t here, call {0} or send it with your enquiry.'.format(LAND[0]), band='band')}

{cta_band(d['cta'][0], d['cta'][1])}
</main>'''
    h += footer(d['key'])
    return h

# ---- Emergency page ----
def emergency_page():
    path = 'emergency-plumber-castleford.html'
    title = '24 Hour Emergency Plumber in Castleford | C Jackson Plumbing'
    desc = 'Burst pipe, leak or no water? Call C Jackson Plumbing on 07872 584 324, day or night. 24-hour emergency plumber for Castleford, Pontefract and Leeds.'
    faqk = ['emergency', 'stopcock', 'small', 'areas', 'insured']
    h = head(title, desc, path, ld(business(), service_schema('24-hour emergency plumber', path, desc, 'Emergency plumbing'), crumbs([('Emergency plumber', path)]), faq_schema(faqk)))
    h += header('emergency')
    steps = [('Turn off the water', 'Close the stopcock. It is usually under the kitchen sink or where the water pipe enters the house.'),
             ('Make electrics safe', 'If water is near sockets, lights or the consumer unit, switch off the electricity at the consumer unit if it is safe to reach.'),
             ('Drain and contain', 'Open the cold taps to drain the pipes, catch drips in buckets and move valuables away from the water.'),
             ('Call the mobile', f'Ring {MOB[0]}, day or night, and tell us what you can see.')]
    st = ''.join(f'<li class="step"><div class="step-num"><b>0{i}</b></div><h3>{E(t)}</h3><p>{E(x)}</p></li>' for i, (t, x) in enumerate(steps, 1))
    h += f'''
<main>
<section class="emergency-head">
  <div class="wrap">
    {crumb_nav([('Emergency plumber', path)])}
    <span class="eyebrow">24-hour emergency plumber &middot; Castleford</span>
    <h1>Emergency plumber in Castleford, day or night.</h1>
    <p class="emergency-lead">Burst pipe, serious leak or no water? Call Craig&rsquo;s mobile now. We cover Castleford, Pontefract, Leeds and the surrounding West Yorkshire towns.</p>
    <a class="emergency-call" href="tel:{MOB[1]}">{ICON['phone']}<span><small>Call now, 24 hours</small>{MOB[0]}</span></a>
    <p class="emergency-alt">Not urgent? Call the office on <a href="tel:{LAND[1]}">{LAND[0]}</a> or <a href="index.html#contact">send us the details</a>.</p>
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">While you wait</span><h2>What to do right now.</h2><p>These steps limit the damage before we arrive.</p></div>
    <ol class="steps">{st}</ol>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="prose">
      <h2>Emergencies we deal with.</h2>
      <p>We&rsquo;re a family-run firm based in Castleford with over 15 years of experience, and we&rsquo;re fully insured. When you call the mobile you speak to us directly, not a call centre.</p>
      <p>Once the emergency is under control, we can also put right any damage to the bathroom or kitchen.</p>
    </div>
    <div class="included-card">
      <h3>We can help with</h3>
      {checklist(['Burst and leaking pipes', 'Leaking taps, toilets and showers', 'Overflowing cisterns', 'Loss of water supply', 'Radiator and heating leaks'])}
    </div>
  </div>
</section>

{faq_section(faqk, 'Emergency plumbing questions.', 'Quick answers for when something has gone wrong.')}

{cta_band('Water escaping right now?', 'Turn off the stopcock, then call the mobile. We answer day or night.', emergency=True)}
</main>'''
    h += footer('emergency')
    return h

# ---- Areas page ----
def miles_from_base(lat, lon):
    b_lat, b_lon = 53.7250, -1.3620
    r = 3958.8
    p1, p2 = math.radians(b_lat), math.radians(lat)
    dphi, dl = math.radians(lat - b_lat), math.radians(lon - b_lon)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))

TOWN_INFO = [
 ('Castleford', 53.7250, -1.3620, 'Plumber in Castleford', 'Castleford is home. We&rsquo;re based at 75 Lower Oxford Street, so Castleford households get the quickest response to emergencies and the easiest home visits for new bathrooms and kitchens.', ['joanne']),
 ('Pontefract', 53.6910, -1.3120, 'Plumber in Pontefract', 'We fit bathrooms and handle plumbing and heating jobs across Pontefract. Pat&rsquo;s bathroom in Pontefract was one we put right after a previous fitter left it unfinished.', ['pat']),
 ('Methley', 53.7350, -1.4090, 'Plumber in Methley', 'Methley is a short drive from our Castleford base, and we cover it for bathroom fitting, repairs and emergency call-outs.', []),
 ('Rothwell', 53.7486, -1.4780, 'Plumber in Rothwell', 'We cover Rothwell for complete bathroom refits, kitchens, everyday plumbing repairs and 24-hour emergencies.', []),
 ('Garforth', 53.7920, -1.3820, 'Plumber in Garforth', 'We work across Garforth on bathrooms, kitchens and plumbing and heating repairs, with emergency call-outs day or night.', []),
 ('Kippax', 53.7670, -1.3700, 'Plumber in Kippax', 'In Kippax we&rsquo;ve handled large bathroom projects, including one that involved removing joists and fitting underfloor heating.', ['richard']),
 ('Whitkirk', 53.7990, -1.4560, 'Plumber in Whitkirk', 'We&rsquo;ve fitted several bathrooms in Whitkirk, including a full replacement completed in two weeks.', ['steve', 'jonathan']),
 ('Roundhay', 53.8347, -1.5023, 'Plumber in Roundhay', 'We cover Roundhay for bathroom and en-suite installations, kitchens and plumbing repairs.', []),
 ('Leeds', 53.7997, -1.5492, 'Plumber in Leeds', 'We work across east and south Leeds for bathroom refits, kitchens and plumbing and heating work.', []),
 ('Harrogate', 53.9921, -1.5418, 'Bathroom projects in Harrogate', 'We have travelled to Harrogate for bathroom projects. Get in touch to talk about yours.', ['meg', 'jason']),
]

def areas_page():
    path = 'areas.html'
    title = 'Areas We Cover | Castleford, Pontefract & Leeds Plumber'
    desc = 'Bathrooms, kitchens, plumbing and 24-hour emergencies across Castleford, Pontefract, Methley, Rothwell, Garforth, Kippax, Whitkirk, Roundhay and Leeds.'
    h = head(title, desc, path, ld(business(), crumbs([('Areas we cover', path)])))
    h += header('areas')
    towns = ''
    for name, lat, lon, h2, text, revs in TOWN_INFO:
        dist = '' if name == 'Castleford' else f'<span class="town-dist">About {round(miles_from_base(lat, lon))} miles from our base</span>'
        rv = ''.join(f'<figure class="review"><blockquote style="margin:0"><p>{E(RV[r]["text"])}</p></blockquote><footer>{review_footer(RV[r])}</footer></figure>' for r in revs)
        towns += f'''
    <article class="town" id="{town_slug(name)}">
      <div class="town-copy">
        <h2>{h2}</h2>{dist}
        <p>{text}</p>
        <p class="town-services"><a href="bathroom-fitters-castleford.html">Bathroom fitting</a> &middot; <a href="kitchen-fitters-castleford.html">Kitchens</a> &middot; <a href="plumbing-heating-castleford.html">Plumbing &amp; heating</a> &middot; <a href="emergency-plumber-castleford.html">24-hour emergencies</a></p>
      </div>
      {'<div class="town-reviews">' + rv + '</div>' if rv else ''}
    </article>'''
    h += f'''
<main>
<section class="page-head">
  <div class="wrap areas">
    <div class="areas-copy">
      {crumb_nav([('Areas we cover', path)])}
      <span class="eyebrow">Areas we cover</span>
      <h1>Plumbing and bathrooms across Castleford, Pontefract and Leeds.</h1>
      <p>We&rsquo;re a family-run firm based at 75 Lower Oxford Street, Castleford WF10 4AF. These are the towns we work in most, with reviews from customers in each.</p>
      <ul class="chips">{area_chips()}</ul>
    </div>
    <figure class="map-card" style="margin:0">
      {build_map()}
      <figcaption>Drawn to scale. Dashed rings at 10 km and 20 km from Castleford.</figcaption>
    </figure>
  </div>
</section>
<section class="band band--white">
  <div class="wrap towns">{towns}
  </div>
</section>
{cta_band('Not sure if we cover you?', 'Call the office on ' + LAND[0] + ' or send your postcode with your enquiry.')}
</main>'''
    h += footer('areas')
    return h

# ---- Old Weebly URLs: keep their links and rankings by redirecting to the new pages ----
REDIRECTS = {'installations.html': 'work.html', 'testimonials.html': 'index.html#reviews', 'contact.html': 'index.html#contact'}
def redirect_page(target):
    canon = SITE + target.split('#')[0].replace('index.html', '')
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Moved | C Jackson Plumbing</title>
<link rel="canonical" href="{canon}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex, follow">
<script>location.replace({json.dumps(target)});</script>
</head><body><p>This page has moved to <a href="{target}">{target}</a>.</p></body></html>
'''

PAGES = [('', 1.0), ('bathroom-fitters-castleford.html', 0.9), ('emergency-plumber-castleford.html', 0.9), ('plumbing-heating-castleford.html', 0.8),
         ('kitchen-fitters-castleford.html', 0.8), ('work.html', 0.7), ('areas.html', 0.7)]

def sitemap():
    urls = ''.join(f'\n  <url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>' for p, pr in PAGES)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n'

def robots():
    return f'''# Search engines and AI assistants are welcome to read this site.
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: {SITE}sitemap.xml
'''

def llms():
    rv = '\n'.join(f'- "{r["text"]}" ({r["name"]}{", " + r["place"] if r["place"] else ""})' for r in REVIEWS)
    faqs = '\n\n'.join(f'### {q}\n{a}' for q, a in FAQ.values())
    return f'''# C Jackson Plumbing

> Family-owned plumbing firm in Castleford, West Yorkshire, UK. Specialists in luxury bathrooms, en-suites, wet rooms and kitchens, with 24-hour emergency call-outs. Fully insured, with over 15 years of experience. Craig runs every job and coordinates the electricians, plasterers and tilers, so customers have one point of contact.

## Contact
- Office: {LAND[0]}
- Mobile and 24-hour emergencies: {MOB[0]}
- Email: {EMAIL}
- Address: 75 Lower Oxford Street, Castleford, West Yorkshire WF10 4AF
- Website: {SITE}

## Services
- [Bathroom fitting]({SITE}bathroom-fitters-castleford.html): complete bathrooms, en-suites, wet rooms, walk-in showers, built-in baths, underfloor heating
- [Kitchen fitting]({SITE}kitchen-fitters-castleford.html): units, worktops, splashbacks, plumbing for sinks and appliances
- [Plumbing and heating repairs]({SITE}plumbing-heating-castleford.html): taps, leaks, toilets, showers, radiators, towel rails, boiler and heating repairs; small jobs welcome
- [24-hour emergency plumber]({SITE}emergency-plumber-castleford.html): burst pipes, leaks, loss of water, day or night

## Areas covered
Castleford, Pontefract, Methley, Rothwell, Garforth, Kippax, Whitkirk, Roundhay, Leeds and the wider West Yorkshire area. Has travelled to Harrogate for bathroom projects. Details: {SITE}areas.html

## Customer reviews
{rv}

## Frequently asked questions
{faqs}

## More
- [Before and after photos of installations]({SITE}work.html)
'''

pages = {'index.html': home(), 'work.html': work(), 'areas.html': areas_page(), 'emergency-plumber-castleford.html': emergency_page()}
for d in SERVICES:
    pages[d['path']] = service_page(d)
for src, dst in REDIRECTS.items():
    pages[src] = redirect_page(dst)
pages['sitemap.xml'] = sitemap()
pages['robots.txt'] = robots()
pages['llms.txt'] = llms()
for name, content in pages.items():
    open(OUT + name, 'w').write(content)
print(('LIVE' if LIVE else 'PREVIEW') + ' build:', ', '.join(pages))
