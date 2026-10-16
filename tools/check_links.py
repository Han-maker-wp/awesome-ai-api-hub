#!/usr/bin/env python3
"""批量检测 data/sites.json 中所有链接的可达性，输出结果表。

用法
----
    python tools/check_links.py                 # 直连
    python tools/check_links.py --proxy http://127.0.0.1:7897   # 走本地代理
    CHECK_PROXY=http://127.0.0.1:7897 python tools/check_links.py

为什么要显式指定代理
--------------------
部分沙箱/IDE 环境会注入自己的代理（例如 127.0.0.1:57026），它会拦截
github.com 等域名，导致大量误报。显式传 --proxy 可覆盖掉注入的代理。

读结果时注意三类
----------------
1. OK      —— 2xx/3xx，或 401/403/405/429（服务活着，只是拒绝了无头请求）
2. ANTIBOT —— 本脚本拿不到响应，但**历史上经人工用浏览器确认过存活**的反爬站。
              这类不算死链，但每次复核建议手动点一下。
3. BAD     —— 真正可疑，优先怀疑是本地网络/代理问题，换网络再试；仍失败才判定失效。
"""
from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sites.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# 无头请求拿不到响应、但已用浏览器人工确认存活的站点（反爬 / TLS 指纹拦截）。
# 复核时若这些站点在浏览器里也打不开，就该摘掉它们。
ANTIBOT_PREFIXES = (
    "https://aijichang.com",
    "https://shadowrocket.one",
    "https://aihubmix.com",
    "https://aiprobe.top",
)


def is_antibot(url: str) -> bool:
    return any(url.startswith(p) for p in ANTIBOT_PREFIXES)


def build_opener(proxy: str | None):
    handlers: list = [urllib.request.HTTPSHandler(context=CTX)]
    if proxy:
        handlers.append(
            urllib.request.ProxyHandler({"http": proxy, "https": proxy})
        )
    else:
        # 明确不继承环境变量里的代理，避免被沙箱注入的代理污染结果
        handlers.append(urllib.request.ProxyHandler({}))
    return urllib.request.build_opener(*handlers)


def probe(opener, url: str, retries: int = 2) -> dict:
    """探测单个 URL。失败会重试，避免单次网络抖动被记成死链。"""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    last: dict = {"url": url, "status": "n/a", "kind": "BAD"}
    for attempt in range(retries + 1):
        try:
            with opener.open(req, timeout=25) as r:
                return {"url": url, "status": r.status, "kind": "OK"}
        except urllib.error.HTTPError as e:
            # 401/403/405/429 说明服务活着，只是拒绝了无头请求
            if e.code in (401, 403, 405, 429):
                return {"url": url, "status": e.code, "kind": "OK"}
            last = {"url": url, "status": e.code, "kind": "BAD"}
        except Exception as e:  # noqa: BLE001
            last = {
                "url": url,
                "status": type(e).__name__,
                "kind": "ANTIBOT" if is_antibot(url) else "BAD",
            }
        if attempt < retries:
            time.sleep(1.5 * (attempt + 1))
    return last


def main() -> int:
    ap = argparse.ArgumentParser(description="批量检测链接可达性")
    ap.add_argument(
        "--proxy",
        default=os.environ.get("CHECK_PROXY") or None,
        help="HTTP 代理，如 http://127.0.0.1:7897（默认不继承环境变量）",
    )
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    opener = build_opener(args.proxy)
    print(f"proxy = {args.proxy or '(direct)'}\n")

    data = json.loads(DATA.read_text(encoding="utf-8"))
    items = [
        (f'{g["title"]} / {c["title"]}', it)
        for g in data["groups"]
        for c in g["categories"]
        for it in c["items"]
    ]
    print(f"probe {len(items)} urls ...\n")
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(
            ex.map(lambda p: (p[0], probe(opener, p[1]["url"]), p[1]["name"]), items)
        )

    buckets: dict[str, list] = {"OK": [], "ANTIBOT": [], "BAD": []}
    for cat, r, name in results:
        buckets[r["kind"]].append((cat, name, r["url"], r["status"]))
        tag = {"OK": "OK     ", "ANTIBOT": "ANTIBOT", "BAD": "BAD    "}[r["kind"]]
        print(f"[{tag}] {str(r['status']):<20} {name}  <{r['url']}>")

    total = len(items)
    ok, ab, bad = len(buckets["OK"]), len(buckets["ANTIBOT"]), len(buckets["BAD"])
    print(f"\n== {ok}/{total} reachable，{ab} antibot，{bad} bad ==")

    if buckets["ANTIBOT"]:
        print("\n-- ANTIBOT（反爬拦截，历史人工确认存活，建议手动点一下）--")
        for cat, name, url, st in buckets["ANTIBOT"]:
            print(f"  {st:<20} {name} | {cat} | {url}")

    if buckets["BAD"]:
        print("\n-- BAD（先换网络/代理重试；仍失败再判定失效）--")
        for cat, name, url, st in buckets["BAD"]:
            print(f"  {st:<20} {name} | {cat} | {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
