<img width="735" height="525" alt="Image" src="https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910" />

# 大致預覽                    
|⭐ STARS|🍴 FORKS|⚠️ ISSUES|🔀 PULLS|
|--------|--------|---------|--------|
|We need it|too|Firefly|Love|
</div>
<br>
<div align="center">
<a href="./README.md">簡體中文</a> |
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
# Firefly-Ⅳ | 星穹·流螢跨平台AI機器人
> Discord + QQ OneBot 雙端一體化智慧機器人｜全Web視覺化設定｜區域網管理後台｜流螢原生人設AI引擎
## 📌 專案簡介
Firefly-IV 基於`discord.py + NoneBot2 + Flask + Qwen LLM + Tavily`開發，完整還原**崩壞：星穹鐵道-流螢**的人物個性與對白邏輯，實現Discord伺服器營運加上QQ群託管的雙平台連動。
### 核心優點
- ❌ 無任何程式硬寫金鑰，所有設定透過網頁填寫儲存
- ✅ Flask綁定0.0.0.0，區網內所有裝置皆可存取管理後台
- ✅ Discord與QQ共用AI記憶，被@時自動觸發流螢專屬回覆
- ✅ 內建：AI問答、網路搜尋、程式執行、影片摘要、線上點歌、群組管理
- ✅ 自助領身分、管理員清理頻道互動按鈕
[開發者](https://discord.com/users/1405492229627187212)
 
## 🧩 技術依賴
| 依賴 | 用途 |
| :--- | :--- |
| discord.py | Discord斜線指令、互動按鈕、伺服器管理 |
| nonebot2+onebot-v11 | QQ串接(LLOneBot/NTQQ) |
| Flask | 登入權限、視覺化設定、啟停管理 |
| DashScope-Qwen | 對話產生、程式生成、影片摘要 |
| Tavily API | 即時網路資源查詢 |
| aiohttp | 非同步網路請求 |
## ⚡ 快速部署
### 1. 安裝依賴
```bash
pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp

2. 前置作業
​
3. 安裝NTQQ搭配LLOneBot，預設連線位址：ws://127.0.0.1:3001
​
4. 於Discord官網申請Bot，開啟全部閘道權限
​
5. 自行申請通義千問、Tavily金鑰
​
6. 啟動專案
執行main.py
本機位址：http://127.0.0.1:5000
區網位址：本機IP:5000
 
🖥️ Web管理後台
功能區塊	內容
設定表單	DiscordToken/QwenKey/TavilyKey/各式Cookie/角色ID/OneBotWS
控制按鈕	啟動機器人、停止機器人、清空對話紀錄
狀態面板	即時顯示上線/離線狀態

🎯 Discord指令
指令	功能
/ask 問題	流螢AI網路問答
/search 關鍵字	全網搜尋
/code 需求	Python程式產生並執行
/點歌 歌名	產生YouTube連結
/bilibili 連結	Bilibili影片摘要
/youtube 連結	YouTube內容統整

🎯 QQ指令
指令	功能
/ask	流螢AI對話
/search	全網查詢
/code	程式編譯執行
/點歌	音樂搜尋
/bilibili	影片解析

💬 流螢人設
固定稱呼使用者為開拓者，口語帶軟綴助詞，設定與薩姆、星核獵人相關，能自動安撫負面情緒。
 
📂 資料夾結構
Firefly-IV/
├─ main.py
├─ bot_config.json
└─ README.md

🔗 開發者資訊
K2ngw / Mikukero | Discord:1405492229627187212
 
⚠️ 免責聲明
 
1. 禁止違法大量掛載QQ帳號
​
2. Discord需開啟Message Content Intent權限
​
3. API金鑰請妥善保管
