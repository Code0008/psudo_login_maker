import make_login as mk
import threading
import sys


def main():
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
    works=[mk.opene, mk.createfile, mk.x]
    
    try:
        for n in works:
            hilo=threading.Thread(target=n, args=(url,))
            hilo.start()
            tareas.append(hilo)
    except KeyboardInterrupt as e:
        print(f"{e}Proceso terminado por el usuario")

if __name__ == '__main__':
    main()
