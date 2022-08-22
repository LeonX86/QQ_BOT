import requests
import json
from nonebot import on_keyword

from nonebot.adapters.onebot.v11 import  Bot,MessageEvent,Message



def remove_upprintable_chars(s):
    return ''.join(x for x in s if x.isprintable())#去除不可见字符

pic=on_keyword({'今日事','jinrishi'})
@pic.handle()
async def _(bot:Bot,event: MessageEvent):#MessageEvent可以使用CQ发图片
    msg = await suijitu()
    try:
        await bot.send(
            event=event,
            message=Message(msg))
    except :
        await bot.send(event=event,
                       message="error")
async def suijitu():
    try:
        url="https://api.iyk0.com/60s"
        resp = requests.get(url)
        resp = resp.text
        resp = remove_upprintable_chars(resp)
        retdata = json.loads(resp)
        lst = retdata['imageUrl']
        pic_ti = f"今日60S读世界已送达\n[CQ:image,file={lst}]"
        return pic_ti
    except:
        url = "https://api.2xb.cn/zaob"#备用网址
        resp = requests.get(url)
        resp = resp.text
        resp = remove_upprintable_chars(resp)
        retdata = json.loads(resp)
        lst = retdata['imageUrl']
        pic_ti1 = f"今日60S读世界已送达\n[CQ:image,file={lst}]"
        return pic_ti1
