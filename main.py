import requests
import os 
import webbrowser
import threading
import sys
## funciones abajo
def createfile(url):
    x = requests.request('GET',url )
    texts=x.text
    with open('login.html', 'w', encoding='utf8') as login:
        login.write(str(texts))   
opene= lambda D: webbrowser.open('http://localhost:8080/scraping/login.html')
x= lambda D: os.system("python3 -m  http.server 8080")
## funciones arrriba

if __name__ == '__main__':
    try:
        url=input("[+] Ingrese la URL: ")
        urlv= lambda url: url if 'http:' or 'https:' in url else 'x'
        if urlv(url):print("URL CORRECTA")
        else: print("url incorrecta"), sys.exit(1)
    except ValueError as v:
        print(f'Ingresa corretamente la url oe')
    except KeyboardInterrupt as k:
        print(f'Interferida por el usuario')
tareas=[]
works=[opene, createfile, x]
try:
    for n in works:
        hilo=threading.Thread(target=n, args=(url,))
        hilo.start()
        tareas.append(hilo)
except KeyboardInterrupt as e:
    print(f"{e}Proceso terminado por el usuario")
