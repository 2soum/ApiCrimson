# Utiliser une image de base Python
FROM python:3.9-slim

# Installer Git
RUN apt-get update && apt-get install -y git

# Définir le répertoire de travail
WORKDIR /app

# Cloner le dépôt Git
RUN git clone https://github.com/2soum/ApiCrimson .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5000

# Définir la commande de démarrage
CMD ["python", "run.py"]
