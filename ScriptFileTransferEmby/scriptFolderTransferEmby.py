import os
import re
import shutil
import requests
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv  # Importe dotenv

import logging

# Configurer le logger
LOG_FILE = "/app/log/script_log.txt"
logging.basicConfig(
    level=logging.DEBUG,  # Enregistre les messages de niveau DEBUG et plus élevés
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  # Log dans un fichier
        logging.StreamHandler()         # Log dans la console (facultatif)
    ]
)

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # Récupère la clé d'API depuis les variables d'environnement

if TMDB_API_KEY is None:
    raise ValueError("La clé d'API TMDB n'est pas définie. Assurez-vous qu'elle est bien présente dans le fichier .env.")


# Dossier source et dossiers de destination pour films et séries
SOURCE_DIR = "/app/source"  # Dossier à surveiller
FILMS_DIR = "/app/destination"
SERIES_DIR = "/app/destination"
 
logging.debug(f"Source path exists: {os.path.exists(SOURCE_DIR)}")
logging.debug(f"Destination path exists: {os.path.exists(FILMS_DIR)}")

# Ajouter du code pour vérifier que les fichiers sont détectés
files = os.listdir(SOURCE_DIR)
logging.debug(f"Files in source: {files}")


class VideoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
 # Log l'événement
        logging.info(f"Fichier détecté : {event.src_path}")
    
        # Extraction du titre et de l'année
        title, year = extract_title_and_year(event.src_path)

        if title:
            # Rechercher le film ou la série dans TMDb
            data = search_tmdb(title, year)
            if data:
                if 'media_type' in data and data['media_type'] == 'tv':
                    dest_folder = os.path.join(SERIES_DIR, sanitize_filename(data['name']))
                else:
                    dest_folder = os.path.join(FILMS_DIR, sanitize_filename(data['title']) + " (" + year + ")")

                # Créer le dossier s'il n'existe pas
                os.makedirs(dest_folder, exist_ok=True)
                logging.info(f"Dossier créé : {dest_folder + '(' + year + ')'}")
                
                # Déplacer le fichier
                dest_path = os.path.join(dest_folder, os.path.basename(event.src_path))
                while True:
                    try:
                        shutil.move(event.src_path, dest_path)
                        print(f"Déplacé dans {dest_path}")
                        logging.info(f"Transfer reussi Déplacé dans {dest_path}")
                        break
                    except PermissionError:
                        print(f"Attente : le fichier {os.path.basename(event.src_path)} est encore en cours d'utilisation...")
                        time.sleep(1)  # Attendre 1 seconde avant de réessayer
                        logging.error(f"Attente : le fichier {os.path.basename(event.src_path)} est encore en cours d'utilisation...")
                    except FileNotFoundError:
                        print(f"Erreur : le fichier source {os.path.basename(src_path)} n'a pas été trouvé.")
                        logging.error(f"Erreur : le fichier source {os.path.basename(src_path)} n'a pas été trouvé.")
                        break  # Sortir de la boucle si le fichier source n'existe plus
                    except shutil.Error as e:
                        print(f"Erreur de shutil : {e}")
                        logging.error(f"Erreur de shutil : {e}")
                        break  # Sortir de la boucle si une erreur de shutil se produit
                    except Exception as e:
                        print(f"Une erreur inattendue est survenue : {e}")
                        logging.error(f"Une erreur inattendue est survenue : {e}")
                        break  # Sortir de la boucle pour éviter une boucle infinie en cas d'erreur inattendue


def extract_title_and_year(filepath):
    filename = os.path.basename(filepath)
    filename = filename.rsplit('.', 1)[0]
    match = re.search(r"(.+?)(\d{4})", filename)
    if match:
        title = match.group(1).replace('.', ' ').strip()
        year = match.group(2)
        return title, year
    else:
        title = filename.split('.')[0]
        return title.replace('.', ' ').strip(), None

def search_tmdb(title, year=None):
    base_url = "https://api.themoviedb.org/3/search/multi" 
    params = {
        "api_key": TMDB_API_KEY,
        "query": title,
        "year": year
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            # Retourne le premier résultat correspondant au film ou à la série
            for result in results:
                if result["media_type"] in ["movie", "tv"]:
                    return result
        else:
            print("Aucun résultat trouvé pour ce titre.")
            logging.warning(f"Aucun résultat trouvé pour {title} ({year})")
    else:
        print("Erreur lors de la requête API:", response.status_code, response.json())
        logging.error(f"Erreur lors de la requête TMDb: {response.status_code} - {response.json()}")
    return None

def sanitize_filename(filename):
    # Remplacer les caractères invalides par un tiret
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

if __name__ == "__main__":
    # Configurer l'observateur pour surveiller le dossier source
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, SOURCE_DIR, recursive=False)
    observer.start()
    print("Surveillance du dossier activée...")
    logging.info("Surveillance du dossier activée...")

    try:
        while True:
            pass  # Maintient le script actif
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Surveillance interrompue par l'utilisateur.")
    observer.join()
