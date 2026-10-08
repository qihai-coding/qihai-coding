<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/hero-mobile-dark.svg">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/hero-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero-dark.svg" width="100%" alt="Jspring / qihai-coding — 后端开发 · 实时通信 · 状态同步。保持好奇，持续构建。">
</picture>

<p align="center"><b>专注后端，把想法写成可运行的系统。</b></p>
<p align="center">我是 Jspring，主要使用 Go（编程语言）构建后端服务，<br>关注实时通信、联机状态同步与社区系统。这里整理我的公开项目与工程实践。</p>
<p align="center"><a href="#user-content-代表项目">代表项目</a> · <a href="#user-content-技术栈">技术栈</a> · <a href="#user-content-公开活动">公开活动</a> · <a href="#user-content-贡献轨迹">贡献轨迹</a></p>

## 代表项目

### 01 ─ [go-statesync](https://github.com/qihai-coding/go-statesync) · 联机状态同步库

面向联机游戏的服务器权威状态同步库。通过 QUIC（基于数据报的加密传输协议）传递输入与快照，提供本地预测、权威校正和进程内断线续接。

`服务器权威`　`预测与校正`　`进程内续接`

[查看项目 →](https://github.com/qihai-coding/go-statesync)　[接入指南](https://github.com/qihai-coding/go-statesync/blob/main/docs/INTEGRATION.md)　[发布验收报告](https://github.com/qihai-coding/go-statesync/blob/main/reports/release-v0.2.0/VALIDATION.md)

### 02 ─ [tech-community-api](https://github.com/qihai-coding/tech-community-api) · 社区后端

基于 Go（编程语言）与 Gin（后端框架）的技术社区服务。覆盖文章与评论、实时聊天和私信、资源分享与对象存储，并接入外部代码执行服务。

`内容服务`　`实时通信`　`对象存储`　`代码执行`

[查看项目 →](https://github.com/qihai-coding/tech-community-api)

### 03 ─ [tech-community-web](https://github.com/qihai-coding/tech-community-web) · 社区前端

以 Vue（前端框架）与 TypeScript（类型化脚本语言）构建技术交流社区的交互界面，提供文章阅读与编辑、聊天室、私信、资源分享和在线编程，与社区后端配套使用。

`社区交互`　`内容编辑`　`在线编程`

[查看项目 →](https://github.com/qihai-coding/tech-community-web)

## 技术栈

围绕公开项目积累的技术实践：以后端服务与实时通信为主，前端用于配套交互。

<p>
  <img src="assets/tech-go.svg" width="160" alt="Go（编程语言）">
  <img src="assets/tech-gin.svg" width="160" alt="Gin（后端框架）">
  <img src="assets/tech-quic.svg" width="160" alt="QUIC（加密传输协议）">
  <img src="assets/tech-mysql.svg" width="160" alt="MySQL（关系型数据库）">
  <img src="assets/tech-minio.svg" width="160" alt="MinIO（对象存储）">
</p>
<p>
  <img src="assets/tech-vue.svg" width="160" alt="Vue（前端框架）">
  <img src="assets/tech-typescript.svg" width="205" alt="TypeScript（类型化脚本语言）">
</p>

## 公开活动

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/stats-light.svg">
  <img src="assets/generated/stats-dark.svg" width="400" alt="公开活动统计：获星、当年提交、合并请求和议题数量。">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/languages-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/languages-light.svg">
  <img src="assets/generated/languages-dark.svg" width="400" alt="自有公开仓库的主要代码语言分布，展示代码量前六项的相对占比。">
</picture>

<sub>来自公开可见的数据，提交数按当年统计。语言图展示代码量前六项的相对占比，不代表熟练程度；已排除本主页仓库。</sub>

## 贡献轨迹

每一格，记录一次持续构建。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/snake-light.svg">
  <img src="assets/generated/snake-dark.svg" width="100%" alt="依据 qihai-coding 真实贡献日历生成的贪吃蛇动画。">
</picture>

<p align="center"><sub>保持好奇，持续构建。</sub></p>

<details>
<summary>关于数据更新与素材</summary>

统计和贡献动画由 GitHub Actions（平台自动工作流）每天北京时间 09:17 尝试更新，也支持手动触发。图片存放在本仓库；生成失败时保留上次成功结果。定时任务可能排队，长期无仓库活动时也可能被平台暂停。

- [查看更新状态](https://github.com/qihai-coding/qihai-coding/actions/workflows/profile.yml)
- [统计生成器](https://github.com/stats-organization/github-readme-stats-action) · [贡献动画生成器](https://github.com/Platane/snk)
- 横幅与技术标签为本主页定制的 SVG（可缩放矢量图）；横幅支持系统的减少动态效果设置。

</details>
