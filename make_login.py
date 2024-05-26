import requests
import os 
import webbrowser


try:
    def createfile(url):
        x = requests.request('GET',url )
        texts=x.text
        with open('scraping/psudologinmaker/login.html', 'w', encoding='utf8') as login:
            login.write(str(texts))   
    opene= lambda D: webbrowser.open('http://localhost:8080/scraping/psudologinmaker/login.html')
    x= lambda D: os.system("python3 -m  http.server 8080")
except KeyboardInterrupt as e:
    print(f"{e}Proceso terminado por el usuario")



