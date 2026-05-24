#该文本懒得改，反正作用差不多，用户直接去改py
# 🔥 Firefly 火萤Ⅳ — Discord 多功能智能机器人，现已开放，用户自定义机器人，前置条件是在DC的Dev里创建app，复制Token
由 **Mikukero** 开发 | AI 对话 · 全网搜索 · 游戏查询 · 网页管理后台

<p align="center">
<img src="https://p0.meituan.net/travelcube/bd587012091933d05090c97951c1532c37319.jpg" width="600">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue">
<img src="https://img.shields.io/badge/Discord.py-2.4+-blueviolet">
<img src="https://img.shields.io/badge/Flask-Web%20Panel-green">
<img src="https://img.shields.io/badge/支持-Termux%2FPC-brightgreen">
<img src="https://discord.com/users/1405492229627187212/作者-Mikukero-ff9eb5">
</p>

---

# 📌 项目总结
Firefly 火萤Ⅳ 是一款功能全面的 Discord 机器人，集成通义千问 AI 对话、Tavily 全网搜索、米游社 / HoYoLab 账号查询、YouTube/B 站视频解析、本地 Flask 管理后台、权限管理、黑名单、日志系统等功能，支持中英文双语自动切换、斜杠指令、按钮面板、上下文记忆，适合社群管理、娱乐互动、AI 智能助手使用。

---

# 📱 Termux 运行教程（安卓手机）
### 1. 安装前置环境
```bash
pkg update && pkg upgrade -y
pkg install python git openssl libffi -y
pip install --upgrade pip


🔥 Firefly 火萤Ⅳ — Discord 多功能智能机器人
 
 
  
# 🔥 Firefly 火萤Ⅳ — Discord 多功能智能机器人
由 **Mikukero** 开发 | AI 对话 · 全网搜索 · 游戏查询 · 网页管理后台

<p align="center">
<img src="https://p0.meituan.net/travelcube/bd587012091933d05090c97951c1532c37319.jpg" width="600">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue">
<img src="https://img.shields.io/badge/Discord.py-2.4+-blueviolet">
<img src="https://img.shields.io/badge/Flask-Web%20Panel-green">
<img src="https://img.shields.io/badge/支持-Termux%2FPC-brightgreen">
<img src="https://img.shields.io/badge/作者-Mikukero-ff9eb5">
</p>

---

# 📌 项目总结
Firefly 火萤Ⅳ 是一款功能全面的 Discord 机器人，集成通义千问 AI 对话、Tavily 全网搜索、米游社 / HoYoLab 账号查询、YouTube/B 站视频解析、本地 Flask 管理后台、权限管理、黑名单、日志系统等功能，支持中英文双语自动切换、斜杠指令、按钮面板、上下文记忆，适合社群管理、娱乐互动、AI 智能助手使用。

---

# 📱 Termux 运行教程（安卓手机）
### 1. 安装前置环境
```bash
pkg update && pkg upgrade -y
pkg install python git openssl libffi -y
pip install --upgrade pip
 
 
2. 安装项目依赖库
 
bash
  
pip install discord.py flask aiohttp
 
 
3. 进入项目文件夹
 
bash
  
cd 你的项目文件夹路径
 
 
4. 编辑配置文件
 
bash
  
nano bot.py
 
 
按说明填写 Token、ID、API Key 等信息。
 
5. 保存并退出编辑
 
按  Ctrl + O  保存，按  Ctrl + X  退出。
 
6. 启动机器人
 
bash
  
python bot.py
 
 
 
 
🖥️ PC 运行教程（Windows / macOS）
 
1. 安装 Python
 
前往官网下载并安装 Python 3.9 ~ 3.11：
https://www.python.org/downloads/
 
安装时务必勾选：Add Python to PATH
 
2. 打开命令行工具
 
- Windows：打开  CMD  或  PowerShell 
- macOS：打开  终端 
 
3. 安装项目依赖
 
bash
  
pip install discord.py flask aiohttp
 
 
4. 编辑配置文件
 
用记事本、VS Code 等工具打开  bot.py ，填写所需配置信息。
 
5. 进入项目目录
 
bash
  
cd 你的项目文件夹路径
 
 
6. 启动机器人
 
bash
  
python bot.py
 
 
 
 
⚙️ 必须填写的配置项
 
python
  
BOT_TOKEN = "你的Discord机器人Token"
BOT_ID = 机器人ID
QWEN_API_KEY = "通义千问API Key"
TAVILY_API_KEY = "Tavily搜索Key"
PUBLIC_ROLE_ID = 可领取身份组ID
MIYUSHE_COOKIE = ""
HOYOLAB_COOKIE = ""
 
 
 
 
🌐 网页管理后台使用教程
 
机器人启动成功后，在浏览器打开：
http://127.0.0.1:5000
 
后台登录教程
 
1. 输入配置文件中设置的管理员账号密码
2. 输入页面显示的验证码
3. 点击登录进入管理控制台
 
后台功能使用教程
 
- 开启/休眠机器人：点击对应按钮即可切换运行状态
- 发送Discord消息：输入频道ID和内容，点击发送
- 同步斜杠指令：点击「同步斜杠指令」，重启机器人生效
- 黑名单管理：输入用户名，可添加/移除黑名单
- 用户权限管理：设置普通用户/管理员权限
- 日志查看：实时显示运行日志，可手动刷新/清空
- 清空聊天记忆：一键清空所有用户的AI对话记录
 
 
 
📌 指令使用教程
 
斜杠指令使用教程
 
在 Discord 频道输入  / ，即可打开指令列表，选择对应功能并按提示输入参数。
 
前缀指令使用教程
 
-  !kick @成员  — 踢出成员
-  !mute @成员 分钟  — 禁言成员
-  !unmute @成员  — 解除禁言
-  !status 内容  — 修改机器人状态
-  !newchat  — 开启新对话（清空记忆）
-  !continuechat  — 继续上一轮对话
-  !history  — 查看聊天记录
-  !userinfo  — 查看用户信息
 
快捷面板使用教程
 
在频道直接发送文字：
 
-  管理面板  — 打开管理员功能按钮
-  权限面板  — 打开身份组领取按钮
 
 
 
⚠️ 常见问题解决教程
 
1. 机器人无法登录
 
- 检查 Bot Token 是否正确
- 检查网络是否可访问 Discord
- 检查开发者门户是否开启全部 Intents
 
2. 斜杠指令不显示
 
- 前往管理后台点击「同步斜杠指令」
- 重启机器人
- 等待 Discord 指令同步（1–5 分钟）
 
3. AI 不回复
 
- 检查 QWEN_API_KEY 是否正确
- 检查 API 余额是否充足
- 检查网络是否正常
 
4. 管理后台打不开
 
- 确认机器人已正常启动
- 检查端口 5000 是否被占用
- 访问地址：http://127.0.0.1:5000
 
5. 米游社查询失败
 
- 检查 Cookie 是否正确
- 检查 Cookie 是否过期
- 检查 UID 是否输入正确
 
 
 
👑 作者与声明
 
原作者：Mikukero
Discord主页：https://discord.com/users/1405492229627187212
Github主页：https://github.com/K2ngw1223/DiscordBot
项目名称：DiscordBot
版权声明：保留所有权利，仅供学习与个人使用，禁止未经授权商用
注意：使用本项目请保留原作者信息
 
 
 
✨ 感谢使用
