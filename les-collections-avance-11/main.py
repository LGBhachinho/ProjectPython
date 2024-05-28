# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"


fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacancEs", "planning.ifr", "data.doc")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

"""definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}"""


'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''

# lower/upper 
# in / index / for
# split
# -1



# faire la correspondance définition
def find_extension(def_ext,ext):
    n=len(def_ext)
    for p in range (n):
        if ext == def_ext[p][0]:
            return def_ext[p][-1]



fichiers_minuscule = [i.lower() for i in fichiers]
fichiers_separe = [i.split(".") for i in fichiers_minuscule]

# extraire extension
for i in range (len(fichiers_separe)):
    extension_extrait=fichiers_separe[i][-1]
    extension_trouve=find_extension(definition_extensions,extension_extrait)
    if len(fichiers_separe[i]) <2:
        extension_trouve="Extension non trouve"
    if not extension_trouve:
        extension_trouve = "Extension inconnu"
    print(fichiers[i] + " ( " + extension_trouve + " ) ")


