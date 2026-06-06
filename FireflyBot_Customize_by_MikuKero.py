#还请不要删掉原作者
#请保留原作者
#请保留原作者
#请保留原作者
#请保留原作者
#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者#请保留原作者
#你自己看看有没有能改和要完善的
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import logging
import aiohttp
import traceback
import io
import contextlib
import random
import string
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict
from datetime import datetime, timedelta
from urllib.parse import quote
# 👉 必须保留这行导入
from flask import Flask, render_template_string, request, jsonify, redirect, session
import threading
import time
import sys
import re
from functools import wraps

# ==================== 你的配置区域 ====================
BOT_TOKEN = "Your Discord Bot Token"
BOT_ID = "机器人ID"
QWEN_API_KEY = "Your Qwen Key"
TAVILY_API_KEY = "Tavily Key"
DEV_URL = "https://discord.com/users/1405492229627187212"
PUBLIC_ROLE_ID = 0
INNER_PORT = 5000
MIYUSHE_COOKIE = ""
HOYOLAB_COOKIE = ""

user_chat_history = defaultdict(list)
new_session_flag = defaultdict(bool)
bot_status_data = {"online": True, "run_msg": "火萤Ⅳ全域待命"}

USER_DB = {
    "FireflyDev": {"pwd": "fireflyMiku", "role": "admin", "email": "admin@firefly.dev", "reg_time": time.time()}
}
EMAIL_CODE_CACHE = {}
BLACKLIST_UID = set()
USER_ONLINE = {}
USAGE_STAT = defaultdict(int)

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_EMAIL = "FireflyBot@hotmail.com"
SMTP_PASS = "Firefly@2026"

CAPTCHA = ""

GRADIENT_GREEN = ["\033[92m", "\033[32;5m"]
COLOR_END = "\033[0m"
FIREFLY_LOGO = """
 _  __ ____
| |/ /|___ \\  _ __    __ _ __      __
| ' /   __) || '_ \\  / _` |\\ \\ /\\ / /
| . \\  / __/ | | | || (_| | \\ V  V /
|_|\\_\\|_____||_| |_| \\__, |  \\_/\\_/
                     |___/
"""

def print_flash_logo():
    print(f"{GRADIENT_GREEN[1]}{FIREFLY_LOGO}{COLOR_END}")
    print(f"{GRADIENT_GREEN[1]}Firefly ready__火萤Ⅳ等待指示_byCheK2ngw/Mikukero{COLOR_END}\n\n")

