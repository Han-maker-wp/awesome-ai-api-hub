#!/usr/bin/env python3
"""从 data/sites.json 生成单文件导航页 index.html（数据内嵌，无外部依赖）。

数据结构：groups[] -> categories[] -> items[]
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sites.json"
OUT = ROOT / "index.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome AI API Hub · AI API 中转站与导航合集</title>
<meta name="description" content="精选 AI API 中转站、聚合网关、官方直连入口、比价导航站与开源自建方案，另附网络代理、账号接码等通用基础设施。">
<style>
:root{
  --bg:#0b0f14; --bg2:#0f151c; --card:#151c24; --card-h:#1b2430;
  --line:#232e3c; --line2:#2e3d4f;
  --fg:#e6edf3; --fg2:#9fb0c0; --fg3:#6b7d90;
  --acc:#4d9fff; --acc2:#7c5cff; --ok:#3fb950; --warn:#e3b341;
  --r:14px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  background:var(--bg);color:var(--fg);
  font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing:antialiased;
}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}

/* ---------- header ---------- */
header{
  position:relative;overflow:hidden;
  border-bottom:1px solid var(--line);
  background:
    radial-gradient(900px 380px at 15% -10%, rgba(77,159,255,.16), transparent 60%),
    radial-gradient(760px 340px at 85% -20%, rgba(124,92,255,.15), transparent 60%),
    var(--bg2);
}
header .wrap{padding-top:58px;padding-bottom:44px}
h1{
  font-size:clamp(30px,4.6vw,46px);font-weight:800;letter-spacing:-.02em;line-height:1.15;
  background:linear-gradient(100deg,#e6edf3 8%,#7cc0ff 48%,#a78bfa 88%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
}
.sub{margin-top:14px;color:var(--fg2);font-size:16.5px;max-width:780px}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.stat{
  background:rgba(255,255,255,.04);border:1px solid var(--line);
  border-radius:999px;padding:7px 15px;font-size:13.5px;color:var(--fg2);
}
.stat b{color:var(--fg);font-weight:700}
.stat .dot{color:var(--ok)}

/* ---------- toolbar ---------- */
.toolbar{
  position:sticky;top:0;z-index:30;
  background:rgba(11,15,20,.9);backdrop-filter:blur(12px);
  border-bottom:1px solid var(--line);padding:13px 0;
}
.toolbar .wrap{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
#q{
  flex:1;min-width:220px;background:var(--card);border:1px solid var(--line2);
  color:var(--fg);border-radius:10px;padding:11px 14px;font-size:14.5px;outline:none;
  transition:border-color .15s,box-shadow .15s;
}
#q::placeholder{color:var(--fg3)}
#q:focus{border-color:var(--acc);box-shadow:0 0 0 3px rgba(77,159,255,.16)}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{
  border:1px solid var(--line2);background:transparent;color:var(--fg2);
  border-radius:999px;padding:7px 14px;font-size:13.5px;cursor:pointer;
  transition:all .15s;white-space:nowrap;
}
.chip:hover{color:var(--fg);border-color:var(--acc);background:rgba(77,159,255,.08)}
.chip.on{background:var(--acc);border-color:var(--acc);color:#08111d;font-weight:650}
.chip.grp{border-color:#3a4b60}

/* ---------- group ---------- */
main{padding:34px 0 10px}
.group{margin-bottom:54px}
.group-head{
  display:flex;align-items:center;gap:13px;flex-wrap:wrap;
  padding:14px 18px;border-radius:var(--r);
  background:linear-gradient(90deg,rgba(77,159,255,.13),rgba(124,92,255,.07) 45%,transparent 85%);
  border:1px solid var(--line);border-left:3px solid var(--acc);
  margin-bottom:10px;
}
.group-head .gi{font-size:24px;line-height:1}
.group-head h2{font-size:24px;font-weight:800;letter-spacing:-.015em}
.group-head .gmeta{margin-left:auto;font-size:12.5px;color:var(--fg3);text-align:right;line-height:1.5}
.group-desc{color:var(--fg2);font-size:14.2px;margin-bottom:26px;max-width:920px}
.group.alt .group-head{background:linear-gradient(90deg,rgba(124,92,255,.14),rgba(77,159,255,.06) 45%,transparent 85%);border-left-color:var(--acc2)}

/* ---------- section ---------- */
section{margin-bottom:34px;scroll-margin-top:76px}
.shead{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:6px}
.shead h3{font-size:19px;font-weight:730;letter-spacing:-.01em}
.shead .cnt{font-size:12.5px;color:var(--fg3);border:1px solid var(--line);border-radius:999px;padding:2px 10px}
.sdesc{color:var(--fg2);font-size:13.8px;margin-bottom:16px;max-width:920px}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:13px}
.card{
  position:relative;display:block;background:var(--card);border:1px solid var(--line);
  border-radius:var(--r);padding:16px 17px 15px;overflow:hidden;
  transition:transform .16s,border-color .16s,background .16s,box-shadow .16s;
}
.card::before{
  content:"";position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(180deg,var(--acc),var(--acc2));opacity:0;transition:opacity .16s;
}
.card:hover{
  transform:translateY(-3px);border-color:var(--line2);background:var(--card-h);
  box-shadow:0 12px 30px -12px rgba(0,0,0,.75);
}
.card:hover::before{opacity:1}
.card .top{display:flex;align-items:center;gap:9px;margin-bottom:8px}
.card .nm{font-weight:700;font-size:15.5px;letter-spacing:-.01em}
.card .st{color:var(--warn);font-size:13px;line-height:1;flex-shrink:0}
.card .note{color:var(--fg2);font-size:13.4px;line-height:1.55}
.card .foot{margin-top:11px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.tag{
  font-size:11.5px;color:var(--fg3);border:1px solid var(--line2);
  border-radius:6px;padding:2px 7px;background:rgba(255,255,255,.02);
}
.host{font-size:11.5px;color:var(--fg3);margin-left:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.empty{color:var(--fg3);text-align:center;padding:60px 0;font-size:15px}

/* ---------- footer ---------- */
footer{border-top:1px solid var(--line);margin-top:34px;padding:34px 0 46px;color:var(--fg3);font-size:13.5px}
footer .box{
  background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--warn);
  border-radius:10px;padding:16px 18px;margin-bottom:22px;color:var(--fg2);line-height:1.75;
}
footer .box b{color:var(--warn)}
footer .meta{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}
footer a{color:var(--acc)}
footer a:hover{text-decoration:underline}
@media(max-width:640px){
  header .wrap{padding-top:40px;padding-bottom:32px}
  .grid{grid-template-columns:1fr}
  .host{display:none}
  .group-head .gmeta{margin-left:0}
}
</style>
</head>
<body>

<header>
  <div class="wrap">
    <h1>🔌 Awesome AI API Hub</h1>
    <p class="sub">一个 Key，打通全世界的大模型。AI API 中转站 · 聚合网关 · 官方直连 · 检测验真 · 比价导航 · 自建方案，外带网络代理、机场评测与账号接码等通用基础设施。</p>
    <div class="stats">
      <span class="stat"><span class="dot">●</span> 收录 <b>__TOTAL__</b> 个站点</span>
      <span class="stat"><b>__NGROUP__</b> 个大类 · <b>__NCAT__</b> 个子分类</span>
      <span class="stat">链接核实于 <b>__DATE__</b></span>
      <span class="stat">⭐ 为整理者主观印象，非背书</span>
    </div>
  </div>
</header>

<div class="toolbar">
  <div class="wrap">
    <input id="q" type="search" placeholder="搜索站点名称、说明或标签，例如：中转 / 比价 / 机场 / Go…" autocomplete="off">
    <div class="chips" id="chips"></div>
  </div>
</div>

<main class="wrap" id="main"></main>

<footer>
  <div class="wrap">
    <div class="box">
      <b>⚠️ 免责声明</b><br>
      本页面为纯信息聚合，所有链接均指向<strong>第三方独立运营</strong>的平台，不对其服务质量、资金安全、数据安全作任何担保。
      中转站、账号交易与网络代理类服务可能违反上游平台服务条款或当地法律法规，请自行核实资质与合法性，风险自负。
      本页与所列任何站点无隶属、代理或利益关系。
    </div>
    <div class="meta">
      <span>数据源：<a href="data/sites.json">data/sites.json</a> · 由 <code>tools/gen_site.py</code> 生成</span>
      <span>Made with 🐦 by <a href="https://github.com/Han-maker-wp">Han-maker-wp</a></span>
    </div>
  </div>
</footer>

<script>
const DATA = __DATA__;

const $main = document.getElementById('main');
const $q = document.getElementById('q');
const $chips = document.getElementById('chips');

let activeGroup = 'all';

const hostOf = u => { try { return new URL(u).host.replace(/^www\\./, ''); } catch (e) { return ''; } };
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

// 一级筛选：大类
const chipDefs = [{ id: 'all', label: '全部', grp: true }].concat(
  DATA.groups.map(g => ({ id: g.id, label: g.icon + ' ' + g.title, grp: true }))
);
$chips.innerHTML = chipDefs.map(c =>
  `<button class="chip${c.grp ? ' grp' : ''}${c.id === 'all' ? ' on' : ''}" data-grp="${c.id}">${esc(c.label)}</button>`
).join('');

$chips.addEventListener('click', e => {
  const b = e.target.closest('.chip');
  if (!b) return;
  activeGroup = b.dataset.grp;
  [...$chips.children].forEach(x => x.classList.toggle('on', x === b));
  render();
});

function hit(item, cat, grp, kw) {
  if (activeGroup !== 'all' && grp.id !== activeGroup) return false;
  if (!kw) return true;
  const hay = (item.name + ' ' + item.note + ' ' + item.tag + ' ' + cat.title + ' ' + grp.title).toLowerCase();
  return kw.split(/\\s+/).filter(Boolean).every(t => hay.includes(t));
}

function card(it) {
  return `<a class="card" href="${esc(it.url)}" target="_blank" rel="noopener noreferrer">
    <div class="top">
      <span class="nm">${esc(it.name)}</span>
      ${it.star ? '<span class="st" title="整理者印象较好">★</span>' : ''}
    </div>
    <div class="note">${esc(it.note)}</div>
    <div class="foot">
      <span class="tag">${esc(it.tag)}</span>
      <span class="host">${esc(hostOf(it.url))}</span>
    </div>
  </a>`;
}

function render() {
  const kw = $q.value.trim().toLowerCase();
  let html = '';
  for (const grp of DATA.groups) {
    if (activeGroup !== 'all' && grp.id !== activeGroup) continue;
    const secs = [];
    let gcount = 0, gcats = 0;
    for (const cat of grp.categories) {
      const items = cat.items.filter(it => hit(it, cat, grp, kw));
      if (!items.length) continue;
      gcount += items.length; gcats += 1;
      secs.push(`<section id="${esc(cat.id)}">
        <div class="shead"><h3>${esc(cat.icon + ' ' + cat.title)}</h3><span class="cnt">${items.length}</span></div>
        <p class="sdesc">${esc(cat.desc)}</p>
        <div class="grid">${items.map(card).join('')}</div>
      </section>`);
    }
    if (!secs.length) continue;
    const alt = grp.id !== 'ai' ? ' alt' : '';
    html += `<div class="group${alt}">
      <div class="group-head">
        <span class="gi">${esc(grp.icon)}</span>
        <h2>${esc(grp.title)}</h2>
        <span class="gmeta">${gcount} 个站点 · ${gcats} 个子分类</span>
      </div>
      <p class="group-desc">${esc(grp.desc)}</p>
      ${secs.join('')}
    </div>`;
  }
  $main.innerHTML = html || '<div class="empty">没有匹配的站点，换个关键词试试。</div>';
}

$q.addEventListener('input', render);
render();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    groups = data["groups"]
    total = sum(len(c["items"]) for g in groups for c in g["categories"])
    ncat = sum(len(g["categories"]) for g in groups)
    html = (
        TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
        .replace("__TOTAL__", str(total))
        .replace("__NGROUP__", str(len(groups)))
        .replace("__NCAT__", str(ncat))
        .replace("__DATE__", data["meta"].get("updated", str(date.today())))
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT}  ({len(html):,} bytes, {total} items, {len(groups)} groups, {ncat} categories)")


if __name__ == "__main__":
    main()
