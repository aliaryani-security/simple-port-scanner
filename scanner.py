#!/usr/bin/env python3

import socket
import time

start_time = time.time()

target = input ("specify the host to scan: ")
target_ip = socket.gethostbyname(target)
print ("initializing scan for : {} ({})".format(target, target_ip))