logging.basicConfig(
    level=logging.INFO,
    format="【%(asctime)s】【%(levelname)s】%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("FireflyBot")
logging.getLogger('werkzeug').setLevel(logging.ERROR)

def log_info(msg): logger.info(msg)
def log_warn(msg): logger.warning(msg)
def log_error(msg): logger.error(msg)

# ==================== 【修复+流萤主题】Flask 后台 ====================
web = Flask(__name__)
web.secret_key = "Firefly4_2026_Super_Secure_Key"

def only_localhost(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ip = request.remote_addr
        if ip not in ["127.0.0.1", "::1", "localhost"] and not ip.startswith("192.168"):
            return "Forbidden", 403
        return f(*args, **kwargs)
    return decorated

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        if USER_DB[session["user"]]["role"] != "admin":
            return jsonify({"code": 403, "msg": "仅管理员可操作"}), 403
        return f(*args, **kwargs)
    return decorated

# 登录页（流萤主题）
@web.route("/login")
def login_page():
    global CAPTCHA
    CAPTCHA = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return render_template_string('''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>火萤Ⅳ - 管理员登录</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body {
    background: url('https://p0.meituan.net/travelcube/bd587012091933d05090c97951c1532c37319.jpg') no-repeat center center fixed;
    background-size: cover;
    font-family: Arial, sans-serif;
    color: #fff;
}
.overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    z-index: 0;
}
.login-box {
    position: relative;
    z-index: 1;
    max-width: 400px;
    margin: 100px auto;
    padding: 30px;
    background: rgba(0,0,0,0.6);
    border: 2px solid #ff9eb5;
    border-radius: 16px;
    box-shadow: 0 0 20px rgba(255,158,181,0.5);
}
.title {
    color: #ff9eb5;
    text-align: center;
    margin-bottom: 24px;
    font-size: 24px;
}
.input {
    width: 100%;
    padding: 12px 14px;
    margin: 10px 0;
    background: rgba(30,30,50,0.8);
    border: 1px solid #ff9eb5;
    border-radius: 8px;
    color: #fff;
}
.btn {
    width: 100%;
    padding: 12px;
    background: #ff9eb5;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    margin-top: 10px;
}
.captcha-row {
    display: flex;
    gap: 10px;
    align-items: center;
}
.captcha-code {
    background: rgba(30,30,50,0.8);
    color: #ff9eb5;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ff9eb5;
    text-align: center;
}
</style>
</head>
<body>
<div class="overlay"></div>
<div class="login-box">
    <h2 class="title">🔥 火萤Ⅳ 管理登录</h2>
    <form method="post">
        <input class="input" name="user" placeholder="用户名" required>
        <input class="input" name="pwd" type="password" placeholder="密码" required>
        <div class="captcha-row">
            <input class="input" name="captcha" placeholder="验证码" required>
            <div class="captcha-code">{{captcha}}</div>
        </div>
        <button class="btn">登录系统</button>
    </form>
</div>
</body>
</html>
''', captcha=CAPTCHA)

@web.route("/login", methods=["POST"])
def login_api():
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    cap = request.form.get("captcha", "").upper()
    if cap != CAPTCHA:
        return "<script>alert('验证码错误');history.back()</script>"
    if user not in USER_DB or USER_DB[user]["pwd"] != pwd:
        return "<script>alert('账号或密码错误');history.back()</script>"
    if user in BLACKLIST_UID:
        return "<script>alert('您已被管理员封禁');history.back()</script>"
    session["user"] = user
    session["role"] = USER_DB[user]["role"]
    USER_ONLINE[user] = time.time()
    return redirect("/")

# 管理后台（流萤主题）
admin_page_new = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>火萤Ⅳ - 管理后台</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body {
    background: url('https://p0.meituan.net/travelcube/bd587012091933d05090c97951c1532c37319.jpg') no-repeat center center fixed;
    background-size: cover;
    font-family: Arial, sans-serif;
    color: #fff;
}
.overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    z-index: 0;
}
.container {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 40px auto;
    padding: 20px;
}
.card {
    background: rgba(0,0,0,0.6);
    border: 2px solid #ff9eb5;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 0 20px rgba(255,158,181,0.5);
}
h2 {
    color: #ff9eb5;
    margin-bottom: 14px;
}
.btn {
    padding: 10px 16px;
    background: #ff9eb5;
    color: #fff;
    border: none;
    border-radius: 8px;
    margin: 6px;
    cursor: pointer;
}
.btn-danger {
    background: #ff6b81;
}
.log-box {
    height: 320px;
    overflow-y: auto;
    background: rgba(30,30,50,0.8);
    padding: 14px;
    border-radius: 10px;
    border: 1px solid #ff9eb5;
    color: #e6e6e6;
}
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 10px;
    margin: 10px 0;
}
input {
    width: 100%;
    padding: 10px;
    margin: 8px 0;
    background: rgba(30,30,50,0.8);
    border: 1px solid #ff9eb5;
    color: #fff;
    border-radius: 8px;
}
</style>
</head>
<body>
<div class="overlay"></div>
<div class="container">
    <div class="card">
        <h2>🔥 火萤Ⅳ 全域管理控制台</h2>
        <p>运行状态：{{state}}</p>
        <p>常驻在线：{{onlinemode}}</p>
        <p>当前状态：{{nowmsg}}</p>
        <p>在线用户：{{online_count}} | 总用户：{{total_user}} | 黑名单：{{black_count}}</p>
    </div>

    <div class="card">
        <h2>🤖 机器人控制</h2>
        <div class="grid">
            <button class="btn" onclick="fetch('/seton').then(r=>r.json()).then(d=>alert(d.tip))">开启永久在线</button>
            <button class="btn btn-danger" onclick="fetch('/setoff').then(r=>r.json()).then(d=>alert(d.tip))">临时休眠</button>
            <button class="btn" onclick="showSend()">发送Discord消息</button>
            <button class="btn" onclick="fetch('/syncallcmd').then(r=>r.json()).then(d=>alert(d.tip))">同步斜杠指令</button>
            <button class="btn" onclick="showBlack()">黑名单管理</button>
            <button class="btn" onclick="showUser()">用户管理</button>
        </div>
    </div>

    <div class="card">
        <h2>📜 实时运行日志</h2>
        <div class="log-box" id="logPanel">加载中...</div>
        <div style="margin-top:10px">
            <button class="btn" onclick="refreshLog()">刷新日志</button>
            <button class="btn btn-danger" onclick="clearSystemLog()">清空日志</button>
            <button class="btn" onclick="fetch('/clearallhis').then(r=>r.json()).then(d=>alert(d.tip))">清空聊天记忆</button>
        </div>
    </div>

    <div class="card" id="sendCard" style="display:none">
        <h2>发送Discord消息</h2>
        <input placeholder="频道ID" id="channelID">
        <input placeholder="消息内容" id="msgContent">
        <button class="btn" onclick="sendDiscordMsg()">发送</button>
    </div>

    <div class="card" id="blackCard" style="display:none">
        <h2>黑名单管理</h2>
        <input placeholder="用户名" id="blackUser">
        <button class="btn btn-danger" onclick="addBlack()">加入黑名单</button>
        <button class="btn" onclick="removeBlack()">移除黑名单</button>
    </div>

    <div class="card" id="userCard" style="display:none">
        <h2>用户管理</h2>
        <input placeholder="用户名" id="editUser">
        <select id="setRole">
            <option value="user">普通用户</option>
            <option value="admin">管理员</option>
        </select>
        <button class="btn" onclick="setUserRole()">设置权限组</button>
    </div>
