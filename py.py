# -*- ─•۞✟ℓℓஆՁゆຸ۞•─ -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,base64,antolib,subprocess,unicodedata,GACSender
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
from multiprocessing import Pool, Process
from googletrans import Translator

#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()
#line = LINE("เมล","พาส")
line = LINE('sunu0734@gmail.com','sunu2018')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))


ki1 = LINE('nunu4844@gmail.com','sunu2018')
ki1.log("Auth Token : " + str(ki1.authToken))
ki1.log("Timeline Token : " + str(ki1.tl.channelAccessToken))

ki2 = LINE('su3nu2018@gmail.com','sunu2018')
ki2.log("Auth Token : " + str(ki2.authToken))
ki2.log("Timeline Token : " + str(ki2.tl.channelAccessToken))

ki3 = LINE('su2nu2018@gmail.com','sunu2018')
ki3.log("Auth Token : " + str(ki3.authToken))
ki3.log("Timeline Token : " + str(ki3.tl.channelAccessToken))

ki4 = LINE('su6nu2018@gmail.com','sunu2018')
ki4.log("Auth Token : " + str(ki4.authToken))
ki4.log("Timeline Token : " + str(ki4.tl.channelAccessToken))


ki5 = LINE('su15nu2018@gmail.com','sunu2018')
ki5.log("Auth Token : " + str(ki5.authToken))
ki5.log("Timeline Token : " + str(ki5.tl.channelAccessToken))

ki6 = LINE('su5nu2018@gmail.com','sunu2018')
ki6.log("Auth Token : " + str(ki6.authToken))
ki6.log("Timeline Token : " + str(ki6.tl.channelAccessToken))

ki7 = LINE('su12nu2p18@gmail.com','sunu2018')
ki7.log("Auth Token : " + str(ki7.authToken))
ki7.log("Timeline Token : " + str(ki7.tl.channelAccessToken))

ki8 = LINE('nu6bot2018@gmail.com','sunu2018')
ki8.log("Auth Token : " + str(ki8.authToken))
ki8.log("Timeline Token : " + str(ki8.tl.channelAccessToken))


ki9 = LINE('su4nu2018@gmail.com','sunu2018')
ki9.log("Auth Token : " + str(ki9.authToken))
ki9.log("Timeline Token : " + str(ki9.tl.channelAccessToken))


