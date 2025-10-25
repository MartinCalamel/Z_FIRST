# Z_FIRST
Z_FIRST un project de développement d'un virus informatique non fonctionnel.  
Il ne s'agit que d'une base avec beaucoup trop de contrainte pour que le virus soit effectif.  
**Auteur** : [MartinCalamel](https://github.com/MartinCalamel)
## Sommaire
1) [Installation](#Installation)
2) [Usages](#Usages)
## Installation
Pour installer il suffit de cloner le repertoire github :
```
git clone 
```
  
Ou télécharger le repos
### Prérequis
#### Logiciel
**Node**  
Dans son fonctionnement Z_FIRST utilise Node.js  
Il faut donc installer Node avant utilisation.  
Pour installer Node.js:
- Via le site [Node.js](https://nodejs.org/en/download)
- En ligne de commande :  
```
# Download and install fnm:
winget install Schniz.fnm
# Download and install Node.js:
fnm install 22
# Verify the Node.js version:
node -v # Should print "v22.14.0".
# Verify npm version:
npm -v # Should print "10.9.2".
```
**Python**  
Il faudra aussi évidement le logiciel python.  
Pour ceux qui n'auraient pas encore installer python voici le lien vers le site [python](https://www.python.org/downloads/)
#### Les prérequis python
Il faudra aussi installé les modules python pour faire fonctionner le logiciel.  
Pour installer les modules :
```
pip install -r requirements.txt
```

## Usage
### lancement
Pour lancer l'application il suffit d'ouvrir `reverse.py`  
Ou en ligne de commande :
```
python3 reverse.py
```
### utilisation
Lorsque vous ouvrirez l'application vous arriverez sur un menu vous proposant de :
* Infecter une nouvelle victime
* Se connecter sur une ancienne victime  

si vous l'utilisez pour la première fois il faudra évidement d'abord infecter une victime.

En choisissant la première option, l'application vas créer un programme `payload.bat` qui devra être envoyer à la victime pour qu'elle l'ouvre. après cela elle se mettra en attente de la victime.

Quand la victime ouvrira le programme `payload.bat`, ses pare-feu seront désactivé, elle nous enverra son adresse IP et un serveur python s'installera sur sa machine prenant la forme d'un *reverse shell*.

Coté attaquant, après avoir reçu l'adresse IP nous tenterons de nous connecter au serveur. Une fois cette connexion établit il est possible d'utiliser toutes les commandes cmd windows.

En plus de cela l'application possède des fonctions spéciales :
| fonction | description |
| --- | --- | 
| cam | Ouvre la caméra de la victime |
| exit | Ferme la connexion coté attaquant laissant le serveur victime ouvert|
| fin | Éteint le serveur de la victime |


