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
line = LINE()
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
line.log("Channel Token : " + str(channelToken))

#~~~~~~~~~~~~~เขียนโดย ༄۞ꪶꪶꪣꪫꪊ۞࿐ ~~~~~~~~~~~~~~~~~~~~~~~~#
#line = LINE()
#line = LINE('susu76917@gmail.com','nunu_kap2018')
ki1 = LINE('nu2bot2018@gmail.com','nunu_kap2018')
ki2 = LINE('nu3bot2018@gmail.com','nunu_kap2018')
ki3 = LINE('nu4bot2018@gmail.com','nunu_kap2018')
ki4 = LINE('nu8bot2018@gmail.com','nunu_kap2018')
ki5 = LINE('nu10bot2018@gmail.com','nunu_kap2018')
ki6 = LINE('bot1nu2018@gmail.com','nunu_kap2018')
ki7 = LINE('bot2nu2018@gmail.com','nunu_kap2018')
ki8 = LINE('bot3nu2018@gmail.com','nunu_kap2018')
ki9 = LINE('nu11bot2018@gmail.com','nunu_kap2018')
ki10 = LINE('nu9bot2018@gmail.com','nunu_kap2018')
#~~~~~~~~~~~เขียนโดย༄۞ꪶꪶꪣꪫꪊุ۞࿐~~~~~~~~~~~~~~~~~~~~~~~~#
print ("Login Succes")
#~~~~~~~~~~~~~~~~~เขียนขึ้นโดย ༄۞ꪶꪶꪣꪫꪊ۞࿐ ~~~~~~~~~~~~~~~~~~~~~~#
KAC = [line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
GUE = [ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10] 
lineMID = line.profile.mid
ki1MID = ki1.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
Bots = [lineMID,ki1MID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID]
creator = ["ue32b11986d8e9e5cf70b642cf7ba88ff"]
Owner = ["ue32b11986d8e9e5cf70b642cf7ba88ff"]
admin = ["ue32b11986d8e9e5cf70b642cf7ba88ff"]
#~~~~~~~~~~~~~~~~~~~~เขียนขึ้นโด ༄۞ꪶꪶꪣꪫꪊ۞࿐ ~~~~~~~~~~~~~~~~~~~~~~~~#
lineProfile = line.getProfile()
ki1Profile = ki1.getProfile()
ki2Profile = ki2.getProfile()
ki3Profile = ki3.getProfile()
ki4Profile = ki4.getProfile()
ki5Profile = ki5.getProfile()
ki6Profile = ki6.getProfile()
ki7Profile = ki7.getProfile()
ki8Profile = ki8.getProfile()
ki9Profile = ki9.getProfile()
ki10Profile = ki10.getProfile()
#~~~~~~~~~~~~~~~~~เขียนขึ้นโดย
lineSettings = line.getSettings()
ki1Settings = ki1.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()
ki5Settings = ki5.getSettings()
ki6Settings = ki6.getSettings()
ki7Settings = ki7.getSettings()
ki8Settings = ki8.getSettings()
ki9Settings = ki9.getSettings()
ki10Settings = ki10.getSettings()
#~~~~~~~~~~~~~~~~~~เขียนขึ้นโดย ༄۞ꪶꪶꪣꪫꪊ۞࿐ ~~~~~~~~~~~~~~~~~~~#
oepoll = OEPoll(line)
oepoll = OEPoll(ki1)
oepoll = OEPoll(ki2)
oepoll = OEPoll(ki3)
oepoll = OEPoll(ki4)
oepoll = OEPoll(ki5)
oepoll = OEPoll(ki6)
oepoll = OEPoll(ki7)
oepoll = OEPoll(ki8)
oepoll = OEPoll(ki9)
oepoll = OEPoll(ki10)
#~~~~~~~~~~~~~~เขียนขึ้นโดย ༄۞ꪶꪶꪣꪫꪊ۞࿐ ~~~~~~~~~~~~~~~~~~~~~~~~~#
responsename = line.getProfile().displayName
responsename = ki1.getProfile().displayName
responsename = ki2.getProfile().displayName
responsename = ki3.getProfile().displayName
responsename = ki4.getProfile().displayName
responsename = ki5.getProfile().displayName
responsename = ki6.getProfile().displayName
responsename = ki7.getProfile().displayName
responsename = ki8.getProfile().displayName
responsename = ki9.getProfile().displayName
responsename = ki10.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ Help 1" + "\n" + \
                  "║͜͡☆➣ Help 2" + "\n" + \
                  "║͜͡☆➣ Tag" + "\n" + \
                  "║͜͡☆➣ Halo ( panggil bot ) " + "\n" + \
                  "║͜͡☆➣ Absen" + "\n" + \
                  "║͜͡☆➣ Balik ( usir bot ) " + "\n" + \
                  "║͜͡☆➣ Aku balik ( kluar semua ) " + "\n" + \
                  "║͜͡☆➣ Cekk ( cek semua bot )" + "\n" + \
                  "║͜͡☆➣ Me" + "\n" + \
                  "║͜͡☆➣ Sp" + "\n" + \
                  "║͜͡☆➣ Status" + "\n" + \
                  "║͜͡☆➣ Ciak @" + "\n" + \
                  "║͜͡☆➣ Kickallmember" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP 2" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ Help 1" + "\n" + \
                  "║͜͡☆➣ Help 2" + "\n" + \
                  "║͜͡☆➣ Protect on/off" + "\n" + \
                  "║͜͡☆➣ QrProtect on/off" + "\n" + \
                  "║͜͡☆➣ InviteProtect on/off" + "\n" + \
                  "║͜͡☆➣ CancelProtect on/off" + "\n" + \
                  "║͜͡☆➣ AutoAdd on/off" + "\n" + \
                  "║͜͡☆➣ AutoJoin on/off" + "\n" + \
                  "║͜͡☆➣ AutoLeave on/off" + "\n" + \
                  "║͜͡☆➣ CheckSticker on/off" + "\n" + \
                  "║͜͡☆➣ AutoRead on/off" + "\n" + \
                  "║͜͡☆➣ DetectMention on/off" + "\n" + \
                  "║͜͡☆➣ Join link on/off" + "\n" + \
                  "║͜͡☆➣ GroupCreator" + "\n" + \
                  "║͜͡☆➣ GroupId" + "\n" + \
                  "║͜͡☆➣ GroupName" + "\n" + \
                  "║͜͡☆➣ GroupPicture" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ Gt" + "\n" + \
                  "║͜͡☆➣ Gt on/off" + "\n" + \
                  "║͜͡☆➣ Mimic on" + "\n" + \
                  "║͜͡☆➣ Mimic off" + "\n" + \
                  "║͜͡☆➣ MimicAdd" + "\n" + \
                  "║͜͡☆➣ MimicDel" + "\n" + \
                  "║͜͡☆➣ Lurking on/off" + "\n" + \
                  "║͜͡☆➣ Lurking" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP 3" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ AdminLit" + "\n" + \
                  "║͜͡☆➣ OwnerList" + "\n" + \
                  "║͜͡☆➣ BanContact" + "\n" + \
                  "║͜͡☆➣ UnbanContact" + "\n" + \
                  "║͜͡☆➣ BanList" + "\n" + \
                  "║͜͡☆➣ Clearban" + "\n" + \
                  "║͜͡☆➣ Restart" + "\n" + \
                  "║͜͡☆➣ About" + "\n" + \
                  "║͜͡☆➣ Me" + "\n" + \
                  "║͜͡☆➣ MyMid" + "\n" + \
                  "║͜͡☆➣ Midnya @" + "\n" + \
                  "║͜͡☆➣ MyName" + "\n" + \
                  "║͜͡☆➣ MyBio" + "\n" + \
                  "║͜͡☆➣ MyPicture" + "\n" + \
                  "║͜͡☆➣ MyVideoProfile" + "\n" + \
                  "║͜͡☆➣ MyCover" + "\n" + \
                  "║͜͡☆➣ StealContact @" + "\n" + \
                  "║͜͡☆➣ StealMid @" + "\n" + \
                  "║͜͡☆➣ StealName「Mention」" + "\n" + \
                  "║͜͡☆➣ StealBio @" + "\n" + \
                  "║͜͡☆➣ StealPicture @" + "\n" + \
                  "║͜͡☆➣ StealVideoProfile @" + "\n" + \
                  "║͜͡☆➣ StealCover @" + "\n" + \
                  "║͜͡☆➣ CloneProfile @" + "\n" + \
                  "║͜͡☆➣ RestoreProfile" + "\n" + \
                  "║͜͡☆➣ GroupCreator" + "\n" + \
                  "║͜͡☆➣ GroupId" + "\n" + \
                  "║͜͡☆➣ GroupName" + "\n" + \
                  "║͜͡☆➣ GroupPicture" + "\n" + \
                  "║͜͡☆➣ Gt" + "\n" + \
                  "║͜͡☆➣ Gt「On/Off」" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ Ciak @" + "\n" + \
                  "║͜͡☆➣ KickAllMember"+ "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ GYEVHA BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] GYEVHA BOTS SATU")
            return
