# Utilise une image de base Python légère
FROM python:3.9-slim

# # Installer les dépendances
# RUN pip install watchdog

# # Copier le script dans le conteneur
# COPY scriptFolderTransferEmby.py /app/scriptFolderTransferEmby.py

# # Définir le dossier de travail
# WORKDIR /app

# # Commande pour lancer le script
# CMD ["python", "scriptFolderTransferEmby.py"]


# # Utiliser une image de base Python
# FROM python:3.9

# Définir le dossier de travail dans le conteneur
WORKDIR /app

RUN mkdir -p /app/log
RUN mkdir -p /app/source
RUN mkdir -p /app/destination

# Copier le contenu de ton projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir les variables d'environnement pour le fichier .env
ENV TMDB_API_KEY=${TMDB_API_KEY}

# Lancer ton application
CMD ["python", "scriptFolderTransferEmby.py"]
