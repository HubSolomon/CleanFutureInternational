# -*- coding: utf-8 -*-
import pathlib, json

NAVY="#0A2540"; BLUE="#0F6FB5"; AQUA="#16B1C4"; TEAL="#0E9C8F"; GREEN="#3AA96B"
AMBER="#D99A2B"; CORAL="#D9674F"; LINE="#D9E4EE"; INK="#16232E"; MUTED="#5E7183"
SAND="#F4F8FB"; SAND2="#EAF2F8"

SHELL = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap">
  <style>
    body {{ margin: 0; font-family: 'Lato', 'Carlito', system-ui, sans-serif; color: {ink}; }}
    a {{ color: {blue}; }} a:hover {{ color: {navy}; }}
    * {{ box-sizing: border-box; }}
  </style>
</helmet>
<div style="width: 1000px; height: 700px; background: {bg}; padding: 44px 48px; display: flex; flex-direction: column; gap: 20px; overflow: hidden;">
  <div style="display: flex; align-items: baseline; gap: 14px;">
    <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.18em; text-transform: uppercase; color: {eyebrow};">{eyebrow_text}</div>
    <div style="flex-grow: 1; height: 1px; background: {line};"></div>
    <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: #93A6B5;">{tag}</div>
  </div>
  <div style="font-size: 34px; font-weight: 900; letter-spacing: -0.02em; color: {navy}; line-height: 1.08;">{title}</div>
  {body}
