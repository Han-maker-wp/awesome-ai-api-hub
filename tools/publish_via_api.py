#!/usr/bin/env python3
"""通过 GitHub Contents API 发布仓库内容（当 git push 不可用时的替代通道）。

为什么需要它：本机环境里 `git push` 到 github.com:443 会被 HTTP 代理拒绝
（`CONNECT tunnel failed, response 502`），但 `gh` 走的 API 通道是通的。
所以用 Contents API 逐文件提交，效果等价于 push。

用法：
    python tools/publish_via_api.py            # 上传所有变化
    python tools/publish_via_api.py --dry-run  # 只看会改什么，不实际提交
    python tools/publish_via_api.py --prune    # 额外删除远端有、本地没有的文件

依赖：gh CLI 已登录（`gh auth status`）。
上传后建议 `git fetch origin main && git reset --hard FETCH_HEAD` 让本地与远端对齐。
"""
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, cwd=str(ROOT)).strip()


def resolve_repo() -> str:
    url = git("config", "--get", "remote.origin.url")
    if url.startswith("git@") or "github.com" not in url:
        sys.exit(f"无法从 remote.origin.url 解析出 GitHub 仓库：{url}")
    tail = url.split("github.com", 1)[1].lstrip(":/")
    return tail[:-4] if tail.endswith(".git") else tail


def api(method: str, path: str, token: str, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        f"{API}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "publish-via-api",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只报告变更，不提交")
    ap.add_argument("--prune", action="store_true", help="删除远端存在但本地已移除的文件")
    ap.add_argument("--branch", default=None, help="目标分支，默认仓库默认分支")
    args = ap.parse_args()

    repo = resolve_repo()
    token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    files = [f for f in git("ls-files").splitlines() if f]

    print(f"repo   : {repo}")
    print(f"files  : {len(files)} tracked\n")

    changed = skipped = failed = 0
    for f in files:
        p = ROOT / f
        if not p.is_file():
            continue
        local_blob = git("hash-object", f)
        content_path = f"/repos/{repo}/contents/{urllib.parse.quote(f)}"
        remote = api("GET", content_path, token)

        if remote and remote.get("sha") == local_blob:
            skipped += 1
            continue

        action = "update" if remote else "create"
        print(f"  {action:6} {f}")
        if args.dry_run:
            changed += 1
            continue

        # 用 git blob 的内容上传（而非工作区原始字节），确保与索引一致：
        # 工作区在 Windows 上是 CRLF，直接用原始字节上传会与本地 blob sha 不符，
        # 导致每次运行都出现"假差异"并反复提交。
        blob = subprocess.run(
            ["git", "cat-file", "blob", local_blob],
            cwd=str(ROOT),
            capture_output=True,
            check=True,
        ).stdout
        body = {
            "message": f"{'chore' if remote else 'feat'}: {action} {f}",
            "content": base64.b64encode(blob).decode("ascii"),
        }
        if remote:
            body["sha"] = remote["sha"]
        if args.branch:
            body["branch"] = args.branch
        try:
            res = api("PUT", content_path, token, body)
            print(f"         → {res['commit']['sha'][:8]}")
            changed += 1
        except urllib.error.HTTPError as e:
            print(f"         ✗ {e.code} {e.read()[:200]!r}")
            failed += 1
        except Exception as e:  # noqa: BLE001
            print(f"         ✗ {type(e).__name__}: {e}")
            failed += 1

    if args.prune:
        remote_tree = api("GET", f"/repos/{repo}/git/trees/HEAD?recursive=1", token) or {}
        remote_files = {n["path"] for n in remote_tree.get("tree", []) if n["type"] == "blob"}
        for path in sorted(remote_files - set(files)):
            print(f"  delete {path}")
            if args.dry_run:
                continue
            cur = api("GET", f"/repos/{repo}/contents/{urllib.parse.quote(path)}", token)
            if not cur:
                continue
            try:
                api(
                    "DELETE",
                    f"/repos/{repo}/contents/{urllib.parse.quote(path)}",
                    token,
                    {"message": f"chore: delete {path}", "sha": cur["sha"]},
                )
                changed += 1
            except Exception as e:  # noqa: BLE001
                print(f"         ✗ {e}")
                failed += 1

    print(f"\n== changed {changed} · unchanged {skipped} · failed {failed} ==")
    if changed and not args.dry_run:
        print("\n本地与远端对齐：git fetch origin main && git reset --hard FETCH_HEAD")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
