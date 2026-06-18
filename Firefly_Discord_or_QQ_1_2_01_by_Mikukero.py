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
from collections import defaultdict
from datetime import datetime, timedelta
from urllib.parse import quote
from flask import Flask, render_template_string, request, jsonify, redirect, session
import threading
import time
import sys
import re
import json
import os
# QQ Nonebot
import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11
from nonebot.plugin import on_command, on_message
from nonebot.params import CommandArg

# 配置文件
CFG_FILE = "bot_config.json"
VIDEO_REG = re.compile(r'(https?://(www\.)?(douyin|bilibili|kuaishou)\.[^\s]+)')
PORT = 5000

# 默认空配置
default_cfg = {
    "discord_token": "",
    "qwen_key": "",
    "tavily_key": "",
    "miyushe_cookie": "",
    "hoyolab_cookie": "",
    "public_role_id": 0,
    "onebot_ws": "ws://127.0.0.1:3001"
}

def load_config():
    if not os.path.exists(CFG_FILE):
        with open(CFG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_cfg, f, ensure_ascii=False, indent=2)
        return default_cfg
    with open(CFG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(cfg):
    with open(CFG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

bot_cfg = load_config()

# 全局变量
user_history = defaultdict(list)
new_chat_flag = defaultdict(bool)
bot_running_info = {"online": True, "status_text": "火萤Ⅳ全域待命"}
USER_ACCOUNT = {"FireflyDev": {"pwd": "fireflycheng", "role": "admin"}}
black_user = set()
captcha_code = ""
discord_bot = None
aio_session = None
BOT_DID = 0

# ==================== 完整流萤人设语料(固定内置) ====================
FLY_PROMPT_ZH = """
你是崩坏星穹铁道-流萤，性格温柔腼腆、容易害羞，说话软糯。
固定称呼对话者为【开拓者】，常用：唔、呀、呢、呜、啦等语气助词。
向往平凡生活，背负星核猎手与萨姆装甲的宿命，偶尔提起萨姆。
安慰情绪低落的开拓者，回复简短自然，不要长篇大论。
"""
FLY_PROMPT_EN = "You are Firefly(Honkai:StarRail),shy and gentle,call user Trailblazer,short soft reply."

# 多语言提示
lang_text = {
    "zh":{
        "no_key":"未配置API密钥",
        "fail_ai":"唔……萤萤暂时没办法回应啦🥺",
        "no_data":"没有搜索到相关内容哦",
        "role_ok":"🎉成功领取身份",
        "no_perm":"只有管理员可以操作哦"
    },
    "en":{
        "no_key":"API key empty",
        "fail_ai":"Sorry,reply failed",
        "no_data":"No result found",
        "role_ok":"Got role",
        "no_perm":"Admin only"
    }
}

# 日志初始化
logging.basicConfig(format="【%(asctime)s】%(message)s",datefmt="%Y-%m-%d %H:%M:%S",level=logging.INFO)
log = logging.getLogger("FireflyLog")
logging.getLogger("werkzeug").setLevel(logging.ERROR)

# ==================== Flask后台【0.0.0.0 局域网全设备可访问】 ====================
app = Flask(__name__)
app.secret_key = "Firefly_2026_LAN_Key_0987"

# 访问限制：仅内网/局域网
def limit_lan(func):
    def wrap(*args,**kwargs):
        ip = request.remote_addr
        allow = ["127.0.0.1","::1","localhost"]
        if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172."):
            allow.append(ip)
        if ip not in allow:
            return "禁止外网访问",403
        return func(*args,**kwargs)
    return wrap

def need_login(func):
    def wrap(*args,**kwargs):
        if "user" not in session:
            return redirect("/login")
        return func(*args,**kwargs)
    return wrap

# 登录页面
@app.route("/login")
def login_html():
    global captcha_code
    captcha_code = ''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    login_tpl = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body{background:#12121c;color:#fff;font-family:Arial}
.box{width:420px;margin:80px auto;padding:28px;background:#1a1a2b;border:2px solid #ff9eb5;border-radius:16px}
.title{text-align:center;color:#ff9eb5;font-size:22px}
input{width:96%;padding:10px;margin:8px 0;background:#222338;border:1px solid #ff9eb5;color:#fff;border-radius:7px}
.capt_row{display:flex;gap:10px}
.capt_show{padding:10px;border:1px solid #ff9eb5;color:#ff9eb5;width:110px;text-align:center;border-radius:7px}
.sub{width:100%;padding:11px;background:#ff9eb5;border:none;border-radius:7px;color:#fff;font-weight:bold}
</style>
</head>
<body>
<div class="box">
<div class="title">🔥火萤机器人管理登录</div>
<form method="post">
<input name="usr" placeholder="用户名" value="FireflyDev">
<input name="pwd" placeholder="密码" type="password">
<div class="capt_row">
<input name="cap" placeholder="验证码">
<div class="capt_show">{{cap}}</div>
</div>
<button class="sub">登录</button>
</form>
</div>
</body>
</html>
'''
    return render_template_string(login_tpl,cap=captcha_code)

@app.route("/login",methods=["POST"])
def login_check():
    usr = request.form.get("usr")
    pwd = request.form.get("pwd")
    cap = request.form.get("cap","").upper()
    if cap != captcha_code:
        return '<script>alert("验证码错误");history.back()</script>'
    if usr not in USER_ACCOUNT or USER_ACCOUNT[usr]["pwd"] != pwd:
        return '<script>alert("账号或密码错误");history.back()</script>'
    session["user"] = usr
    return redirect("/")

# 主页配置面板
@app.route("/")
@limit_lan
@need_login
def index_page():
    page = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
*{box-sizing:border-box}
body{background:#111120;color:#eee}
.w{max-width:900px;margin:25px auto}
.card{background:#191930;border:2px solid #ff9eb5;border-radius:16px;padding:20px;margin-bottom:16px}
h2{color:#ff9eb5;margin:0 0 10px}
input{width:100%;padding:9px;margin:6px 0;background:#232342;border:1px solid #ff9eb5;color:#fff;border-radius:6px}
.btn{padding:9px 14px;background:#ff9eb5;border:0;border-radius:6px;margin:4px;color:#fff}
.btn_red{background:#ff5c7c}
.btngroup{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
</style>
</head>
<body>
<div class="w">
<div class="card">
<h2>⚙️ 全局配置（局域网填写保存）</h2>
<form action="/saveconfig" method="post">
<label>Discord Token</label>
<input name="dt" value="{{dt}}">
<label>Qwen API Key</label>
<input name="qt" value="{{qt}}">
<label>Tavily搜索Key</label>
<input name="tt" value="{{tt}}">
<label>米游社Cookie</label>
<input name="mt" value="{{mt}}">
<label>HoYoLab Cookie</label>
<input name="ht" value="{{ht}}">
<label>领角色ID</label>
<input name="rt" value="{{rt}}">
<label>OneBot QQ WS</label>
<input name="ot" value="{{ot}}">
<button class="btn" type="submit">保存配置</button>
</form>
</div>
<div class="card">
<h2>🎛️ 机器人控制｜运行状态：{{runstate}}</h2>
<div class="btngroup">
<a href="/startbot"><button class="btn">启动双端机器人</button></a>
<a href="/stopbot"><button class="btn btn_red">停止机器人</button></a>
<a href="/clearmem"><button class="btn">清空全量聊天记忆</button></a>
</div>
</div>
</div>
</body>
</html>
'''
    runstate = "已在线运行" if discord_bot else "未启动"
    return render_template_string(page,
        dt=bot_cfg["discord_token"],qt=bot_cfg["qwen_key"],tt=bot_cfg["tavily_key"],
        mt=bot_cfg["miyushe_cookie"],ht=bot_cfg["hoyolab_cookie"],
        rt=bot_cfg["public_role_id"],ot=bot_cfg["onebot_ws"],runstate=runstate)

# 保存配置接口
@app.route("/saveconfig",methods=["POST"])
def save_web_cfg():
    global bot_cfg
    bot_cfg["discord_token"] = request.form["dt"].strip()
    bot_cfg["qwen_key"] = request.form["qt"].strip()
    bot_cfg["tavily_key"] = request.form["tt"].strip()
    bot_cfg["miyushe_cookie"] = request.form["mt"].strip()
    bot_cfg["hoyolab_cookie"] = request.form["ht"].strip()
    bot_cfg["public_role_id"] = int(request.form["rt"]) if request.form["rt"].isdigit() else 0
    bot_cfg["onebot_ws"] = request.form["ot"].strip()
    save_config(bot_cfg)
    return '<script>alert("配置保存成功，重启机器人生效");location="/"</script>'

@app.route("/clearmem")
def clear_mem():
    user_history.clear()
    new_chat_flag.clear()
    return '<script>alert("聊天记忆全部清空");location="/"</script>'

# ==================== AI、搜索公用函数 ====================
async def tavily_search(word):
    if not bot_cfg["tavily_key"]:
        return []
    try:
        res = await aio_session.post("https://api.tavily.com/search",json={
            "api_key":bot_cfg["tavily_key"],"query":word,"max_results":3
        },timeout=20)
        data = await res.json()
        return data.get("results",[])
    except:
        return []

async def qwen_chat(question,search_data=None):
    if not bot_cfg["qwen_key"]:
        return lang_text["zh"]["no_key"]
    msg_list = [{"role":"system","content":FLY_PROMPT_ZH}]
    if search_data:
        content = f"开拓者提问：{question}\n参考搜索内容：{search_data}"
    else:
        content = f"开拓者提问：{question}"
    msg_list.append({"role":"user","content":content})
    try:
        res = await aio_session.post("https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
            headers={"Authorization":f"Bearer {bot_cfg['qwen_key']}","Content-Type":"application/json"},
            json={"model":"qwen-turbo","messages":msg_list,"temperature":0.95},timeout=25)
        js = await res.json()
        return js["choices"][0]["message"]["content"]
    except:
        return lang_text["zh"]["fail_ai"]

# ==================== Discord机器人构建 ====================
def create_discord():
    global BOT_DID
    intent = discord.Intents.all()
    bot = commands.Bot(command_prefix="!",intents=intent,help_command=None)
    slash = bot.tree
    if bot_cfg["discord_token"]:
        BOT_DID = int(bot_cfg["discord_token"].split(".")[1])

    # 领取身份按钮
    class RoleBtnView(discord.ui.View):
        def __init__(self):super().__init__(timeout=None)
        @discord.ui.button(label="🎁领取身份",style=discord.ButtonStyle.success,custom_id="getrole")
        async def getr(self,inter,btn):
            rid = bot_cfg["public_role_id"]
            if rid ==0:
                return await inter.response.send_message("未配置身份ID",ephemeral=True)
            r = inter.guild.get_role(rid)
            if not r:
                return await inter.response.send_message("身份不存在",ephemeral=True)
            if r in inter.user.roles:
                return await inter.response.send_message("已拥有该身份",ephemeral=True)
            await inter.user.add_roles(r)
            await inter.response.send_message(lang_text["zh"]["role_ok"],ephemeral=True)

    # 管理员按钮
    class AdminBtnView(discord.ui.View):
        def __init__(self):super().__init__(timeout=None)
        @discord.ui.button(label="🧹清空频道",style=discord.ButtonStyle.primary)
        async def clean(self,inter,btn):
            if not inter.user.guild_permissions.administrator:
                return await inter.response.send_message(lang_text["zh"]["no_perm"],ephemeral=True)
            await inter.channel.purge(limit=100)
            await inter.response.send_message("清理完成",ephemeral=True)

    # 斜杠指令
    @slash.command(name="ask",description="联网AI问答(流萤回复)")
    @app_commands.describe(问题="输入提问内容")
    async def cmd_ask(inter,问题:str):
        await inter.response.defer()
        sr = await tavily_search(问题)
        ans = await qwen_chat(问题,sr)
        await inter.followup.send(ans)

    @slash.command(name="search",description="全网搜索")
    @app_commands.describe(关键词="搜索内容")
    async def cmd_search(inter,关键词:str):
        await inter.response.defer()
        data = await tavily_search(关键词)
        if not data:
            return await inter.followup.send(lang_text["zh"]["no_data"])
        txt = "🔍搜索结果:\n"+"\n".join([x["content"] for x in data])[:1900]
        await inter.followup.send(txt)

    @slash.command(name="code",description="生成运行Python代码")
    @app_commands.describe(需求="描述代码功能")
    async def cmd_code(inter,需求:str):
        await inter.response.defer()
        raw = await qwen_chat(f"仅输出可运行python代码，无多余文字:{需求}",None)
        code = raw.replace("```python","").replace("```","").strip()
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):exec(code,{})
            await inter.followup.send(f"```python\n{code}\n```输出：{buf.getvalue()}")
        except Exception as e:
            await inter.followup.send(f"报错:{str(e)}")

    @slash.command(name="点歌",description="油管搜索歌曲")
    @app_commands.describe(歌名="歌曲名称")
    async def cmd_music(inter,歌名:str):
        link = f"https://www.youtube.com/results?search_query={quote(歌名)}"
        await inter.response.send_message(f"🎵点歌链接:{link}")

    @slash.command(name="bilibili",description="B站解析总结")
    @app_commands.describe(链接="B站视频链接")
    async def cmd_bili(inter,链接:str):
        await inter.response.defer()
        res = await qwen_chat(f"总结这个B站视频:{链接}",None)
        await inter.followup.send(f"📺{链接}\n内容简介:{res}")

    @slash.command(name="youtube",description="油管视频总结")
    @app_commands.describe(链接="Youtube链接")
    async def cmd_ytb(inter,链接:str):
        await inter.response.defer()
        res = await qwen_chat(f"总结:{链接}",None)
        await inter.followup.send(f"🎬{链接}\n简介:{res}")

    # 机器人上线
    @bot.event
    async def on_ready():
        global aio_session
        aio_session = aiohttp.ClientSession()
        bot.add_view(RoleBtnView())
        bot.add_view(AdminBtnView())
        await slash.sync()
        log.info("Discord流萤上线成功")
        asyncio.create_task(auto_presence(bot))

    # @机器人触发对话
    @bot.event
    async def on_message(msg):
        if msg.author.bot:return
        await bot.process_commands(msg)
        if bot.user in msg.mentions:
            async with msg.channel.typing():
                uid = msg.author.id
                cnt = msg.content.replace(f"<@{BOT_DID}>","").strip()
                if new_chat_flag.get(uid,False):
                    new_chat_flag[uid]=False
                    his=[]
                else:
                    his = user_history.get(uid,[])
                ans = await qwen_chat(cnt)
                user_history[uid].append({"user":cnt,"bot":ans})
                await msg.channel.send(ans)
    return bot

# 在线保活状态
async def auto_presence(bot):
    while bot_running_info["online"]:
        await bot.change_presence(activity=discord.Game("陪着开拓者呢~ Visual Studio Code in Workspace:FireflyGI/6_6_55.proto｛/｝Dev✨ Sleep🛏"))
        await asyncio.sleep(50)

# ==================== QQ OneBot构建 ====================
def create_qq():
    nonebot.init()
    drv = nonebot.get_driver()
    drv.register_adapter(ONEBOT_V11)
    nonebot.load_from_dict({"onebot": {"ws_url":bot_cfg["onebot_ws"]}})

    # QQ斜杠指令
    q_ask = on_command("ask")
    @q_ask.handle()
    async def qq_ask(arg=CommandArg()):
        txt = arg.extract_plain_text()
        sd = await tavily_search(txt)
        rep = await qwen_chat(txt,sd)
        await q_ask.finish(rep)

    q_search = on_command("search")
    @q_search.handle()
    async def qq_sea(arg=CommandArg()):
        txt = arg.extract_plain_text()
        res = await tavily_search(txt)
        if not res:
            return await q_search.finish(lang_text["zh"]["no_data"])
        await q_search.finish("🔍"+"\n".join([i["content"] for i in res])[:1800])

    q_code = on_command("code")
    @q_code.handle()
    async def qq_code(arg=CommandArg()):
        req = arg.extract_plain_text()
        raw = await qwen_chat(f"只输出代码:{req}",None)
        c = raw.replace("```python","").replace("```","").strip()
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):exec(c,{})
            await q_code.finish(f"```\n{c}\n输出:{out.getvalue()}")
        except Exception as e:
            await q_code.finish(f"错误:{e}")

    q_music = on_command("点歌")
    @q_music.handle()
    async def qq_mus(arg=CommandArg()):
        name = arg.extract_plain_text()
        url = f"https://www.youtube.com/results?search_query={quote(name)}"
        await q_music.finish(f"🎵点歌：{url}")

    q_bili = on_command("bilibili")
    @q_bili.handle()
    async def qq_bili(arg=CommandArg()):
        link = arg.extract_plain_text()
        res = await qwen_chat(f"总结{link}",None)
        await q_bili.finish(f"{link}\n简介:{res}")

    # QQ@聊天 + 短视频解析
    q_msg = on_message(priority=5)
    @q_msg.handle()
    async def qq_chat(event):
        raw = event.get_plaintext().strip()
        # 视频解析
        vl = VIDEO_REG.search(raw)
        if vl:
            await q_msg.finish("链接解析：自行打开原视频，无水印接口受限")
        # @机器人
        if event.is_to_me():
            uid = event.user_id
            if new_chat_flag.get(uid):
                new_chat_flag[uid]=False
                his=[]
            else:
                his=user_history.get(uid,[])
            ans = await qwen_chat(raw)
            user_history[uid].append({"user":raw,"bot":ans})
            await q_msg.finish(ans)
    return nonebot

# ==================== 启停接口 ====================
@app.route("/startbot")
def start_all():
    global discord_bot
    tk = bot_cfg["discord_token"].strip()
    if not tk:
        return '<script>alert("先在后台填写Discord Token！");location="/"</script>'
    if discord_bot:
        return '<script>alert("机器人已在运行");location="/"</script>'
    # 子线程启动机器人
    def run_task():
        global discord_bot
        discord_bot = create_discord()
        qq_app = create_qq()
        nonebot.run(app="nonebot")
        discord_bot.run(tk)
    threading.Thread(target=run_task,daemon=True).start()
    return '<script>alert("后台启动成功！");location="/"</script>'

@app.route("/stopbot")
def stop_all():
    global discord_bot
    if discord_bot and not discord_bot.is_closed():
        asyncio.run_coroutine_threadsafe(discord_bot.close(),discord_bot.loop)
    discord_bot = None
    return '<script>alert("机器人已停止");location="/"</script>'

# ==================== 启动入口：0.0.0.0=全局域网开放 ====================
if __name__ == "__main__":
    # Flask监听0.0.0.0，局域网所有IP可访问
    threading.Thread(target=lambda:app.run(host="0.0.0.0",port=PORT,debug=False,use_reloader=False),daemon=True).start()
    print(f"\n✅ 管理后台地址：本机 http://127.0.0.1:{PORT}")
    print(f"✅ 局域网访问：电脑内网IP:{PORT}（手机连同WiFi打开）")
    while True:
        time.sleep(9999)