</div>
</x-dc>
</body>
</html>
"""

def shell(fn, eyebrow_text, eyebrow, tag, title, body, bg=SAND):
    html = SHELL.format(ink=INK, blue=BLUE, navy=NAVY, bg=bg, line=LINE,
                        eyebrow=eyebrow, eyebrow_text=eyebrow_text, tag=tag,
                        title=title, body=body)
    pathlib.Path(fn).write_text(html, encoding="utf-8")

def card(inner, accent=None, pad="16px 18px", bg="#fff", grow=""):
    top = f"border-top: 4px solid {accent};" if accent else ""
    return (f'<div style="background: {bg}; border: 1px solid {LINE}; border-radius: 10px; '
            f'padding: {pad}; {top} {grow}">{inner}</div>')

def h(t, size=15, color=None, mb=6):
    return f'<div style="font-size: {size}px; font-weight: 900; color: {color or NAVY}; margin-bottom: {mb}px; line-height: 1.2;">{t}</div>'

def p(t, size=13, color="#42535F", lh=1.5):
    return f'<div style="font-size: {size}px; line-height: {lh}; color: {color};">{t}</div>'

def grid(items, cols=3, gap=14, grow=True):
    g = "flex-grow: 1;" if grow else ""
    return (f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); '
            f'gap: {gap}px; {g}">' + "".join(items) + "</div>")

def row(items, gap=14, grow=True, align="stretch"):
    g = "flex-grow: 1;" if grow else ""
    return (f'<div style="display: flex; gap: {gap}px; align-items: {align}; {g}">' + "".join(items) + "</div>")

def chip(label, bg, color="#fff", w=None, fs=12):
    wd = f"width: {w}px;" if w else "flex-grow: 1;"
    return (f'<div style="{wd} background: {bg}; color: {color}; border-radius: 8px; padding: 11px 8px; '
            f'text-align: center; font-size: {fs}px; font-weight: 900; letter-spacing: 0.02em;">{label}</div>')

def arrow():
    return ('<div style="width: 14px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; '
            f'color: #9FB3C2; font-size: 15px; font-weight: 900;">&rsaquo;</div>')

print("helpers ready")

# ============ 1. MAIN — identity ============
body = row([
  f'''<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px;">
    {p("Clean Future International is a mission-driven international organization that solves practical community infrastructure problems — working where community need, engineering, finance, implementation and long-term operations meet.", 15, "#2B3B49", 1.6)}
    <div style="background: linear-gradient(135deg, #0A2540 0%, #0E4A75 55%, #0E9C8F 100%); border-radius: 12px; padding: 22px 24px;">
      <div style="font-size: 10px; font-weight: 900; letter-spacing: 0.18em; text-transform: uppercase; color: #8FE3E8; margin-bottom: 10px;">The defining distinction</div>
      <div style="font-size: 18px; line-height: 1.45; color: #F2FAFC;">Success is not a completed construction project. Success is <strong style="color:#fff;">a functioning asset that continues to deliver value</strong> to its intended community.</div>
    </div>
    {row([
      card(h("Not this", 13, CORAL) + p("Build → hand over → decline → replace", 12), CORAL, "13px 15px"),
      card(h("This", 13, TEAL) + p("Need → evidence → solution → capital → delivery → function → maintenance → measurement → reinvestment", 12), TEAL, "13px 15px"),
    ], grow=False)}
  </div>''',
  f'''<div style="width: 300px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px;">
    {card(f'<div style="font-size:40px;font-weight:900;color:{BLUE};line-height:1;">7</div>' + p("Strategic pillars", 12, MUTED), BLUE, "16px 18px")}
    {card(f'<div style="font-size:40px;font-weight:900;color:{AQUA};line-height:1;">12</div>' + p("Lifecycle stages", 12, MUTED), AQUA, "16px 18px")}
    {card(f'<div style="font-size:40px;font-weight:900;color:{TEAL};line-height:1;">12</div>' + p("Approval gates", 12, MUTED), TEAL, "16px 18px")}
    {card(f'<div style="font-size:40px;font-weight:900;color:{GREEN};line-height:1;">3</div>' + p("Money layers", 12, MUTED), GREEN, "16px 18px")}
  </div>'''
])
shell("Main.dc.html", "Clean Future International", AQUA, "CFI 2.0 · Operating model board", "The model, on one board", body)

# ============ 2. PROBLEM ============
causes = ["Problems poorly defined","Insufficient evidence of need","Inappropriate technical design","Fragmented funding",
          "Weak procurement and delivery","Inadequate construction supervision","Unclear ownership","Weak operating arrangements",
          "Insufficient maintenance","No replacement planning","Poor monitoring","No functionality data"]
cause_cards = "".join(
  f'<div style="background:#fff;border:1px solid {LINE};border-left:3px solid {CORAL};border-radius:6px;padding:9px 11px;font-size:11.5px;font-weight:700;color:{NAVY};line-height:1.3;">{c}</div>'
  for c in causes)
old = row([chip("NEED","#FBECE8","#B4482F"), arrow(), chip("PROJECT","#FBECE8","#B4482F"), arrow(),
           chip("CONSTRUCTION","#FBECE8","#B4482F"), arrow(), chip("HANDOVER","#FBECE8","#B4482F"), arrow(),
           chip("DECLINE","#FBECE8","#B4482F"), arrow(), chip("FAILURE","#FBECE8","#B4482F")], gap=0, grow=False)
new = row([chip("NEED",BLUE), arrow(), chip("EVIDENCE","#1478B8"), arrow(), chip("SOLUTION","#16A8C0"), arrow(),
           chip("CAPITAL",AQUA), arrow(), chip("DELIVERY",TEAL), arrow(), chip("FUNCTION","#2AA471"), arrow(),
           chip("REINVEST",GREEN)], gap=0, grow=False)
body = f'''
  {p("Infrastructure does not fail for want of money alone. Twelve recurring causes — every one of them institutional rather than technical.", 14, "#2B3B49")}
  <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:9px;">{cause_cards}</div>
  <div style="display:flex;flex-direction:column;gap:8px;flex-grow:1;justify-content:flex-end;">
    <div style="font-size:11px;font-weight:900;letter-spacing:0.14em;text-transform:uppercase;color:{CORAL};">The recurring cycle</div>
    {old}
    <div style="font-size:11px;font-weight:900;letter-spacing:0.14em;text-transform:uppercase;color:{TEAL};margin-top:8px;">The cycle CFI builds instead</div>
    {new}
  </div>'''
shell("Problem.dc.html", "Part I · Strategic identity", CORAL, "Section 02", "The problem CFI exists to solve", body)

# ============ 3. EQUATION ============
eq = row([chip("COMMUNITY NEED",SAND2,NAVY), chip("EVIDENCE",SAND2,NAVY), chip("ENGINEERING",SAND2,NAVY),
          chip("CAPITAL",SAND2,NAVY), chip("DELIVERY",SAND2,NAVY), chip("OPERATIONS",SAND2,NAVY)], gap=10, grow=False)
body = f'''
  {p("The strategy in one line, and the six questions every project must answer before it starts.", 14, "#2B3B49")}
  {eq}
  <div style="background: linear-gradient(90deg,{NAVY} 0%,{TEAL} 100%); border-radius:10px; padding:16px; text-align:center; font-size:18px; font-weight:900; color:#fff; letter-spacing:0.04em;">= SUSTAINABLE IMPACT</div>
  <div style="font-size:11px;font-weight:900;letter-spacing:0.14em;text-transform:uppercase;color:{AQUA};margin-top:4px;">The CFI project test</div>
  {grid([
    card(h("1 · Is the problem real?",12.5) + p("Evidence, not assumption.",11.5), BLUE, "12px 14px"),
    card(h("2 · Is the solution appropriate?",12.5) + p("Fits users, site, environment, operating conditions.",11.5), "#1583C0", "12px 14px"),
    card(h("3 · Can it be delivered?",12.5) + p("Land, permissions, procurement, capacity.",11.5), AQUA, "12px 14px"),
    card(h("4 · Will it function after completion?",12.5) + p("Operations, staffing, utilities, repairs.",11.5), TEAL, "12px 14px"),
    card(h("5 · Can we demonstrate impact?",12.5) + p("A baseline to compare against.",11.5), "#2AA471", "12px 14px"),
    card(h("6 · Can it be improved or replicated?",12.5) + p("Every project makes institutional knowledge.",11.5), GREEN, "12px 14px"),
  ], cols=3)}'''
shell("Equation.dc.html", "Part I · Strategic identity", AQUA, "Sections 06 & 08", "The strategic equation", body)
print("1-3 written")

# ============ 4. LIFECYCLE ============
st = [("DISCOVER",BLUE),("VERIFY","#1478B8"),("DESIGN","#1A85BC"),("FUND","#1892BF"),("BUILD","#169FC2"),("COMMISSION",AQUA),
      ("OPERATE","#13A8B4"),("MAINTAIN",TEAL),("MEASURE","#189E7D"),("LEARN","#2AA471"),("REINVEST",GREEN),("SCALE",NAVY)]
r1 = row([x for i,(n,c) in enumerate(st[:6]) for x in ([chip(n,c)] if i==0 else [arrow(),chip(n,c)])], gap=0, grow=False)
r2 = row([x for i,(n,c) in enumerate(st[6:]) for x in ([chip(n,c)] if i==0 else [arrow(),chip(n,c)])], gap=0, grow=False)
body = f'''
  {p("Twelve stages, one continuous chain of accountability. Construction is one stage, not the finish line — and the loop closes: what is measured determines what is discovered next.", 14, "#2B3B49")}
  <div style="display:flex;flex-direction:column;gap:10px;">
    {r1}
    <div style="display:flex;align-items:center;gap:8px;color:#9FB3C2;font-size:12px;font-weight:700;">
      <div style="flex-grow:1;height:1px;background:{LINE};"></div><div>then</div><div style="flex-grow:1;height:1px;background:{LINE};"></div>
    </div>
    {r2}
  </div>
  {grid([
    card(h("Stages 1–3 · Define",13,BLUE) + p("Establish that the problem is real, verified and solvable before anything is designed.",12), BLUE),
    card(h("Stages 4–6 · Deliver",13,AQUA) + p("Fund, build and commission with documented controls and trained operators.",12), AQUA),
    card(h("Stages 7–12 · Sustain",13,GREEN) + p("Operate, maintain, measure and reinvest — replicate only where evidence supports it.",12), GREEN),
  ], cols=3)}
  <div style="background:#FBECE8;border-radius:8px;padding:12px 16px;font-size:12.5px;color:#B4482F;font-weight:700;">A project that skips a stage has not saved time. It has moved an unanswered question further downstream.</div>'''
shell("Lifecycle.dc.html", "Part IV · Delivery system", AQUA, "Section 12", "The CFI project lifecycle", body)

# ============ 5. GATES ============
gates = [("0","Problem","Is there a meaningful problem?",BLUE),("1","Evidence","Has the need been sufficiently verified?","#1478B8"),
 ("2","Feasibility","Can it be solved technically, legally and socially?","#1A85BC"),("3","Sustainability","Can the asset be operated and maintained?","#1892BF"),
 ("4","Finance","Is there sufficient capital and a credible OPEX plan?","#169FC2"),("5","Design","Has the technical package been reviewed?",AQUA),
 ("6","Procurement","Is procurement transparent and controlled?","#13A8B4"),("7","Construction","Are quality and progress controlled?",TEAL),
 ("8","Commissioning","Does the infrastructure actually work?","#189E7D"),("9","Operations","Is a responsible operator and O&amp;M system in place?","#2AA471"),
 ("10","Impact","Is the intended result being achieved?",GREEN),("11","Scale","Is there sufficient evidence to replicate?",NAVY)]
rows_ = "".join(
 f'''<div style="display:flex;gap:12px;align-items:center;padding:7px 0;border-bottom:1px solid {LINE};">
   <div style="width:26px;height:26px;border-radius:50%;background:{c};color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{n}</div>
   <div style="width:120px;flex-shrink:0;font-size:13px;font-weight:900;color:{NAVY};">{t}</div>
   <div style="font-size:12.5px;color:#42535F;">{q}</div>
 </div>''' for n,t,q,c in gates)
body = f'''
  {p("Each gate is a single question that must be answered affirmatively, with evidence, before a project may proceed. A gate that cannot be passed is not a delay — it is the model working.", 14, "#2B3B49")}
  <div style="flex-grow:1;">{rows_}</div>
  <div style="background:{SAND2};border-radius:8px;padding:12px 16px;font-size:12.5px;color:{NAVY};font-weight:700;">Gates 3 and 4 are the ones most development projects skip. No construction approval without a named operator and a funded operating plan.</div>'''
shell("Gates.dc.html", "Part IV · Delivery system", TEAL, "Section 13", "Twelve approval gates", body)

# ============ 6. DIVISIONS ============
divs = [("CFI Community","Problems, people, partnership",BLUE),("CFI Engineering","Technical solution and quality","#1583C0"),
        ("CFI Capital","Funding and capital strategy",AQUA),("CFI Delivery","Procurement and construction",TEAL),
        ("CFI Operations","Running and maintaining assets",GREEN),("CFI Impact &amp; Digital","Evidence and the data layer",AMBER)]
dcards = [card(h(n,14,NAVY,4) + p(d,12,MUTED), c) for n,d,c in divs]
body = f'''
  {p("One integrated organization: six specialist divisions around a single mission core, supported by shared institutional functions. No division delivers a project alone.", 14, "#2B3B49")}
  {grid(dcards[:3], cols=3, grow=False)}
  <div style="background: linear-gradient(135deg,{NAVY} 0%,{TEAL} 100%); border-radius:10px; padding:16px; text-align:center;">
    <div style="font-size:16px;font-weight:900;color:#fff;letter-spacing:0.04em;">CLEAN FUTURE INTERNATIONAL</div>
    <div style="font-size:11px;font-weight:700;letter-spacing:0.16em;color:#8FE3E8;margin-top:5px;">ONE MISSION</div>
  </div>
  {grid(dcards[3:], cols=3, grow=False)}
  <div style="background:{SAND2};border:1px solid {LINE};border-radius:8px;padding:12px 16px;text-align:center;font-size:12.5px;font-weight:700;color:{NAVY};">Finance · Governance · Procurement · Safeguarding · Legal &amp; Compliance · Partnerships</div>'''
shell("Divisions.dc.html", "Part III · Organization", AQUA, "Section 11", "Organizational architecture", body)

# ============ 7. PILLARS ============
pil = [("1","Community &amp; Need","CFI Community","A registry of verified needs that drives project selection",BLUE),
 ("2","Engineering &amp; Innovation","CFI Engineering","Standard design packages, each with a maintenance specification","#1583C0"),
 ("3","Infrastructure Delivery","CFI Delivery","An auditable delivery file for every project",AQUA),
 ("4","Sustainable Finance","CFI Capital","Every project funded for its life, not its opening","#12A79A"),
 ("5","Operations &amp; Asset Management","CFI Operations","Failure detected by CFI before it is reported",TEAL),
 ("6","Impact, Data &amp; Learning","Impact &amp; Digital","New design decisions traceable to old evidence","#2AA471"),
 ("7","Institutional Strength","Board &amp; shared","A country-entry standard, met before entry",GREEN)]
cols = "".join(
 f'''<div style="background:{c};border-radius:10px;padding:14px 10px;display:flex;flex-direction:column;gap:8px;">
   <div style="font-size:22px;font-weight:900;color:#fff;line-height:1;">{n}</div>
   <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;">{t}</div>
   <div style="font-size:10px;font-weight:700;color:#DCEEF6;letter-spacing:0.04em;">{o}</div>
   <div style="flex-grow:1;"></div>
   <div style="font-size:10.5px;color:#EAF6FA;line-height:1.35;border-top:1px solid rgba(255,255,255,.25);padding-top:7px;">{m}</div>
 </div>''' for n,t,o,m,c in pil)
body = f'''
  {p("Each pillar has one accountable owner, a capability to build and a maturity marker that shows whether it is working. A weakness in one appears as failure in another.", 14, "#2B3B49")}
  <div style="background:{NAVY};border-radius:10px;padding:13px;text-align:center;font-size:14px;font-weight:900;color:#fff;letter-spacing:0.04em;">SUSTAINABLE COMMUNITY INFRASTRUCTURE</div>
  <div style="display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:9px;flex-grow:1;">{cols}</div>
  <div style="background: linear-gradient(90deg,{AQUA},{GREEN}); border-radius:10px;padding:13px;text-align:center;font-size:13px;font-weight:900;color:#fff;letter-spacing:0.06em;">EVIDENCE · GOVERNANCE · LOCAL PARTNERSHIP</div>'''
shell("Pillars.dc.html", "Part II · Strategic pillars", AQUA, "Section 10", "The seven strategic pillars", body)
print("4-7 written")

# ============ 8. MONEY LAYERS ============
lay = [("Layer 1","PROJECT CAPITAL","Building the asset","Finite, restricted, ends at commissioning. Grants, CSR, institutional capital.","Fails by: being raised without Layer 2 in place.",BLUE),
       ("Layer 2","HUB OPERATING","Keeping the asset working","Recurring for the asset's life — operator, utilities, maintenance and the renewal reserve.","Fails by: being assumed rather than funded.",TEAL),
       ("Layer 3","CFI CORE","Running the organization","Governance, audit, safeguarding, finance, standards, the registries, fundraising.","Fails by: having no dedicated income at all.",AMBER)]
rows_ = "".join(
 f'''<div style="display:flex;gap:14px;align-items:stretch;">
   <div style="width:140px;flex-shrink:0;background:{c};border-radius:10px;padding:14px 10px;display:flex;flex-direction:column;align-items:center;justify-content:center;">
     <div style="font-size:16px;font-weight:900;color:#fff;">{n}</div>
     <div style="font-size:9.5px;font-weight:900;letter-spacing:0.12em;color:#EAF6FA;margin-top:5px;text-align:center;">{k}</div>
   </div>
   <div style="flex-grow:1;background:#fff;border:1px solid {LINE};border-radius:10px;padding:14px 16px;">
     {h(t,14)}{p(d,12.5)}
     <div style="font-size:11.5px;font-weight:900;color:{c};margin-top:7px;">{f}</div>
   </div>
 </div>''' for n,k,t,d,f,c in lay)
body = f'''
  {p("Three kinds of money with different sources, different rules and different failure modes. The most common cause of trouble is treating them as one pot.", 14, "#2B3B49")}
  <div style="display:flex;flex-direction:column;gap:12px;flex-grow:1;">{rows_}</div>
  <div style="background:#FBECE8;border-radius:8px;padding:12px 16px;font-size:12.5px;color:#B4482F;font-weight:700;">Only two sources reach Layer 3 at any scale: unrestricted giving and cost recovery. Layer 3 must be funded before there is anything to show a funder.</div>'''
shell("MoneyLayers.dc.html", "Part V · Finance", GREEN, "Volume II · Section 02", "The three money layers", body)

# ============ 9. HUB ECONOMICS ============
bars = [("25/day","−33.5k",-33.5,CORAL),("50/day","−15.2k",-15.2,"#D9674F"),("71/day","0",0,AMBER),
        ("100/day","+21.3k",21.3,GREEN),("200/day","+94.3k",94.3,"#2AA471"),("300/day","+167.3k",167.3,TEAL)]
mx=180.0
def bar(lbl,val,v,c):
    up = v>0; hgt = max(3, abs(v)/mx*150)
    top = f'<div style="height:{150-hgt:.0f}px;"></div><div style="height:{hgt:.0f}px;background:{c};border-radius:4px 4px 0 0;"></div><div style="height:150px;"></div>' if up \
        else f'<div style="height:150px;"></div><div style="height:{hgt:.0f}px;background:{c};border-radius:0 0 4px 4px;"></div><div style="height:{150-hgt:.0f}px;"></div>'
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:5px;flex-grow:1;">'
            f'<div style="font-size:11px;font-weight:900;color:{c};">{val}</div>'
            f'<div style="width:100%;display:flex;flex-direction:column;">{top}</div>'
            f'<div style="font-size:10.5px;color:{MUTED};">{lbl}</div></div>')
chart = '<div style="display:flex;gap:10px;align-items:flex-end;flex-grow:1;">' + "".join(bar(*b) for b in bars) + "</div>"
body = f'''
  {p("One hub, one year, Ghana cedis — modelled from the board's own assumptions with renewal and core cost added. Break-even is 71 paying users a day at GHS 2.", 14, "#2B3B49")}
  {row([
    card(f'<div style="font-size:26px;font-weight:900;color:{NAVY};line-height:1;">27,600</div>' + p("Direct operating cost",11.5,MUTED), BLUE, "13px 15px"),
    card(f'<div style="font-size:26px;font-weight:900;color:{NAVY};line-height:1;">20,000</div>' + p("Renewal provision",11.5,MUTED), AQUA, "13px 15px"),
    card(f'<div style="font-size:26px;font-weight:900;color:{NAVY};line-height:1;">4,140</div>' + p("Cost recovery (15%)",11.5,MUTED), TEAL, "13px 15px"),
    card(f'<div style="font-size:26px;font-weight:900;color:{CORAL};line-height:1;">51,740</div>' + p("Full annual cost",11.5,MUTED), CORAL, "13px 15px"),
  ], grow=False)}
  <div style="font-size:11px;font-weight:900;letter-spacing:0.14em;text-transform:uppercase;color:{MUTED};">Annual surplus or deficit by daily footfall</div>
  {chart}
  <div style="background:{SAND2};border-radius:8px;padding:11px 16px;font-size:12.5px;color:{NAVY};font-weight:700;">Capital of 250,000–400,000 repays in 12–19 years at 100/day, and under two years at 500/day. Same building, entirely different investment.</div>'''
shell("HubEconomics.dc.html", "Part C · Economics", AMBER, "Volume III · Section 09", "Unit economics of one hub", body)

# ============ 10. CATEGORIES ============
cats = [("A","Revenue-Sustainable","Lorry stations and large markets","Legitimate revenue covers operating and maintenance in full.","Capital only",GREEN),
        ("B","Partially Revenue-Supported","Community centres, smaller markets","Real income, but grants or subsidy remain necessary — especially for renewal.","Capital + stated subsidy",AQUA),
        ("C","Social Infrastructure","Every school hub","Significant social value, little realistic commercial revenue.","Capital + full lifetime cost",AMBER)]
cds = [card(f'<div style="font-size:38px;font-weight:900;color:{c};line-height:1;">{L}</div>' + h(t,13.5,NAVY,4)
            + f'<div style="font-size:11px;font-weight:900;color:{c};margin-bottom:7px;">{w}</div>' + p(d,12)
            + f'<div style="margin-top:9px;padding-top:9px;border-top:1px solid {LINE};font-size:11.5px;font-weight:900;color:{NAVY};">{a}</div>', c)
       for L,t,w,d,a,c in cats]
body = f'''
  {p("Every project is classified before funding. The category belongs to the site, not the programme — one CFI WASH portfolio will contain all three.", 14, "#2B3B49")}
  {grid(cds, cols=3)}
  <div style="background:#FBECE8;border-radius:8px;padding:12px 16px;font-size:12.5px;color:#B4482F;font-weight:700;">Funding a Type C asset with a Type A business case is how facilities end up abandoned — money for the building, nothing for the twenty years afterwards.</div>'''
shell("Categories.dc.html", "Part V · Finance", AMBER, "Volume I · Section 14.1", "Three sustainability categories", body)
print("8-10 written")

# ============ 11. THE HUB ============
svc = ["Gender-separated toilet blocks","Handwashing stations","Menstrual-hygiene provision"]
con = ["Borehole and water storage","Solar power and lighting","Septic tank or biodigester"]
rev = ["Adult user fee","Attached kiosk rental","Advertising panels"]
def lst(items,c):
    return "".join(f'<div style="font-size:12px;color:#42535F;line-height:1.5;">&bull; {i}</div>' for i in items)
sites = [("Basic, JHS &amp; SHS","Highest need, lowest ability to pay","Type C",AMBER),
         ("Markets &amp; community centres","High footfall, revenue viable","Type B",AQUA),
         ("Bus and lorry stations","Highest footfall of all","Type A",GREEN),
         ("Leisure areas","Seasonal — needs testing","Untested",MUTED)]
scards = [card(h(n,12.5,NAVY,4) + p(d,11.5) + f'<div style="margin-top:7px;font-size:11px;font-weight:900;color:{c};">{t}</div>', c, "12px 14px") for n,d,t,c in sites]
body = f'''
  {p("The first CFI programme. Components grouped by what each is for — because the three categories fail differently: service failures are visible, continuity failures are silent.", 14, "#2B3B49")}
  {row([
    card(h("SERVICE — what users come for",12,BLUE,7) + lst(svc,BLUE), BLUE),
    card(h("CONTINUITY — what keeps it open",12,TEAL,7) + lst(con,TEAL), TEAL),
    card(h("REVENUE — what pays for it",12,AMBER,7) + lst(rev,AMBER), AMBER),
  ])}
  <div style="font-size:11px;font-weight:900;letter-spacing:0.14em;text-transform:uppercase;color:{MUTED};">Where hubs are sited — and what each one is</div>
  {grid(scards, cols=4, grow=False)}
  <div style="background:{SAND2};border-radius:8px;padding:11px 16px;font-size:12.5px;color:{NAVY};font-weight:700;">These four sites do not share one financial model. Treating them as one product with one revenue line is the central modelling error to avoid.</div>'''
shell("Hub.dc.html", "Part VI · Operating context", BLUE, "Volume I · Section 19", "The CFI Sustainable Sanitation Hub", body)

# ============ 12. 24-MONTH ROADMAP ============
ph = [("0–3","Establish the institution","Governance, legal review, financial controls, safeguarding, procurement, technical standards. Set the cost-recovery rate. Register the Ghana branch.","Know the real number CFI needs",BLUE),
      ("3–6","Measure, then classify","Footfall and willingness-to-pay study at three sites. Baseline and condition survey. Classify each site Type A, B or C. Prototype design, independently reviewed.","Layer 3 covered before Project 001",AQUA),
      ("6–12","Fund one hub properly","Raise Layer 1 with recovery included and Layer 2 with its renewal provision, as two separate asks. Operator agreement signed before construction.","An asset funded for its life",TEAL),
      ("12–24","Prove it, then replicate","Commission, operate, publish real functionality, cost and revenue data. Replace every modelled number with a measured one.","A second project funded on evidence",GREEN)]
rows_ = "".join(
 f'''<div style="display:flex;gap:14px;align-items:stretch;">
   <div style="width:96px;flex-shrink:0;background:{c};border-radius:9px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px 6px;">
     <div style="font-size:17px;font-weight:900;color:#fff;">{m}</div>
     <div style="font-size:9px;font-weight:900;letter-spacing:0.12em;color:#EAF6FA;margin-top:3px;">MONTHS</div>
   </div>
   <div style="flex-grow:1;background:#fff;border:1px solid {LINE};border-radius:9px;padding:12px 15px;">
     {h(t,13.5)}{p(d,12)}
     <div style="font-size:11.5px;font-weight:900;color:{c};margin-top:6px;">Unlocks: {u}</div>
   </div>
 </div>''' for m,t,d,u,c in ph)
body = f'''
  {p("The first two years establish the institution, prove the lifecycle on a single project, and generate the evidence needed to decide whether to replicate.", 14, "#2B3B49")}
  <div style="display:flex;flex-direction:column;gap:11px;flex-grow:1;">{rows_}</div>
  <div style="background:#FBECE8;border-radius:8px;padding:11px 16px;font-size:12.5px;color:#B4482F;font-weight:700;">Fund one hub, not three. Three unproven hubs multiply an unvalidated assumption; one measured for a year turns it into evidence.</div>'''
shell("Roadmap24.dc.html", "Part VIII · Roadmap", TEAL, "Volume I · Section 24", "The initial 24 months", body)

# ============ 13. TEN-YEAR HORIZONS ============
hz = [("YEAR 1","PROVE","Build the institution and deliver Project 001","~1 asset · 1 programme · 1 country",BLUE),
      ("YEAR 3","REPEAT","Turn one project into a method","3–5 assets · v1 standard designs · first evaluation",AQUA),
      ("YEAR 5","SYSTEMATIZE","Run a country programme, not a series of projects","10–20 assets · 2 programme areas · 1 country assessed",TEAL),
      ("YEAR 10","SCALE","Become an infrastructure development platform","2–4 countries · portfolio reporting · the system as the asset",NAVY)]
cds = "".join(
 f'''<div style="flex-grow:1;display:flex;flex-direction:column;gap:9px;">
   <div style="background:{c};border-radius:9px;padding:12px 14px;">
     <div style="font-size:16px;font-weight:900;color:#fff;">{y}</div>
     <div style="font-size:9.5px;font-weight:900;letter-spacing:0.14em;color:#EAF6FA;margin-top:3px;">{k}</div>
   </div>
   <div style="flex-grow:1;background:#fff;border:1px solid {LINE};border-radius:9px;padding:12px 14px;">
     {h(t,13,NAVY,7)}
     <div style="font-size:11.5px;color:{MUTED};line-height:1.5;">{m}</div>
   </div>
 </div>''' for y,k,t,m,c in hz)
body = f'''
  {p("Four horizons defined by capability, not by date. Figures are planning assumptions, deliberately conservative, revised against evidence at each horizon.", 14, "#2B3B49")}
  <div style="display:flex;gap:13px;flex-grow:1;">{cds}</div>
  {grid([
    card(h("Year 1 → 3",12.5,AQUA,5) + p("Project 001 functioning twelve months after commissioning, its costs known and covered.",11.5), AQUA, "12px 14px"),
    card(h("Year 3 → 5",12.5,TEAL,5) + p("The method repeated at least three times with comparable results; reserves tested by real repairs.",11.5), TEAL, "12px 14px"),
    card(h("Year 5 → 10",12.5,NAVY,5) + p("Country-entry standard documented and met; local leadership in place; portfolio reporting credible externally.",11.5), NAVY, "12px 14px"),
  ], cols=3, grow=False)}
  <div style="background:#FBECE8;border-radius:8px;padding:11px 16px;font-size:12.5px;color:#B4482F;font-weight:700;">If a horizon's conditions are not met, CFI stays at that horizon and improves. Growing on schedule while the previous horizon is still failing is the pattern this model exists to avoid.</div>'''
shell("Horizons.dc.html", "Part VIII · Roadmap", BLUE, "Volume I · Section 25", "The ten-year horizons", body)
print("11-13 written")

# ============ 14. PRINCIPLES ============
pr = [("1","Community before solution","Understand the problem before selecting an intervention.",BLUE),
      ("2","Engineering before construction","Develop an appropriate technical solution before building.","#1583C0"),
      ("3","Lifecycle before opening day","Plan operations, maintenance and renewal from the beginning.",AQUA),
      ("4","Local ownership before dependency","Build local capacity and responsibility.","#12A79A"),
      ("5","Transparency before fundraising","Protect confidence through traceable systems.",TEAL),
      ("6","Evidence before impact claims","Measure outcomes rather than relying on publicity.","#2AA471"),
      ("7","Sustainability before short-term visibility","Long-term service over launch-day appearance.","#33A86E"),
      ("8","Proven models before scale","Replicate what evidence shows can work.",GREEN)]
cds = [f'''<div style="background:{SAND2};border-left:4px solid {c};border-radius:0 8px 8px 0;padding:11px 14px;display:flex;gap:11px;align-items:flex-start;">
  <div style="font-size:19px;font-weight:900;color:{c};line-height:1;flex-shrink:0;">{n}</div>
  <div><div style="font-size:12.5px;font-weight:900;color:{NAVY};margin-bottom:3px;">{t}</div>
  <div style="font-size:11.5px;color:#52636F;line-height:1.4;">{d}</div></div></div>''' for n,t,d,c in pr]
body = f'''
  {p("Eight rules of sequence. Each names what must come first — because almost every failure this model prevents comes from doing the second thing before the first.", 14, "#2B3B49")}
  {grid(cds, cols=2, gap=12)}
  <div style="background:{SAND2};border-radius:8px;padding:11px 16px;font-size:12.5px;color:{NAVY};font-weight:700;">Each principle is tested at an approval gate. Where a project cannot satisfy the earlier half, it does not proceed to the later half.</div>'''
shell("Principles.dc.html", "Part IX · Identity", AQUA, "Volume I · Section 26", "Eight operating principles", body)

# ============ 15. RED LINES ============
proj = ["build first and solve maintenance later","assume donor funding will permanently cover operating costs",
        "assume user fees automatically make infrastructure profitable","treat construction completion as proof of impact",
        "describe a project as sustainable without evidence"]
fund = ["accept restricted funding that leaves core costs unfunded","build an asset without a funded Layer 2 plan",
        "spend a maintenance reserve on anything but its own asset","treat reserves as working capital",
        "delay reporting bad news to a funder"]
def rl(items):
    return "".join(
      f'''<div style="display:flex;gap:9px;align-items:flex-start;padding:6px 0;border-bottom:1px solid {LINE};">
        <div style="width:17px;height:17px;border-radius:4px;background:#FBECE8;color:#C4553B;font-size:11px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;">&times;</div>
        <div style="font-size:12px;color:#42535F;line-height:1.4;">CFI will <strong style="color:{NAVY};">not</strong> {i}.</div>
      </div>''' for i in items)
body = f'''
  {p("A model is defined as much by its refusals as by its ambitions. Each of these describes a decision that is easy to make under pressure — a deadline, a funding window, a photograph.", 14, "#2B3B49")}
  {row([
    card(h("Project red lines",13,CORAL,9) + rl(proj), CORAL),
    card(h("Funding red lines",13,AMBER,9) + rl(fund), AMBER),
  ])}
  <div style="background:{SAND2};border-radius:8px;padding:11px 16px;font-size:12.5px;color:{NAVY};font-weight:700;">Each refusal has a matching control — an approval gate, a financial rule, a governance requirement. A refusal without a control is only an intention.</div>'''
shell("RedLines.dc.html", "Part IX · Identity", CORAL, "Volumes I &amp; II", "What CFI will not do", body)

# ============ 16. NEXT STEPS ============
todo = [("Core-cost budget template","Produces the real cost-recovery rate","Volume II",BLUE),
        ("Lifecycle costing spreadsheet","Produces the Layer 2 renewal contribution per asset","Volume II",AQUA),
        ("Due-diligence pack","The twelve documents funders ask for","Volume II · Section 08",TEAL),
        ("Footfall &amp; willingness-to-pay study","Converts the revenue assumption into evidence","Volume III · Section 11",GREEN),
        ("Ghana regulatory checklist","Registration, licensing, tax, employment, procurement, environment","Volume I · Section 18",AMBER),
        ("Site selection criteria","Scoring matrix and needs-verification protocol","Volume I · Section 12",CORAL)]
cds = [card(h(t,13,NAVY,5) + p(d,11.5) + f'<div style="margin-top:7px;font-size:10.5px;font-weight:900;letter-spacing:0.06em;color:{c};">{s}</div>', c) for t,d,s,c in todo]
body = f'''
  {p("The model is defined. These six instruments turn it into practice — each one named in the volumes, none of them built yet.", 14, "#2B3B49")}
  {grid(cds, cols=3, gap=13)}
  <div style="background: linear-gradient(135deg,{NAVY} 0%,{TEAL} 100%); border-radius:10px; padding:18px 22px;">
    <div style="font-size:10px;font-weight:900;letter-spacing:0.18em;text-transform:uppercase;color:#8FE3E8;margin-bottom:8px;">The order that matters</div>
    <div style="font-size:15px;line-height:1.45;color:#F2FAFC;">Unrestricted income first, because it is the only money that can be spent on becoming fundable. Then measure. Then build one hub — properly.</div>
  </div>'''
shell("NextSteps.dc.html", "Part D · Delivery", TEAL, "Across all three volumes", "What is still to build", body)

# ============ canvas.json ============
W,H,GX,GY = 1000,700,140,190
order = ["Main","Problem","Equation","Lifecycle",
         "Gates","Divisions","Pillars","MoneyLayers",
         "HubEconomics","Categories","Hub","Roadmap24",
         "Horizons","Principles","RedLines","NextSteps"]
arts=[]
for i,name in enumerate(order):
    r,c = divmod(i,4)
    arts.append({"file": f"{name}.dc.html", "x": c*(W+GX), "y": r*(H+GY), "w": W, "h": H})
notes=[
 {"id":"row-identity","x":-320,"y":250,"w":260,"text":"IDENTITY\nWhy CFI exists, the problem it solves, and the equation behind it."},
 {"id":"row-architecture","x":-320,"y":1140,"w":260,"text":"ARCHITECTURE\nHow work is structured, approved and owned."},
 {"id":"row-money","x":-320,"y":2030,"w":260,"text":"MONEY\nHow projects and the organization are funded — and what one hub actually earns."},
 {"id":"row-growth","x":-320,"y":2920,"w":260,"text":"GROWTH & DISCIPLINE\nHow CFI scales, what it commits to, and what is still to build."},
]
pathlib.Path("canvas.json").write_text(json.dumps(
  {"artboards":arts,"annotations":notes,"launch":{"view":"canvas"}}, indent=2), encoding="utf-8")
print("16 artboards + canvas.json written")
