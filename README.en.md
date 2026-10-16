<div align="center">

# 🔌 Awesome AI API Hub

**One key. Every model.**

**102** curated entries in two top-level groups: **AI-related** (relay stations / aggregators / official endpoints / comparison directories / self-hosted gateways) and **Non-AI · General Infrastructure** (network proxies / airport reviews / network tools / accounts & SMS)

Pay with Alipay/WeChat, no foreign card, no network gymnastics — call GPT, Claude, Gemini, DeepSeek and every major Chinese LLM from one endpoint

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-3da639.svg)](LICENSE)
[![Links Checked](https://img.shields.io/badge/links%20checked-2026--10--16-blue.svg)](#-changelog)

**English** · [简体中文](README.md)

<br>

<a href="index.html"><img src="assets/screenshot.png" alt="Awesome AI API Hub preview" width="880"></a>

<sub>↑ A single-file navigator (<a href="index.html"><code>index.html</code></a>) ships with this repo — searchable, filterable, drop it on GitHub Pages and you're done</sub>

</div>

---

## 😤 The problem

Want to call an LLM API? You hit a wall:

| Wall | Reality |
| :--- | :--- |
| "Sign-up needs an overseas phone number" | SMS verification hoops, one after another |
| "Top-up needs a Visa card" | No foreign card, and binding one often triggers risk control |
| "Can't even reach the endpoint" | Now you also have a network problem to solve |
| "There are 20 Chinese model vendors" | 20 consoles, 20 docs sets, 20 invoices |

**Relay stations / aggregators** exist to tear that wall down: one key, one top-up, one OpenAI-compatible protocol, dozens or hundreds of models behind it. Change one `base_url` and you move from GPT to Claude to DeepSeek.

This repo organizes those entry points **into two top-level groups**, and marks how each link was verified.

> 📌 **This project is information aggregation only. It operates no service and takes part in no transaction.** See [Disclaimer](#️-disclaimer).

---

## 🗺️ Contents

### 🤖 I. AI-related

| Category | What's inside | Who it's for |
| :--- | :--- | :--- |
| [🔌 Relay Stations / Aggregators](#-relay-stations--aggregators) | 17, reachable from China, Alipay-friendly | Solo devs, small teams |
| [🏢 Official · Chinese Vendors](#-official--chinese-vendors) | 14 official consoles, free credits | Compliance, invoicing, stability |
| [🌍 Official · Global Platforms](#-official--global-platforms) | 12, newest model coverage | Overseas network + foreign card |
| [🔬 Detection · Verification](#-ai-api-detection--verification) | 7, test real model identity and dilution | **Verify before you pay** |
| [🧭 AI Directories · Comparison](#-ai-directories--comparison) | 10, live pricing and uptime | Do your homework before picking |
| [🛒 AI Accounts · Subscriptions](#-ai-accounts--subscriptions) | 3, buy AI memberships | When you need a ready account |
| [🛠️ Self-Hosted Gateways](#️-self-hosted-gateways) | 7 open-source, deploy yourself | When you don't want to hand over keys |

### 🌐 II. Non-AI · General Infrastructure

| Category | What's inside | Who it's for |
| :--- | :--- | :--- |
| [🚀 Network Proxies · Airports / VPN](#-network-proxies--airports--vpn) | 12, cross-border egress | When you need a stable egress (⚠️ see notice) |
| [📊 Airport Reviews · Exit-Scam Watch](#-airport-reviews--exit-scam-watch--blogs) | 13, independent tests & scam lists | **Read how others got burned, before you pay** |
| [🔧 Network Tools · IP Check · CF](#-network-tools--ip-check--cloudflare) | 4, IP purity and node optimization | Inspect IP quality before buying |
| [📱 Accounts · SMS · Pools](#-accounts--sms--pools) | 3, overseas accounts & SMS codes | When you need an overseas account |

---

## ⚡ 30-second quickstart

Nearly every station speaks the **OpenAI-compatible protocol**. Change two fields:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://<your-station-domain>/v1",  # ← swap in the station's endpoint
    api_key="sk-xxxxxxxxxxxxxxxx",                # ← swap in your key
)

resp = client.chat.completions.create(
    model="gpt-4o",                               # or claude-sonnet-4-5 / gemini-2.5-pro / deepseek-chat
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

Tools like Claude Code, Codex, Cline, Cherry Studio and LobeChat all accept a **custom API base URL + key**.

---

# 🤖 I. AI-related

## 🔌 Relay Stations / Aggregators

> OpenAI-compatible, one key for many models, Alipay/WeChat supported, reachable from mainland China.
> ⭐ marks stations the curator personally found solid — **not an endorsement.**
>
> 💡 **Curator's daily drivers**: [**NikoAPI**](https://us2.nikoapi.xyz/wallet) and [**WawAPI**](https://wawapi.xyz/model-square) — best latency-to-stability ratio in practice, both allow small top-ups and daily check-in credit. **Still run the [checklist](#️-how-to-avoid-getting-burned) before you top up.**

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**302.AI**](https://302.ai/) ⭐ | Pay-as-you-go, 10 API families plus ready-made online apps | `Aggregator` |
| [**AiHubMix**](https://aihubmix.com/) ⭐ | 720+ models, official cloud routes, auto-failover | `Aggregator` |
| [**V-API (gpt.ge)**](https://gpt.ge/) ⭐ | 650+ models, natively speaks Chat / Responses / Claude / Gemini | `Aggregator` |
| [**基元律动 TokenRhythm**](https://tokenrhythm.ai/) ⭐ | China's answer to OpenRouter — one key for the full model catalog, agent-native smart routing | `Aggregator` |
| [**数眼智能 DataEyesAI**](https://www.shuyanai.com/) ⭐ | Enterprise model cloud, 5M free tokens for new users, WeChat/Alipay top-up, multi-team key management | `Aggregator` |
| [**Faro API**](https://faroapi.com/pricing) ⭐ | Daily check-in gives free trial credit | `Relay` |
| [**Pixel API**](https://ai-pixel.online/dashboard) ⭐ | Solid stability reputation, beginner friendly | `Relay` |
| [**NikoAPI**](https://us2.nikoapi.xyz/wallet) ⭐ | US nodes, good latency | `Relay` |
| [**WawAPI**](https://wawapi.xyz/model-square) ⭐ | Model marketplace + quick activation | `Relay` |
| [梦幻API](https://mhapi.cn/available-channels) | Live channel-status page, broad model coverage ⚠️ Possibly dead as of 2026-10; domain may have changed | `Relay` |
| [Camel API](https://luotuokj.top/dashboard) | Clean console, fine for light usage | `Relay` |
| [AIAPIBANK](https://aiapibank.com/) | Browse by model, pick your channel | `Relay` |
| [元衡 API](https://cn.meta-api.vip/pricing) | Domestic nodes, transparent pricing | `Relay` |
| [EMOAI](https://api.emooo.cc/dashboard) | Focused on Chinese models, cheap | `CN models` |
| [OhMyGPT](https://www.ohmygpt.com/) | 240+ models, running since 2023, corporate invoicing | `Aggregator` |
| [API2D](https://api2d.com/) | Veteran relay, stability proven over time | `Aggregator` |
| [CloseAI](https://www.closeai-asia.com/) | Asian nodes, enterprise-oriented | `Aggregator` |

## 🏢 Official · Chinese Vendors

> Vendor-run consoles. Usually free credits for new users, best price and stability, real-name verification required.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**Alibaba Cloud Bailian**](https://bailian.console.aliyun.com/) ⭐ | Full Qwen lineup plus many third-party models | `Qwen` |
| [**Volcengine Ark**](https://console.volcengine.com/ark) ⭐ | Doubao series, aggressive pricing, high throughput | `Doubao` |
| [**SiliconFlow**](https://cloud.siliconflow.cn/) ⭐ | Top choice for hosting open models, free credits | `Open models` |
| [**Zhipu BigModel**](https://bigmodel.cn/) ⭐ | GLM series, free credits, strong tool calling | `GLM` |
| [**Moonshot Kimi**](https://platform.moonshot.cn/) ⭐ | Kimi series, ultra-long context | `Kimi` |
| [SenseNova](https://platform.sensenova.cn/) | Full multimodal capability | `SenseNova` |
| [Baidu Qianfan](https://console.bce.baidu.com/qianfan/) | ERNIE family | `ERNIE` |
| [Tencent Hunyuan](https://console.cloud.tencent.com/hunyuan) | Integrated with Tencent Cloud | `Hunyuan` |
| [iFlytek Spark](https://console.xfyun.cn/) | Strong speech capabilities | `Spark` |
| [MiniMax](https://platform.minimaxi.com/) | Great long-context and speech | `MiniMax` |
| [StepFun](https://platform.stepfun.com/) | Fast multimodal iteration | `Step` |
| [01.AI](https://platform.lingyiwanwu.com/) | Yi series, good value | `Yi` |
| [Infinigence Infini-AI](https://cloud.infini-ai.com/) | Compute + models, heterogeneous scheduling | `Compute` |
| [PPIO](https://ppio.com/) | Distributed GPU cloud, cheap model API | `Compute` |

## 🌍 Official · Global Platforms

> Mainstream international aggregators and inference platforms. Newest models, standard protocols; some need overseas network and a foreign card.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**OpenRouter**](https://openrouter.ai/) ⭐ | The largest model router; one key, every model | `Aggregator` |
| [**Groq**](https://console.groq.com/) ⭐ | LPU-speed inference, generous free tier | `Inference` |
| [Together AI](https://api.together.xyz/) | Fast, cheap open-model inference | `Inference` |
| [Fireworks AI](https://fireworks.ai/) | Low latency, production-ready | `Inference` |
| [DeepInfra](https://deepinfra.com/) | Per-token billing, full open-model coverage | `Inference` |
| [Novita AI](https://novita.ai/) | Many models, credits on sign-up | `Inference` |
| [Hyperbolic](https://hyperbolic.xyz/) | Decentralized compute, competitive pricing | `Inference` |
| [Cerebras](https://cloud.cerebras.ai/) | Wafer-scale chips, startling speed | `Inference` |
| [Replicate](https://replicate.com/) | One-click open models, rich image/video | `Hosting` |
| [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) | Unified entry to many inference providers | `Hosting` |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | Edge inference, free tier | `Edge` |
| [Poe](https://poe.com/) | By Quora, chat-style multi-model access | `Aggregator` |

## 🔬 AI API Detection · Verification

> The biggest trap with relay stations is **"swapping and dumbing down"** — you pay for GPT-5 and get a distilled small model. Some third-party reviews claim nearly half of relay endpoints do this to some degree.
> **Verify before you pay.**
> ⚠️ Always test with a **temporary key**, never your main key, on an unknown station.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**Hvoy AI**](https://www.hvoy.ai/) ⭐ | Station rankings + API authenticity testing (dilution, latency, uptime) | `Ranking+Test` |
| [**Ztest**](https://ztest.cc/) ⭐ | 25–40 probes measure model authenticity and response quality; publishes a trust ranking | `Probe` |
| [**API-CHECK**](https://api-check.com/) ⭐ | Detects fake models, token injection, prompt extraction, instruction override, response fingerprinting | `Check` |
| [**Model-Check**](https://model-check.org/) ⭐ | Finds model swapping, dilution, stream breaks, crippled tool calling | `Check` |
| [**API Ranking**](https://apiranking.com/) ⭐ | 139+ stations tested: authenticity, billing reconciliation, cache hits, degradation | `Benchmark` |
| [火眼金睛识 AI](http://eagle.videogen.art/) | Client-side only; dedicated tests to spot swapped Claude / OpenAI models | `Check` |
| [Zhizhi API Purity](https://github.com/businesszhizhiai/zhizhi-api-purity) | Open-source purity checker you can self-host, with stability logging | `Open source` |

## 🧭 AI Directories · Comparison

> Not sure which one to pick? Compare first — live pricing, uptime, shutdown warnings.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**TokenNav**](https://tokennav.cc/) ⭐ | 200+ stations with price / payment / uptime comparison | `Directory` |
| [**PriceAI**](https://priceai.cc/) ⭐ | Price radar for cheap subscriptions and relay APIs | `Compare` |
| [**OpenPrice**](https://www.openprice.cc/card-products) ⭐ | Aggregates 280+ vendors, lowest price and stock counts | `Compare` |
| [**Aibijia**](https://aibijia.org/) ⭐ | One-click subscription comparison | `Compare` |
| [**CardNav**](https://cardnav.xyz/) ⭐ | Directory for buying LLM accounts | `Directory` |
| [AI Coding Welfare Directory](https://github.com/panxunying/ai-coding-welfare) | Free-tier relay stations for Claude Code / Codex, quotas refreshed every 6 hours, ships a one-click setup script ⚠️ Contains referral links — judge for yourself | `Welfare` |
| [AI Subscription Directory](https://cheap-ai.uk/) | Discover GPT / Claude / Gemini / Grok in one place | `Directory` |
| [AI-Bot](https://ai-bot.cn/) | The most complete Chinese AI tool directory | `Directory` |
| [AIGC Directory](https://www.aigc.cn/) | Categorized generative-AI tools | `Directory` |
| [WayToAGI](https://www.waytoagi.com/) | Large AGI learning community | `Knowledge` |

## 🛒 AI Accounts · Subscriptions

> ⚠️ **Third-party vendors, unaffiliated with the official platforms, no guarantee of availability or support.**
> Account trading may violate the target platform's terms of service.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [Aivora](https://www.aivora.cn/) | Self-service Cursor / ChatGPT / Claude / Gemini | `Account` |
| [AIProbe](https://aiprobe.top/) | AI accounts + SMS verification in one | `Account+SMS` |
| [AI Cloud Shop](https://pay.ldxp.cn/shop/Z6I0VZ0Q) | Auto-delivery card shop | `Cards` |

## 🛠️ Self-Hosted Gateways

> Don't want to hand your keys to anyone? Run your own relay: multi-key rotation, multi-channel balancing, unified billing.
> Also ideal for a team-internal gateway with usage auditing.

| Project | Notes | Stack |
| :--- | :--- | :--- |
| [**one-api**](https://github.com/songquanpeng/one-api) ⭐ | The classic OpenAI-compatible aggregation system, 30+ upstreams, single-binary Docker deploy | `Go · 37k★` |
| [**new-api**](https://github.com/QuantumNous/new-api) ⭐ | Enhanced fork, modern UI, cross-converts OpenAI / Claude / Gemini | `Go · 50k★` |
| [**sub2api**](https://github.com/Wei-Shaw/sub2api) ⭐ | **Subscription-to-API** gateway: turn Claude / OpenAI / Gemini / Grok **subscription accounts** into API keys, with carpooling, token-level billing and self-service top-up ⚠️ May violate upstream subscription terms | `Go · 44k★` |
| [**LiteLLM**](https://github.com/BerriAI/litellm) ⭐ | 100+ LLMs behind one call, plus a proxy gateway with cost tracking | `Python · 61k★` |
| [uni-api](https://github.com/yym68686/uni-api) | YAML-configured multi-backend, lightweight | `Python` |
| [gpt-load](https://github.com/tbphp/gpt-load) | Multi-key rotation with failover and usage stats | `Go · 7k★` |
| [Portkey Gateway](https://github.com/Portkey-AI/gateway) | Production-grade gateway, 1600+ models, 50+ guardrails | `TS · 13k★` |

---

# 🌐 II. Non-AI · General Infrastructure

> Not directly about LLMs, but these are the **prerequisites**: network egress, how to pick an airport, IP quality, accounts and SMS.

## 🚀 Network Proxies · Airports / VPN

> ⚠️ **Compliance notice**: this category is a link collection only, not a recommendation or usage advice. In mainland China, providing or using such cross-border proxy services may violate local law and the terms of the underlying services. Judge for yourself and bear all risk.
> Pricing varies wildly and shutdown rates are high — if you do use one, **pay monthly, don't gamble on a yearly plan.**

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [Webshare](https://dashboard.webshare.io/staticResidential/pricing) | Static residential proxy IPs, metered or monthly | `Residential IP` |
| [Yue.to](https://my.yue.to/) | High traffic allowance, for heavier use | `Airport` |
| [GLaDOS](https://glados-facility.com/) | Clean IPs + education discount, long-running | `Airport` |
| [星辰VPN](https://xcvpn.us/) | Home-broadband nodes, ~¥17/month | `Airport` |
| [iKuuu VPN](https://ikuuu.win/) | Free / low-cost tier, light use | `Airport` |
| [Mitce](https://mitce.io/) | Cheap small-traffic plan | `Airport` |
| [FlyBit](https://fb.fastfastfast.buzz/) | ~¥15/month, home-broadband nodes ⚠️ Possibly dead as of 2026-10; domain may have changed | `Airport` |
| [良心云](https://xn--9kqz23b19z.com/) | Budget-friendly airport | `Airport` |
| [寰宇云](https://hyy.52kok.cn/) | Native IPs, ~¥79/year | `Airport` |
| [极连云](https://bhjsehj3u.jilianat.homes/) | Native IPs, ~¥96/year (random subdomain entry) | `Airport` |
| [TAG](https://honven.l49.net/) | Includes home-broadband nodes, ~¥162/year | `Airport` |
| [筋斗云](https://yongjichang.com/) | ~¥17/month, has third-party reviews | `Airport` |

## 📊 Airport Reviews · Exit-Scam Watch · Blogs

> This market suffers from **severe information asymmetry**: every landing page claims "IPLC dedicated lines, native IPs, no throttling", while real-world performance varies enormously — and vendors disappearing with prepaid money is routine.
> Before paying, read independent tests and search the vendor's name in the exit-scam lists. That matters far more than saving a few yuan.
>
> ⚠️ Most of these sites run on **affiliate commissions**, so their recommendation lists carry commercial bias. Treat them as **information sources**, not **leaderboards**.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**Limbopro (毒奶博客)**](https://limbopro.com/) ⭐ | Hands-on airport tests + exit-scam warnings; the most trusted veteran blog | `Review` |
| [**Paolujichang (跑路机场清单)**](https://github.com/limbopro/Paolujichang) ⭐ | Open-source GitHub list of dead and high-risk vendors | `Scam list` |
| [**Ermo (二毛)**](https://ermao.net/) ⭐ | Airport reviews + self-hosting guides, updated steadily | `Review` |
| [**ClashX Blog (茶波博客)**](https://clashx.pro/) ⭐ | Airport reviews and client tutorials, practical focus | `Review` |
| [**AiJichang (爱机场)**](https://aijichang.com/) ⭐ | Recommendations + exit-scam warnings + news, actively updated | `Review` |
| [RocketWang (火箭旺)](https://shadowrocket.one/) | Per-vendor hands-on tests (WgetCloud / Flower Cloud / Jilianyun), updated into 2026 | `Review` |
| [Fanqiangdao (翻墙岛)](https://fanqiangdao.com/) | Recommendations plus networking explainers | `Review` |
| [JichangCN](https://jichangcnweb.com/) | Cross-vendor recommendation roundups | `Recs` |
| [Jichang Tuijian Pro](https://jichangtuijianpro.com/) | Categorized recommendations and deals | `Recs` |
| [RuntuShare (润兔分享)](https://runtushare.net/) | Airport reviews and deal sharing | `Review` |
| [DuyaoSS (毒药SS)](https://duyaoss.com/) | Classic review site, ⚠️ essentially dormant since 2024-04; historical reference only | `Review` |
| [Telegram channel (翻墙频道)](https://t.me/ffqchannel) | Real-time exit-scam reports and node sharing | `Channel` |
| [Airport Directory](https://vpsknow.com/airport-recommendations) | Cross-comparison and reviews of airports | `Directory` |

## 🔧 Network Tools · IP Check · Cloudflare

> Verify egress quality, optimize nodes, build your own tunnel. **Inspect IP quality before buying.**

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**Ping0**](https://www.ping0.cc/) ⭐ | IP purity / risk score check | `IP Check` |
| [CF Preferred Domains](https://cf.090227.xyz/) | Cloudflare preferred IP / domain list | `CF` |
| [BestCF · CF EDT](https://bestcf.pages.dev/) | Cloudflare EdgeTunnel related directory | `CF` |
| [Cloudflare Dashboard](https://dash.cloudflare.com/) | Pages / Workers / Zero Trust console | `Console` |

## 📱 Accounts · SMS · Pools

> ⚠️ **All third-party vendors, unaffiliated with the official platforms, no guarantee of availability or support.**
> Account trading and SMS verification may violate the target platform's terms of service.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [Account Planet](https://accboyytbptech.acceboy.com/) | Apple ID / overseas IDs / Telegram accounts | `Account` |
| [Aurora SMS](https://sms.iamu.eu.org/) | Global SMS verification codes | `SMS` |
| [NexusVault](https://nvtokens.com/) | Account pool trading and quota management | `Pool` |

---

## 🎯 Which one should you pick?

| Your situation | Recommended path |
| :--- | :--- |
| Just want to spend a few dollars and try it | A relay with **check-in credit / low minimum top-up** → [🔌 Relay Stations](#-relay-stations--aggregators) |
| Personal long-term use, want stability and low price | Check the [🧭 directories](#-ai-directories--comparison) for uptime and price, then pick two for redundancy |
| Need invoices and compliance | [Chinese vendor consoles](#-official--chinese-vendors) or [global aggregators](#-official--global-platforms) |
| Team-wide gateway with usage auditing | [Self-host new-api / LiteLLM](#️-self-hosted-gateways) |
| Just want free credits | SiliconFlow, Zhipu, Volcengine Ark, Groq, Cloudflare Workers AI |
| Have overseas network + foreign card | Go straight to [OpenRouter](#-official--global-platforms) |
| API works but network is unstable | Fix the egress first → [🚀 Proxies](#-network-proxies--airports--vpn), [🔧 IP Check](#-network-tools--ip-check--cloudflare) |

---

## 🛡️ How to avoid getting burned

Relay stations are **third-party resellers** of wildly varying quality. Five minutes of homework before you pay saves 90% of the pain:

1. **Check uptime and age** — look at historical data on [TokenNav](https://tokennav.cc/) / [Hvoy AI](https://www.hvoy.ai/). Be careful topping up heavily on a two-month-old station.
2. **Test the "dilution rate"** — some stations quietly route `gpt-4o` requests to a cheaper small model. Authenticity-testing sites can detect this.
3. **Top up small first, never a yearly plan up front** — start with the minimum, run real workloads, then extend. Shutdowns are normal, not exceptional.
4. **Verify model identity** — asking "what model are you" isn't enough. Use **known-answer hard questions** and compare against official results.
5. **Don't send sensitive data to unknown stations** — your prompts pass through their servers.
6. **Know whether it's "official route" or "reverse-engineered channel"** — the latter is dirt cheap but can cut out at any moment.
7. **Always keep a spare** — have at least two working stations and keep config switchable.
8. **Airports have their own set of traps** — prefer monthly billing, verifiable IP purity, and long operating history. A "super-cheap yearly blowout" is usually a warning sign. Search the vendor's name in the [📊 reviews and scam lists](#-airport-reviews--exit-scam-watch--blogs) before paying — **but remember those sites live on affiliate commissions, so discount their leaderboards accordingly.**

---

## 🤝 Contributing

Found a good station, got burned, spotted a dead link? Open an [Issue](../../issues) or a PR:

- **Adding a station**: edit [`data/sites.json`](data/sites.json), add an entry under the right group → category, then run the link checker.
- **Dead links**: delete or update to the new domain. Relay stations change domains constantly.
- **Inclusion bar**: the site must be genuinely reachable and offer a real service. Pure ad pages, obvious phishing sites, and undocumented short links are rejected outright.
- **Prohibited**: invitation codes, referral links, affiliate links. **Instant rejection.**

```bash
python tools/check_links.py   # check reachability
python tools/gen_site.py      # regenerate the navigator page
```

---

## 📅 Changelog

| Date | Change |
| :--- | :--- |
| 2026-10-16 | Full re-check of all **102 links**: **98 reachable directly**; 2 (爱机场 / 火箭旺) block headless requests but were confirmed live in a browser; 2 confirmed dead (梦幻API / FlyBit) kept and flagged. `tools/check_links.py` upgraded: `--proxy` support, automatic retry, and an anti-bot allowlist to eliminate flaky false negatives |
| 2026-10-16 | Added **基元律动 TokenRhythm** and **数眼智能 DataEyesAI** aggregators; **sub2api** (subscription-to-API gateway) under self-hosted; **AI Coding Welfare Directory** under directories; removed the dead Lucis API; added a curator's daily-driver note (Niko / WaW). **102** entries total |
| 2026-10-16 | Added **📊 Airport Reviews · Exit-Scam Watch · Blogs** category (13 review sites / scam lists / channels); **99** entries / 11 categories total |
| 2026-10-16 | Added **🔬 AI API Detection · Verification** category (7 checkers) to counter "swapping and dumbing down"; **87** entries / 10 categories total |
| 2026-10-16 | Re-verified all **81 links** through a real proxy: **75 reachable**. Flagged 3 likely-dead entries (梦幻API / Lucis API / FlyBit), fixed the 极连云 entry domain |
| 2026-10-16 | **Restructured into two top-level groups**: 🤖 AI-related (61) + 🌐 Non-AI · General Infrastructure (20) — 81 entries across 9 categories; added proxy, network-tool and account sections |
| 2026-10-16 | Initial release, 64 entries. Fixed `new-api` → `QuantumNous/new-api` and `V3 API` → `gpt.ge` migrations |

---

## ⚠️ Disclaimer

- This project is **pure information aggregation**. It makes no guarantee about the service quality, financial safety, or data safety of any third-party site.
- Every link points to an **independently operated third-party platform**. Verify its credentials, terms and legality before use.
- Relay, account-trading and network-proxy services **may violate upstream platform terms of service or local law**. You bear the risk of use.
- Comply with the laws and regulations of your jurisdiction. **Do not use these services for any unlawful purpose.**
- This project has **no affiliation, agency, or financial relationship** with any listed site (a ⭐ reflects the curator's subjective impression only and is not a recommendation or endorsement).
- If you operate one of these sites and want to be included, corrected, or removed, open an Issue.
- The MIT license **covers this repository's own content only** (list, docs, scripts) and grants no rights to, or warranty regarding, any third-party site or service.

---

<div align="center">

**If this list saved you an afternoon of searching, a ⭐ Star is the best thanks.**

<sub>Made with 🐦 by <a href="https://github.com/Han-maker-wp">Han-maker-wp</a></sub>

</div>
