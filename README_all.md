【简体中文 README.md】
|分类|内容详情|
| ---- | ---- |
|头部横幅链接|图片：https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910；多语言跳转：./README.md、./README_EN.md、./README_zh-TW.md、./README_JP.md；项目Wiki：https://github.com/K2ngw/Firefly-IV/wiki；发布页：https://github.com/K2ngw/Firefly-IV/releases；开发者Discord：https://discord.com/users/1405492229627187212；项目数据：STAR=16763，FORKS=4324，ISSUES=147，PULLS=3；版本V1.0.0，协议MIT LICENSE，更新JUNE 2026|
|项目名称|Firefly-Ⅳ | 星穹·流萤跨平台AI机器人|
|项目简介|基于discord.py + NoneBot2 + Flask + Qwen LLM + Tavily开发，还原崩坏：星穹铁道流萤人设，实现Discord+QQ双平台机器人联动|
|核心亮点|1.无硬编码密钥，网页配置；2.Flask绑定0.0.0.0支持局域网访问后台；3.双端共用AI记忆，@触发对话；4.内置问答、检索、代码运行、视频总结、点歌、群管理；5.自助领身份、频道清理交互按钮|
|技术依赖|discord.py：Discord斜杠指令、交互按钮、服务器管控；nonebot2+onebot-v11：QQ对接(LLOneBot/NTQQ)；Flask：登录鉴权、可视化配置、启停控制；DashScope-Qwen：对话生成、代码生成、视频总结；Tavily API：联网实时信息检索；aiohttp：全异步网络请求|
|部署依赖安装命令|pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp|
|前置部署准备|1.QQ：NTQQ+LLOneBot，WS地址ws://127.0.0.1:3001；2.Discord申请Bot并开启全部Privileged网关权限；3.自备通义千问APIKey、TavilyKey，米游社Cookie可选|
|项目启动|运行main.py，本地后台http://127.0.0.1:5000，局域网[内网IP]:5000|
|Web后台配置项|配置表单：DiscordToken/QwenKey/TavilyKey/各类Cookie/角色ID/OneBotWS；控制按键：启停机器人、清空聊天记忆；状态面板：在线离线监控；账号FireflyDev，密码fireflycheng，仅内网访问，改配置需重启|
|Discord指令|/ask 问题：AI联网问答；/search 关键词：全网搜索；/code 需求：Python生成运行；/点歌 歌名：Youtube链接；/bilibili 链接：视频总结；/youtube 链接：内容概括；附带领取身份、清频道按钮|
|QQ指令|/ask：AI对话；/search：全网检索；/code：代码运行；/点歌：在线搜歌；/bilibili：视频总结；@机器人自动聊天、短视频解析|
|人设设定|固定称呼开拓者，语气带唔、呀、呢，关联萨姆、星核猎手，自动安抚负面情绪|
|目录结构|Firefly-IV/；main.py(主程序)；bot_config.json(配置缓存)；README.md(文档)|
|开发者信息|作者K2ngw / Mikukero；Discord：1405492229627187212|
|免责条款|1.禁止违规批量托管QQ；2.Discord开启Message Content Intent；3.妥善保管API密钥|

【英文 README_EN.md】
|分类|内容详情|
| ---- | ---- |
|头部横幅链接|图片：https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910；多语言跳转：./README.md、./README_EN.md、./README_zh-TW.md、./README_JP.md；项目Wiki：https://github.com/K2ngw/Firefly-IV/wiki；发布页：https://github.com/K2ngw/Firefly-IV/releases；开发者Discord：https://discord.com/users/1405492229627187212；项目数据：STAR=16763，FORKS=4324，ISSUES=147，PULLS=3；版本V1.0.0，协议MIT LICENSE，更新JUNE 2026|
|项目名称|Firefly-Ⅳ | Honkai: Star Rail Firefly Cross-platform AI Bot|
|项目简介|Built with discord.py + NoneBot2 + Flask + Qwen LLM + Tavily Search, restore Firefly personality, support Discord & QQ group management|
|核心亮点|No hardcoded API keys, web config; Flask 0.0.0.0 for LAN access; shared chat history; AI chat/search/code/video summary/music/group manage|
|技术依赖|discord.py：Discord slash & button；nonebot2+onebot-v11：QQ LLOneBot connect；Flask：Web backend & auth；DashScope-Qwen：LLM chat & code；Tavily API：Real-time search；aiohttp：Async request|
|安装命令|pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp|
|部署准备|QQ WS ws://127.0.0.1:3001；Discord full intents；apply Qwen & Tavily API|
|项目地址|Run main.py → http://127.0.0.1:5000|
|后台配置|Config：Token/API/Cookie/RoleID/OneBot；Control：Start/Stop/Clear Chat；Status：Online/Offline；User:FireflyDev,pwd:fireflycheng,LAN only|
|Discord指令|/ask text:AI chat；/search key:Web search；/code req:Run Python；/点歌 name:Youtube link；/bilibili url:Video summary|
|QQ指令|/ask:AI Talk；/search:Web search；/code:Code execute|
|文件目录|Firefly-IV/；main.py；bot_config.json；README_EN.md|
|开发者|Author:K2ngw / Mikukero；Discord:1405492229627187212|
|免责|Follow platform rules, keep API secure|

【繁体 README_zh-TW.md】
|分类|内容详情|
| ---- | ---- |
|头部横幅链接|圖片：https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910；語言切換：./README.md、./README_EN.md、./README_zh-TW.md、./README_JP.md；Wiki：https://github.com/K2ngw/Firefly-IV/wiki；發布：https://github.com/K2ngw/Firefly-IV/releases；開發Discord：https://discord.com/users/1405492229627187212；數據STAR=16763，FORKS=4324，ISSUES=147，PULLS=3，V1.0.0，MIT授權，JUNE 2026|
|專案名稱|Firefly-Ⅳ｜星穹鐵道流螢跨平台AI機器人|
|依賴清單|discord.py：Discord斜線指令；nonebot2+onebot-v11：QQ掛載；Flask：網頁後台管理|
|安裝指令|pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp|
|可用指令|/ask：流螢AI對話；/search：網路查詢；/code：程式執行|
|開發者|K2ngw / Mikukero；Discord鏈接https://discord.com/users/1405492229627187212|

【日文 README_JP.md】
|分类|内容详情|
| ---- | ---- |
|头部横幅链接|画像：https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910；言語切替：./README.md、./README_EN.md、./README_zh-TW.md、./README_JP.md；Wiki：https://github.com/K2ngw/Firefly-IV/wiki；リリース：https://github.com/K2ngw/Firefly-IV/releases；開発者Discord：https://discord.com/users/1405492229627187212；STAR=16763，FORKS=4324，ISSUES=147，PULLS=3、V1.0.0、MITライセンス、JUNE 2026|
|プロジェクト名|Firefly-Ⅳ｜スターレール 流蛍AIボット|
|使用ライブラリ|discord.py：Discordコマンド；nonebot2：QQ連携；Flask：WEB管理画面|
|インストールコマンド|pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp|
|コマンド一覧|/ask：AIチャット；/search：ネット検索|
|開発者|K2ngw / Mikukero；Discordリンク：https://discord.com/users/1405492229627187212|
