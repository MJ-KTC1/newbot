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
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
#~~~~~~~~~~~~~~~~~~~~♡─•۞✟ℓℓஆՁゆຸ۞•─~~~~~~~~~~~~~~~~~~#
def myhelp():
    myHelp = """╔══════════════┓
╠─┅🕸✟ℓຫຼี้छゆຸ۞🕸
╚══════════════┛
 ────┅═ই۝ई═┅────
             คำสั่งทั่วไป
 ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ เช็ค
╠❂➣ ผส
╠❂➣ ข้อมูล
╠❂➣ ข้อมูล @
╠❂➣ Help1
╠❂➣ Help2
╠❂➣ Help3
╠❂➣ Help4
╠❂➣ Help5
╠❂➣ Help6
╠❂➣ ไอดี @
╠❂➣ ชื่อ @
╠❂➣ ตัส @
╠❂➣ รูป @
╠❂➣ ปก @
╠❂➣ คท @
╠❂➣ วีดีโอ @
╠❂➣ ไอดีล่อง
╠❂➣ คทล่อง
╠❂➣ แทคล่อง
╠❂➣ ปฏิทิน
╠❂➣ Mimic on/off
╠❂➣ MimicList
╠❂➣ MimicAdd
╠❂➣ MimicDel
╠❂➣ ส่งเสียงกลุ่ม
╠❂➣ ส่งเสียงแชท
╠❂➣ เริ่มใหม่
╠❂➣ เวลออน
╠❂➣ แอด เชิญแอด
╠❂➣ ชื่อกลุ่ม                                                           
╠❂➣ ไอดีกลุ่ม                                                          
╠❂➣ เปิดลิ้ง
╠❂➣ ปิดลิ้ง                                                            
╠❂➣ ลิ้ง                                                              
╠❂➣ ลิ้งกลุ่ม                                                           
╠❂➣ รายการกลุ่ม 
╠❂➣ ข้อมูลกลุ่ม 
╠❂➣ รูปกลุ่ม 
╠❂➣ แจ๊ะ 
╠❂➣ จับ
╠❂➣ ไอดีล่อง                                                                                                                                                                        
╠❂➣ เลิกจับ
╠❂➣ จับใหม่
╠❂➣ เช็คไอดี  
╠❂➣ อ่าน
╠❂➣ ไอดีล่อง
╠❂➣ คทล่อง 
╠❂➣ แทคล่อง
╠❂➣ เปิดแสกน/ปิดแสกน
╠❂➣ เปิดรับแขก/ปิดรับแขก
╠❂➣ เปิดส่งแขก/ปิดส่งแขก
╠❂➣ เปิดทักเตะ/ปิดทักเตะ
╠❂➣ เช็คดำ
╠❂➣ ลงดำ
╠❂➣ ล้างดำ
╠❂➣ ไล่ดำ
╠❂➣ ปวดตัป
╠❂➣ ไอจี [ชื่อยูส]ภาพซเชลมีเดี่ย
╠❂➣ รปภาพ [ชอรปภาพ]
╠❂➣ Lyric
╠❂➣ ScreenshootWebsite
╠❂➣ หนัง [ชื่อหนัง]
╠❂➣ วีดีโอ [ชื่อวีดีโอ]                                                   
╠❂➣ รูปการ์ตูน [ชื่อรูป]site                                              
╠❂➣ ไอจี [ชื่อยูส]]
╠❂➣ Urban
╠❂➣ กูเกิ้ล [ข้อความ]
╔══════════════┓
╠❂➣ คท /เช็คคทเรา
╠❂➣ ไอดี/ไอดีเรา
╠❂➣ ชื่อ/ดูชื่อเรา                                                             
╠❂➣ ตัส /ดูตัสเรา                                                             
╠❂➣ รูปโปร /ดูรูปโปรเรา 
╠❂➣ รูปปก/ดูปกเรา
╠❂➣ วัดรอบ/เช็คความไว
╠❂➣ Sp /เช็คความไว 
╠❂➣ คอมเม้น  
╠❂➣ ข้อความแทค                                                       
╠❂➣ ข้อความแอด  
╠❂➣ ชื่อ: 
╠❂➣ ตัส: /ตั้งตัสเรา 
╠❂➣ ทักเข้า: ตั้งข้อความคนเข้า
╠❂➣ ทักออก: /ตั้งข้อความคนออก
╠❂➣ ทักเตะ: /ตั้งคนเตะ
╠❂➣ ตั้งแอด: /ตั้งข้อความคนแอดมา
╠❂➣ คอมเม้น: /ตั้งคอมเม้น
╠❂➣ เวลออน /ดูเวลาบอทใช้งาน
╠❂➣ แบน @
╠❂➣ ลบแบน @
╠❂➣ ลบรัน/ลบห้องรัน
╠❂➣ ดึง
╠❂➣ หวด @ /สั่งเตะคนปากดี
╠❂➣ สอย @
╠❂➣ ลาก่อย @
╠❂➣ ปลิว @สั่งเตะคน
╠❂➣ เพื่อน
╠❂➣ ไอดีเพื่อน/เอาไอดีเพื่อน
╠❂➣ Gcancel:(จำนวนสมาชิก)
╔══════════════
╠❂➣ เปิดกัน/ปิดกัน
╠❂➣ กันยก/ปิดกันยก
╠❂➣ กันเชิญ/ปิดกันเชิญ
╠❂➣ กันลิ้ง/ปิดกันลิ้ง
╠❂➣ กันเข้า/ปิดกันเข้า
╠❂➣ เปิดหมด/ปิดหมด
╠❂➣ เปิดเข้า/ปิดเข้
╠❂➣ เปิดออก/ปิดออก                                                    
╠❂➣ เปิดติ๊ก/ปิดติ๊ก                                                      
╠❂➣ เปิดบล็อค/ปิดบล็อค                                                  
╠❂➣ เปิดอ่าน/ปิดอ่าน
╠❂➣ เปิดแทค/ปิดแทค
╠❂➣ เปิดแทค2/ปิดแทค2
╠❂➣ เปิดแทคเจ็บ/ปิดแทคเจ็บ
╠❂➣ เปิดติ๊ก/ปิดติ๊ก
╠❂➣ เปิดแสกน/ปิดแสกน
╠❂➣ เปิดรับแขก/ปิดรับแขก
╠❂➣ เปิดส่งแขก/ปิดส่งแขก
╠❂➣ เปิดทักเตะ/ปิดทักเตะ
╠❂➣ ปฏิทิน 
╔┅ 🕸✟ℓຫຼี้छゆຸ۞🕸                                                            
╠❂➣ รปภาพ [ชอรปภาพ]                                                
╠❂➣ คนหารปภาพ [ชอรปภาพ]                                             
╠❂➣ ยทป [ขอความ]
╠❂➣ เพลง [ชอเพลง]
╠❂➣ Lyric
╠❂➣ ScreenshootWebsite
╠❂➣ หนัง [ชื่อหนัง]
╠❂➣ วีดีโอ [ชื่อวีดีโอ]
╠❂➣ รูปการ์ตูน [ชื่อรูป]
╠❂➣ ไอจี [ชื่อยูส]
╠❂➣ Urban
╠❂➣ กูเกิ้ล [ข้อความ]
╠❂➣ องครักษ์
╠❂➣ เช็คชื่อ
╠❂➣ ชื่อคิก:
╠❂➣ ตัสคิก:
╠❂➣ 1-3หวด
╠❂➣ 1-3กลุ่ม
╠❂➣ ลบรัน
╠❂➣ ลบรันคิก
╠❂➣ Pz:gac +66+เบอร์โทร                                             
╠❂➣ ไล่ดำ                                                            
╠❂➣ ปวดตับ                                                           
╠❂➣ ถอนกำลัง                                                         
╠❂➣ ออกทุกกลุ่ม                                                        
╠❂➣ sayonara                                                        
╠❂➣ ลบแชท                                                           
╠❂➣ ลบแชทคิก
╰═─┅🕸✟ℓຫຼี้छゆຸ۞🕸

 *หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งเวลาใช้ด้วยเด้อ"""

    return myHelp

