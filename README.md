# Projet 12 - Développez une architecture back-end sécurisée en utilisant Django ORM - OpenClassrooms 

Cette application permet de gestioner la relation client (CRM) de l'entreprise *Epic Events*, qui effectue le suivi de tous les clients et événements.

## Mise en place du projet

#### I) Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet :

    $ git clone https://github.com/Appryll/Projet-12-D-veloppez-une-architecture-back-end-s-curis-e-en-utilisant-Django-ORM.git

    Se déplacer dans le repertoire du projet :

    $ cd Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST-master

###### -Créer et activer l'environnement virtuel :
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis :
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python manage.py runserver <your_port>

###### - Naviguer sur le site :
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel :
    deactivate

-----
#### II) MacOS, Linux :
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet :
     $ git clone https://github.com/Appryll/Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST.git

    Se déplacer dans le repertoire du projet :
    $ cd Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST-master

###### -Créer et activer l'environnement virtuel :
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis :
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python3 manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python3 manage.py runserver <your_port>

###### - Naviguer sur le site :
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel :
    deactivate

------------------------------------------------------------------------------------------------------------------------
## Installer la base de données Postgresql  

###### - Télécharger et installer le package :

    Download [PostgreSQL](https://www.postgresql.org/download/) Installer. 

###### - Connectez-vous à la base de données PostgreSQL à l'aide du shell SQL (psql) :

    CREATE DATABASE EpicEvents; 

(Attention! ne changez pas le nom de la base de données )

Plus d'info -> [Documentation PostgreSQL](https://www.postgresql.org/docs/)

------------------------------------------------------------------------------------------------------------------------
###### - Générer un rapport flake8 :

    $ flake8 --format=html --htmldir=flake8_rapport

------------------------------------------------------------------------------------------------------------------------

### Diagramme de cas d'utilisation avec les roles et les autorisations de chaque utilisateur

<img src="img/Diagramme de cas d'utilisation.png" width="400" height="450">

------------------------------------------------------------------------------------------------------------------------

### Documentation de l'API

#### [Documentation Postman](https://documenter.getpostman.com/view/21413114/VUxKVAUs) 
------------------------------------------------------------------------------------------------------------------------

### Suivi des erreurs et des exceptions 

Toutes les erreurs et exceptions rencontrées par l'application sont suivies sur le projet [Sentry](https://sentry.io/welcome/) associé.

