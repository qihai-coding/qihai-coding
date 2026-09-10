"""为固定的上游 2.0.2 / 核心 2.1.3 修正公开获星数查询的令牌兼容性。"""

from pathlib import Path

root = Path(__file__).resolve().parents[2]
entry = root / ".stats-action/index.js"
source = entry.read_text(encoding="utf-8")
old_import = 'import { mkdir, mkdtemp, writeFile } from "node:fs/promises";'
old_resolve = 'const modulePath = installRequire.resolve(CORE_PACKAGE_NAME);'
patch = r'''
  // 2.1.3 的 stargazers 连接会要求额外权限；公开数量使用等价标量字段。
  const statsPath = path.join(path.dirname(modulePath), "fetchers/stats.js");
  const statsSource = await readFile(statsPath, "utf8");
  const connection = /stargazers\s*\{\s*totalCount\s*\}/g;
  if ([...statsSource.matchAll(connection)].length !== 1 ||
      statsSource.split(".stargazers.totalCount").length !== 3) {
    throw new Error("统计核心结构已改变，请重新核对公开获星数兼容补丁。");
  }
  const fixedStats = statsSource
    .replace(connection, "stargazerCount")
    .replaceAll(".stargazers.totalCount", ".stargazerCount");
  await writeFile(statsPath, fixedStats, "utf8");
'''
if source.count(old_import) != 1 or source.count(old_resolve) != 1:
    raise RuntimeError("上游组件结构已改变，停止生成以免应用错误补丁。")
source = source.replace(old_import, old_import.replace("{ mkdir,", "{ readFile, mkdir,"))
entry.write_text(source.replace(old_resolve, old_resolve + patch), encoding="utf-8")
print("已为固定上游组件加入公开获星数量兼容补丁，保持原有统计口径。")