ki10 = LINE('su7nu2018@gmail.com','sunu2018')
ki10.log("Auth Token : " + str(ki10.authToken))
ki10.log("Timeline Token : " + str(ki10.tl.channelAccessToken))


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
Rfu = [line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
Exc = [ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
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
Family=["ud3a6bfda60a956cca0f58f2a14bae808",lineMID,ki1MID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID,]
admin=['ud3a6bfda60a956cca0f58f2a14bae808',lineMID]
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
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":5},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "contact": False,
    "kiebot": True, 
    "potoMention": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "KIEBOT1":"\n[เฮโหลๆๆๆ 😚มาใหม่แก้ผ้าน่ะเเจ๊ะ ไหนๆเอา หำกะหอยมาเบิ่งติ่ละ ❣ ]",
    "KIEBOT2":"\n[เอ้า ! ไปละติ่ บักปอบ บ๊ายยยยย 🖑]",
    "tag1":"\n[แทคทำมัย !!นัดเยสเลยมั้ยเตง ^^ โวโวเยเย 😛]",
    "tag2":"\n[แทคทำมัย ? นัดเยสเลยมั้ยเตง ^^ โวโวเยเย 😛]",
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": True,
    "cName":"",
    "cNames":"",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"คุณไม่สามารถเพิ่มเพื่อนได้/nเนื่องจากคุณไม่ได้รับอนุญาติจาก ─•۞✟ℓℓஆՁՃิ۞•─ /nขอบคุณที่แอดมา (◡‿◡✿)\n •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•\n::: (\_(\ …*…*…*…*…*…*…*…*…::::::::::::::\n*: (=’ :’) :: ออโต้บล็อค  นะจ๊ะ! :::::::::::::::::::::\n•.. (,(”)(”)¤…*…*…*…*…*…*…*…*…:::::::::::\n¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸",
    "comment":"(◡‿◡✿)@ID.LINE [http://line.me/ti/p/p2nGSe0XoX] ",
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
    "protect": True,
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
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน","เตะ","อีชิ","อิชิ"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
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
    line.log("[ ─•۞✟ℓℓஆՁゆຸ۞•─ ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

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
 
def myhelp():
    myHelp = "✰「  SELFBOT 🌸ℓຫຼี้छՃิ🌸  」✰   " + "\n" \
                  "🍭「บัญชี」" + "\n" + \
                  "🍭「คำสั่ง1-5」วิทีใช้งานมี5คำสั่ง" + "\n" + \
                  "🍭「Languange」" + "\n" + \
                  "🍭「ผู้สร้าง」[บุคคลเขียนบอท]" + "\n" + \
                  "🍭「คท」[คทเราเอง]" + "\n" + \
                  "🍭「มิส」[MIDเรา]" + "\n" + \
                  "🍭「ชื่อ」[ชื่อเรา]" + "\n" + \
                  "🍭「ตัส」[ตัสเรา]" + "\n" + \
                  "🍭「ดิส」[ดิสเรา]" + "\n" + \
                  "🍭「ปก」[ปกเรา]" + "\n" + \
                  "🍭「วีดีโอ」[วีดีโอเรา]" + "\n" + \
                  "🍭「มิส @」[MIDเพื่อน]" + "\n" + \
                  "🍭「ชื่อ @」[ชื่อเพื่อน]" + "\n" + \
                  "🍭「ตัส @」[ตัสเพื่อน]" + "\n" + \
                  "🍭「ดิส @」[ดิสเพื่อน]" + "\n" + \
                  "🍭「ปก @」[ปกเพื่อน]" + "\n" + \
                  "🍭「วีดีโอ @」[วีดีโอเพื่อน]" + "\n" + \
                  "🍭「Copy」" + "\n" + \
                  "🍭「Restore」" + "\n" + \
                  "🍭「Mimic on/off」" + "\n" + \
                  "🍭「MimicList」" + "\n" + \
                  "🍭「MimicAdd」" + "\n" + \
                  "🍭「MimicDel」" + "\n" + \
                  "🍭「Broadcastvoice」" + "\n" + \
                  "🍭「Cbroadcastvoice」" + "\n" + \
                  "🍭「Tag1」" + "\n"\
                  "🍭「Tag2」" + "\n"\
                  "🍭「speed」[เช็คความไวบอท]" + "\n"\
                  "🍭「sp」[เช็คความไวบอท]" + "\n"\
                  "🍭「ล่องหน」[ค้นหาคนไส่กันแทค]" + "\n"\
                  "🍭「จัด @」[เตะโดยแอดชื่อ]" + "\n"\
                  "🍭「รีบอท」" + "\n" + \
                  "🍭「ออน」" + "\n" + \
                  "🍭「แอด」[แอดนิ้นกลุ่ม]" + "\n" + \
                  "🍭「ไอดีกลุ่ม」" + "\n" + \
                  "🍭「ชื่อกลุ่ม」" + "\n" + \
                  "🍭「รูปกลุ่ม」" + "\n" + \
                  "🍭「บันชีกลุ่ม」" + "\n" + \
                  "🍭「GroupMemberList」" + "\n" + \
                  "🍭「กลุ่มทั้งหมด」[กลุ่มทั้งหมดที่เรามี]" + "\n" + \
                  "🍭「ลิ้ง」[ขอลิ้งกลุ่ม]" + "\n" + \
                  "🍭「ลิ้งเปิด/ปิด」[เปิดปิดลิ้ง]" + "\n" + \
                  "🍭「เปิดลิ้ง」[ขอลิ้งกลุ่ม]" + "\n" + \
                  "🍭「เพื่อน」" + "\n" + \
                  "🍭「รายการบล็อค」" + "\n" + \
                  "🍭「เพื่อน mid」" + "\n" + \
                  "🍭「Invite:gcreator」" + "\n" + \
                  "🍭「Spam on/off」" + "\n" + \
                  "🍭「Reject inv」" + "\n" + \
                  "🍭「Allban」" + "\n" + \
                  "🍭「กลุ่มทั้งหมด」" + "\n" + \
                  "🍭「เชคดำ」" + "\n" + \
                  "🍭「แทค」" + "\n" + \
                  "🍭「1แทค」" + "\n" + \
                  "🍭「Lurking on」" + "\n" + \
                  "🍭「Lurking off」" + "\n" + \
                  "🍭「Lurking reset」" + "\n" + \
                  "🍭「Lurking」" + "\n" + \
                  "🍭「Invite」" + "\n" + \
                  "🍭「uninstall」" + "\n" + \
                  "🍭「Kick」" + "\n" + \
                  "🍭「ดำ」" + "\n" + \
                  "🍭[ขาว]" + "\n" + \
                  "🍭「ล้างดำ」[แก้ไขคนที่ติดบันชีดำ]" + "\n" + \
                  "🍭「Instagram」" + "\n" + \
                  "🍭「Fotoig」" + "\n" + \
                  "🍭「ยูทูป」" + "\n" + \
                  "🍭「Music」" + "\n" + \
                  "🍭「Lyric」" + "\n" + \
                  "🍭「ScreenshootWebsite」" + "\n" + \
                  "🍭「Film:」" + "\n" + \
                  "🍭「Kalender」" + "\n" + \
                  "🍭「CheckDate」" + "\n" + \
                  "🍭「Textig」" + "\n" + \
                  "🍭「Wikipedia」" + "\n" + \
                  "🍭「Urban」" + "\n" + \
                  "🍭「Anime」" + "\n" + \
                  "🍭「รูป」" + "\n" + \
                  "🍭「Pornhub」" + "\n" + \
                  "🍭[.bye @][ลบสมาชิคออกจากกลุ่ม]" + "\n" + \
                  "🍭[ข้อมูล @][ขอมูลเพื่อน]" + "\n" + \
                  "🍭[Spam on ][]" + "\n" + \
                  "🍭「Set」[เช็คการตั้งค่าบอท]" + "\n" + \
                  "🍭「ก็อปปี้ @」[ก็อปปี้ไลน์คนอื่น]" + "\n" + \
                  "🍭「เลิกก็อปปี้」[กลับคืนค่าปกติ]" + "\n" + \
                  "🍭「รายงาน」[เช็คบอท]" + "\n" + \
                  "🍭「บอท」[เชคบอท]" + "\n" + \
                  "🍭「ดิสกู」ดิสเรา" + "\n" + \
                  "🍭「ชื่อใหม่: 」ชื่อเรา" + "\n" + \
                  "🍭「ตัสใหม่: 」ตัสเรา" + "\n" + \
                  "🍭「ตัสคิก: 」ตัสคิกทั้งหมด" + "\n" + \
                  "🍭「ชื่อคิก: 」ชื่อคิกทั้งหมด" + "\n" + \
                  "🍭「ดิสคิก1-10」ดิสคิกทั้งหมด" + "\n" + \
                  "🍭「ดิสกลุ่ม」เปลี่ยนรูปกลุ่ม" + "\n" + \
                  "🍭「ลบรัน」[ลบรันเรา]" + "\n" + \
                  "🍭「ลบรันคิก」[ลบรันคิกเก้อทั้งหมด]" + "\n" + \
                  "🍭「.รัน @」[รันกลุ่มโดยแอดชื่อ]" + "\n" + \
                  "🍭「.รันแชท @」[รันแชทโดยแอดชื่อ]" + "\n" + \
                  "🍭「.รัน: 」[รันโดยใช้ชื่อ]" + "\n" + \
                  "🍭「รันโทร」เชินโทรกลุ่ม" + "\n" + \
                  "🍭「.gift」เราส่งของขวัญ" + "\n" + \
                  "🍭「.gift @」ส่งของขวัญไปที่แทช" + "\n" + \
                  "🍭「.giftall」คิกส่งของขวัญ" + "\n" + \
                  "🍭「เปิดแสกน」เปิดหาคนแอบอ่าน" + "\n" + \
                  "🍭「ปิดแสกน」ปิดหาคนแอบอ่าน" + "\n" + \
                  "🍭「.เชินแอด」เชินเจ้าของกลุ่ม" + "\n" + \
                  "🍭「.invitecancel」ยกเลิกค้างเชินในกลุ่ม" + "\n" + \
                  "🍭「ลบแชท」ลบแชททั้งหมด" + "\n" + \
                  "🍭「แทค2ปิด」" + "\n" + \
                  "🍭「แทค2เปิด」" + "\n" + \
                  "🍭「แทคเปิด」" + "\n" + \
                  "🍭「แทคเปิด」" + "\n" + \
                  "🍭「ต้อนรับ เปิด/ปิด」" + "\n" + \
                  "🍭「ออก เปิด/ปิด」" + "\n" + \
                  "🍭「ทักเตะ เปิด/ปิด」" + "\n" + \
                  "🍭「ทักเจ็บ เปิด/ปิด」" + "\n" + \
                  "🍭「คอมเม้น: 」" + "\n" + \
                  "🍭「ทักเตะ: 」" + "\n" + \
                  "🍭「ยกเชิน」" + "\n" + \
                  "🍭「ดึง」" + "\n" + \
                  "🍭「บอทยก」" + "\n" + \
                  "🍭「ข้อความแอด: 」" + "\n" + \
                  "🍭「ส่งเสียงกลุ่ม 」" + "\n" + \
                  "🍭「ส่งเสียงแชท」" + "\n" + \
                  "🍭「เปิดป้องกัน」" + "\n" + \
                  "🍭「ปิดป้องกัน」" + "\n" + \
                  "🍭「Tx1:」ตั้งข้อความเข้า" + "\n" + \
                  "🍭「Tx2:」ตั้งข้อความออก" + "\n" + \
                  "🍭「Tag1:」ตั้งข้อความแทค1" + "\n" + \
                  "🍭「Tag2:」ตั้งข้อความแทค2" + "\n" + \
                  "🍭「Tx1-2」ดูข้อความล่าสุด" + "\n" + \
                  "🍭「Tag1-2」ดูข้อความล่าสุด" + "\n" + \
                  "🌧🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦🌦" + "\n" + \
                  "۞~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~۞" + "\n" + \
                  "❄「─•۞✟ℓℓஆՁՃิ۞•─」❄" + "\n" + \
                  "❄「@ID. http://line.me/ti/p/p-susu000nunu 」❄" + "\n" + \
                  "❄════"
    return myHelp

    
def helpset():
    helpSet = "╭════[─•۞✟ℓℓஆՁゆຸ۞•─] " + "\n" + \
    "║แชร์เปิด/ปิด]" + "\n" + \
    "║สแปม]" + "\n" + \
    "║อัฟวีดีโอ]" + "\n" + \
    "║คิกวีดีโอ]" + "\n" + \
    "║วีดีโอคิก1-10]" + "\n" + \
    "║ว่างเปล่า]" + "\n" + \
    "║ว่างเปล่า" + "\n" + \
    "║ว่างเปล่า" + "\n" + \
    "╰════"
    return helpSet 

def helpkicker():
    helpKicker = "╭════HelpKicker " + "\n" + \
    "❥「K1-4 kick」คำสั่งบินกลุ่ม" + "\n" + \
    "❥「1-4ลบสิริ」สั่งเตะบอทสิริ" + "\n" + \
    "❥「ดิสคิก1-10」เปลี่ยนดิสคิกทีละตัว" + "\n" + \
    "❥「ชื่อคิก1-10: 」เปลี่ยนชื่อคิกทีละตัว" + "\n" + \
    "❥「ตัสคิก1-10:」เปลี่ยนตัสคิกทีละตัว" + "\n" + \
    "❥「K1 invite」" + "\n" + \
    "❥「K2 inv」" + "\n" + \
    "❥「K3 vit」" + "\n" + \
    "❥「K1 tag」" + "\n" + \
    "❥「K1กลุ่ม」" + "\n" + \
    "❥「K2กลุ่ม」" + "\n" + \
    "❥「K3กลุ่ม」" + "\n" + \
    "❥「อาบน้ำ」[คำสั่งล้างห้อง]" + "\n" + \
    "❥「ไล่ดำ」" + "\n" + \
    "❥「ล้างดำ」" + "\n" + \
    "❥「ชื่อคิก:」[เปลี่ยนชื่อคิกทั้งหมด]" + "\n" + \
    "❥「ดิสคิก:」[เปลี่ยนดิสคิกทั้งหมด]" + "\n" + \
    "❥「Protect on/off」" + "\n" + \
    "❥「Cancel pro on/off」" + "\n" + \
    "❥「block on/off」" + "\n" + \
    "❥「Invit pro on/off」" + "\n" + \
    "❥「Link pro on/off」" + "\n" + \
    "❥「Join pro on/off」" + "\n" + \
    "❥「Proall on/off」" + "\n" + \
    "❥「Join on/off」" + "\n" + \
    "❥「leave on/off」" + "\n" + \
    "❥「read on/off」" + "\n" + \
    "❥「แทคเปิด/ปิด」[เปิดข้อความแทค]" + "\n" + \
    "❥「Selfbot on/off」" + "\n" + \
    "❥「แทค1เปิด/ปิด [เปิดข้อความแทคที่1]" + "\n" + \
    "❥「แทค2เปิด/ปิด」[เปิดข้อความแทคที่2]" + "\n" + \
    "❥「Checksticker on/off」" + "\n" + \
    "❥「Sider on/off」" + "\n" + \
    "❥「ต้อนรับ on/off」" + "\n" + \
    "❥「ข้อความออก on/off」" + "\n" + \
    "❥════"
    return helpKicker
 
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
                ki1.blockContact(op.param1)
                ki2.blockContact(op.param1)
                ki3.blockContact(op.param1) 
                ki4.blockContact(op.param1)
                ki5.blockContact(op.param1)
                ki6.blockContact(op.param1) 
                ki7.blockContact(op.param1)
                ki8.blockContact(op.param1)
                ki9.blockContact(op.param1)
                ki10.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
#        if op.type == 24:
#            if settings["autoLeave"] == True:
#                line.leaveRoom(op.param1)
        if op.type == 24:
            print ("[ 24 ] ออกแชทรวมแล้ว")
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message           
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        line.sendMessage(msg.to,"[ชื่อ]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ตัส]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))
                    else:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        line.sendMessage(msg.to,"[ชื่อ]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ตัส]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#~~~~~~~~~~~~~~~~เขียนโดยนุจัง~~~~~~~~~~~~~~#
 
                if "สแปม " in msg.text.lower():
                    spl = re.split("สแปม ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
#~~~~~~~~~~~~~~~~~~~เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─~~~~~~~~~~~~~~#
              
                if text.lower() == 'คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'คำสั่ง2':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'คำสั่ง3':
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
                elif text.lower() == 'คำสั่ง4':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'คำสั่ง5':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, " กำลังทดสอบความเร็ว...")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")						
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "💙 โปรดรอสักครู่..เจ้านาย 💙")
                    line.sendMessage(to, "💙 รีสตารท..เสร็จสิ้น 💙")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "💜ชีวิตที่เหลืออยู่...💜\n {}".format(str(runtime)))
                elif text.lower() == 'บัญชี':
                    try:
                        arr = []
                        owner = "ud3a6bfda60a956cca0f58f2a14bae808"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[─•۞✟ℓℓஆՁՃิ۞•─]"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ]"
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ✯KIEBOTLINE✯ ]"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔═[─•۞✟ℓℓஆՁՃิ۞•─]═══"
                        if settings["contact"] == True: ret_ += "\n❥ 「อ่านคอนแทค」 ✔"
                        else: ret_ += "\n❥ 「อ่านคอนแทค」    ✘ "
                        if settings["autoAdd"] == True: ret_ += "\n❥ 「บล้อคออโต้」 ✔"
                        else: ret_ += "\n❥ 「บล้อคออโต้」    ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n❥ 「เข้าห้องออโต้」 ✔"
                        else: ret_ += "\n❥ 「เข้าห้องออโต้」    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n❥ 「ยกเลิกเชิญกลุ่ม」: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n❥ 「ยกเลิกเชิญกลุ่ม」    ✘ "
                        if settings["autoLeave"] == True: ret_ += "\n❥ 「ออกแชทรวม」 ✔"
                        else: ret_ += "\n❥ 「ออกแชทรวม」 ✘ "
                        if settings["autoRead"] == True: ret_ += "\n❥ 「อ่านออโต้」 ✔"
                        else: ret_ += "\n❥ 「อ่านออโต้」   ✘ "				
                        if settings["checkSticker"] == True: ret_ += "\n❥ 「Sticker」 ✔"
                        else: ret_ += "\n❥ 「Sticker」        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n❥ 「ตอบกลับคนแทค」 ✔"
                        else: ret_ += "\n❥ 「ตอบกลับคนแทค」 ✘ "
                        if settings["potoMention"] == True: ret_ += "\n❥ 「แสดงภาพคนแทค」 ✔"
                        else: ret_ += "\n❥ 「แสดงภาพคนแทค」 ✘ "						
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n❥ 「กันเชิญ」 ✔"
                        else: ret_ += "\n❥ 「กันเชิญ 」✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n❥ 「กันยกเชิญ」 ✔"
                        else: ret_ += "\n❥ 「กันยกเชิญ」 ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n❥ 「ป้องกัน」 ✔"
                        else: ret_ += "\n❥ 「ป้องกัน」 ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n❥ 「ป้องกันเปิดลิ้ง」 ✔"
                        else: ret_ += "\n❥ 「ป้องกันเปิดลิ้ง」 ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n❥ 「ป้องกันสมาชิก」 ✔"
                        else: ret_ += "\n❥ 「ป้องกันสมาชิก」 ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n❥ 「ป้องกันเข้ากลุ่ม」 ✔"
                        else: ret_ += "\n❥ 「ป้องกันเข้ากลุ่ม」 ✘ "						
                        ret_ += "\n╚════[ Status ]═════┛"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'block on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "💙 เปิดบล็อคเรียบร้อย..")
                elif text.lower() == 'block off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "💙 ปิดบล็อคเรียบร้อย..")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "💙 เปิดเข้ากลุ่มเรียบร้อย..")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "💙 ปิดเข้ากลุ่มเรียบร้อย..ชล")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    line.sendMessage(to, "เปิดอ่านคอนแทค")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    line.sendMessage(to, "ปิดอ่านคอนแทค")
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendMessage(msg.to,"❥ปิดกันรันเรียบร้อยแล้ว")
                                else:
                                    line.sendMessage(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendMessage(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendMessage(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Value is wrong")
                        else:
                                line.sendMessage(msg.to,"Bizarre ratings")					
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "💙 เปิดออกแชทรวมเรียบร้อย..")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "💙 ปิดออกแชทรวมเรียบร้อย..")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "💙 เปิดอ่านออโต้เรียบร้อย..")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "💙 ปิดอ่านออโต้เรียบร้อย..")
                elif text.lower() == 'เปิดติ้ก':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "💙 เปิดเช็คสติ๊กเรียบร้อย..")
                elif text.lower() == 'ปิดติ้ก':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "💙 ปิดเช็คสติ๊กเรียบร้อย..")    
                elif text.lower() == 'แชร์เปิด':
                    settings["timeline"] = True
                    line.sendMessage(to, "เปิดลิ้งแชร์แล้ว.")
                elif text.lower() == 'แชร์ปิด':
                    settings["timeline"] = False
                    line.sendMessage(to, "ปิดลิ้งแชร์แล้ว.")
