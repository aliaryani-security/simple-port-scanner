#!/usr/bin/env python3

import socket
import time

start_time = time.time()

target = input ("specify the host to scan: ")
target_ip = socket.gethostbyname(target)
print ("initializing scan for : {} ({})".format(target, target_ip))

for i in range (1,1000):
    scanner = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    conn = scanner.connect_ex ((target_ip, i))
    if conn == 0:
        print (f"[+] Port {i} open")
    scanner.close()