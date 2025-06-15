## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

# Documentation

[![Read The Doc link](https://python-oc-lettings-doc.readthedocs.io/en/latest/)](https://python-oc-lettings-doc.readthedocs.io/en/latest/)

# Installation

This guide will help you install and run the project on **Windows**, **Linux/macOS**, or using **Docker**.

---

## Windows

1. **Clone the repository:**

   ```powershell
   git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   ```

2. **Create a virtual environment and activate it:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```powershell
   python manage.py migrate
   ```

5. **Start the development server:**

   ```powershell
   python manage.py runserver
   ```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Linux / macOS

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Docker (using Docker Hub)

1. **Pull the image from Docker Hub:**

   ```bash
   docker pull hdandev/oc-lettings:latest
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 8000:8000 hdandev/oc-lettings:latest
   ```

3. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

**If you want to build the Docker image yourself:**

1. **Build the image:**

   ```bash
   docker build -t your-dockerhub-username/your-image-name .
   ```

2. **Push it to Docker Hub:**

   ```bash
   docker push your-dockerhub-username/your-image-name
   ```

# Linting

   ```bash
   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   flake8
   ```

# Tests

   ```bash
   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pytest
   ```

# Database

Start shell session:
   ```bash
   cd /path/to/Python-OC-Lettings-FR
   sqlite3
   ```

Connect to database:
   ```bash
   .open oc-lettings-site.sqlite3
   ```

Display tables:
   ```bash
   .tables
   ```

Display columns:
   ```bash
   pragma table_info(Python-OC-Lettings-FR_profile);
   ```

Custom query:
   ```bash
   select user_id, favorite_city from
   Python-OC-Lettings-FR_profile where favorite_city like 'B%';
   ```

End session:
   ```bash
   .quit
   ```

# Connect as administrator

[Admin login URL](http://localhost:8000/admin)

Username: `admin`
Password: `Abc1234!`