#==============================================================================#
                elif text.lower() == 'คท':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'ผู้สร้าง':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "ud3a6bfda60a956cca0f58f2a14bae808")
                elif text.lower() == 'มิส':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("มิส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชือ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("ดิส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ก็อปปี้ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "ก๊อปได้แล้ว  (◡‿◡✿) ")
                        except:
                            line.sendMessage(msg.to, "ก๊อปไม่ได้เนื่องจากมีบางอย่างไม่ปกติ  (◡‿◡✿) ")
                            
                elif text.lower() == 'เลิกก็อปปี้':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")

                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
						
#==============================================================================#
#===================================================================#
                elif text.lower() == 'ดิสกู':
                            settings["changePicture"] = True
                            line.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก1':
                            settings["changePicture"] = True
                            ki1.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก2':
                            settings["changePicture"] = True
                            ki2.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก3':
                            settings["changePicture"] = True
                            ki3.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก4':
                            settings["changePicture"] = True
                            ki4.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก5':
                            settings["changePicture"] = True
                            ki5.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก6':
                            settings["changePicture"] = True
                            ki6.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก7':
                            settings["changePicture"] = True
                            ki7.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก8':
                            settings["changePicture"] = True
                            ki8.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก9':
                            settings["changePicture"] = True
                            ki9.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสคิก10':
                            settings["changePicture"] = True
                            ki10.sendMessage(to, "ส่งรูปลงมา จ่ะ (^__^)..?")
                elif text.lower() == 'ดิสกลุ่ม':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                line.sendMessage(to, "เปลี่ยนรูปกลุ่มเรียบร้อย.")


