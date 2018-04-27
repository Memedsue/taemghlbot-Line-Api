# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,urllib2,urllib3,subprocess,tempfile
import requests,urllib,json
from bs4 import BeautifulSoup
from gtts import gTTS
from threading import Thread
from urllib import urlopen

cl = LINETCR.LINE()
cl.login(token="EsmZDEVOSAFYnGMjV1pe.f6NMtPAP1WmKrSzRgriRpG.zpAxGrbmwGySedzGNUOgd0xTmU6GHw7L1lrvrmPVkD0=")
cl.loginResult()


print "SUKSES LOGIN KE ZiieYo V.6"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 

  ══════════════════
═════> 「тазм бнк вот」 <═════
  ══════════════════
[K on/off
[Join︎ on/off
[Leave︎ on/off
[Add on/off
[Share on/off
[Jam on/off
[Like on/off
[Welcome on/off
[Bye on/off
[Tag on/off : respon text
[Tag2 on/off: respon voice
[Sider on/off
════════════
        □ G R O U B □
════════════
[Id
[Group id
[Mid
[Me︎
[Creator
[Sp/Speed
[Up
[Curl
[Ourl
[Gurl
[Ginfo
[Cancel
[Jinlep
[Cancelall
[Bersihkan]
[Nk @
[Kill ban
[Ban︎:Share Contact
[Unban︎:Share Contact
[Ban @
[Unban @
[Banlist︎
[Invite :mid
[Kick :mid
[Gift
[Kibar/Play
[Liat
[Anu
[Creator grup/Owner grup
[Myname:tulis nama
[Mybio:「text」
[Copas pp @
[Backup
[Yank @
[Mid @
[Getid @
[Kontak @
[Hai @
[Spam anu @
[Spam on jmlh @
[Foto @]
[Midfoto mid
[Foto grup
[/musik text
[/lirik text
[/youtube text
[Jam berapa
[Kedapkedip @
[/say @
[Kapan @
[Apakah @
[Runtime
[Reboot
[Ifconfig
[System
[Kernel
[Gr on/off :Protect QR grup
[Cancl on/off :Cancel invite
[Joinn on/off :Kick member masuk
══════════════════
  ● http://line.me/ti/p/~memet1603 ●
══════════════════
"""

Setgroup =""" 

📃[Protect Group]
✒✒Gr on/off
📃[Cancel All Invited]
✒✒Cancl on/off
📃[No Joinned]
✒✒Joinn on/off
"""
DEF=[cl]
mid = cl.getProfile().mid

Bots=[mid]
admin=["u17a9e64e96a9d7032446c66b19122b3e"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add me kaka..",
    "lang":"JP",
    "comment":"Auto like by : ⊰•ZiieYo•﻿⊱ \n\n http://line.me/ti/p/YLmroWrxro",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"⊰•ᎎeƦᤉƧǟ•﻿⊱ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Wc":True,
    "Lv":True,
    "tag":True,
    "tag2":True,
    "Sider":{},
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['sepi']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = ("woooy jangan tag² " +cl.getProfile().displayName+" lagi anu\nKalo penting pm aja langsung\n「тазм бнк вот」")
                    jawaban = (jawab)
                    cl.sendText(msg.to,jawaban)                                                                                                                               

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag2"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = "Jangan tag gue, gue lagi anu, udah tanggung, lu ganggu, sue banget !"
                    jawaban = (jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mkp3')
                    cl.sendAudio(msg.to,'tts.mp3')

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in Bots:
                  group = cl.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        if op.type == 17:
          if wait["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nMoga Betah ya ka ^_^")
            cl.sendImageWithURL(op.param1,image)
            print 

        if op.type == 15:
          if wait["Lv"] == True:
                if op.param2 in Bots:
                     return
                cl.sendText(op.param1, "Papay kaka " + cl.getContact(op.param2).displayName + "\nMoga kau tenang di alam sana 😰😰")
                print 
                
        if op.type == 55:
                try:
                    if cctv['liat'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-) ")
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-) ")
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat... ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass


        else:
            pass
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                       
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Set group"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])

            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CREATOR SELFBOT 「тазм бнк вот」")
                msg.contentMetadata = {'mid': 'u17a9e64e96a9d7032446c66b19122b3e'}
                cl.sendMessage(msg)
            elif msg.text in ["Me","Aim"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Gak ada kaka dudul")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Ourl","Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done kaka dudul")
                    else:
                        cl.sendText(msg.to,"already open kaka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Curl","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done kaka dudul")
                    else:
                        cl.sendText(msg.to,"already close kaka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["K on","Contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka dudul")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka")
                    else:
                        cl.sendText(msg.to,"done kaka")
            elif msg.text in ["K off","Contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka kaka dudul")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
            elif msg.text in ["Join on","Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
            elif msg.text in ["Join off","Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                       cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka dudul")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Leave off","Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka dudul")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka dudul")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka dudul")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done kaka")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already kaka")
            elif msg.text in ["Auto like:off","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done kaka")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already kaka")

            elif msg.text in ["Welcome on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"auto welcome on kaka")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")

            elif msg.text in ["Welcome off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"udah di off kaka")


            elif msg.text in ["Bye on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Bye off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")

            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")

            elif msg.text in ["Tag2 on"]:
                if wait["tag2"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag2"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag2 off"]:
                if wait["tag2"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag2"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")

            elif msg.text in ["Set"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)

            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Add on","Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on kaka")
                    else:
                        cl.sendText(msg.to,"done kaka")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off kaka")
                    else:
                        cl.sendText(msg.to,"done kaka")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Comment on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"already on kaka")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Comment on","Comment off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"already off kaka")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done kaka")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off kaka dudul")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done kaka")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#-----------------------------------------------
            elif "sepi" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
#-----------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio : " + string + "")

#-----------------------------------------------
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
#-----------------------------------------------
            elif "Grup bc " in msg.text:
	        print "[Group Broadcast]"
	        bctxt = msg.text.replace("Grup bc ","")
		n = cl.getGroupIdsJoined()
		for people in n:
		    cl.sendText(people, (bctxt))

	    elif "Kawan bc " in msg.text:
	        print "[Friend Broadcast]"
	        bctxt = msg.text.replace("Kawan bc ","")
		n = cl.getAllContactIds()
	        for people in n:
	    	    cl.sendText(people, (bctxt))

#-----------------------------------------------
            elif "Jam berapa" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,"Udah jam " + datetime.today().strftime('%H:%M:%S'))
#-----------------------------------------------
            elif msg.text == "Liat":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Ketik Cek untuk liat sider")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "Anu":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, " %s\n\n|=======PELAKU=======|\n\n%s\n\nKetik Point untuk memperbaharui pelaku cctv..\npoint(｀・ω・´)\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "Sider ga bisa di read, Liat dulu dudul")

#-----------------------------------------------
            elif "Kang intip" in msg.text:
#	      if msg.from_ in admin:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Siap Om Cek Yang suka ngintip")
            elif "Sider off" in msg.text:
#	      if msg.from_ in admin:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom") 
#-----------------------------------------------
            elif "/say " in msg.text:
                say = msg.text.replace("/say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi","Mungkin tidak")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")

            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
#-----------------------------------------------
            elif "/lirik " in msg.text:
                try:
                    songname = msg.text.replace("/lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif "/wikipedia " in msg.text:
                  try:
                      wiki = msg.text.replace("/wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))

#-----------------------------------------------
            elif "/playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("/playstore ","")
                    cl.sendText(msg.to,"Loading")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"Done")
                    
            elif "/google " in msg.text:
                    a = msg.text.replace("/google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Loading")
                    cl.sendText(msg.to, "https://www.google.co.jp/search?q=" + b)
                    cl.sendText(msg.to,"Done")

#-----------------------------------------------
            elif msg.text == "Jalan":
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama:\n"+waktu(eltime)
                cl.sendText(msg.to,van)

            elif msg.text == "Reboot":
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text == "Ifconfig":
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text == "System":
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text == "Kernel":
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text == "Cpu":
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#-----------------------------------------------
            elif "/instagram " in msg.text:
                try:
                    instagram = msg.text.replace("/instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

            elif "/musik " in msg.text:
                try:
                    songname = msg.text.replace("/musik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))

            elif "/video " in msg.text:
                    try:
                        textToSearch = (msg.text).replace("/video ", "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "/youtube " in msg.text:
                    query = msg.text.replace("/youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print "[Command] Youtube"
#-----------------------------------------------
            elif "Midfoto " in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midfoto ","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass                

#-----------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getid @" in msg.text:
                 _name = msg.text.replace("Getid @","")
                 _nametarget = _name.rstrip(" ")
                 gs = cl.getGroup(msg.to)
                 for h in gs.members:
                   if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName + "\n[mid]:\n" + h.mid + "\n[StatusMessage]:\n" + h.statusMessage) 
                   else:
                     pass
            elif "Foto @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Foto @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"

            elif "Foto grup" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path) 

            elif "Kontak " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Gcreator","Creator grup","Owner grup"]:                                                 
                if msg.toType == 2:
                      msg.contentType = 13
                      ginfo = cl.getGroup(msg.to)
                      gCreator = ginfo.creator.mid
                      try:
                          msg.contentMetadata = {'mid': gCreator}
                          gCreator1 = ginfo.creator.displayName
                      except:
                          gCreator = "Error"
                      cl.sendText(msg.to, "Group Creator : " + gCreator1)
                      cl.sendMessage(msg)

#-----------------------------------------------
            elif "Spam anu @" in msg.text:
                _name = msg.text.replace("Spam anu @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Siap2 ya.. \n\( ö )/")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")  
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       cl.sendText(g.mid,"Tes spam !")
                       
                       cl.sendText(msg.to, "Kena dia kaka \nd=(´▽｀)=b")
                       print "Done spam" 

#------------------------------------------------
            elif "Yank @" in msg.text:
                _name = msg.text.replace("Yank @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Aku mau bilang sesuatu..")
                       cl.sendText(g.mid,"Sayank...")  
                       cl.sendText(g.mid,"Mungkin aku bukanlah cinta yang paling sempurna")  
                       cl.sendText(g.mid,"hanya sebatas hati yang ingin mencurah rasa padamu")
                       cl.sendText(g.mid,"karena mencintaimu adalah keindahan dilangit hatiku")
                       cl.sendText(g.mid,"dan dicintaimu adalah kesempurnaan kebahagiaan hatiku")
                       cl.sendText(g.mid,"Aku mencintaimu ")
                       cl.sendText(g.mid,"seperti bunga mencintai keharumannya")
                       cl.sendText(g.mid,"seperti hujan mencintai tetasan airnya")
                       cl.sendText(g.mid,"seperti bulan mencintai langit malamnya")
                       cl.sendText(g.mid,"seperti matahari yang mencintai cahayanya")  
                       cl.sendText(g.mid,"jantung ini takkan pernah berdetak selamanya")  
                       cl.sendText(g.mid,"tapi jika Tuhan mengizinkan")
                       cl.sendText(g.mid,"selama jantungku berdetak")
                       cl.sendText(g.mid,"ijinkan mencintaimu dalam ketulusan")
                       cl.sendText(g.mid,"Aku mencintaimu")
                       cl.sendText(g.mid,"bukan karena aku ingin memiliki apa yang ada di dirimu")
                       cl.sendText(g.mid,"hanya ingin melihatmu tersenyum")
                       cl.sendText(g.mid,"melukis rasa bahagia disetiap titian hidupmu")
                       cl.sendText(g.mid,"Aku mencintaimu")  
                       cl.sendText(g.mid,"bukan karena aku kagum pada dirimu")  
                       cl.sendText(g.mid,"hanya ingin membuatmu sempurna")
                       cl.sendText(g.mid,"meski aku tak pernah bisa sempurna")
                       cl.sendText(g.mid,"Aku mencintaimu")
                       cl.sendText(g.mid,"bukan kemarin atau saat ini")
                       cl.sendText(g.mid,"tapi percayalah")
                       cl.sendText(g.mid,"kemarin, kini dan nanti")
                       cl.sendText(g.mid,"adalah saat - saat dimana aku kan terus mencintaimu")

                       cl.sendText(msg.to, "Coba cek pm nya ya..")
                       print "Done puisi"

#------------------------------------------------

            elif "Hai @" in msg.text:
                _name = msg.text.replace("Hai @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Maaf kaka, dede tes dulu ya..")
                       cl.sendText(g.mid,"Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank")  
                       cl.sendText(g.mid,"Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank")  
                       cl.sendText(g.mid,"Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank")

#-----------------------------------------------
            elif msg.text in ["List group"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[~]%s\n" % (cl.getGroup(i).name   +str (len (cl.getGroup(i).members)))
                cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))

#-----------------------------------------------
            elif "Spam " in msg.text:
            	if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  
                   if txt[1] == "on":
                        if jmlh <= 500:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 500:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif msg.text in ["Jinlep"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Fuck You")
                        cl.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Bersihkan" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "Bersihkan semua member"
                    _name = msg.text.replace("Bersihkan","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ô")
                    cl.sendText(msg.to,"Eemmuuaaacchhh...")
                    cl.sendText(msg.to,"Lemes kan lu w cipok, papay..")
                    
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Group cleanse.")
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Succes")
                                    cl.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes")
                                except:
                                    cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes")
                            except:
                                cl.sendText(msg.to,"Succes")

#-----------------------------------------------
            elif msg.text in ["Backup"]:
                if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Backup Done")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
            elif "Copas pp @" in msg.text:
                if msg.from_ in admin:
                    print "[Copy] OK"
                    _name = msg.text.replace("Copas pp @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Tidak ditemukan...")
                    else:
                        for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Sukses mengkopi pp..")
                            except Exception as e:
                                print "Sukses copy pp"

#-----------------------------------------------
            elif msg.text in ["Kibar","Play"]:
                msg.contentType = 13
                cl.sendText(msg.to, "🍌MICI... MICI... MICIII...!!!\n\n🍌DEDE CENTIL HADIR DI GC ANDA🍌\n\n🍌DEDE CENTIL MAU NIKUNG DI GC INI DULU YEE🍌\n\n🍌DAPET TIKUNGAN BELAKANGAN, PENTING KIBAR DULU🍌\n\n⏬KETIKUNG PM DI OA KAMI NOH⏬\n\n[DM] DARK MOON\n\nhttp://line.me/ti/p/%40gfe4091t\n\n[DA] DARK ANGEL\n\nhttps://line.me/R/ti/p/%40bod3234v\n\n[KA] KUNVIL KILLER\n\nhttp://line.me/ti/p/%40com4798s")
                msg.contentMetadata = {'mid': 'u3f6341d797b849834252c86576bb8b5f'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u6d0b34f47f09c0732c2a7698b4984216'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uac3e5ee61208025d0c5cd57bcb24df03'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u029da567f478df363646fe9b9906e32f'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u4ca71a9ea642c40179a87b125062f9bc'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uf4b4ae38f00e02c200d0449ff40db645'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u6f28f70f8ea1d30d31341545ed2ecfea'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u3cf64007fbc25458a209852e3b9501d7'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u3b215495467690e17863cf28c876cb82'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "🍌JANGAN DI TANGKIS BEB, LEMESIN AJAHHH...🍌")

#KIBARAN BY VITHA
#-----------------------------------------------
            elif msg.text in ["Code","Unicode","Awas","Salken"]:
                cl.sendText(msg.to,"Salken kaka... Cipok ampe lemessss.... Eemmuuaacchhh... \n\n\n\n\n\n\n\n Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bankk.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.Bank.BankBank.Bank.Bank.Bank.Bank.Ban")

#SPAM UNICODE BY VITHA
#-----------------------------------------------
            elif "Vit say " in msg.text:
                string = msg.text.replace("Vit say ","")
                if len(string.decode('utf-8')) <= 50:
                    cl.sendText(msg.to," " + string + " ")
                    cl.sendText(msg.to," " + string + " ")
                    cl.sendText(msg.to," " + string + " ")

#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Waitttt...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Kecepatan anu: \n%s detik" % (elapsed_time))

#-----------------------------------------------
            elif "Kedapkedip " in msg.text:
                txt = msg.text.replace("Kedapkedip ","")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)
#-----------------------------------------------

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Gak ada dudul")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])

            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 55:
             try:
                 if op.param1 in wait2['readPoint']:
                     Nama = cl.getContact(op.param2).displayName
                     if Nama in wait2['readMember'][op.param1]:
                           pass
                     else:
                            wait2['readMember'][op.param1] += "\n|• " + Nama
                            wait2['ROM'][op.param1][op.param2] = "|• " + Nama
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                 else:
                        cl.sendText
             except:
                 pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   
                   
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
