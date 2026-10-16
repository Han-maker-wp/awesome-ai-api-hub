<div align="center">

# 🔌 Awesome AI API Hub

**一个 Key，打通全世界的大模型。**

精选 **60+** 个 AI API 中转站 · 聚合网关 · 官方直连入口 · 比价导航站 · 开源自建方案

不用外币卡、不用折腾网络，支付宝/微信充值即可调用 GPT、Claude、Gemini、DeepSeek 与全部国产大模型

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-3da639.svg)](LICENSE)
[![Links Checked](https://img.shields.io/badge/links%20checked-2026--10--16-blue.svg)](#-更新记录)

<br>

<a href="index.html"><img src="assets/screenshot.png" alt="Awesome AI API Hub 导航页预览" width="880"></a>

<sub>↑ 仓库内置单文件导航页 <a href="index.html"><code>index.html</code></a>，可搜索、可筛选，直接丢 GitHub Pages 就能用</sub>

</div>

---

## 😤 先说痛点

想用大模型 API 写点东西，你会撞上这堵墙：

| 撞墙现场 | 现实 |
| :--- | :--- |
| 「注册 OpenAI 要海外手机号」 | 接码 / 虚拟号，一步一个坑 |
| 「充值得用 Visa 卡」 | 没有外币卡，绑卡还容易被风控 |
| 「网络连不上」 | 还得先解决网络问题 |
| 「国内模型厂商有 20 家」 | 20 个控制台、20 套文档、20 份账单 |

**中转站 / 聚合平台**就是为了拆掉这堵墙：一个 Key、一次充值、一套 OpenAI 兼容协议，背后挂几十上百个模型。改一行 `base_url` 就能从 GPT 切到 Claude，再切到 DeepSeek。

这个仓库把这类入口**按用途分类整理好**，并标注每条链接的核实状态，省得你在无数个「AI 导航站」之间来回跳。

> 📌 **本项目只做信息聚合与整理，不运营任何服务、不参与任何交易。** 详见底部[免责声明](#-免责声明)。

---

## 🗺️ 目录

| 分类 | 内容 | 适合谁 |
| :--- | :--- | :--- |
| [🔌 中转站 / 聚合平台](#-ai-api-中转站--聚合平台) | 16 个，国内可直连，支付宝充值 | 个人开发者、小团队、快速验证 |
| [🏢 官方直连 · 国内厂商](#-官方直连--国内大模型厂商) | 14 个，官方控制台，注册送额度 | 要合规、要发票、要稳定性 |
| [🌍 官方直连 · 国际平台](#-官方直连--国际平台) | 12 个，模型最新最全 | 有海外网络与外币卡的用户 |
| [🧭 导航站 · 比价 · 评测](#-导航站--比价--评测) | 10 个，实时报价与在线率 | 选型前做功课，避坑 |
| [🛒 账号 · 接码 · 号池](#-账号--接码--号池) | 6 个，第三方配套资源 | 需要海外账号的场景 |
| [🛠️ 自建网关](#️-自建网关--开源自部署) | 5 个，开源自部署 | 不想把 Key 交给别人 |

---

## ⚡ 30 秒上手

拿到任意中转站的 Key 后，绝大多数站点都是 **OpenAI 兼容协议**，改两个参数即可：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://<中转站域名>/v1",   # ← 换成对应站点的接口地址
    api_key="sk-xxxxxxxxxxxxxxxx",        # ← 换成你的 Key
)

resp = client.chat.completions.create(
    model="gpt-4o",                       # 或 claude-sonnet-4-5 / gemini-2.5-pro / deepseek-chat
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

对应地，Claude Code / Codex / Cline / Cherry Studio / LobeChat 这类工具，也都支持填写**自定义 API 地址 + Key**，填上就能用。

---

## 🔌 AI API 中转站 / 聚合平台

> OpenAI 兼容协议，一个 Key 打通多家模型，支持支付宝 / 微信支付，国内网络可直连。
> ⭐ 为个人使用体验较好、社区口碑较稳的站点。

| 名称 | 说明 | 标签 |
| :--- | :--- | :--- |
| [**302.AI**](https://302.ai/) ⭐ | 按量付费，10 大类 API（LLM/图像/视频/音频/RAG）+ 开箱即用的在线 App | `聚合` |
| [**AiHubMix**](https://aihubmix.com/) ⭐ | 720+ 模型，官方云路由 + 自动故障转移，多 SDK 即插即用 | `聚合` |
| [**V-API (gpt.ge)**](https://gpt.ge/) ⭐ | 650+ 模型，原生兼容 Chat / Responses / Claude / Gemini 四种协议，运营 3 年+ | `聚合` |
| [**Faro API**](https://faroapi.com/pricing) ⭐ | 支持每日签到，可以白嫖试用额度 | `中转` |
| [**Pixel API**](https://ai-pixel.online/dashboard) ⭐ | 稳定性口碑不错，新手友好 | `中转` |
| [**NikoAPI**](https://us2.nikoapi.xyz/wallet) ⭐ | 美区节点，延迟表现好 | `中转` |
| [**WawAPI**](https://wawapi.xyz/model-square) ⭐ | 模型广场 + 快速开通 | `中转` |
| [梦幻API](https://mhapi.cn/available-channels) | 渠道状态页实时可查，模型覆盖面广 | `中转` |
| [Camel API](https://luotuokj.top/dashboard) | 骆驼科技，控制台清爽，适合轻量调用 | `中转` |
| [AIAPIBANK](https://aiapibank.com/) | 模型广场式浏览，按模型挑渠道 | `中转` |
| [Lucis API](https://www.lucisapi.ai/keys) | 独立 Key 管理，便于多项目隔离 | `中转` |
| [元衡 API](https://cn.meta-api.vip/pricing) | 国内节点，价格表公开透明 | `中转` |
| [EMOAI](https://api.emooo.cc/dashboard) | 主打国产大模型，价格低 | `国产模型` |
| [OhMyGPT](https://www.ohmygpt.com/) | 240+ 模型，2023 年运营至今，支持对公发票 | `聚合` |
| [API2D](https://api2d.com/) | 老牌中转，稳定性经过时间检验 | `聚合` |
| [CloseAI](https://www.closeai-asia.com/) | 亚洲节点，企业向服务 | `聚合` |

---

## 🏢 官方直连 · 国内大模型厂商

> 厂商官方控制台。新用户普遍送免费额度，价格最实、最稳，缺点是需要实名认证。

| 名称 | 说明 | 标签 |
| :--- | :--- | :--- |
| [**阿里云百炼**](https://bailian.console.aliyun.com/) ⭐ | 通义千问全系 + 大量三方模型 | `通义` |
| [**火山方舟**](https://console.volcengine.com/ark) ⭐ | 豆包系列，价格激进，吞吐高 | `豆包` |
| [**硅基流动 SiliconFlow**](https://cloud.siliconflow.cn/) ⭐ | 开源模型托管首选，注册即送额度 | `开源模型` |
| [**智谱 BigModel**](https://bigmodel.cn/) ⭐ | GLM 系列，新用户送额度，工具调用强 | `GLM` |
| [**Moonshot Kimi**](https://platform.moonshot.cn/) ⭐ | Kimi 系列，超长上下文 | `Kimi` |
| [商汤 SenseNova](https://platform.sensenova.cn/) | 日日新大模型，多模态能力完整 | `日日新` |
| [百度千帆](https://console.bce.baidu.com/qianfan/) | 文心一言 + ERNIE 全系 | `文心` |
| [腾讯混元](https://console.cloud.tencent.com/hunyuan) | 混元大模型，腾讯云生态集成 | `混元` |
| [讯飞星火](https://console.xfyun.cn/) | 星火大模型，语音能力强 | `星火` |
| [MiniMax](https://platform.minimaxi.com/) | abab 系列，长文本与语音出色 | `MiniMax` |
| [阶跃星辰 StepFun](https://platform.stepfun.com/) | Step 系列，多模态迭代快 | `Step` |
| [零一万物](https://platform.lingyiwanwu.com/) | Yi 系列，性价比高 | `Yi` |
| [无问芯穹 Infini-AI](https://cloud.infini-ai.com/) | 算力 + 模型一体，异构调度 | `算力` |
| [PPIO 派欧云](https://ppio.com/) | 分布式 GPU 云，模型 API 便宜 | `算力` |

---

## 🌍 官方直连 · 国际平台

> 国际主流聚合与推理平台。模型最新、协议最标准，部分需要海外网络与外币卡。

| 名称 | 说明 | 标签 |
| :--- | :--- | :--- |
| [**OpenRouter**](https://openrouter.ai/) ⭐ | 全球最大模型路由平台，一个 Key 全模型 | `聚合` |
| [**Groq**](https://console.groq.com/) ⭐ | LPU 极速推理，免费额度大方 | `推理` |
| [Together AI](https://api.together.xyz/) | 开源模型推理快，价格低 | `推理` |
| [Fireworks AI](https://fireworks.ai/) | 低延迟推理，适合生产环境 | `推理` |
| [DeepInfra](https://deepinfra.com/) | 按 token 计费，开源模型齐全 | `推理` |
| [Novita AI](https://novita.ai/) | 模型多、注册送额度 | `推理` |
| [Hyperbolic](https://hyperbolic.xyz/) | 去中心化算力，价格有优势 | `推理` |
| [Cerebras](https://cloud.cerebras.ai/) | 晶圆级芯片，速度惊人 | `推理` |
| [Replicate](https://replicate.com/) | 开源模型一键跑，图像 / 视频丰富 | `托管` |
| [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) | 多家推理服务商统一入口 | `托管` |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | 边缘推理，免费额度可白嫖 | `边缘` |
| [Poe](https://poe.com/) | Quora 出品，聊天式多模型聚合 | `聚合` |

---

## 🧭 导航站 · 比价 · 评测

> 不知道选哪家？先上这些站比一比 —— 实时报价、渠道在线率、掺水率、跑路预警都在这儿。
> **选站之前先看这里，比看任何推荐文都靠谱。**

| 名称 | 说明 | 标签 |
| :--- | :--- | :--- |
| [**TokenNav**](https://tokennav.cc/) ⭐ | 收录 200+ 中转站，含价格 / 支付方式 / 在线率对比 | `导航` |
| [**禾维 AI**](https://www.hvoy.ai/) ⭐ | 中转站排名 + API 真假检测（查掺水率、延迟） | `排名+检测` |
| [**PriceAI**](https://priceai.cc/) ⭐ | 低价卡网订阅与中转 API 比价雷达 | `比价` |
| [**OpenPrice**](https://www.openprice.cc/card-products) ⭐ | 聚合 280+ 渠道商报价，含最低价与在售数 | `比价` |
| [**Aibijia**](https://aibijia.org/) ⭐ | AI 订阅一键比价，帮你找便宜 Token | `比价` |
| [**卡网大全**](https://cardnav.xyz/) ⭐ | 一站式大模型账号购买导航 | `导航` |
| [AI 订阅与资源聚合导航](https://cheap-ai.uk/) | GPT / Claude / Gemini / Grok 一站发现 | `导航` |
| [AI 工具集](https://ai-bot.cn/) | 国内收录最全的 AI 工具导航 | `导航` |
| [AIGC 工具导航](https://www.aigc.cn/) | 生成式 AI 工具分类检索 | `导航` |
| [WayToAGI](https://www.waytoagi.com/) | 飞书知识库起家的 AGI 学习社区 | `知识库` |

---

## 🛒 账号 · 接码 · 号池

> ⚠️ **本分类均为第三方商家，与官方无任何关联，不保证可用性与售后。**
> 涉及平台账号交易与短信验证码代收，可能违反目标平台的服务条款，请自行评估合规性与风险。

| 名称 | 说明 | 标签 |
| :--- | :--- | :--- |
| [账号星球](https://accboyytbptech.acceboy.com/) | 苹果 ID / 国外 ID / Telegram 账号 | `账号` |
| [爱窝啦 AI 账号店](https://www.aivora.cn/) | Cursor / ChatGPT / Claude / Gemini 自助购买 | `账号` |
| [AIProbe](https://aiprobe.top/) | 账号与接码二合一 | `账号+接码` |
| [极光动能](https://sms.iamu.eu.org/) | 全球短信验证码服务 | `接码` |
| [NexusVault 号池交易台](https://nvtokens.com/) | 号池交易与额度管理 | `号池` |
| [AI 云智聪聪的小店](https://pay.ldxp.cn/shop/Z6I0VZ0Q) | 链动小铺自动发货 | `发卡` |

---

## 🛠️ 自建网关 · 开源自部署

> 不想把 Key 交给别人？自己搭一个中转：多 Key 轮询、多渠道负载、统一计费，全在自己手里。
> 也适合团队内部做统一网关 + 用量审计。

| 项目 | 说明 | 技术栈 |
| :--- | :--- | :--- |
| [**one-api**](https://github.com/songquanpeng/one-api) ⭐ | 经典 OpenAI 接口聚合管理系统，支持 30+ 上游，单文件 Docker 一键部署 | `Go · 37k★` |
| [**new-api**](https://github.com/QuantumNous/new-api) ⭐ | one-api 增强分支，UI 更现代，支持 OpenAI / Claude / Gemini 三种协议互转 | `Go · 50k★` |
| [**LiteLLM**](https://github.com/BerriAI/litellm) ⭐ | 100+ LLM 统一调用 + 代理网关，带成本追踪与负载均衡 | `Python · 61k★` |
| [uni-api](https://github.com/yym68686/uni-api) | YAML 配置多后端，轻量好部署 | `Python` |
| [gpt-load](https://github.com/tbphp/gpt-load) | 多 Key / 多凭据轮询，含调度容错与用量统计 | `Go · 7k★` |
| [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 生产级 AI 网关，1600+ 模型路由 + 50+ 护栏 | `TS · 13k★` |

---

## 🎯 怎么选？一张决策表

| 你的情况 | 推荐路径 |
| :--- | :--- |
| 只想花几十块试水，跑通再说 | 找个支持**签到白嫖 / 低起充**的中转站 → [🔌 中转站](#-ai-api-中转站--聚合平台) |
| 个人长期用，追求稳定与低价 | 先看 [🧭 导航站](#-导航站--比价--评测) 对比在线率与价格，再挑 2 家做冗余 |
| 需要开发票、要合规 | 走[国内厂商官方](#-官方直连--国内大模型厂商) 或 [OpenRouter 等国际聚合](#-官方直连--国际平台) |
| 团队内部统一管理、要审计用量 | [自建 new-api / LiteLLM](#️-自建网关--开源自部署) |
| 只想白嫖免费额度 | 硅基流动、智谱、火山方舟、Groq、Cloudflare Workers AI 都有新用户额度 |
| 有海外网络 + 外币卡 | 直接 [OpenRouter](#-官方直连--国际平台)，模型最新最全 |

---

## 🛡️ 防坑指南

中转站是**第三方转售**，质量参差不齐。花钱前花 5 分钟做这几件事，能省掉 90% 的坑：

1. **先查在线率和运营时长** —— 去 [TokenNav](https://tokennav.cc/) / [禾维 AI](https://www.hvoy.ai/) 看历史数据，只运营了两个月的新站慎充大额。
2. **测「掺水率」** —— 有些站会把 `gpt-4o` 的请求偷偷路由到便宜的小模型。禾维 AI 这类检测站能查出来。
3. **小额试充，别一次充年费** —— 首次充最小额度，跑通真实业务再续。中转站跑路是常态，不是意外。
4. **验证模型身份** —— 问它「你的模型名称和版本是什么」不够，最好用**已知答案的难题**（比如特定数学题、特定日期的事件）横向对比官方结果。
5. **别把敏感数据发给不明来源的站** —— 你的 prompt 会经过对方服务器，商业机密、个人隐私、代码资产都算敏感数据。
6. **看清是「官方直连」还是「逆向渠道」** —— 后者价格极低但随时可能断供，且可能违反上游条款。
7. **留一手** —— 至少准备 2 家可用站，把 `base_url` 和 Key 做成配置项，断了一家 5 分钟切走。

---

## 🤝 贡献

发现了好站、踩到了坑、链接失效了？欢迎提 [Issue](../../issues) 或 PR：

- **新增站点**：请编辑 [`data/sites.json`](data/sites.json)，在对应分类的 `items` 里加一条，并顺手跑一次链接检测（见下）。
- **失效链接**：直接删或更新为新域名，中转站换域名很频繁，欢迎帮忙修正。
- **收录标准**：站点需真实可访问、有明确的服务内容；纯广告页、明显钓鱼站、无任何说明的短链一律不收。

```bash
# 检测所有链接可达性（需能正常访问对应站点）
python tools/check_links.py
```

---

## 📅 更新记录

| 日期 | 内容 |
| :--- | :--- |
| 2026-10-16 | 项目初始化，收录 64 个站点；核实链接状态，修正 `new-api` 迁移至 `QuantumNous/new-api`、`V3 API` 迁移至 `gpt.ge` |

---

## ⚠️ 免责声明

- 本项目是**纯信息聚合与整理**，不对任何第三方站点的服务质量、资金安全、数据安全作任何担保。
- 所有链接均指向**第三方运营**的平台。使用前请自行核实其资质、条款与合法性。
- 中转站 / 账号交易类服务**可能违反上游平台的服务条款**（如 OpenAI、Anthropic 的使用政策），使用风险由使用者自行承担。
- 请遵守所在地区法律法规及各平台服务条款，**不得将相关服务用于任何违法用途**。
- 本项目与所列任何站点**无隶属、代理或利益关系**（标注 ⭐ 仅为整理者的主观使用印象，不构成推荐或背书）。
- 若你是某个站点的运营者，希望被收录、修正描述或移除，请提 Issue，会尽快处理。

---

<div align="center">

**如果这个列表帮你省下了一个下午的搜索时间，点个 ⭐ Star 就是最好的支持。**

<sub>Made with 🐦 by <a href="https://github.com/Han-maker-wp">Han-maker-wp</a></sub>

</div>