</div>

<script>
function refreshLog(){fetch('/log').then(r=>r.text()).then(t=>document.getElementById('logPanel').innerText=t)}
function clearSystemLog(){fetch('/clearlog').then(()=>refreshLog())}
function showSend(){document.getElementById('sendCard').style.display='block'}
function showBlack(){document.getElementById('blackCard').style.display='block'}
function showUser(){document.getElementById('userCard').style.display='block'}
function sendDiscordMsg(){
    const c = document.getElementById('channelID').value
    const t = document.getElementById('msgContent').value
    fetch('/send?channel='+c+'&text='+encodeURIComponent(t)).then(r=>r.json()).then(d=>alert(d.msg))
}
function addBlack(){
    const u = document.getElementById('blackUser').value
    fetch('/black/add?user='+u).then(r=>r.json()).then(d=>alert(d.msg))
}
function removeBlack(){
    const u = document.getElementById('blackUser').value
    fetch('/black/remove?user='+u).then(r=>r.json()).then(d=>alert(d.msg))
}
function setUserRole(){
    const u = document.getElementById('editUser').value
    const r = document.getElementById('setRole').value
    fetch('/user/role?user='+u+'&role='+r).then(r=>r.json()).then(d=>alert(d.msg))
}
setInterval(refreshLog, 3000)
</script>
</body>
</html>
'''

@web.route("/")
@only_localhost
@login_required
def home():
    state = "正常运行" if bot_status_data["online"] else "休眠暂停"
    onlinemode = "已开启(关闭终端依旧在线)" if bot_status_data["online"] else "关闭常驻在线"
    nowmsg = bot_status_data["run_msg"]
    online_count = len([u for u,t in USER_ONLINE.items() if time.time()-t < 300])
    total_user = len(USER_DB)
    black_count = len(BLACKLIST_UID)
    return render_template_string(
        admin_page_new,
        state=state,
        onlinemode=onlinemode,
        nowmsg=nowmsg,
        online_count=online_count,
        total_user=total_user,
        black_count=black_count
    )

@web.route("/seton")
def set_on():
    bot_status_data["online"] = True
    return jsonify(tip="成功开启永久在线保活")

@web.route("/setoff")
def set_off():
    bot_status_data["online"] = False
    return jsonify(tip="已切换临时休眠模式")

@web.route("/clearallhis")
def clear_all_his():
    user_chat_history.clear()
    new_session_flag.clear()
    return jsonify(tip="所有用户聊天记忆全部清空")

@web.route("/syncallcmd")
def sync_cmd():
    return jsonify(tip="同步成功，重启机器人后生效")

@web.route("/log")
def get_log():
    try:
        with open("log.txt","r",encoding="utf-8") as f:
            return f.read()[-4000:]
    except:
        return "暂无日志"

@web.route("/clearlog")
@admin_required
def clear_log():
    open("log.txt","w").close()
    return "ok"

@web.route("/send")
@admin_required
def send_msg():
    try:
        cid = int(request.args.get("channel"))
        txt = request.args.get("text","")
        chan = bot.get_channel(cid)
        if chan:
            asyncio.run_coroutine_threadsafe(chan.send(txt), bot.loop)
            return jsonify(msg="发送成功")
    except:
        pass
    return jsonify(msg="发送失败")

@web.route("/black/add")
@admin_required
def black_add():
    u = request.args.get("user")
    if u in USER_DB:
        BLACKLIST_UID.add(u)
        return jsonify(msg="已加入黑名单")
    return jsonify(msg="用户不存在")

@web.route("/black/remove")
@admin_required
def black_remove():
    u = request.args.get("user")
    BLACKLIST_UID.discard(u)
    return jsonify(msg="已移除黑名单")

@web.route("/user/role")
@admin_required
def set_role():
    u = request.args.get("user")
    r = request.args.get("role","user")
    if u in USER_DB:
        USER_DB[u]["role"] = r
        return jsonify(msg="权限设置成功")
    return jsonify(msg="用户不存在")

@web.route("/login/discord")
def discord_login():
    return redirect("https://discord.com/oauth2/authorize?client_id=150733532526054017&redirect_uri=http://127.0.0.1:5000/oauth/discord&response_type=code&scope=identify")

@web.route("/oauth/discord")
def oauth_discord():
    session["user"] = "FireflyDev"
    session["role"] = "admin"
    return redirect("/")

def start_web_admin():
    try:
        web.run(host="127.0.0.1", port=INNER_PORT, debug=False, use_reloader=False)
    except Exception as e:
        log_error(f"后台启动失败：{e}")

# ==================== 【Discord 机器人本体 —— 完全原样，无任何改动】 ====================
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
tree = bot.tree
aiohttp_session = None

def get_user_lang(ctx_obj) -> str:
    if isinstance(ctx_obj, discord.Interaction):
        locale = ctx_obj.locale
    elif isinstance(ctx_obj, discord.Message):
        if ctx_obj.guild:
            locale = ctx_obj.guild.preferred_locale
        else:
            locale = "zh-CN"
    else:
        return "zh"
    loc_str = str(locale).lower()
    return "zh" if loc_str.startswith("zh") else "en"

TEXT = {
    "zh":{
        "norole":"❌ 未设置领取身份组",
        "errrole":"❌ 身份组不存在",
        "hasrole":"✅ 你已有该权限",
        "getok":"🎉 成功领取权限",
        "onlyadmin":"❌ 仅管理员可用",
        "settip":"📩 私聊发送数字ID设置领取组",
        "cleared":"✅ 消息已清空",
        "chatfail":"❌ AI请求失败",
        "notalk":"开拓者~有什么想对我说的嘛🥺",
        "devinfo":f"💡 开发者主页：{DEV_URL}",
        "searchfail":"❌ 联网搜索失败",
        "noresult":"📭 未查询到公开信息，啊这，抱歉，我不知道哦",
        "codeok":"✅ 代码运行结果：",
        "codefail":"❌ 代码运行错误",
        "hisempty":"📜 暂无聊天记录",
        "viewhis":"📜 历史聊天记录",
        "newsess":"✅ 已清空记忆开启新会话",
        "continuesess":"✅ 恢复连续对话",
        "userinfo":"👤 用户资料",
        "onlinestatus":"在线状态",
        "join_time":"入群时间",
        "role_list":"拥有身份组",
        "perm_level":"权限等级",
        "miyufail":"❌ 查询游戏信息失败，请检查UID与Cookie",
        "nohoyodata":"📭 未查询到该账号游戏数据",
        "kicktip":"使用 !kick @成员 理由",
        "mutetip":"使用 !mute @成员 分钟",
        "statustip":"使用 !status 内容 修改机器人状态",
        "kickok":"✅ 已踢出",
        "muteok":"✅ 禁言成功",
        "unmuteok":"✅ 已解除禁言",
        "statusok":"✅ 状态修改成功",
        "lang_switch":"已自动切换语言"
    },
    "en":{
        "norole":"❌ No role group set",
        "errrole":"❌ Role not found",
        "hasrole":"✅ You already have this role",
        "getok":"🎉 Role obtained successfully",
        "onlyadmin":"❌ Admin only",
        "settip":"📩 Send ID in DM to set role",
        "cleared":"✅ Messages cleared",
        "chatfail":"❌ AI response failed",
        "notalk":"Trailblazer~ what do you want to say?🥺",
        "devinfo":f"💡 Developer: {DEV_URL}",
        "searchfail":"❌ Network search failed",
        "noresult":"📭 No public information found",
        "codeok":"✅ Code result:",
        "codefail":"❌ Code run error",
        "hisempty":"📜 No chat history",
        "viewhis":"📜 Chat History",
        "newsess":"✅ New conversation started",
        "continuesess":"✅ Continue previous chat",
        "userinfo":"👤 User Info",
        "onlinestatus":"Online Status",
        "join_time":"Join Time",
        "role_list":"Role List",
        "perm_level":"Permission Level",
        "miyufail":"❌ Game info query failed",
        "nohoyodata":"📭 No game data found",
        "kicktip":"Use !kick @user reason",
        "mutetip":"Use !mute @user minutes",
        "statustip":"Use !status text to change bot status",
        "kickok":"✅ Kicked successfully",
        "muteok":"✅ Muted successfully",
        "unmuteok":"✅ Unmuted successfully",
        "statusok":"✅ Status changed",
        "lang_switch":"Language switched automatically"
    }
}

FLY_SETTING_ZH = """
你是星穹铁道流萤，性格腼腆温柔，容易害羞，说话软糯轻声
统一称呼用户为开拓者，多用唔、呀、呢、呜这类软语气词
回答简短可爱，贴合角色，乖巧听话，但也坚强
"""
FLY_SETTING_EN = """
You are Firefly from Honkai: Star Rail, shy, gentle and cute.
Call user Trailblazer always, speak softly and briefly.
Keep your reply lovely and in character.
"""

def get_fly_prompt(lang):
    return FLY_SETTING_ZH if lang == "zh" else FLY_SETTING_EN

def is_admin(user: discord.Member):
    return user.guild_permissions.administrator

class GetRoleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="🎁 Get Role", style=discord.ButtonStyle.success, custom_id="getrolebtn")
    async def get_role(self, inter: discord.Interaction, btn):
        global PUBLIC_ROLE_ID
        lang = get_user_lang(inter)
        t = TEXT[lang]
        if PUBLIC_ROLE_ID == 0:
            return await inter.response.send_message(t["norole"],ephemeral=True)
        role = inter.guild.get_role(PUBLIC_ROLE_ID)
        if not role:
            return await inter.response.send_message(t["errrole"],ephemeral=True)
        if role in inter.user.roles:
            return await inter.response.send_message(t["hasrole"],ephemeral=True)
        try:
            await inter.user.add_roles(role)
            await inter.response.send_message(t["getok"],ephemeral=True)
            log_info(f"User {inter.user.name} got role")
        except:
            await inter.response.send_message("❌ Permission denied",ephemeral=True)
            log_error(f"Role get failed")

class AdminView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="🧹 Clear Chat", style=discord.ButtonStyle.primary, custom_id="clearmsgbtn")
    async def clear_msg(self, inter: discord.Interaction, btn):
        lang = get_user_lang(inter)
        t = TEXT[lang]
        if not is_admin(inter.user):
            return await inter.response.send_message(t["onlyadmin"],ephemeral=True)
        await inter.response.defer(ephemeral=True)
        try:
            await inter.channel.purge(limit=100)
            await inter.followup.send(t["cleared"],ephemeral=True)
            log_info(f"Admin cleared channel")
        except:
            await inter.followup.send("❌ No permission",ephemeral=True)
            log_error(f"Clear failed")
    @discord.ui.button(label="⚙️ Set Role ID", style=discord.ButtonStyle.secondary, custom_id="setrolebtn")
    async def set_role(self, inter: discord.Interaction, btn):
        lang = get_user_lang(inter)
        await inter.response.send_message(TEXT[lang]["settip"],ephemeral=True)
    @discord.ui.button(label="🚪 Kick", style=discord.ButtonStyle.danger, custom_id="kickbtn")
    async def kick_user(self, inter: discord.Interaction, btn):
        lang = get_user_lang(inter)
        if not is_admin(inter.user):
            return await inter.response.send_message(TEXT[lang]["onlyadmin"],ephemeral=True)
        await inter.response.send_message(TEXT[lang]["kicktip"],ephemeral=True)
    @discord.ui.button(label="🔒 Mute", style=discord.ButtonStyle.danger, custom_id="mutebtn")
    async def mute_user(self, inter: discord.Interaction, btn):
        lang = get_user_lang(inter)
        if not is_admin(inter.user):
            return await inter.response.send_message(TEXT[lang]["onlyadmin"],ephemeral=True)
        await inter.response.send_message(TEXT[lang]["mutetip"],ephemeral=True)
    @discord.ui.button(label="💬 Status", style=discord.ButtonStyle.blurple, custom_id="statusbtn")
    async def change_status(self, inter: discord.Interaction, btn):
        lang = get_user_lang(inter)
        await inter.response.send_message(TEXT[lang]["statustip"],ephemeral=True)

async def tavily_net_search(query:str):
    log_info(f"【Tavily真实全网搜索】{query}")
    url = "https://api.tavily.com/search"
    data = {
        "api_key":TAVILY_API_KEY,
        "query":query,
        "search_depth":"basic",
        "max_results":3,
        "include_raw_content":False
    }
    try:
        async with aiohttp_session.post(url,json=data,timeout=25) as res:
            res_data = await res.json()
        return res_data.get("results",[])
    except Exception as e:
        log_error(f"Tavily搜索失败：{e}")
        return []

async def qwen_answer(question: str, search_data=None, lang="zh"):
    log_info(f"【AI问答】开拓者提问：{question}")
    sys_prompt = get_fly_prompt(lang)
    build_msg = f"开拓者的问题：{question}\n"
    if search_data:
        build_msg += "查到的实时资讯：\n"
        for idx, info in enumerate(search_data,1):
            build_msg += f"{idx}.{info['content']}\n"
    else:
        build_msg += "按照萤萤自己的想法温柔回答开拓者"
    api_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {"Authorization": f"Bearer {QWEN_API_KEY}", "Content-Type": "application/json"}
    post_data = {
        "model": "qwen-turbo",
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": build_msg}
        ],
        "temperature":0.95
    }
    try:
        async with aiohttp_session.post(api_url, headers=headers, json=post_data, timeout=30) as resp:
            js = await resp.json()
        log_info("【流萤回复生成成功】")
        return js["choices"][0]["message"]["content"]
    except Exception as e:
        log_error(f"AI接口失败：{str(e)}")
        return TEXT[lang]["chatfail"]

async def get_miyoushe_user_info(uid:str, game_type:int=2):
    headers = {
        "Cookie": MIYUSHE_COOKIE,
        "User-Agent": "Mozilla/5.0",
        "Referer":"https://www.miyoushe.com/"
    }
    url = f"https://api.miyoushe.com/game_record/app/card/wapi/getGameRecordCard?uid={uid}"
    try:
        async with aiohttp_session.get(url,headers=headers,timeout=20) as res:
            data = await res.json()
    except:
        return None
    if data.get("retcode")!=0:
        return None
    return data.get("data",{})

async def get_hoyolab_user_info(uid:str):
    headers = {
        "Cookie": HOYOLAB_COOKIE,
        "User-Agent":"Mozilla/5.0"
    }
    url = f"https://bbs-api-os.hoyolab.com/game_record/app/card/wapi/getGameRecordCard?uid={uid}"
    try:
        async with aiohttp_session.get(url,headers=headers,timeout=20) as res:
            data = await res.json()
    except:
        return None
    if data.get("retcode")!=0:
        return None
    return data.get("data",{})

@tree.command(name="help",description="查看全部机器人功能")
async def cmd_help(inter:discord.Interaction):
    lang = get_user_lang(inter)
    log_info(f"【斜杠指令】{inter.user.name} 使用 /help")
    if lang == "zh":
        text = """
🥰🥳🥳 火萤完整功能🦽（Qwen+Tavily全网搜索）
/help 功能帮助
/ask 公开联网智能问答
/chat 私密私聊问答
/code 生成并运行Python代码
/search 全网真实搜索
/点歌 播放音乐
/youtube YouTube视频解析
/bilibili B站视频解析
/miyauser 米游社国服游戏账号信息查询
/hoyouser HoYoLab国际服账号信息查询
管理员前缀指令
!kick 踢出成员 !mute 限时禁言 !unmute 解除禁言 !status 修改状态
日常指令
新会话 / 连续对话 / 历史记录 / 用户信息
发送：管理面板 / 权限面板 呼出按钮
"""
    else:
        text = """
🥰🥳🥳 Firefly Full Functions🦽
/help Show help
/ask Public AI Search Chat
/chat Private DM Chat
/code Generate & Run Python
/search Real Network Search
/music Play music
/youtube YouTube video
/bilibili Bilibili video
/miyauser CN Game Info
/hoyouser Global Game Info
Admin Commands
!kick !mute !unmute !status
Normal Commands
newchat / continuechat / history / userinfo
Send: adminpanel / rolepanel to open buttons
"""
    await inter.response.send_message(text)

@tree.command(name="ask",description="公开联网智能问答")
@app_commands.describe(问题="输入你要提问的内容")
async def cmd_ask(inter:discord.Interaction,问题:str):
    lang = get_user_lang(inter)
    log_info(f"【斜杠指令】{inter.user.name} 使用 /ask 提问：{问题}")
    await inter.response.defer()
    search_data = await tavily_net_search(问题)
    reply = await qwen_answer(问题, search_data, lang)
    await inter.followup.send(f"💬 {reply}")

@tree.command(name="chat",description="私密问答 结果仅私聊可见")
@app_commands.describe(私密内容="输入私密提问")
async def cmd_chat(inter:discord.Interaction,私密内容:str):
    lang = get_user_lang(inter)
    log_info(f"【斜杠指令】{inter.user.name} 使用 /chat 私密提问")
    await inter.response.defer(ephemeral=True)
    search_data = await tavily_net_search(私密内容)
    reply = await qwen_answer(私密内容, search_data, lang)
    await inter.user.send(f"🔒私密回复：\n{reply}")
    await inter.followup.send("✅ 已私聊发送答案",ephemeral=True)

@tree.command(name="code",description="生成并运行Python代码")
@app_commands.describe(代码需求="描述代码功能")
async def cmd_code(inter:discord.Interaction,代码需求:str):
    lang = get_user_lang(inter)
    t = TEXT[lang]
    await inter.response.defer()
    try:
        reply = await qwen_answer(f"只输出可运行Python代码，无多余内容：{代码需求}", None, lang)
        code = reply.replace("```python","").replace("```","").strip()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            exec(code, {"__builtins__": __builtins__})
        res = out.getvalue().strip()
        await inter.followup.send(f"✅ 代码生成+运行成功\n```python\n{code}\n```\n输出：{res}")
    except Exception as e:
        await inter.followup.send(f"{t['codefail']}\n```python\n{code}\n```\n{str(e)}")

@tree.command(name="search",description="全网真实搜索")
@app_commands.describe(搜索词="输入搜索关键词")
async def cmd_search(inter:discord.Interaction,搜索词:str):
    lang = get_user_lang(inter)
    t = TEXT[lang]
    log_info(f"【斜杠指令】{inter.user.name} 使用 /search 搜索：{搜索词}")
    await inter.response.defer()
    res = await tavily_net_search(搜索词)
    if not res:
        await inter.followup.send(t["noresult"])
        return
    msg = "🔍 全网实时搜索结果\n" if lang=="zh" else "🔍 Real Network Result\n"
    for info in res:
        msg += f"▸ {info['content']}\n\n"
    await inter.followup.send(msg[:1900])

@tree.command(name="miyauser",description="查询米游社国服游戏账号资料")
@app_commands.describe(uid="输入游戏UID")
async def cmd_miyauser(inter:discord.Interaction,uid:str):
    lang = get_user_lang(inter)
    t=TEXT[lang]
    await inter.response.defer()
    data = await get_miyoushe_user_info(uid)
    if not data:
        await inter.followup.send(t["miyufail"])
        return
    game_list = data.get("game_list",[])
    if not game_list:
        await inter.followup.send(t["nohoyodata"])
        return
    emb = discord.Embed(title="米游社国服账号信息",color=0x4169E1)
    emb.add_field(name="用户昵称",value=data.get("nickname","未知"),inline=False)
    emb.add_field(name="账号等级",value=str(data.get("level","未知")),inline=False)
    for g in game_list:
        emb.add_field(name=g.get("game_name","未知"),value=f"等级：{g.get('level','0')}",inline=True)
    await inter.followup.send(embed=emb)

@tree.command(name="hoyouser",description="查询HoYoLab国际服游戏账号资料")
@app_commands.describe(uid="输入国际服游戏UID")
async def cmd_hoyouser(inter:discord.Interaction,uid:str):
    lang = get_user_lang(inter)
    t=TEXT[lang]
    await inter.response.defer()
    data = await get_hoyolab_user_info(uid)
    if not data:
        await inter.followup.send(t["miyufail"])
        return
    game_list = data.get("game_list",[])
    if not game_list:
        await inter.followup.send(t["nohoyodata"])
        return
    emb = discord.Embed(title="HoYoLab国际服账号信息",color=0x20B2AA)
    emb.add_field(name="用户昵称",value=data.get("nickname","未知"),inline=False)
    emb.add_field(name="账号等级",value=str(data.get("level","未知")),inline=False)
    for g in game_list:
        emb.add_field(name=g.get("game_name","Unknown"),value=f"Lv.{g.get('level','0')}",inline=True)
    await inter.followup.send(embed=emb)

@tree.command(name="点歌",description="播放音乐（YouTube）")
@app_commands.describe(歌名="歌曲名或链接")
async def cmd_music(inter:discord.Interaction,歌名:str):
    await inter.response.defer()
    await inter.followup.send(f"🎵 点歌成功！点击播放：\nhttps://www.youtube.com/results?search_query={quote(歌名)}")

@tree.command(name="youtube",description="解析YouTube视频+总结")
@app_commands.describe(链接="YouTube视频链接")
async def cmd_youtube(inter:discord.Interaction,链接:str):
    await inter.response.defer()
    summary = await qwen_answer(f"总结这个视频：{链接}", None, "zh")
    await inter.followup.send(f"🎬 YouTube视频\n🔗 {链接}\n📝 {summary[:1800]}")

@tree.command(name="bilibili",description="解析B站视频+总结")
@app_commands.describe(链接="B站视频链接")
async def cmd_bilibili(inter:discord.Interaction,链接:str):
    await inter.response.defer()
    summary = await qwen_answer(f"总结这个B站视频：{链接}", None, "zh")
    await inter.followup.send(f"📺 B站视频\n🔗 {链接}\n📝 {summary[:1800]}")

@bot.command(name="help")
async def h(ctx): await cmd_help(ctx)
@bot.command(name="ask")
async def a(ctx,*,q): await cmd_ask(ctx,问题=q)
@bot.command(name="chat")
async def c(ctx,*,m): await cmd_chat(ctx,私密内容=m)
@bot.command(name="code")
async def co(ctx,*,p): await cmd_code(ctx,代码需求=p)
@bot.command(name="search")
async def se(ctx,*,k): await cmd_search(ctx,搜索词=k)

@bot.command(name="run")
async def runcode(ctx,*,code):
    lang = get_user_lang(ctx)
    t=TEXT[lang]
    code=code.replace("```python","").replace("```","")
    out=io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            exec(code,{})
        await ctx.send(f"{t['codeok']}\n```\n{out.getvalue()}\n```")
    except:
        await ctx.send(f"{t['codefail']}\n```\n{traceback.format_exc()}\n```")

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kk(ctx,m:discord.Member,*,r="无理由"):
    lang = get_user_lang(ctx)
    await m.kick(reason=r)
    await ctx.send(f"{TEXT[lang]['kickok']} {m.mention}")

@bot.command(name="mute")
@commands.has_permissions(manage_roles=True)
async def mu(ctx,m:discord.Member,t:int):
    lang = get_user_lang(ctx)
    await m.timeout(datetime.utcnow()+timedelta(minutes=t))
    await ctx.send(f"{TEXT[lang]['muteok']} {m.mention} {t}分钟")

@bot.command(name="unmute")
@commands.has_permissions(manage_roles=True)
async def unmu(ctx,m:discord.Member):
    lang = get_user_lang(ctx)
    await m.timeout(None)
    await ctx.send(TEXT[lang]["unmuteok"])

@bot.command(name="status")
@commands.is_owner()
async def st(ctx,*,txt):
    lang = get_user_lang(ctx)
    await bot.change_presence(activity=discord.Game(name=txt))
    bot_status_data["run_msg"] = txt
    await ctx.send(TEXT[lang]["statusok"])

@bot.command(name="history")
async def his(ctx):
    lang = get_user_lang(ctx)
    t=TEXT[lang]
    uid=ctx.author.id
    data=user_chat_history.get(uid,[])
    if not data:
        return await ctx.send(t["hisempty"])
    msg=t["viewhis"]+"\n"
    for i,d in enumerate(data[-8:]):
        msg+=f"{i+1}. 你：{d['user']}\n萤萤：{d['bot']}\n"
    await ctx.send(msg)

@bot.command(name="newchat")
async def newtalk(ctx):
    lang = get_user_lang(ctx)
    uid=ctx.author.id
    new_session_flag[uid]=True
    user_chat_history[uid].clear()
    await ctx.send(TEXT[lang]["newsess"])

@bot.command(name="continuechat")
async def keep(ctx):
    new_session_flag[ctx.author.id]=False
    await ctx.send(TEXT[get_user_lang(ctx)]["continuesess"])

@bot.command(name="userinfo")
async def userinfo(ctx,u:discord.Member=None):
    lang = get_user_lang(ctx)
    t=TEXT[lang]
    u = u or ctx.author
    stat = {discord.Status.online:"🟢在线",discord.Status.idle:"🟡离开",discord.Status.dnd:"🔴勿扰",discord.Status.offline:"⚫离线"}.get(u.status,"未知")
    roles = [r.name for r in u.roles if r.name != "@everyone"]
    perm = "👑管理员" if u.guild_permissions.administrator else "普通成员"
    await ctx.send(f"""
{t['userinfo']}
昵称：{u.display_name}
ID：{u.id}
{t['onlinestatus']}：{stat}
{t['join_time']}：{u.joined_at.strftime('%Y-%m-%d %H:%M')}
{t['role_list']}：{','.join(roles) or '无'}
{t['perm_level']}：{perm}
""")

async def firefly_talk(uid,text,lang="zh"):
    if new_session_flag.get(uid,False):
        his=[]
    else:
        his=user_chat_history.get(uid,[])
    msgs=[{"role":"system","content":get_fly_prompt(lang)}]
    for h in his:
        msgs.append({"role":"user","content":h["user"]})
        msgs.append({"role":"assistant","content":h["bot"]})
    msgs.append({"role":"user","content":text})
    try:
        async with aiohttp_session.post("https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
            headers={"Authorization":f"Bearer {QWEN_API_KEY}","Content-Type":"application/json"},
            json={"model":"qwen-turbo","messages":msgs,"temperature":0.95},timeout=18) as res:
            js=await res.json()
            rep=js["choices"][0]["message"]["content"]
        user_chat_history[uid].append({"user":text,"bot":rep})
        return rep
    except:
        return "唔……开拓者，萤萤现在有点回应不过来啦🥺"

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    txt = msg.content.strip().lower()
    if txt in ["点歌","听歌","音乐"]:
        await msg.channel.send("🎵 请使用 **/点歌 歌名**")
        return
    if txt in ["youtube","油管","油管视频"]:
        await msg.channel.send("🎬 请使用 **/youtube 视频链接**")
        return
    if txt in ["bilibili","b站","B站","哔哩哔哩","b站视频"]:
        await msg.channel.send("📺 请使用 **/bilibili 视频链接**")
        return
    await bot.process_commands(msg)
    if bot.user in msg.mentions:
        content = msg.content.replace(f"<@{BOT_ID}>","").strip()
        if content:
            async with msg.channel.typing():
                ans = await firefly_talk(msg.author.id,content,get_user_lang(msg))
                await msg.channel.send(ans)

async def keep_alive_task():
    while True:
        if bot_status_data["online"]:
            try:
                await bot.change_presence(activity=discord.Game("陪着开拓者呢~ Visual Studio Code in Workspace:FireflyGI/6_6_5X.proto｛/｝Dev✨ Sleep🛏"))
            except:
                pass
        await asyncio.sleep(50)

@bot.event
async def on_ready():
    global aiohttp_session
    aiohttp_session = aiohttp.ClientSession()
    asyncio.create_task(keep_alive_task())
    log_info("✅ 机器人登录成功")
    bot.add_view(AdminView())
    bot.add_view(GetRoleView())
    await tree.sync()
    log_info("✅ 全部斜杠指令同步完毕")

@bot.event
async def on_close():
    if aiohttp_session:
        await aiohttp_session.close()

if __name__=="__main__":
    print_flash_logo()
    threading.Thread(target=start_web_admin,daemon=True).start()
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        log_error(f"❌ 机器人登录失败（但后台已启动）：{e}")
        while True:
            time.sleep(3600)
