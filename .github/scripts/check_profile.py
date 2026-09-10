"""检查主页素材；仅在完整验证通过后提交并推送。仅使用 Python 标准库。"""

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET

GENERATED = tuple(
    f"assets/generated/{kind}-{theme}.svg"
    for kind in ("stats", "languages", "snake")
    for theme in ("dark", "light")
)


def git(root, *args):
    return subprocess.check_output(
        ["git", "-C", str(root), *args], text=True, encoding="utf-8"
    ).strip()


def check(root):
    for name in GENERATED:
        path = root / name
        raw = path.read_text(encoding="utf-8")
        svg = ET.fromstring(raw)
        if len(raw) < 200 or svg.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"不是有效的完整矢量图：{name}")
        if re.search(r"something went wrong|could not resolve to a user|API rate limit exceeded", raw, re.I):
            raise ValueError(f"生成器返回了错误卡片：{name}")
        if "snake" not in name and not "".join(svg.itertext()).strip():
            raise ValueError(f"统计图片缺少文字：{name}")
    for path in (root / "assets").rglob("*.svg"):
        ET.parse(path)
    readme = root / "README.md"
    if readme.exists():
        for name in re.findall(r'(?:src|srcset)="(assets/[^"\s]+)"', readme.read_text(encoding="utf-8")):
            if not (root / name).is_file():
                raise ValueError(f"主页图片不存在：{name}")


def publish(root):
    check(root)
    # 仅检查和提交指定的六张动态图片，避免包含其他工作区文件。
    git(root, "add", "--", *GENERATED)
    if not git(root, "diff", "--cached", "--name-only", "--", *GENERATED):
        print("公开数据与图片未变化，跳过提交。")
        return False
    git(root, "-c", "user.name=github-actions[bot]", "-c",
        "user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit", "--only", "-m", "更新主页公开统计与贡献动画",
        "-m", "依据当前公开活动重新生成深浅色统计、语言分布和贡献贪吃蛇；完整素材验证通过后统一发布，保持主页图片可用。",
        "--", *GENERATED)
    git(root, "push", "origin", "HEAD:main")
    print("完整动态素材已发布。")
    return True


def self_test(root):
    """用隔离仓库和真实图片检查：失败不推送，变化才提交，重复不空提交。"""
    with tempfile.TemporaryDirectory(prefix="profile-check-") as temp:
        base = Path(temp)
        remote, repo = base / "remote.git", base / "repo"
        git(base, "init", "--bare", "--quiet", str(remote))
        repo.mkdir()
        git(repo, "init", "--quiet", "-b", "main")
        git(repo, "config", "user.name", "profile-test")
        git(repo, "config", "user.email", "test@example.invalid")
        git(repo, "config", "core.autocrlf", "false")
        for name in GENERATED:
            target = repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        git(repo, "add", ".")
        git(repo, "commit", "--quiet", "-m", "初始化测试素材")
        git(repo, "remote", "add", "origin", str(remote))
        git(repo, "push", "--quiet", "origin", "main")
        before = git(remote, "rev-parse", "main")
        broken = repo / GENERATED[-1]
        original = broken.read_bytes()
        broken.write_text("<svg>broken", encoding="utf-8")
        try:
            publish(repo)
        except (ValueError, ET.ParseError):
            pass
        else:
            raise AssertionError("不完整素材不能通过发布检查")
        assert git(remote, "rev-parse", "main") == before, "失败修改了已发布图片"
        broken.write_bytes(original)
        assert not publish(repo), "相同素材产生了空提交"
        with broken.open("a", encoding="utf-8") as stream:
            stream.write("\n<!-- isolated publication check -->\n")
        assert publish(repo), "新素材未发布"
        after = git(remote, "rev-parse", "main")
        assert after != before
        assert not publish(repo), "重复运行产生了空提交"
        assert git(remote, "rev-parse", "main") == after
    print("隔离检查通过：失败保留旧图、变化才提交、重复无空提交。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    check(root)
    if args.self_test:
        self_test(root)
    if args.publish:
        publish(root)
    print("主页素材检查通过。")
