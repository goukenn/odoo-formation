# Python

## Créer par Guido Van Rossum

## Aborescense

### __pycache__
- Stocke l’ensemble des fichiers compilé

### __init__.py
- Defini la présence d’un module. Son contenu défini le module lui même. Le fichier “.py” du dossier définisse les membres du module.

## Installation

### Unix
- -apt-get install python
- -apt-get install python3
- -apt-get install pip
- -apt-get install python3-setuptools
- -pip install pyvenv
- -apt install python3.8-venv
- -pip install bpython
	- Invite de command avec coloration syntaxique
- -apt-get install ipython3
	- Invite de commande avancé
	- >pip install notebook

### Windows
- https://python.org/downloads

### VSCode
- Extension: python
- Extension: Python Environment Manager

## Algorightmique

### casting

### boucle

### exception

## if __name__ == "__main__":  
      run()

## Syntaxe

### Mots réserver
- if
- and
- or
- in
- for
- else
- not
- True
- False
- import
	- Importe un module défini dans l’arborescense ou système.
- try
- except
- as
- elif
- pass
	- Passer une exception
	- Passer la def d une fonction
- break
- while
- def
- return
- del
- assert
- self
- None
	- Void du langage
- global
- async
- await
- raise
	- Permet de générer une exception
- yield
- with
- finally
- is
- continue
- from
- lamda
- nonlocal

### Opérateurs
- Arithmétique
	- +,-,/,*,
	- +=, -=, *=, /=
	- **
	- <<, >>
	- /, //
	- &, |, 
	- ^
- logique
	- <,<=,>,>=
	- ==, !=
	- and, or
	- not
- Assesseur d’Object
	- .
- affectation
	- = utilisé
	- Affectation multiple séparer par des “,”. Exemple : x, y = 23, 19
	- “:=“ est ajouté dans python 3.8. affecter et utiliser la valeur.
- concatenation
	- “+” utilisé pour concatener deux chaine de caractère
- Tester dans une chaine
	- A in B
- indexation
	- []
- del
- ->
- Multiline instruction
	- “\” a la fin de la ligne
- Décorateur @
- Test sur un object
	- is
	- is not
- with … as var 

### Instruction
- “:” termine une instruction et identation

### Identation Importante

### Fonction
- Déclaration de fonction avec le mot “def”
- "return" permet de renvoyer une valeur
- On peux définir des valeurs par defaut
- Fonction anonyme
	- lambda x[,…]: result 
- Forcer le dommage des paramètres. Placer après *
	- def info(x,y,*,z): 

### Variable
- Declaration directe par le nom
- Python ne supporte pas de constante

### Sensible à la case

### Commentaire
- “#” Sur une ligne 

### Documenter
- Une triple chaine non assigné constitue la documentation
	- def method():  
	      """  
	      permet le chargement de method  
	      """  
	      print("le chargement est effectué")

### Dictionnaire
- Notation json

### Nombre
- Hexadécimal
	- 0x…
- Floattan
	- 0.45
- Entier
	- 10

### Boucle et structure de control
- for … in datas:
- while condition: 
- async for … in datas: 
- Les générateurs : grâce à yield

### Liste
- Creation [] ou list()
- Possède un indice qui commence à 0
- Permet l’extraction
	- [index[:indice_de_fin[:pas]]]
- Mutable
- Quelque methodes
	- pop
	- remove
	- append
	- insert
	- extend

### Python3
- “->” Opérateur de fonction de class

### Classe
- Definie une class
- Surcharge utile
	- __init__(self[,…]) -> None
		- Constructeur de la classe
	- __str__(self)-> str
	- __add__(self, other)->self
	- __sub__(self, other)->self
	- __mul__(self, other)
	- __invert__(self)
		- Pour l’opérateur ~
	- __neg__(self)
		- Pour la négation
	- __rmul__(self, other)
	- __imul__(self, other)
		- Inlace multiplication
	- __enter__(self)
	- __exit__(self)
	- __doc__(self)
		- Retourne la documentation
	- __or__(self, other)
	- __xor__(self, other)
- héritage
	- Héritage multiple
	- Se fait à l’aide l’appel de la classe comme méthode
		- class Point2D(Point):  
		      def __init__(self, x, y) -> None:  
		          super().__init__(x, y)

### Tupples
- (X1,x2,…,xn)

### Les compréhensions
- Generator ( I for I in m)
- Liste [ i for i in m]
- Dictionnaire { i: for i in m }

### String
- Interpolation
	- “%s data” %(interpolate value,…)

### Set

### Destructuring
- A, b = [a,b]
-  a, *b= [a, b, c]
- *b, a= [a,b,c]

### Tenary opertor
- trueResult if condition else falseResult

## Environment Virtuel

## Commandes

### Command: python
- --version
- -O (désactive le mode de dubuggage )
- -c code

### Command: pip
- >pip freeze
- >pip install package_name[==version]
- >pip uninstall package_name
- >pip show package_name

### Command: pyvenv
- >pyvenv list
- >chmod 777 env_path/bin/activate
- Crée un environment virtuel
- >pyvenv create env_path
- >pyvenv remove env_path
- >source env_path/bin/activate
- >deactivate

### command: bpython

## Modules

### Aborescence contenant un fichier “__init__.py”
- Les modules sont importer en cascade et relatif au module en cour. 
- from module import * 
- import module [as newName] 

### builtins
- Module principale, nulle besoin de l’importer 
- Quelques fonctions
	- print
	- range
	- len
	- input
	- ord
	- chr
	- del
	- type
	- dir
	- getattr
		- Récupère la valeur d’un attribut. Sinon la valeur par défaut
	- open
	- help
	- exec
	- eval
	- set
- type
	- int
	- str
	- list
	- tuple
	- set

### sys

### random

### pickle

### sqlite

### sqlalchemy

### math

### unicodedata

### String

### pdb
- debugger

### keyword
- Manipulation des mots réserver de python.
- méthodes
	- kwlist
	- iskeyword

### os

### asyncore - < v3.4

### asyncio - = 3.5

### typing

### datetime
- Gestion et manipulation du temps
- Quelques méthodes
	- replace(self, ):date

### calendar
- Gestion et manipulation du calendier
- Quelques Methodes

### json
- JSon notation library
- Quelques Methods
	- dumps

### base64

### tarfile
- Outils d’aide a la compression
- Quelques methods
	- open
	- extractall

### ssl

### pycrypto*

### hashlib

### requests

### pandas

### 

## Fichiers

### .py code source

### .pyc code compiler

## Chaine de caractère

### Python ne fait pas de différence en “ et ‘

### Multi chaine
- Avec la triple notation ”””

### object

### Formattage
- String.format format à l’aide d’accolade de position {[position]}
- “%s” % data|[array]
- f" chaine à formater {variable}”

### concatenation
- +

### Quelques méthodes utiles
- lower
- upper
- count
	- Conter l’occurence dans une chaine
- index
	- Position dans la chaine
- find
- replace
- split
- join

### Tester la présence dans la chaine à l’aide l’opérateur “in”

## tools

### anaconda

### pycharm

### vscode

# Python and MYSQL

## >pip install pymysql

## >apt-get install mysql-client

## Import pymysql as mysql

## Mysql.connect(host=“IP”, user=“root”, passwd=“”, db=“”)


[build-in-function-documentation](https://docs.python.org/3/library/functions.html#callable)
