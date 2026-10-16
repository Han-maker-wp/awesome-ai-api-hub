#!/usr/bin/env python3
"""批量检测 data/sites.json 中所有链接的可达性，输出结果表。

注意：本机若走 HTTP 代理，部分域名可能被代理拦截并返回 502，
此时该条目的失败不代表站点真的挂了，请换网络或浏览器复核。
"""
import json
import ssl
import sys
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


def probe(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return {"url": url, "status": r.status, "ok": 200 <= r.status < 400}
    except urllib.error.HTTPError as e:
        # 401/403/405/429 说明服务活着，只是拒绝了无头请求
        return {"url": url, "status": e.code, "ok": e.code in (401, 403, 405, 429)}
    except Exception as e:  # noqa: BLE001
        return {"url": url, "status": type(e).__name__, "ok": False}


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    items = [(c["title"], it) for c in data["categories"] for it in c["items"]]
    print(f"probe {len(items)} urls ...\n")
    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(lambda p: (p[0], probe(p[1]["url"]), p[1]["name"]), items))

    bad = []
    for cat, r, name in results:
        flag = "OK " if r["ok"] else "BAD"
        if not r["ok"]:
            bad.append((cat, name, r["url"], r["status"]))
        print(f"[{flag}] {r['status']:<5} {name}  <{r['url']}>")

    print(f"\n== {len(items) - len(bad)}/{len(items)} reachable ==")
    if bad:
        print("\n-- unreachable（可能是站点挂了，也可能是本地网络/代理拦截）--")
        for cat, name, url, st in bad:
            print(f"  {st:<20} {name} | {cat} | {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