def listgrup():
    listGrup = """╔══════════════┓
╠™🕸✟ℓຫຼี้छゆຸ۞🕸
╚══════════════┛
 ────┅═ই۝ई═┅────
             คำสั่งในกลุ่ม
 ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ แอด เชิญแอด
╠❂➣ ชื่อกลุ่ม
╠❂➣ ไอดีกลุ่ม
╠❂➣ เปิดลิ้ง
╠❂➣ ปิดลิ้ง
╠❂➣ ลิ้ง
╠❂➣ ลิ้งกลุ่ม
╠❂➣ รายการกลุ่ม
╠❂➣ สมาชิกกลุ่ม
╠❂➣ ข้อมูลกลุ่ม
╠❂➣ รูปกลุ่ม
╠❂➣ แจ๊ะ
╠❂➣ เช็คไอดี
╠❂➣ ไอดีล่อง
╠❂➣ คทล่อง
╠❂➣ แทคล่อง
╠❂➣ จับ
╠❂➣ เลิกจับ
╠❂➣ จับใหม่
╠❂➣ อ่าน
╠❂➣ เปิดแสกน/ปิดแสกน
╠❂➣ เปิดรับแขก/ปิดรับแขก
╠❂➣ เปิดส่งแขก/ปิดส่งแขก
╠❂➣ เปิดทักเตะ/ปิดทักเตะ
╠❂➣ เช็คดำ
╠❂➣ ลงดำ
╠❂➣ ล้างดำ
╠❂➣ ไล่ดำ
╠❂➣ ปวดตัป
╰═✰™🕸✟ℓຫຼี้छゆຸ۞🕸"""
    return listGrup