#-------------------------------------------------------------------------------
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
        if op.type == 25:
            print ("[ 25 ] GYEVHA BOTS TIGA")
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
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    line.sendMessage(to, str(helpMessage))
                    line.sendContact(to, "ue32b11986d8e9e5cf70b642cf7ba88ff")
                    line.sendMessage(to,"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == 'help 1':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                    line.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == 'help 2':
                    helpTranslate = helptranslate()
                    line.sendMessage(to, str(helpTranslate))
                    line.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "Cek Speed...")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':    
                    line.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    line.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "login bot selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u104e95aaefb53cf411f77353f6a96ece"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╭════════╬♥╬════════╮\nStatus Bots\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╰════════╬♥╬════════╯\n\nGYEVHA BOTS╭════════╬♥╬════════╮\n╰════════╬♥╬════════╯"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╭════════╬♥╬════════╮\n ║͜͡☆➣ ♥ Status Bots ♥\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ Protect ✅"
                        else: ret_ += "║͜͡☆➣  Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ Qr Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ Invite Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ Cancel Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✅"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✅"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰════════╬♥╬════════╯\n╭════════╬♥╬════════╮\n  ║͜͡☆➣ ♥ GYEVHA BOTS ♥\n╰════════╬♥╬════════╯"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                        
                elif msg.text.lower().startswith("spaminvite "):
                   #if msg._from in admin:
                    dan = text.split("|")
                    userid = dan[0]
                    namagrup = dan[0]
                    jumlah = int(dan[0])
                    grups = line.groups
                    tgb = line.findContactsByUserid(userid)
                    if jumlah <= 10000000:
                        for var in range(0,jumlah):
                            try:
                                line.createGroup(str(namagrup), [tgb.mid])
                                for i in grups:
                                    grup = line.getGroup(i)
                                    if grup.name == namagrup:
                                        line.inviteIntoGroup(grup.id, [tgb.mid])
                                        line.sendMessage(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            except Exception as Nigga:
                                line.sendMessage(to, str(Nigga))
                            #else:
                                line.sendMessage(to, "@! kebanyakan njer!!", [sender])
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                line.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    
                elif msg.text.lower().startswith("ownerdel "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                line.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                        if Owner == []:
                            line.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            line.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠PHANTOM GHOST\n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +line.getContact(mi_d).displayName + "\n"
                            line.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~nunu_kap123 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                line.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                line.sendMessage(msg.to,"Added Target Fail !")
                                break
                    
                elif msg.text.lower().startswith("admindel "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                line.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
              #      else:
               #         gye.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                #    if msg._from in Owner:
                        if admin == []:
                            line.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            line.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠PHANTOM GHOST\n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +line.getContact(mi_d).displayName + "\n"
                            line.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~nunu_kap123 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Already On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Set To On")
                                
                elif text.lower() == 'protect off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Already Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Set To Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Qr Already On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Qr Set To On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Qr Already Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Invite Already On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Invite Set To On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'pro on':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["join link"] = True
                        line.sendMessage(msg.to,"Join link on")
                        line.sendMessage(msg.to,"Qrprotect on")
                        line.sendMessage(msg.to,"Protect on")
                        line.sendMessage(msg.to,"Inviteprotect on")
                        line.sendMessage(msg.to,"Cancelprotect on")
                        line.sendMessage(msg.to,"➲ All Protect Set To On")
                        		            
                elif text.lower() == 'pro off':
             #       if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        line.sendMessage(msg.to,"Qrprotect Off")
                        line.sendMessage(msg.to,"Protect Off")
                        line.sendMessage(msg.to,"Inviteprotect Off")
                        line.sendMessage(msg.to,"Cancelprotect Off")
                        line.sendMessage(msg.to,"➲ All Protect Set To Modar")
            #        else:
             #           gye.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
             #     if msg._from in Owner:    
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                #  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
               #   if msg._from in Owner:
                    settings["autoLeave"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
             #     if msg._from in Owner:
                    settings["autoLeave"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'join link on':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'join link off':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif msg.text.lower() == 'cekk':
                        line.sendContact(to, lineMID)
                        ki1.sendContact(to, ki1MID)
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        ki5.sendContact(to, ki5MID)
                        ki6.sendContact(to, ki6MID)
                        ki7.sendContact(to, ki7MID)
                        ki8.sendContact(to, ki8MID)
                        ki9.sendContact(to, ki9MID)
                        ki10.sendContact(to, ki10MID)			
                elif text.lower() in ["balik"]:    
                    #gye.leaveGroup(msg.to)
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
                elif text.lower() in ["aku pamit yah"]:    
                    line.leaveGroup(msg.to)
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
                elif text.lower() in ["halo"]:    
                    G = line.getGroup(msg.to)
                    ginfo = line.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    invsend = 0
                    Ticket = line.reissueGroupTicket(msg.to)
                    ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki6.acceptGroupInvitationByTicket(msg.to,Ticket)    
                    ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki9.acceptGroupInvitationByTicket(msg.to,Ticket)	
                    ki10.acceptGroupInvitationByTicket(msg.to,Ticket)	    
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    line.updateGroup(G)
#~~~~~~~~~~~~~~~~~~~~~~~~~เขียนโดย ༄۞ꪶꪶꪣꪫꪊ۞࿐  ~~~~~~~~~~~~~~~~~~~~~~~~~~~#             
                elif text.lower() == 'me':
                    sendMessageWithMention(to, gyeMID)
                    line.sendContact(to, lineMID)
                    line.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                elif text.lower() == 'mymid':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
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
                elif msg.text.lower().startswith("midnya "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
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
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
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
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            line.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        line.updateProfile(gyeProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Target ditambahkan!")
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
                            line.sendMessage(msg.to,"Target dihapuskan!")
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
                            line.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'gt':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            line.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'gt on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'gt off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
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
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
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
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                        settings["blacklist"] = {}
                        line.sendMessage(msg.to,"➲ Done")
                        ki1.sendMessage(msg.to,"➲ Done")
                        ki2.sendMessage(msg.to,"➲ Done")
                        ki3.sendMessage(msg.to,"➲ Done")
                        ki4.sendMessage(msg.to,"➲ Done")
                        ki5.sendMessage(msg.to,"➲ Done")
                        ki6.sendMessage(msg.to,"➲ Done")
                        ki7.sendMessage(msg.to,"➲ Done")
                        ki8.sendMessage(msg.to,"➲ Done")
                        ki9.sendMessage(msg.to,"➲ Done")
                        ki10.sendMessage(msg.to,"➲ Done")
                        ki1.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki2.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki3.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki4.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki5.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki6.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki7.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki8.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki9.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki10.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki10.sendMessage(msg.to,"➲ Jangan Jadi Penjahat yah kakak Agar Tak Masuk Blaclist ku")
                        
                elif text.lower() == 'absen':
                        line.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 1")
                        ki1.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 2")
                        ki2.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 3")
                        ki3.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 4")
                        ki4.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 5")
                        ki5.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 6")
                        ki6.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 7")
                        ki7.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 8")
                        ki8.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 9")
                        ki9.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 10")
                        ki10.sendMessage(msg.to,"➲  ༄۞ꪶꪶꪣꪫꪊ۞࿐ 11")
                        line.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                        
                elif text.lower() == 'bancontact':
                        settings["wblacklist"] = True
                        line.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        line.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                        if settings["blacklist"] == {}:
                            line.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            line.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, line.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            line.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("ciak "):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ciak all member':
                 #   if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            #gs = gye.getGroup(msg.to)
                            gs = ki1.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
                            gs = ki5.getGroup(msg.to)
                            gs = ki6.getGroup(msg.to)
                            gs = ki7.getGroup(msg.to)
                            gs = ki8.getGroup(msg.to)
                            gs = ki9.getGroup(msg.to)
                            gs = ki10.getGroup(msg.to)
                           #gye.sendMessage(msg.to,"「 Bye All 」")
                           #gye.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    line.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'tag':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
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
                                line.sendMessage(msg.to,"Lurking already on")
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
                            line.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                            
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
                        line.sendMessage(msg.to,"Lurking already off")
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
                        if read["ROM"][receiver].items() == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
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
                        
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] GYEVHA BOTS KICK")
            try:
                if op.param3 in lineMID:
                    if op.param2 in ki10MID:
                        G = ki10.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki10.updateGroup(G)
                        invsend = 0
                        Ticket = ki10.reissueGroupTicket(op.param1)
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
#-------------------------------------------------------------------------------[gyeMID - ki2MID]
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

#-------------------------------------------------------------------------------[gyeMID - ki3MID]
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
#-------------------------------------------------------------------------------[gyeMID - ki4MID]
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
#===============================================================================[kiMID gyeMID]
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
#-------------------------------------------------------------------------------[kiMID ki2MID]
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
#-------------------------------------------------------------------------------[kiMID ki3MID]
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
#-------------------------------------------------------------------------------[kiMID ki4MID]
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
#===============================================================================[ki2MID gyeMID]
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

#-------------------------------------------------------------------------------[ki2MID kiMID]
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
#-------------------------------------------------------------------------------[ki2MID ki3MID]
#-------------------------------------------------------------------------------[ki2MID ki4MID]

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
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    line.sendMessage(op.param1,"Jangan Buka Qr")
            else:
                line.sendMessage(op.param1,"")
#==============================================================================#
       # if op.type == 55:
        #    print ("[ 55 ] GYEVHA BOTS EMPAT")
         #   if op.param1 in read["readPoint"]:
          #      _name = gye.getContact(op.param2).displayName
           #     tz = pytz.timezone("Asia/Jakarta")
           #     timeNow = datetime.now(tz=tz)
            #    timeHours = datetime.strftime(timeNow," (%H:%M)")
             #   read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
     #   backupData()
    #except Exception as error:
     #   logError(error)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["join ticket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = line.findGroupByTicket(ticket_id)
                        line.acceptGroupInvitationByTicket(group.id,ticket_id)
                        line.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        line.acceptGroupInvitation(op.param1)
        ki1.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
        ki5.acceptGroupInvitation(op.param1)
        ki6.acceptGroupInvitation(op.param1)
        ki7.acceptGroupInvitation(op.param1)
        ki8.acceptGroupInvitation(op.param1)
        ki9.acceptGroupInvitation(op.param1)
        ki10.acceptGroupInvitation(op.param1)
    except Exception as e:
        line.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        line.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
