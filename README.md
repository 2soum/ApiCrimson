
# ApiCrimson

ApiCrimson est un projet API basé sur Python qui intègre Firebase pour l'authentification des utilisateurs et les opérations de base de données en temps réel. Ce README fournit des instructions détaillées sur la configuration, l'exécution et l'utilisation du projet.

## Table des Matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Déploiement avec Docker](#déploiement-avec-docker)
- [Endpoints](#endpoints)
- [Licence](#licence)

## Prérequis
- Python 3.8+
- Docker (optionnel, pour le déploiement en conteneur)
- Compte et projet Firebase

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/2soum/ApiCrimson.git
   cd ApiCrimson
   ```

2. **Créer et activer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scriptsctivate`
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Configurer Firebase :**
   - Créez un projet Firebase sur [Firebase Console](https://console.firebase.google.com/).
   - Ajoutez un fichier `firebaseConfig.json` à la racine du projet avec les informations de configuration Firebase.

2. **Configurer les variables d'environnement :**
   - Créez un fichier `.env` en suivant l'exemple fourni dans `.env.example`.

## Utilisation

1. **Lancer le serveur :**
   ```bash
   python app.py
   ```

2. **Accéder à l'API :**
   - L'API sera disponible à `http://localhost:5000`.

## Déploiement avec Docker

1. **Construire l'image Docker :**
   ```bash
   docker build -t flask-firebase-app .
   ```

2. **Lancer le conteneur Docker :**
   ```bash
   docker run -p 5001:5001 flask-firebase-app
   ```

## Endpoints

### Authentification
- **POST /signup**: Inscription d'un nouvel utilisateur
- **POST /login**: Connexion d'un utilisateur existant

### Utilisateurs
- **GET /users**: Récupérer la liste des utilisateurs
- **GET /users/<id>**: Récupérer les détails d'un utilisateur par ID

### Exemples de Requêtes
- **Inscription :**
   ```bash
   curl -X POST http://localhost:5000/signup -d '{"email":"user@example.com", "password":"password123"}'
   ```

- **Connexion :**
   ```bash
   curl -X POST http://localhost:5000/login -d '{"email":"user@example.com", "password":"password123"}'
   ```

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

Pour plus de détails et les dernières mises à jour, veuillez consulter le [dépôt GitHub](https://github.com/2soum/ApiCrimson).