def helpset():
    helpSet = """╔══════════════┓
╠™🕸✟ℓຫຼี้छゆຸ۞🕸
╚══════════════┛
  ────┅═ই۝ई═┅────
           คำสั่งเซลบอท
  ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ โย่ว
╠❂➣ ไอดี
╠❂➣ ชื่อ
╠❂➣ ตัส
╠❂➣ รูปโปร
╠❂➣ รูปปก
╠❂➣ วัดรอบ
╠❂➣ Sp
╠❂➣ ทักเข้า
╠❂➣ ทักออก
╠❂➣ ทักเตะ
╠❂➣ คอมเม้น
╠❂➣ ข้อความแทค
╠❂➣ ข้อความแอด
╠❂➣ ชื่อ:
╠❂➣ ตัส:
╠❂➣ ทักเข้า:
╠❂➣ ทักออก:
╠❂➣ ทักเตะ:
╠❂➣ ตั้งแทค:
╠❂➣ ตั้งแอด:
╠❂➣ คอมเม้น:
╠❂➣ เวลออน
╠❂➣ แบน @
╠❂➣ ลบแบน @
╠❂➣ ลบรัน
╠❂➣ ดึง
╠❂➣ หวด @
╠❂➣ สอย @
╠❂➣ ลาก่อย @
╠❂➣ ปลิว @
╠❂➣ เพื่อน
╠❂➣ ไอดีเพื่อน
╠❂➣ Gcancel:(จำนวนสมาชิก)
╰═✰™🕸✟ℓຫຼี้छゆຸ۞🕸"""
    return helpSet

def helpsetting():
    helpSetting = """╔══════════════┓
╠™🕸✟ℓຫຼี้छゆຸ۞🕸
╚══════════════┛
 ────┅═ই۝ई═┅────
         คำสั่งการตั้งค่า
 ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ เปิดกัน/ปิดกัน
╠❂➣ กันยก/ปิดกันยก
╠❂➣ กันเชิญ/ปิดกันเชิญ
╠❂➣ กันลิ้ง/ปิดกันลิ้ง
╠❂➣ กันเข้า/ปิดกันเข้า
╠❂➣ เปิดหมด/ปิดหมด
╠❂➣ เปิดเข้า/ปิดเข้า
╠❂➣ เปิดออก/ปิดออก
╠❂➣ เปิดติ๊ก/ปิดติ๊ก
╠❂➣ เปิดบล็อค/ปิดบล็อค
╠❂➣ เปิดอ่าน/ปิดอ่าน
╠❂➣ เปิดแทค/ปิดแทค
╠❂➣ เปิดแทค2/ปิดแทค2
╠❂➣ เปิดแทคเจ็บ/ปิดแทคเจ็บ
╠❂➣ เปิดติ๊ก/ปิดติ๊ก
╠❂➣ เปิดแสกน/ปิดแสกน
╠❂➣ เปิดรับแขก/ปิดรับแขก
╠❂➣ เปิดส่งแขก/ปิดส่งแขก
╠❂➣ เปิดทักเตะ/ปิดทักเตะ
╰══™🕸✟ℓຫຼี้छゆຸ۞🕸"""
    return helpSetting

def helpkicker():
    helpKickker = """╔══════════════┓
╠™🕸✟ℓຫຼี้छゆຸ۞🕸
╚══════════════┛
  ────┅═ই۝ई═┅────
           คำสั่งคิกเกอร์
  ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ องครักษ์
╠❂➣ เช็คชื่อ
╠❂➣ ชื่อคิก:
╠❂➣ ตัสคิก:
╠❂➣ 1-3หวด
╠❂➣ 1-3กลุ่ม
╠❂➣ ลบรัน
╠❂➣ ลบรันคิก
╠❂➣ Pz:gac +66+เบอร์โทร
╠❂➣ ไล่ดำ
╠❂➣ ปวดตับ
╠❂➣ ถอนกำลัง
╠❂➣ ออกทุกกลุ่ม
╠❂➣ sayonara
╠❂➣ ลบแชท
╠❂➣ ลบแชทคิก
╰═✰™🕸✟ℓຫຼี้छゆຸ۞🕸"""
    return helpKickker
#~~~~~~~~~~~~~~~~~~~~เขียนโดย[─•۞✟ℓℓஆՁゆຸ۞•─]~~~~~~~~~~~~~~~#
