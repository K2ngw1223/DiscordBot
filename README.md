<img width="735" height="525" alt="Image" src="https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910" />

# 大致预览
|⭐ STARS|🍴 FORKS|⚠️ ISSUES|🔀 PULLS|
|--------|--------|---------|--------|
|We need it|too|Firefly|Love|
</div>

<br>
<div align="center">
<a href="./README.md">简体中文</a> |
<a href="./README_EN.md">English</a> |
<a href="./README_zh-TW.md">繁體中文</a> |
<a href="./README_JP.md">日本語</a>
<br><br>
<a href="https://github.com/K2ngw/Firefly-IV/wiki">
  <kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">WIKI</kbd>
  <kbd style="background:#3078cb;color:#fff;padding:12px 40px;font-size:17px;border:none;">FIREFLY-IV</kbd>
</a>
<br><br>
<a href="https://github.com/K2ngw/Firefly-IV/releases">
  <kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">RELEASE</kbd>
  <kbd style="background:#3078cb;color:#fff;padding:12px 40px;font-size:17px;border:none;">V1.0.0</kbd>
</a>
<br><br>
<kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">LICENSE</kbd>
<kbd style="background:#666666;color:#fff;padding:12px 180px;font-size:17px;border:none;">MIT LICENSE</kbd>
<br><br>
<kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">LAST COMMIT</kbd>
<kbd style="background:#c46226;color:#fff;padding:12px 180px;font-size:17px;border:none;">JUNE 2026</kbd>
<br><br>
<kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">🔧 BUILD</kbd>
<kbd style="background:#666666;color:#fff;padding:12px 180px;font-size:17px;border:none;">NO STATUS</kbd>
<br><br>
<a href="https://discord.com/users/1405492229627187212">
<kbd style="background:#333333;color:#fff;padding:12px 40px;font-size:17px;border:none;">💬 DISCORD</kbd>
<kbd style="background:#35a839;color:#fff;padding:12px 180px;font-size:17px;border:none;">DEVELOPER HOME</kbd>
</a>
</div>

# Firefly-Ⅳ | 星穹·流萤跨平台AI机器人
> Discord + QQ OneBot 双端一体化智能Bot | 全Web可视化配置 | 局域网管理后台 | 流萤原生人设AI引擎

## 📌 项目简介
Firefly-IV 基于`discord.py + NoneBot2 + Flask + Qwen LLM + Tavily`开发，完整还原**崩坏：星穹铁道-流萤**人物性格与台词逻辑，实现Discord服务器运维+QQ群托管双平台联动。
### 核心亮点
- ❌ 无任何硬编码密钥，全部配置网页填写保存
- ✅ Flask绑定`0.0.0.0`，全局域网设备访问管理面板
- ✅ 双端共用一套AI记忆，@自动触发流萤专属对话
- ✅ 内置：AI问答/全网检索/代码运行/视频总结/在线点歌/群管
- ✅ 自助领身份、频道清理交互式按钮

[开发者](https://discord.com/users/1405492229627187212)
 
## 🧩 技术依赖
| 依赖 | 作用 |
| :--- | :--- |
| discord.py | Discord斜杠指令、交互按钮、服务器管控 |
| nonebot2+onebot-v11 | QQ对接(LLOneBot/NTQQ) |
| Flask | 登录鉴权、可视化配置、启停控制 |
| DashScope-Qwen | 对话生成、代码生成、视频总结 |
| Tavily API | 联网实时信息检索 |
| aiohttp | 全异步网络请求 |

## ⚡ 快速部署
### 1. 安装依赖
```bash
pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp
2. 前置准备
 
1. QQ：安装NT客户端+LLOneBot，默认WS： ws://127.0.0.1:3001 
​
2. Discord申请Bot，全开网关权限
​
3. 自行申请Qwen、Tavily密钥
 
3. 启动项目
 
运行 main.py 
本地： http://127.0.0.1:5000 
局域网： 本机IP:5000 
 
🖥️ Web管理后台
功能区域	内容
配置表单	DiscordToken/QwenKey/TavilyKey/Cookie/角色ID/OneBotWS
控制按键	启动双端机器人、停止机器人、清空聊天记忆
状态面板	在线/离线实时展示

🎯 Discord指令
指令	功能
流萤AI联网问答
全网检索
Python生成运行
Youtube链接
视频总结
视频概括

🎯 QQ指令
指令	功能
AI聊天
搜索
代码
搜歌
解析视频

💬 流萤人设
 
固定称呼开拓者，语气软糯带唔/呀，关联萨姆与星核猎手，自动安抚情绪。
 
📂 文件结构
Firefly-IV/
├─ main.py
├─ bot_config.json
└─ README.md


🔗 开发者主页
K2ngw / Mikukero | Discord:1405492229627187212
 
⚠️ 免责
 
1. 禁止违规批量托管QQ
​
2. Discord开启Message Content Intent
​
3. API密钥妥善保管
