# coding:utf-8
from bs4 import BeautifulSoup as B
import requests as r
import json
import threading as tr
import time
timeS=time.time()
def onlyText(ssrc,ignoreTag):
    return "".join([text.strip() for text in ssrc(text=True) if text.parent.name !=ignoreTag and text.strip()])

def getMsg(BOBJ):
    li_raw=BOBJ("div",attrs={"class":"list list_preferential"})
    for li_single in li_raw:
        infos.append(
            {
                "link":li_single.find("a",attrs={"class":"picLeft"})["href"],
                "normalTitle":onlyText(li_single.find("h3",attrs={"class":"itemName"}).a,"span"),
                "redTitle":li_single.find("h3",attrs={"class":"itemName"}).a.span.get_text(),
                "info":"".join([j.strip() for j in li_single.find("div",attrs={"class":"lrInfo"})(text=True) if j.strip() and j!="阅读全文"])
            }
        )

def updateTodo(BOBJ):
    tdl=BOBJ.find("ul",attrs={"class":"pagination"})("li")
    for i in tdl:
        try:
            if i.a["href"] not in todoList and i.a["href"] not in visited:
                todoList.append(i.a["href"])
        except TypeError:
            pass
        except Exception as e:
            print(e)

def nowtask(nowlnk):
    taskList.append(nowlnk)
    ss=B(ses.get(nowlnk).text,"html.parser")
    updateTodo(ss)
    getMsg(ss)
    taskList.remove(nowlnk)

ses=r.session()
ses.headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"__ckguid=yXa2pi61v2BBVp32Fkhh2NJ6; device_id=191204048515671745044839662526fd55df59161fca8e769dbf196060; __jsluid_s=e085a9f43d816a5225881cbbc1230aef; homepage_sug=g; r_sort_type=score; _zdmA.uid=ZDMA.gZsKwfV0J.1569457714.2419200; _zdmA.vid=*; PHPSESSID=8d5d18d656dc62a513b77098f4347b81; ad_date=26; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%22J_feed_ad1%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%22J_feed_ad3%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%22J_feed_ad4%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%7D; _zdmA.time=1569457717278.1472.https%3A%2F%2Fwww.smzdm.com%2F; smzdm_user_view=2AB7DD871F92C09C7772D4F1A36BD23E; smzdm_user_source=F780F04B8A832B0A97F5416911DED571",
    "Host":"www.smzdm.com",
    "Referer":"https://www.smzdm.com/tag/%E6%AF%8F%E5%A4%A9%E5%88%B7%E4%BB%80%E4%B9%88/youhui/",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

todoList=[]
taskList=[]
infos=[]

lnkPrefix="https:"
lnk="https://www.smzdm.com/tag/%E6%AF%8F%E5%A4%A9%E5%88%B7%E4%BB%80%E4%B9%88/youhui/"
visited=[lnk]

rp=ses.get(lnk)
s=B(rp.text,"html.parser")

updateTodo(s)
getMsg(s)

while len(todoList)!=0 or len(taskList)!=0:
    if len(todoList)==0:
        pass
    else:
        visited.append(todoList.pop())
        lnk=lnkPrefix+visited[-1]
        #print("Getting %s"%lnk)
        tr.Thread(target=nowtask,args=(lnk,)).start()
        

with open("DumpResource2.txt","w") as f:
    f.write(json.dumps(infos))
print(time.time()-timeS)