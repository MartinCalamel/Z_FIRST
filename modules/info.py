"""
Author: Martin Calamel
Created: 2025-02-26
Description: module pour afficher les information  
             avec des couleur en fonction de leurs types:
             * erreur
             * information
             * validation
TODO: 
"""



from colorama import Fore

class Info:
    def erreur(message : str) -> None:
        """
        # erreur
        ## Presentation
        Fonction pour afficher les erreurs
        ## Fonctionnement
        On initialise la couleur à rouge  
        On affiche le message  
        On remet la couleur a blanc par default  
        ##  Entrées
        * message : str, contenue du message a afficher  
        # Sorties
        Aucunes sortie
        """
        print(Fore.RED, message, Fore.RESET)
        return None
    
    def info(message : str) -> None:
        """
        # info
        ## Presentation
        Fonction pour afficher les informations
        ## Fonctionnement
        On initialise la couleur à bleu  
        On affiche le message  
        On remet la couleur a blanc par default  
        ##  Entrées
        * message : str, contenue du message a afficher  
        # Sorties
        Aucunes sortie
        """
        print(Fore.BLUE, message, Fore.RESET)
        return None
    
    def valide(message : str) -> None:
        """
        # valide
        ## Presentation
        Fonction pour afficher les validations
        ## Fonctionnement
        On initialise la couleur à vert  
        On affiche le message  
        On remet la couleur a blanc par default  
        ##  Entrées
        * message : str, contenue du message a afficher  
        # Sorties
        Aucunes sortie
        """
        print(Fore.GREEN+message+Fore.RESET)
        return None