#==============================================
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "คนสร้างกลุ่ม")
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "Name Group -> \n" + gid.name)
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'ลิ้งเปิด':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Link Qr to open")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to open")
                elif text.lower() == 'ลิ้งปิด':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Link Qr to closed.")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to closed.")
                elif text.lower() == 'บัญชีกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

                elif text.lower() == 'k1กลุ่ม':
                        groups = ki.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki.sendMessage(to, str(ret_))

                elif text.lower() == 'k2กลุ่ม':
                        groups = kk.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kk.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        kk.sendMessage(to, str(ret_))

                elif text.lower() == 'k3กลุ่ม':
                        groups = kc.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kc.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        kc.sendMessage(to, str(ret_))
						
                elif text.lower() == 'k4กลุ่ม':
                        groups = ke.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ke.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ke.sendMessage(to, str(ret_))					
                elif "รันโทร" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")	
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendMessage(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass	
                elif msg.text.lower() == "ไอดีกลุ่ม":
                    line.sendMessage(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendMessage(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendMessage(msg.to,text[:-2])
                    cnt = 0				
                elif "|!" in msg.text:
                    spl = msg.text.split("|!")
                    if spl[len(spl)-1] == "":
                        line.sendMessage(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)	
                elif ".ยกเลิกกลุ่ม" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == ".myid":
                    line.sendMessage(msg.to,user1)
                elif msg.text.lower().startswith(".mentionall"):
                    data = msg.text[len(".mentionall"):].strip()
                    if data == "":
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendMessage(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendMessage(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendMessage(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendMessage(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendMessage(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendMessage(msg.to,"[[NO MENTION]]")
         
                elif ".ชื่อ " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendMessage(msg.to,"สำเร็จแล้ว")
         
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendMessage(msg.to,str(e))	
                					
                elif msg.text.lower().startswith("pz:gac "):
                    pnum = re.split("pz:gac ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                ki2.sendMessage(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                ki2.sendMessage(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                ki2.sendMessage(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                ki2.sendMessage(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                ki2.sendMessage(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                ki2.sendMessage(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendMessage(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendMessage(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendMessage(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendMessage(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")

                if msg.text.lower() == ".me":
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': user1}
                    line.sendMessage(msg)
                if msg.text.lower() == ".gift":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
                if msg.text.lower() == ".giftall":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    ki1.sendMessage(msg)
                    ki2.sendMessage(msg)
                    ki3.sendMessage(msg)
                    ki4.sendMessage(msg)
                    ki5.sendMessage(msg)
                    ki6.sendMessage(msg)
                    ki7.sendMessage(msg)
                    ki8.sendMessage(msg)
                    ki9.sendMessage(msg)
                    ki10.sendMessage(msg)
                if ".gift " in msg.text.lower():
                    red = re.compile(re.escape('.gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)						
#==============================================================================#
                elif text.lower() == 'แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "ทั้งหมด {} คน".format(str(len(nama))))

                elif text.lower() == '1แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members if contact.mid != lineMID]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        ki1.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        ki1.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))          

                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#============================ระบบรัน====เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─==============================================#
                elif ".รัน @" in msg.text:
                    print ("[Command]covergroup")
                    _name = msg.text.replace(".รัน @","")
                    _nametarget = _name.rstrip('  ')
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                               thisgroup = line.getGroups([msg.to])
                               Mids = [target for contact in thisgroup[0].members]
                               mi_d = Mids[:33]
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.sendText(msg.to,"เรียบร้อย")
                            except:
                                pass
                    print ("[Command]covergroup]")
                elif ".รันแชท @" in msg.text:
                    _name = msg.text.replace(".รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendText(g.mid,"555555555")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞") 
                           line.sendText(g.mid,"💞รักนะม๋าน้อย💞")
                           line.sendText(msg.to, "เสร็จแล้ว..จ่ะ")
                           print (" Spammed !")
                elif ".รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        line.findAndAddContactsByMid(key)                   
                        contact = line.getContact(key)
                        line.createGroup("🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾",[key])
                        line.sendText(msg,to,"🐾ъମਫ਼ีีઈஇ ମู Ҩန❍🐾")
#==============================================================================#   
#~~~~~~~~~~~~~~~~~~จัดเรียงโดย[─•۞✟ℓℓஆՁゆຸ۞•─]~~~~~~~~~~~~~~~#

              

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 

                
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ จำนวน Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "fotoig" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1):
                            print(('send foto : ', count))
                            r = x.get(profile, params={'max_id': end_cursor})                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                print((node['display_src']))
                                line.sendImageWithURL(msg.to,node['display_src'])
                elif "รูป" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "anime" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "ยูทูป" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["Cctv on","เปิดแสกน","เปิดสแกน"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดค้นหาคนแอบอ่านแล้ว")
                elif msg.text in ["Cctv off","ปิดแสกน","ปิดสแกน"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendMessage(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดค้นหาคนแอบอ่านแล้ว")

                elif text.lower() == 'selfbot off':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)

                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่น🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อน🎎\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["รายการบล๊อก"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════บัญชีคนที่ถูกบล้อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["เพื่อน mid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════List FriendMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'ขอลิ้ง':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂ ลิ้ ง ข อ ง ก ลุ่ ม นี้ \n╚══════════════┛")

                elif msg.text == "เว็บโป๊":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text.lower() == 'ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/uninstall"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)
                            ki1.leaveGroup(receiver)
                            ki2.leaveGroup(receiver)
                            ki3.leaveGroup(receiver)
                            ki4.leaveGroup(receiver)							
                        except:
                            pass

                elif msg.text in ["Tagimage on","Tag2 on","แทค2เปิด","แทค2 เปิด","แทค2 off","แทค2off"]:
                        settings['potoMention'] = True
                        line.sendMessage(msg.to,"แทค2เปิดแล้ว")
                
                elif msg.text in ["Tagimage off","Tag2 off","แทค2ปิด","แทค2 ปิด","แทค2 off","แทค2off"]:
                        settings['potoMention'] = False
                        line.sendMessage(msg.to,"แทค2ปิดแล้ว")

                elif msg.text in ["Respontag on","Tag on","My respon on","Respon:on","แทคเปิด","แทคon"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"แทคทั้งหมดเปิดแล้ว..")
                
                elif msg.text in ["Respontag off","Tag off","My respon off","Respon:off","แทคปิด","แทคoff"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"แทคทั้งหมดปิดแล้ว..")

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["1ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki1.getGroup(msg.to)
                        if ki1MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki1.sendMessage(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki1.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
										
                elif msg.text in ["2ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki2.getGroup(msg.to)
                        if ki2MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki2.sendMessage(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    k2.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["3ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki3.getGroup(msg.to)
                        if ki4MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki3.sendMessage(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["4ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki4.getGroup(msg.to)
                        if ki4MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki4.sendMessage(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki4.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass									
                elif msg.text in ["Inviteuser"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".invitecancel2":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "เวลา":
                    line.sendMessage(msg.to,(str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[1].split(":")[0]+" ชั่วโมง " if "days" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[1].split(":")[0]+" ชั่วโมง " if "day" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(":")[0]+" ชั่วโมง ")+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[1]+" นาที "+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[2]+" วินาที")
#=============COMMAND KICKER===========================#
                elif msg.text in ["ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")

                elif text.lower() == "มาหอย":
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        group.preventedJoinByTicket = True
                        line.updateGroup(group)
                        print ("คิกเก้อเข้าห้อง")

                elif 'kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"จัดการลบคนออกกลุ่มเรียบร้อยแล้วครับ 😫")

                elif 'kill' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'k1 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki1.kickoutFromGroup(msg.to,[target])           
                               print ("K1 Kick User")
                           except:
                               ki1.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'k2 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki2.kickoutFromGroup(msg.to,[target])
                               print ("K2 kick user")
                           except:
                               ki2.sendMessage(msg.to,"Limit kaka 😫")                              

                elif 'k3 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki3.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               ki3.sendMessage(msg.to,"Limit kaka 😫")                              

                elif 'k4 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki4.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               ki4.sendMessage(msg.to,"Limit kaka 😫")                              
                               
                elif 'invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")

                elif 'k1 invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki1.inviteIntoGroup(msg.to,[target])
                               ki1.sendMessage(receiver, "Type👉 Invite Succes")
                               print ("R1 invite User")
                           except:
                               ki1.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k2 inv' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki2.inviteIntoGroup(msg.to,[target])
                               ki2.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R2 invite User")
                           except:
                               ki2.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k3 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki3.inviteIntoGroup(msg.to,[target])
                               ki3.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R3 invite User")
                           except:
                               ki3.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k4 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki4.inviteIntoGroup(msg.to,[target])
                               ki4.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R4 invite User")
                           except:
                               ki4.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif "อาบน้ำ" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("Cleanse","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"เกิดข้อผิดพลาดเป็นไปได้ว่าบันชีคุณบัค  (◡‿◡✿) ")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"ล้างห้องเรียบร้อยแล้ว")
                                         print ("Cleanse Group")

                elif msg.text in ["ไล่ดำ"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")

                elif text.lower() == "ลบแชท":
                        if msg._from in Family:
                            try:
                                ki1.removeAllMessages(op.param2)
                                ki2.removeAllMessages(op.param2)
                                ki3.removeAllMessages(op.param2)
                                ki4.removeAllMessages(op.param2)
                                ki5.removeAllMessages(op.param2)
                                ki6.removeAllMessages(op.param2)
                                ki7.removeAllMessages(op.param2)
                                ki8.removeAllMessages(op.param2)
                                ki9.removeAllMessages(op.param2)
                                ki10.removeAllMessages(op.param2)
                                line.removeAllMessages(op.param2) 
                                line.sendMessage(msg.to,"รอสักครู่กำลังลบแชท.")
                            except:
                                pass
                                print ("Remove Chat Kicker")

                elif text.lower() == "หนีหอย":
                    if msg._from in Family:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        print ("คิกเก้อออกจากกลุ่ม")

                elif text.lower() == "leaveall":
                    if msg._from in Family:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki1.leaveGroup(i)
                            ki2.leaveGroup(i)
                            ki3.leaveGroup(i)
                            ki4.leaveGroup(i) 
                            print ("Kicker Leave All group")

                elif "ชื่อใหม่: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("Update Name")

                elif "ตัสใหม่: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
                        print ("Update Bio Succes")
#~~~~~~~~~~~~~~~~~ตัส~~เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─~~~~~~~~~~~~~~#

                elif "ชื่อคิก1: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki1.getProfile()
                        profile_A.displayName = string
                        ki1.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki1.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก2: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki2.getProfile()
                        profile_A.displayName = string
                        ki1.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki2.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก3: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki3.getProfile()
                        profile_A.displayName = string
                        ki3.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki3.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก4: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki4.getProfile()
                        profile_A.displayName = string
                        ki4.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki4.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก5: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki5.getProfile()
                        profile_A.displayName = string
                        ki5.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki5.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")


                elif "ชื่อคิก6: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki6.getProfile()
                        profile_A.displayName = string
                        ki6.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki6.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก7: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki7.getProfile()
                        profile_A.displayName = string
                        ki7.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki7.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก8: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki8.getProfile()
                        profile_A.displayName = string
                        ki8.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki8.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก9: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki9.getProfile()
                        profile_A.displayName = string
                        ki9.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki9.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")
			

                elif "ชื่อคิก10: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki10.getProfile()
                        profile_A.displayName = string
                        ki10.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้วเป็น " + string)
                        ki10.sendMessage(msg.to,"ถูกใจข่อยหลายคักเด้อลูกพี่(◡‿◡✿) ")
                        print ("Update Name")

#~~~~~~~~~~~~~~~~~~~เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─~~~~~~~~~~~~~~#
                elif "ชื่อคิก: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki1.getProfile()
                        profile_B = ki2.getProfile()
                        profile_C = ki3.getProfile()
                        profile_D = ki4.getProfile()
                        profile_E = ki5.getProfile()
                        profile_F = ki6.getProfile()
                        profile_G = ki7.getProfile()
                        profile_H = ki8.getProfile()
                        profile_I = ki9.getProfile()
                        profile_J = ki10.getProfile()
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        profile_D.displayName = string
                        profile_E.displayName = string
                        profile_F.displayName = string
                        profile_G.displayName = string
                        profile_H.displayName = string
                        profile_I.displayName = string
                        profile_J.displayName = string
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D) 
                        ki.updateProfile(profile_E)
                        kk.updateProfile(profile_F)
                        kc.updateProfile(profile_G)
                        ke.updateProfile(profile_H) 
                        ki.updateProfile(profile_I)
                        kk.updateProfile(profile_J)
                        line.sendMessage(msg.to,"Update Name All Kicker to : " + string)
                        print ("Update Name All Kicker")

                elif "ตัสคิก: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki1.getProfile()
                        profile_B = ki2.getProfile()
                        profile_C = ki3.getProfile()
                        profile_D = ki4.getProfile()  
                        profile_E = ki5.getProfile()
                        profile_F = ki6.getProfile()
                        profile_G = ki7.getProfile()
                        profile_H = ki8.getProfile()  
                        profile_I = ki9.getProfile()
                        profile_J = ki10.getProfile()
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        profile_D.statusMessage = string
                        profile_E.statusMessage = string
                        profile_F.statusMessage = string
                        profile_G.statusMessage = string
                        profile_H.statusMessage = string
                        profile_I.statusMessage = string
                        profile_J.statusMessage = string
                        ki1.updateProfile(profile_A)
                        ki2.updateProfile(profile_B)
                        ki3.updateProfile(profile_C)
                        ki4.updateProfile(profile_D)
                        ki5.updateProfile(profile_E)
                        ki6.updateProfile(profile_F)
                        ki7.updateProfile(profile_G)
                        ki8.updateProfile(profile_H)
                        ki9.updateProfile(profile_I)
                        ki10.updateProfile(profile_J)
                        line.sendMessage(msg.to,"Update Bio All Kicker to : " + string)
                        print ("Update Bio All Kicker")

                elif text.lower() == "รายงาน":
                    if msg._from in Family:
                        profile = ki1.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki1.sendMessage(to, text)                                
                        profile = ki2.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki2.sendMessage(to, text)                                
                        profile = ki3.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki3.sendMessage(to, text)
                        profile = ki4.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki4.sendMessage(to, text)                                
                        profile = ki5.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki5.sendMessage(to, text)                                
                        profile = ki6.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki6.sendMessage(to, text)
                        profile = ki7.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki7.sendMessage(to, text)
                        profile = ki8.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki8.sendMessage(to, text)                                
                        profile = ki9.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki9.sendMessage(to, text)                                
                        profile = ki10.getProfile()
                        text = profile.displayName + "รายงานตัว\nเจ้าค่ะ (◡‿◡✿) "
                        ki10.sendMessage(to, text)
                        print ("Kicker Respon")

                elif msg.text in ["บอท"]:
                    ki1.sendMessage(msg.to,"1(⊙_⊙)")
                    ki2.sendMessage(msg.to,"2(⊙_⊙)")
                    ki3.sendMessage(msg.to,"3(⊙_⊙)")
                    ki4.sendMessage(msg.to,"4(⊙_⊙)")   
                    ki5.sendMessage(msg.to,"5(⊙_⊙)")
                    ki6.sendMessage(msg.to,"6(⊙_⊙)")
                    ki7.sendMessage(msg.to,"5(⊙_⊙)")
                    ki8.sendMessage(msg.to,"8(⊙_⊙)") 
                    ki9.sendMessage(msg.to,"9(⊙_⊙)")
                    ki10.sendMessage(msg.to,"10(⊙_⊙)")
                elif msg.text.lower().startswith("bitcoin"):
                   search = msg.text.split("bitcoin")
                   with requests.session() as web:
                       web.headers["User-Agent"] = random.choice(settings["userAgent"])
                       url = "https://xeonwz.herokuapp.com/bitcoin.api"
                       r = web.get(url)
                       data=r.text
                       data=json.loads(data)
                       print(data)
                       hasil = "「 Bitcoin Result 」"
                       hasil += "\nPrice : " +str(data["btc"])                                
                       hasil += "\nExpensive : " +str(data["high"])
                       hasil += "\nCheap : " +str(data["low"])               
                       line.sendMessage(to, str(hasil))
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'Protect on':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == 'Protect off':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == 'cancel pro on':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'cancel pro off':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'invit pro on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'invit pro off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'link pro on':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'link pro off':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'guest pro on':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'guest pro off':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'join pro on':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'join pro off':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'เปิดป้องกัน':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == 'ปิดป้องกัน':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'ต้อนรับ เปิด':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   .")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                elif msg.text.lower() == 'ต้อนรับ ปิด':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")

                elif msg.text.lower() == 'ออก เปิด':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                elif msg.text.lower() == 'ออก ปิด':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")

                elif msg.text in ["Tag1","Tag1"]:
                   line.sendMessage(msg.to,"❥ข้อความแทคล่าสุดคือ\n\n" + str(settings["tag1"]))

                elif msg.text in ["Tag2","Tag2"]:
                   line.sendMessage(msg.to,"❥ข้อความแทคล่าสุดคือ\n\n" + str(settings["tag2"]))

                elif "Tag1:" in msg.text:
                      settings["tag1"] = msg.text.replace("Tag1: ","")
                      line.sendMessage(msg.to,"❥คุณได้ตั้งข้อความแทคแล้ว")

                elif "Tag2:" in msg.text:
                      settings["tag2"] = msg.text.replace("Tag2: ","")
                      line.sendMessage(msg.to,"❥คุณได้ตั้งข้อความแทคแล้ว")

                elif "Tx1:" in msg.text:
                      settings["KIEBOT1"] = msg.text.replace("Tx1: ","")
                      line.sendMessage(msg.to,"❥คุณได้ตั้งข้อความเข้าแล้ว")

                elif "Tx2:" in msg.text:
                      settings["KIEBOT2"] = msg.text.replace("Tx2: ","")
                      line.sendMessage(msg.to,"❥คุณได้ตั้งข้อความออกแล้ว")

                elif msg.text in ["Tx1","Tx1"]:
                   line.sendMessage(msg.to,"❥ข้อความเข้าล่าสุดคือ\n\n" + str(settings["KIEBOT1"]))

                elif msg.text in ["Tx2","Tx2"]:
                   line.sendMessage(msg.to,"❥ข้อความออกล่าสุดคือ\n\n" + str(settings["KIEBOT2"]))                                                
#====================================================
                      
                elif msg.text.lower() == 'ทักเตะ เปิด':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...")
                                
                elif msg.text.lower() == 'ทักเตะ ปิด':
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว..")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว...")

#==============================================================================#   
                elif "ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงกลุ่ม ", "")
                    bc = ("เชล...บอท..น้องสุ..บาย")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงแชท ", "")
                    bc = ("เชลบอทน้องสุ..บาย")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')   
	
                elif msg.text in ["ทักเจ็บ เปิด"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแท็ก")
                
                elif msg.text in ["ทักเจ็บ ปิด"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแท็ก")
                    
                    
                elif 'ข้อความแอด: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ข้อความแอด: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["message"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))
                         
                elif 'คอมเม้น: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('คอมเม้น: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["comment"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้👇\n\n👉{}".format(str(spl))) 
                    
                
                elif 'ทักเตะ: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ทักเตะ: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนคนลบสมาชิดเรียบร้อย")
                     else:
                          settings["kick"] = spl
                          line.sendMessage(msg.to, "ตั้งค่าข้อความเมื่อมีคนลบสมาชิกแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))

                	
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == "ยกเชิน":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                
#====================================================
                elif text.lower() == 'ล่องหน':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "แน๊ะไม่มีคนใส่ร่องหนในกลุ่มนี้")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'zm':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)                   
                elif text.lower() == 'zc':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "แน๊ะไม่มีคนใส่ร่องหนในกลุ่มนี้")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
#===========≠==========================================#
                elif "จัด " in msg.text:
                        vkick0 = msg.text.replace("จัด ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = line.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line.inviteIntoGroup(msg.to,[target])
                                    line.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass       
#===========≠=================เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─=========================#
                elif text.lower() == 'ลบรันคิก':
                    gid = ki1.getGroupIdsInvited()
                    gid = ki2.getGroupIdsInvited()
                    gid = ki3.getGroupIdsInvited()
                    gid = ki4.getGroupIdsInvited()
                    gid = ki5.getGroupIdsInvited()
                    gid = ki6.getGroupIdsInvited()
                    gid = ki7.getGroupIdsInvited() 
                    gid = ki8.getGroupIdsInvited()
                    gid = ki9.getGroupIdsInvited()
                    gid = ki10.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        ki1.rejectGroupInvitation(i)
                        ki2.rejectGroupInvitation(i)
                        ki3.rejectGroupInvitation(i)
                        ki4.rejectGroupInvitation(i)
                        ki5.rejectGroupInvitation(i)
                        ki6.rejectGroupInvitation(i)
                        ki7.rejectGroupInvitation(i)
                        ki8.rejectGroupInvitation(i)
                        ki9.rejectGroupInvitation(i)
                        ki10.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    ki1.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki1.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki2.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki2.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki3.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki3.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))	
                    ki4.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki4.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki5.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki5.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki6.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki6.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki7.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki7.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki8.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki8.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki9.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki9.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
                    ki10.sendMessage(to, "ลบรันคิกทั้งหมดเสร็จแล้วขอรับ")
                    ki10.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))

#===========≠===============เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─===========================#       
                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))								
			
#~~~~~~~~~~~~~~~~~~~เขียนโดย◇─•۞✟ℓℓஆՁゆຸ۞•─~~~~~~~~~~~~~~#					
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"All members has been added ban.")
										   
                elif 'ban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif 'unban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

            
                elif msg.text in ["เช็คดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text in ["Ban","ดำ"]:
                    settings["wblacklist"] = True
                    line.sendMessage(msg.to,"send contact to ban")
                
                elif msg.text in ["Unban","ขาว"]:
                    settings["dblacklist"] = True
                    line.sendMessage(msg.to,"send contact to ban")    

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki1.getGroup(op.param1)
                  G = ki2.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki2.updateGroup(G)
                  ticket = ki2.reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  G.preventedJoinByTicket = True
                  line.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in ki1MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki3.getGroup(op.param1)
                  ki2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki3.updateGroup(G)
                  ticket = ki3.reissueGroupTicket(op.param1)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki2.updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01) 
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)  
                  G.preventedJoinByTicket = True
                  ki.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki2MID:
              if op.param2 not in Family:
                try:
                  G = ki3.getGroup(op.param1)
                  G = ki1.getGroup(op.param1)
                  ki3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki3.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki2.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki3MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki4.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki1.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki3.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in ki4MID:
              if op.param2 not in Family:
                try:
                  G = ki1.getGroup(op.param1)
                  G = ki3.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki1.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki4.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

			                  
            if op.param3 in ki5MID:
              if op.param2 not in Family:
                try:
                  G = ki6.getGroup(op.param1)
                  G = ki4.getGroup(op.param1)
                  ki3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki3.updateGroup(G)
                  ticket = ki3.reissueGroupTicket(op.param1)
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki5.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
			                  
            if op.param3 in ki6MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki5.getGroup(op.param1)
                  ki4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki4.updateGroup(G)
                  ticket = ki4.reissueGroupTicket(op.param1)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki6.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki7MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki4.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki1.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki7.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki8MID:
              if op.param2 not in Family:
                try:
                  G = ki9.getGroup(op.param1)
                  G = ki10.getGroup(op.param1)
                  ki5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki5.updateGroup(G)
                  ticket = ki5.reissueGroupTicket(op.param1)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki8.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki9MID:
              if op.param2 not in Family:
                try:
                  G = ki8.getGroup(op.param1)
                  G = ki9.getGroup(op.param1)
                  ki7.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki7.updateGroup(G)
                  ticket = ki7.reissueGroupTicket(op.param1)
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki9.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki10MID:
              if op.param2 not in Family:
                try:
                  G = ki1.getGroup(op.param1)
                  G = ki4.getGroup(op.param1)
                  ki2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki2.updateGroup(G)
                  ticket = ki2.reissueGroupTicket(op.param1)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki10.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)
                ki5.leaveRoom(op.param1)
                ki6.leaveRoom(op.param1)
                ki7.leaveRoom(op.param1)
                ki8.leaveRoom(op.param1)
                ki9.leaveRoom(op.param1)
                ki10.leaveRoom(op.param1)
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)
                ki5.leaveRoom(op.param1)
                ki6.leaveRoom(op.param1)
                ki7.leaveRoom(op.param1)
                ki8.leaveRoom(op.param1)
                ki9.leaveRoom(op.param1)
                ki10.leaveRoom(op.param1)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                   if 'displayName' in msg.contentMetadata:
                       contact = line.getContact(msg.contentMetadata["mid"])
                       try:
                           cu = line.getProfileCoverURL(msg.contentMetadata["mid"])
                       except:
                           cu = ""
                       line.sendMessage(msg.to,"[ชื่อ]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[เข้าสู่ระบบ]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))
                   else:
                       contact = line.getContact(msg.contentMetadata["mid"])
                       try:
                           cu = line.getProfileCoverURL(msg.contentMetadata["mid"])
                       except:
                           cu = ""
                       line.sendMessage(msg.to,"[ชื่อ]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[เข้าสู่ระบบ]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))

#==============================================================================#
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in ki10MID:
                        G = ki10.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki10.updateGroup(G)
                        ticket = ki10.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki10.updateGroup(G)
                        ticket = ki10.reissueGroupTicket(op.param1)	
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki10.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in ki1MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki2MID:
                    if op.param2 in ki1MID:
                        G = ki1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                    else:
                        G = ki1.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
			
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        ticket = ki3.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        ticket = ki3.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki5MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        ticket = ki4.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        ticket = ki4.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki6MID:
                    if op.param2 in ki5MID:
                        G = k5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        ticket = ki5.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        ticket = ki5.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)			
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki7MID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        ticket = k6.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        ticket = ki6.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki8MID:
                    if op.param2 in ki7MID:
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        ticket = ki7.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        ticket = ki7.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki9MID:
                    if op.param2 in ki8MID:        
                        G = ki8.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki8.updateGroup(G)
                        ticket = ki8.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki8.updateGroup(G)
                        ticket = ki8.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki8.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki10MID:
                    if op.param2 in ki9MID:
                        G = ki9.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki9.updateGroup(G)
                        ticket = ki9.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)				
                        G.preventedJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki9.updateGroup(G)
                        ticket = ki9.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki5.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki6.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki7.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        ki8.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki10.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki9.updateGroup(G)
                        settings["blacklist"][op.param2] = True
            except:
                pass
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)      
#====================================================================================

            elif msg.contentType == 1:
                    if settings["changePictureProfile"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changePictureProfile"] = False                                                                               
                        line.updateProfilePicture(path)                                                                                        
                        line.sendMessage(to, "เปลี่ยนโปรไฟล์สำเร็จแล้ว")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = line.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            line.updateGroupPicture(to, path)
                            line.sendMessage(to, "เปลี่ยนรูปกลุ่มสำเร็จแล้ว")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "ลิ้งโพส\n" + msg.contentMetadata["postEndUrl"]
                    line.sendMessage(msg.to,msg.text)              
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
                    ki1.sendMessage(op.param1,str(settings["message"]))
                    ki2.sendMessage(op.param1,str(settings["message"]))
                    ki3.sendMessage(op.param1,str(settings["message"]))
                    ki4.sendMessage(op.param1,str(settings["message"])) 
                    ki5.sendMessage(op.param1,str(settings["message"]))
                    ki6.sendMessage(op.param1,str(settings["message"]))
                    ki7.sendMessage(op.param1,str(settings["message"]))
                    ki8.sendMessage(op.param1,str(settings["message"])) 
                    ki9.sendMessage(op.param1,str(settings["message"]))
                    ki10.sendMessage(op.param1,str(settings["message"]))

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki1.sendChatChecked(to, msg_id)
                    ki2.sendChatChecked(to, msg_id)
                    ki3.sendChatChecked(to, msg_id)
                    ki4.sendChatChecked(to, msg_id)
                    ki5.sendChatChecked(to, msg_id)
                    ki6.sendChatChecked(to, msg_id)
                    ki7.sendChatChecked(to, msg_id)
                    ki8.sendChatChecked(to, msg_id)
                    ki9.sendChatChecked(to, msg_id)
                    ki10.sendChatChecked(to, msg_id)    
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)                        
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                            # balas = ["『 Auto Respon』\n " + cName + "\n" + str(settings["tag1"])
                             balas = ["『 Auto Respon』\n " + cName + "\n" + str(settings["tag1"]) , "『 Auto Respon』\n" + cName + "\n" + str(settings["tag2"])]
                            # ret_ = msg.text1 + random.choice(balas)
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)                                                                         
                                          break                        
                                 #         sendMessageWithMention(to, contact.mid)
                                      #    break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                            contact = line.getContact(msg._from)
                            cName = contact.displayName
                            balas = ["Dont Tag Me!! Im Buy",cName + ""]
                            ret_ = "@" + random.choice(balas)
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                  if mention['M'] in lineMID:
                                         line.sendMessage(msg.to,ret_)                                         
                                         break                                          
                if msg.text in ["Me","me",".me",".Me","คท","/me"]:
                    line.sendMessage(msg.to,"เชคทั้งวันไอ้สัส ไม่หลุดหรอก จวย 😆")
                if msg.text in ["sp","speed",".speed","/speed","Sp",".Speed"]:
                    line.sendMessage(msg.to,"เชคควยรัยหนักหรา สึด !!!😉")
                if msg.text in ["runtime","Runtime","/uptime","ออน",".uptime"]:
                    line.sendMessage(msg.to,"ออน ทั้งวันว่างหรา ลูก")	
                if msg.text in ["@","แอด","แอดมิน","แอดมิ้น","หัวห้อง"]:
                    line.sendMessage(msg.to,"👇นี้ไงแอดกลุ่ม👇")
                    line.sendMessage(msg.to,"Siriv10:グル作成者")				
                if msg.text in ["@รอง","แอดรอง","แอดสำรอง","รอง","รองแอด","@@"]:
                    line.sendMessage(msg.to,"siri:予備作成者")
                    line.sendMessage(msg.to,"ขิเหล่จัง แอด รอง คนนี้อ่ะ😂")				
                if msg.text in ["พี่ชิ","ชิ","พี่","พี่สุ","สุ","ที่รัก"]:
                    line.sendMessage(msg.to,"เรียกทำไมค่ะ เดะตีหัว ลากเข้าป่าเลย")
                    line.sendMessage(msg.to,"นี้เป็นระบบอัตโนมัติ ขณะนี้ผู้ใช้รายนี้ยังไม่ว่าง.กรุณาติดต่อใหม่ อีกครั้ง ขอบคุณค่ะ")				
                if msg.text in ["สวัดดี","สวัสดี","ดีครับ","สวัดดีครับ","สวัสดีครับ","สวัสดีคับ","สวัดดีคับ","ดีค่ะ","ดีคับ"]:
                    line.sendMessage(msg.to,"ไหว้พระเถอะลูก...YES😂")
                    line.sendMessage(msg.to,"ยินดีที่รู้จัก ค่ะ😊")				
                if msg.text in ["5","55","555","5555","55555","555555","5555555"]:
                    line.sendMessage(msg.to,"ขรรม ไร ค่ะ")
                    line.sendMessage(msg.to,"ไม่ตลก...")				
                if msg.text in ["กำ","กำนะ","กำหำ","กำหอย"]:
                    line.sendMessage(msg.to,"ไสไส..")
                    line.sendMessage(msg.to,"หำยู่วว..ใสมากำเบิ่งดุ(◡‿◡✿)  ")				
                if msg.text in ["มอง","มองแรง","มองบน",".มอง"]:
                    line.sendMessage(msg.to,"มองอะไร ค่ะ เดียว ทิ่มตาบอดเลย")
                    line.sendMessage(msg.to,"มองหำ..(◡‿◡✿) ")				         
                if msg.text in dangerMessage:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendMessage(msg.to,"ระบบตรวจพบคำหยาบคาย จำเป็นต้องนำออกเพื่อความสงบของสมาชิก (｀・ω・´)")										
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in bot1:
                return
            dan = line.getContact(op.param2)
            tgb = line.getGroup(op.param1)
            line.sendMessage(op.param1,str(settings["KIEBOT1"]) + "\n\n" + line.getContact(op.param2).displayName)
          #  line.sendMessage(op.param1, "สวัสดี {}, Welcome to Group {}\nเข้ามาแร้วคุยกันนะม่คุยกุเตะนะ (｀・ω・´)".format(str(dan.displayName),str(tgb.name)))
            line.sendContact(op.param1, op.param2)
            line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if settings['Lv'] == True:
            if op.param2 in bot1:
                return
            dan = line.getContact(op.param2)
            tgb = line.getGroup(op.param1)
            line.sendMessage(op.param1,str(settings["KIEBOT2"]) + "\n\n" + line.getContact(op.param2).displayName)
       #     line.sendMessage(op.param1, "เอ้า {}, ได้ออกจากกลุ่ม {} \nยืนไว้อาลัยแด่เขาเป็นเวลา3วินาที  (｀・ω・´)".format(str(dan.displayName),str(tgb.name)))
            line.sendContact(op.param1, op.param2)
            line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["kick"]) + "\nเฮ้ย {}, คือหยังมันโหดแท้วะΣ(っﾟДﾟ；)っ ".format(str(dan.displayName)))
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
#~~~~~~~~~~~~~~~~~เขียนโดยแมวนุ~~~~~~~~~~~~~~~~~~~~~~~#
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['อย่าแอบกันสิ','ออกมาเถอะ']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ 55 ] (◡‿◡✿) ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
