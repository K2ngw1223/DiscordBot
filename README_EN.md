<img width="735" height="525" alt="Image" src="https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910" />
# Preview
|⭐ STARS|🍴 FORKS|⚠️ ISSUES|🔀 PULLS|
|--------|--------|---------|--------|
|We need it|too|Firefly|Love|
</div>
<br>
<div align="center">
<a href="./README.md">Simplified Chinese</a> |
<a href="./README_EN.md">English</a> |
<a href="./README_zh-TW.md">Traditional Chinese</a> |
<a href="./README_JP.md">Japanese</a>
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
# Firefly-Ⅳ | Honkai: Star Rail Cross-platform AI Bot
> Discord + QQ OneBot Dual-integrated Bot | Full Visualized Web Configuration | LAN Management Backend | Firefly Original Character AI Engine
## 📌 Project Introduction
Firefly-IV is developed based on `discord.py + NoneBot2 + Flask + Qwen LLM + Tavily`. It fully restores Firefly's personality and lines from Honkai: Star Rail and realizes linkage between Discord server management and QQ group hosting.
### Core Highlights
- ❌ No hardcoded secret keys, all settings saved via web page input
- ✅ Flask binds to 0.0.0.0 for LAN-wide backend access
- ✅ Shared chat history for Discord & QQ, auto reply when being @mentioned
- ✅ Built-in: AI chat, web search, code execution, video summary, music search, group management
- ✅ Interactive buttons for self role acquisition and channel clearance
[Developer](https://discord.com/users/1405492229627187212)
 
## 🧩 Dependencies
| Dependency | Usage |
| :--- | :--- |
| discord.py | Discord slash commands, interactive buttons and server management |
| nonebot2+onebot-v11 | QQ connection via LLOneBot/NTQQ |
| Flask | Login authorization and visualized configuration management |
| DashScope-Qwen | Dialogue and code generation |
| Tavily API | Real-time web search |
| aiohttp | Asynchronous network requests |
## ⚡ Quick Setup
### 1. Install Dependencies
```bash
pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp
2. Preparations
​
3. Install NTQQ + LLOneBot on QQ side, default WS: ws://127.0.0.1:3001
​
4. Apply a Discord Bot with full gateway permissions
​
5. Apply Qwen and Tavily API keys by yourself
​
6. Start Project
Run main.py
Local: http://127.0.0.1:5000
LAN: Your local IP:5000
 
🖥️ Web Admin Panel
Area	Content
Config Form	DiscordToken/QwenKey/TavilyKey/Cookie/RoleID/OneBotWS
Control Buttons	Start Bot, Stop Bot, Clear Chat History
Status Panel	Real-time online/offline display

🎯 Discord Commands
Command	Function
/ask	Firefly AI chat
/search	Global search
/code	Python execution
/点歌	Get YouTube link
/bilibili	Video summary
/youtube	Video overview

🎯 QQ Commands
Command	Function
/ask	AI Chat
/search	Network Search
/code	Code Run
/点歌	Music Search
/bilibili	Video Parse

💬 Character Setting
Automatically address users as Trailblazer, soft spoken tone, related to Sam and Stellaron Hunters, comfort users in bad mood.
 
📂 File Structure
Firefly-IV/
├─ main.py
├─ bot_config.json
└─ README.md

🔗 Developer Homepage
K2ngw / Mikukero | Discord:1405492229627187212
 
⚠️ Disclaimer
 
1. Illegal bulk QQ account hosting is prohibited
​
2. Enable Message Content Intent on Discord Developer Portal
​
3. Keep your API keys safe
