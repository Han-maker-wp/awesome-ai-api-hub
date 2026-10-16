<div align="center">

# 🔌 Awesome AI API Hub

**One key. Every model.**

A curated collection of **60+** AI API relay stations · aggregators · official endpoints · comparison directories · self-hosted gateways

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

This repo organizes those entry points **by use case**, and marks how each link was verified — so you don't have to hop between a dozen "AI directory" sites.

> 📌 **This project is information aggregation only. It operates no service and takes part in no transaction.** See [Disclaimer](#️-disclaimer).

---

## 🗺️ Contents

| Category | What's inside | Who it's for |
| :--- | :--- | :--- |
| [🔌 Relay Stations / Aggregators](#-relay-stations--aggregators) | 16, reachable from China, Alipay-friendly | Solo devs, small teams, quick validation |
| [🏢 Official · Chinese Vendors](#-official--chinese-vendors) | 14 official consoles, free credits on sign-up | Compliance, invoicing, stability |
| [🌍 Official · Global Platforms](#-official--global-platforms) | 12, newest and most complete model coverage | Users with overseas network + foreign card |
| [🧭 Directories · Comparison · Reviews](#-directories--comparison--reviews) | 10, live pricing and uptime data | Do your homework before picking |
| [🛒 Accounts · SMS · Pools](#-accounts--sms--pools) | 6 third-party supporting services | When you need overseas accounts |
| [🛠️ Self-Hosted Gateways](#️-self-hosted-gateways) | 6 open-source, deploy yourself | When you don't want to hand over your keys |

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

Tools like Claude Code, Codex, Cline, Cherry Studio and LobeChat all accept a **custom API base URL + key** — fill them in and you're running.

---

## 🔌 Relay Stations / Aggregators

> OpenAI-compatible, one key for many models, Alipay/WeChat supported, reachable from mainland China.
> ⭐ marks stations the curator personally found solid — **not an endorsement.**

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**302.AI**](https://302.ai/) ⭐ | Pay-as-you-go, 10 API families (LLM/image/video/audio/RAG) plus ready-made online apps | `Aggregator` |
| [**AiHubMix**](https://aihubmix.com/) ⭐ | 720+ models, official cloud routes, auto-failover, drop-in for existing SDKs | `Aggregator` |
| [**V-API (gpt.ge)**](https://gpt.ge/) ⭐ | 650+ models, natively speaks Chat / Responses / Claude / Gemini, 3+ years running | `Aggregator` |
| [**Faro API**](https://faroapi.com/pricing) ⭐ | Daily check-in gives free trial credit | `Relay` |
| [**Pixel API**](https://ai-pixel.online/dashboard) ⭐ | Solid stability reputation, beginner friendly | `Relay` |
| [**NikoAPI**](https://us2.nikoapi.xyz/wallet) ⭐ | US nodes, good latency | `Relay` |
| [**WawAPI**](https://wawapi.xyz/model-square) ⭐ | Model marketplace + quick activation | `Relay` |
| [梦幻API](https://mhapi.cn/available-channels) | Live channel-status page, broad model coverage | `Relay` |
| [Camel API](https://luotuokj.top/dashboard) | Clean console, fine for light usage | `Relay` |
| [AIAPIBANK](https://aiapibank.com/) | Browse by model, pick your channel | `Relay` |
| [Lucis API](https://www.lucisapi.ai/keys) | Per-key management, good for project isolation | `Relay` |
| [元衡 API](https://cn.meta-api.vip/pricing) | Domestic nodes, transparent pricing | `Relay` |
| [EMOAI](https://api.emooo.cc/dashboard) | Focused on Chinese models, cheap | `CN models` |
| [OhMyGPT](https://www.ohmygpt.com/) | 240+ models, running since 2023, supports corporate invoicing | `Aggregator` |
| [API2D](https://api2d.com/) | Veteran relay, stability proven over time | `Aggregator` |
| [CloseAI](https://www.closeai-asia.com/) | Asian nodes, enterprise-oriented | `Aggregator` |

---

## 🏢 Official · Chinese Vendors

> Vendor-run consoles. Usually free credits for new users, best price and stability, real-name verification required.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**Alibaba Cloud Bailian**](https://bailian.console.aliyun.com/) ⭐ | Full Qwen lineup plus many third-party models | `Qwen` |
| [**Volcengine Ark**](https://console.volcengine.com/ark) ⭐ | Doubao series, aggressive pricing, high throughput | `Doubao` |
| [**SiliconFlow**](https://cloud.siliconflow.cn/) ⭐ | Top choice for hosting open models, free credits on sign-up | `Open models` |
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

---

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

---

## 🧭 Directories · Comparison · Reviews

> Not sure which one to pick? Compare first — live pricing, uptime, dilution rate, shutdown warnings.
> **Check these before reading any "recommendation" article.**

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [**TokenNav**](https://tokennav.cc/) ⭐ | 200+ stations with price / payment / uptime comparison | `Directory` |
| [**Hvoy AI**](https://www.hvoy.ai/) ⭐ | Station rankings + API authenticity testing (dilution, latency) | `Ranking+Test` |
| [**PriceAI**](https://priceai.cc/) ⭐ | Price radar for cheap subscriptions and relay APIs | `Compare` |
| [**OpenPrice**](https://www.openprice.cc/card-products) ⭐ | Aggregates 280+ vendors, lowest price and stock counts | `Compare` |
| [**Aibijia**](https://aibijia.org/) ⭐ | One-click subscription comparison | `Compare` |
| [**CardNav**](https://cardnav.xyz/) ⭐ | Directory for buying LLM accounts | `Directory` |
| [AI Subscription Directory](https://cheap-ai.uk/) | Discover GPT / Claude / Gemini / Grok in one place | `Directory` |
| [AI-Bot](https://ai-bot.cn/) | The most complete Chinese AI tool directory | `Directory` |
| [AIGC Directory](https://www.aigc.cn/) | Categorized generative-AI tools | `Directory` |
| [WayToAGI](https://www.waytoagi.com/) | Large AGI learning community | `Knowledge` |

---

## 🛒 Accounts · SMS · Pools

> ⚠️ **All third-party vendors, unaffiliated with the official platforms, with no guarantee of availability or support.**
> Account trading and SMS verification may violate the target platform's terms of service. Assess compliance and risk yourself.

| Name | Notes | Tag |
| :--- | :--- | :--- |
| [Account Planet](https://accboyytbptech.acceboy.com/) | Apple ID / overseas IDs / Telegram accounts | `Account` |
| [Aivora](https://www.aivora.cn/) | Self-service Cursor / ChatGPT / Claude / Gemini | `Account` |
| [AIProbe](https://aiprobe.top/) | Accounts + SMS verification in one | `Account+SMS` |
| [Aurora SMS](https://sms.iamu.eu.org/) | Global SMS verification codes | `SMS` |
| [NexusVault](https://nvtokens.com/) | Account pool trading and quota management | `Pool` |
| [AI Cloud Shop](https://pay.ldxp.cn/shop/Z6I0VZ0Q) | Auto-delivery card shop | `Cards` |

---

## 🛠️ Self-Hosted Gateways

> Don't want to hand your keys to anyone? Run your own relay: multi-key rotation, multi-channel balancing, unified billing — all under your control.
> Also ideal for a team-internal gateway with usage auditing.

| Project | Notes | Stack |
| :--- | :--- | :--- |
| [**one-api**](https://github.com/songquanpeng/one-api) ⭐ | The classic OpenAI-compatible aggregation system, 30+ upstreams, single-binary Docker deploy | `Go · 37k★` |
| [**new-api**](https://github.com/QuantumNous/new-api) ⭐ | Enhanced fork of one-api, modern UI, cross-converts OpenAI / Claude / Gemini | `Go · 50k★` |
| [**LiteLLM**](https://github.com/BerriAI/litellm) ⭐ | 100+ LLMs behind one call, plus a proxy gateway with cost tracking | `Python · 61k★` |
| [uni-api](https://github.com/yym68686/uni-api) | YAML-configured multi-backend, lightweight | `Python` |
| [gpt-load](https://github.com/tbphp/gpt-load) | Multi-key / multi-credential rotation with failover and usage stats | `Go · 7k★` |
| [Portkey Gateway](https://github.com/Portkey-AI/gateway) | Production-grade gateway, 1600+ models, 50+ guardrails | `TS · 13k★` |

---

## 🎯 Which one should you pick?

| Your situation | Recommended path |
| :--- | :--- |
| Just want to spend a few dollars and try it | A relay with **check-in credit / low minimum top-up** → [🔌 Relay Stations](#-relay-stations--aggregators) |
| Personal long-term use, want stability and low price | Check the [🧭 directories](#-directories--comparison--reviews) for uptime and price, then pick two for redundancy |
| Need invoices and compliance | [Chinese vendor consoles](#-official--chinese-vendors) or [global aggregators](#-official--global-platforms) |
| Team-wide gateway with usage auditing | [Self-host new-api / LiteLLM](#️-self-hosted-gateways) |
| Just want free credits | SiliconFlow, Zhipu, Volcengine Ark, Groq, Cloudflare Workers AI all offer new-user credit |
| Have overseas network + foreign card | Go straight to [OpenRouter](#-official--global-platforms) |

---

## 🛡️ How to avoid getting burned

Relay stations are **third-party resellers** of wildly varying quality. Five minutes of homework before you pay saves 90% of the pain:

1. **Check uptime and age** — look at historical data on [TokenNav](https://tokennav.cc/) / [Hvoy AI](https://www.hvoy.ai/). Be careful topping up heavily on a station that's only two months old.
2. **Test the "dilution rate"** — some stations quietly route `gpt-4o` requests to a cheaper small model. Authenticity-testing sites like Hvoy AI can detect this.
3. **Top up small first, never a yearly plan up front** — start with the minimum, run real workloads, then extend. Relay stations shutting down is normal, not exceptional.
4. **Verify model identity** — asking "what model are you" isn't enough. Use **known-answer hard questions** (specific math problems, dated events) and compare against official results.
5. **Don't send sensitive data to unknown stations** — your prompts pass through their servers. Trade secrets, personal data and proprietary code all count as sensitive.
6. **Know whether it's "official route" or "reverse-engineered channel"** — the latter is dirt cheap but can cut out at any moment and may violate upstream terms.
7. **Always keep a spare** — have at least two working stations, keep `base_url` and key in config, and switch away in five minutes when one dies.

---

## 🤝 Contributing

Found a good station, got burned, spotted a dead link? Open an [Issue](../../issues) or a PR:

- **Adding a station**: edit [`data/sites.json`](data/sites.json), add an entry to the right category, then run the link checker.
- **Dead links**: delete or update to the new domain. Relay stations change domains constantly — fixes are very welcome.
- **Inclusion bar**: the site must be genuinely reachable and offer a real service. Pure ad pages, obvious phishing sites, and undocumented short links are rejected outright.

```bash
# Check reachability of every link
python tools/check_links.py
```

---

## 📅 Changelog

| Date | Change |
| :--- | :--- |
| 2026-10-16 | Initial release, 64 entries. Verified link status; fixed `new-api` migration to `QuantumNous/new-api` and `V3 API` migration to `gpt.ge` |

---

## ⚠️ Disclaimer

- This project is **pure information aggregation**. It makes no guarantee about the service quality, financial safety, or data safety of any third-party site.
- Every link points to an **independently operated third-party platform**. Verify its credentials, terms and legality before use.
- Relay and account-trading services **may violate upstream platform terms of service** (e.g. OpenAI's, Anthropic's usage policies). You bear the risk of use.
- Comply with the laws and regulations of your jurisdiction and with each platform's terms. **Do not use these services for any unlawful purpose.**
- This project has **no affiliation, agency, or financial relationship** with any listed site (a ⭐ reflects the curator's subjective impression only and is not a recommendation or endorsement).
- If you operate one of these sites and want to be included, corrected, or removed, open an Issue and it will be handled promptly.

---

<div align="center">

**If this list saved you an afternoon of searching, a ⭐ Star is the best thanks.**

<sub>Made with 🐦 by <a href="https://github.com/Han-maker-wp">Han-maker-wp</a></sub>

</div>
