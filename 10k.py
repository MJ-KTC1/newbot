# ~~~~~~~ ─•۞✟ℓℓஆՁゆຸ۞•─ ~~~~~~#
# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()
#line = LINE("เมล","พาส")
line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))


ki1 = LINE('')
ki1.log("Auth Token : " + str(ki1.authToken))
ki1.log("Timeline Token : " + str(ki.tl.channelAccessToken))

ki2 = LINE('')
ki2.log("Auth Token : " + str(ki2.authToken))
ki2.log("Timeline Token : " + str(kk.tl.channelAccessToken))

ki3 = LINE('')
ki3.log("Auth Token : " + str(ki3.authToken))
ki3.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ki4 = LINE('')
ki4.log("Auth Token : " + str(ki4.authToken))
ki4.log("Timeline Token : " + str(ke.tl.channelAccessToken))


ki5 = LINE('')
ki5.log("Auth Token : " + str(ki5.authToken))
ki5.log("Timeline Token : " + str(ki.tl.channelAccessToken))

ki6 = LINE('')
ki6.log("Auth Token : " + str(ki6.authToken))
ki6.log("Timeline Token : " + str(kk.tl.channelAccessToken))

ki7 = LINE('')
ki7.log("Auth Token : " + str(ki7.authToken))
ki7.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ki8 = LINE('')
ki8.log("Auth Token : " + str(ki8.authToken))
ki8.log("Timeline Token : " + str(ke.tl.channelAccessToken))


ki9 = LINE('')
ki9.log("Auth Token : " + str(ki9.authToken))
ki9.log("Timeline Token : " + str(ki.tl.channelAccessToken))

ki9 = LINE('')
ki9.log("Auth Token : " + str(ki9.authToken))
ki9.log("Timeline Token : " + str(kk.tl.channelAccessToken))

ki10 = LINE('')
ki10.log("Auth Token : " + str(ki10.authToken))
ki10.log("Timeline Token : " + str(kc.tl.channelAccessToken))


print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

ki1MID = ki1.profile.mid
ki1Profile = ki1.getProfile()
ki1Settings = ki1.getSettings()

ki2MID = ki2.profile.mid
ki2Profile = ki2.getProfile()
ki2Settings = ki2.getSettings()

ki3MID = ki3.profile.mid
ki3Profile = ki3.getProfile()
ki3Settings = ki3.getSettings()

ki4MID = ki4.profile.mid
ki4Profile = ki4.getProfile()
ki4Settings = ki4.getSettings()

ki5MID = ki5.profile.mid
ki5Profile = ki5.getProfile()
ki5Settings = ki5.getSettings()

ki6MID = ki6.profile.mid
ki6Profile = ki6.getProfile()
ki6Settings = ki6.getSettings()

ki7MID = ki7.profile.mid
ki7Profile = ki7.getProfile()
ki7Settings = ki7.getSettings()

ki8MID = ki8.profile.mid
ki8Profile = ki8.getProfile()
ki8Settings = ki8.getSettings()

ki9MID = ki9.profile.mid
ki9Profile = ki9.getProfile()
ki9Settings = ki9.getSettings()

ki10MID = ki10.profile.mid
ki10Profile = ki10.getProfile()
ki10Settings = ki10.getSettings()


oepoll = OEPoll(ki10)
oepoll = OEPoll(ki9)
oepoll = OEPoll(ki8)
oepoll = OEPoll(ki7)
oepoll = OEPoll(ki6)
oepoll = OEPoll(ki5)
oepoll = OEPoll(ki4)
oepoll = OEPoll(ki3)
oepoll = OEPoll(ki2)
oepoll = OEPoll(ki1)
oepoll = OEPoll(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
lineMID = line.getProfile().mid
kiMID = ki1.getProfile().mid
kkMID = ki2.getProfile().mid
kcMID = ki3.getProfile().mid
kcMID = ki4.getProfile().mid
kiMID = ki5.getProfile().mid
kkMID = ki6.getProfile().mid
kcMID = ki7.getProfile().mid
kcMID = ki8.getProfile().mid
kiMID = ki9.getProfile().mid
kkMID = ki10.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID,ki1MID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID]
RfuBot=[lineMID]
Family=["u8f4b03bd2f026a30dbff351d5a08dfc3",lineMID]
admin=['u8f4b03bd2f026a30dbff351d5a08dfc3',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#~~~~~~~~~~~~~~~~~~[─•۞✟ℓℓஆՁゆຸ۞•─]~~~~~~~~~~~~~~~~#
settings = {
    "autoAdd": False,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":3},	
    "autoLeave": True,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "gift":False,
    "likeOn":False,
    "timeline":False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture":False,
    "changePictureProfile":False,
    "welcome":"🙏สวีสดีครับคนมาใหม่🙏",
    "kick":"😱อุ๊ต๊ะ😱",
    "bye":"🙌บาย..",
    "Respontag":"😳",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message1":"🕸✟ℓຫຼี้छゆຸ۞🕸 \n🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭\nselfbotฟรี\nติดต่อขอลงทะเบียนที่\n@ไลน์ http://line.me/ti/p/t39FP9K59s \nselfbot by:\n╔══════════════┓\n╠™NUNU_KAP \n╚══════════════┛",
    "message":"บัญชีนี้ถูกป้องกันโดย Selfbot By ™🕸✟ℓຫຼี้छゆຸ۞🕸 ระบบได้ทำการบล็อคคุณอัตโนมัติเนื่องจากคุณยังไม่ได้ยืนยันตัวตนกับผู้สร้างบอท\nสามารถยืนตัวตนได้ง่ายโดยการพิม unblockกับ™SUSU_KAPระบบจะทำการปลดบล็อคท่านโดยอัตโนมัต",
    
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]
fukgerMessage = [".ควย",".หี",".แตด",".เย็ดแม่","เย็ดเข้","ค.วย",".สัส",".เหี้ย",".ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้นุ","ไอ้เหี้ยนุ","ไอ่นุ","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#~~~~~~~~~~~~~~~~~(─•۞✟ℓℓஆՁゆຸ۞•─)~~~~~~~~~~~~~~~~~~~~~~~~~~~#
