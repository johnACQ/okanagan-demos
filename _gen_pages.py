# Generate branded preview pages from the betts.html template.
TEMPLATE = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Website preview for {name} · by Apex ACQ</title>
<meta property="og:title" content="A free website preview for {name}">
<meta property="og:description" content="Built by Apex ACQ. Left is your site today, right is the version we'd build.">
<meta property="og:image" content="https://preview.apexacq.co/{img}">
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',Roboto,Arial,sans-serif}}
body{{background:#0b0b0b;color:#e8e8e8;line-height:1.55}}
.bar{{background:#000;border-bottom:1px solid #1c1c1c;padding:16px 24px;display:flex;align-items:center;gap:10px}}
.bar b{{color:#fff;font-weight:800;font-size:18px;letter-spacing:.3px}}
.bar b span{{color:#4baabf}}
.wrap{{max-width:1000px;margin:0 auto;padding:40px 20px 60px;text-align:center}}
h1{{font-size:30px;font-weight:800;color:#fff;margin-bottom:10px}}
h1 span{{color:#4baabf}}
.sub{{color:#9aa6b2;font-size:17px;max-width:700px;margin:0 auto 28px}}
.shot{{width:100%;border:1px solid #222;border-radius:12px;box-shadow:0 20px 50px rgba(0,0,0,.5)}}
.cap{{color:#7e8a96;font-size:13px;margin-top:10px}}
.cta{{margin:38px auto 0;background:#101820;border:1px solid #1f2b33;border-radius:16px;padding:30px 24px;max-width:680px}}
.cta h2{{color:#fff;font-size:22px;margin-bottom:8px}}
.cta p{{color:#9aa6b2;font-size:15px;margin-bottom:20px}}
.btn{{display:inline-block;background:#4baabf;color:#04222b;font-weight:800;font-size:17px;padding:15px 30px;border-radius:10px;text-decoration:none}}
.foot{{color:#5a646e;font-size:12px;margin-top:34px}}
</style></head><body>
<div class="bar"><b>APEX <span>ACQ</span></b><span style="color:#5a646e;font-size:13px">· free website preview</span></div>
<div class="wrap">
<h1>A free preview we built for <span>{name}</span></h1>
<p class="sub">{sub}</p>
<img class="shot" src="{img}" alt="{name} website before and after">
<p class="cap">Left: {domain} today · Right: the version Apex built</p>
<div class="cta">
<h2>Want something like this live?</h2>
<p>This is what we do for home-service contractors across BC. Here's how it works.</p>
<a class="btn" href="https://grow.apexacq.co">See how we work &#8594;</a>
</div>
<p class="foot">Built by Apex ACQ · Kelowna, BC · This preview is yours to keep.</p>
</div></body></html>'''

PAGES = [
 dict(key="aalto", name="Aalto Renovations", img="AALTO_before_after.png", domain="aaltorenovations.com",
      sub="No catch. Left is your site today, right is the version we'd build: a clean modern layout, your reviews showing, a tappable phone, and a spot to request a quote right up top instead of scrolling to find it."),
 dict(key="bigvalley", name="Big Valley Homes", img="BIGVALLEY_before_after.png", domain="bigvalleyhomes.ca",
      sub="No catch. Left is your site today, right is the version we'd build: 35 years and 500+ builds finally shown off, real reviews up top, a tappable phone, and a clear way for someone to start a project with you."),
 dict(key="aspen", name="Aspen Landscaping", img="ASPEN_before_after.png", domain="aspenlandscaping.ca",
      sub="No catch. Left is your site today, right is the version we'd build: 24 years of work shown off, a form right up top, and a clear way for someone to grab an on-site quote without scrolling to the bottom."),
 dict(key="gle", name="GLE Heating & Air", img="GLE_before_after.png", domain="gleheating.com",
      sub="No catch. Left is your site today, right is the version we'd build: your licenses front and centre, a clean quote form up top, your reviews showing, and a clear way to book service for a 30-year name."),
 dict(key="signature", name="Signature Siding", img="SIGNATURE_before_after.png", domain="signaturesiding.ca",
      sub="No catch. Left is your site today, right is the version we'd build: a modern hero instead of the early-2000s layout, your workmanship guarantee up top, and a quote form right there instead of on a separate page."),
]

for p in PAGES:
    html = TEMPLATE.format(**p)
    assert "—" not in html and "&mdash;" not in html, f"EM DASH in {p['key']}"
    open(f"/tmp/okanagan-demos/{p['key']}.html", "w").write(html)
    print("wrote", p["key"] + ".html")
