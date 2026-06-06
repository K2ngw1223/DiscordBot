<img width="735" height="525" alt="Image" src="https://github.com/user-attachments/assets/92ffd51e-0568-478d-8667-e3fe242b5910" />

# 概要プレビュー
|⭐ STARS|🍴 FORKS|⚠️ ISSUES|🔀 PULLS|
|--------|--------|---------|--------|
|We need it|too|Firefly|Love|
</div>
<br>
<div align="center">
<a href="./README.md">簡体中国語</a> |
<a href="./README_EN.md">English</a> |
<a href="./README_zh-TW.md">繁體中国語</a> |
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
# Firefly-Ⅳ | スターレール 流蛍クロスプラットフォームAIボット
> Discord + QQ OneBot デュアル統合型ボット | Webによる全設定 | LAN管理コンソール | 流蛍キャラ設定AIエンジン
## 📌 プロジェクト概要
Firefly-IVは`discord.py + NoneBot2 + Flask + Qwen LLM + Tavily`をベースに開発され、『スターレイル』の流蛍の性格・台詞を再現し、Discordサーバー管理とQQグループのボット連携を実現します。
### 主な特長
- ❌ コードに鍵情報を直書きせず、Web画面から設定保存
- ✅ Flaskを0.0.0.0で起動、同一LAN内の全機器から管理画面にアクセス可能
- ✅ Discord/QQで会話履歴を共有、@タグ時に流蛍専用返答を自動送信
- ✅ AIチャット・ネット検索・コード実行・動画要約・音楽検索・グループ管理を標準搭載
- ✅ ロール自動取得・チャンネル削除用管理者ボタンを実装
[開発者ページ](https://discord.com/users/1405492229627187212)

## 🧩 使用ライブラリ
| ライブラリ | 役割 |
| :--- | :--- |
| discord.py | Discordスラッシュコマンド・インタラクティブボタン・サーバー管理 |
| nonebot2+onebot-v11 | LLOneBot経由でQQと連携 |
| Flask | ログイン認証・可視化設定・起動停止管理 |
| DashScope-Qwen | 会話生成・コード作成・動画概要作成 |
| Tavily API | リアルタイムWEB検索 |
| aiohttp | 非同期HTTP通信 |

## ⚡ 導入手順
### 1. 依存パッケージインストール
```bash
pip install discord nonebot2 nonebot-adapter-onebot flask aiohttp
2. 事前準備
​
3. NTQQ+LLOneBotをインストール、接続先 ws://127.0.0.1:3001
​
4. DiscordにてBotアプリケーション作成、全ゲートウェイ権限を有効化
​
5. Qwen、TavilyのAPIキーを各自取得
​
6. 起動方法
main.pyを実行
ローカル：http://127.0.0.1:5000
LAN：自身のIP:5000
 
🖥️ Web管理画面
項目	内容
設定欄	DiscordToken/QwenKey/TavilyKey/クッキー/ロールID/OneBotWS
操作ボタン	起動・停止・チャット履歴消去
状態表示	オンライン/オフラインをリアルタイム表示

🎯 Discordコマンド
コマンド	機能
/ask 質問文	流蛍によるAIチャット
/search キーワード	ネット全文検索
/code 要求	Pythonコード生成・実行
/点歌 曲名	YouTubeリンク取得
/bilibili URL	B站動画要約
/youtube URL	YouTube内容まとめ

🎯 QQコマンド
コマンド	機能
/ask	AI雑談
/search	ネット検索
/code	コード実行
/点歌	音楽検索
/bilibili	動画解析

💬 キャラ設定
ユーザーを開拓者と呼び、柔らかい口調。サムや星核ハンターと関連する設定、落ち込んだユーザーを慰める台詞を搭載。
 
📂 フォルダ構成
Firefly-IV/
├─ main.py
├─ bot_config.json
└─ README.md

🔗 開発者情報
K2ngw / Mikukero | Discord:1405492229627187212
 
⚠️ 免責事項
 
1. QQアカウントの不正大量設置を禁止
​
2. Discord側でMessage Content Intentを有効にする
​
3. APIキーは厳重に管理してください
