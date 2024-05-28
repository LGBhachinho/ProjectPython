

import random


# Petit programme pour savoir qui fera un cadeau a qui pour noel pour les grande famille qui
# Veullent pas faire de cadeau a tout le monde ^^
"""
# Demander les particpants au tirage au sort
participant_init=[]


while True:
    add_participant=input("Quel est le nom de la personne a ajouter ? : ")
    if  add_participant == "fin":
        break
    participant_init.append(add_participant)

#print(random.choice(participant),"------>",(random.choice(participant)))
participant_rest=participant_init
num_participant=len(participant_init)
for i in range(len(participant_init)):
    choice_random_1=random.choice(participant_rest)
    choice_random_2=random.choice(participant_rest)
    if not choice_random_1==choice_random_2:
        print(choice_random_1,"------->",choice_random_2)
        participant_rest.remove(choice_random_1)
 #   print(participant_rest)

print(len(participant_init))


import random

# Demander à l'utilisateur d'entrer les noms des personnes séparés par des virgules
noms = input("Entrez les noms des personnes séparés par des virgules : ")
personnes = [nom.strip() for nom in noms.split(",")]

# Créer un dictionnaire pour enregistrer les couples
couples = {}


# Fonction pour vérifier les couples dans la liste des personnes
def trouver_couples():
    couples.clear()
    couples_list = input("Entrez les couples séparés par des virgules (ex: Alice,Bob;Charlie,David;Eva,Frank) ou appuyez sur Entrée pour passer : ")
    if couples_list:
        couples_pairs = [couple.strip().split(",") for couple in couples_list.split(";")]
        print("Couples entrés :", couples_pairs)  # Afficher les couples pour débogage
        for couple in couples_pairs:
            if len(couple) == 2:
                couples[couple[0]] = couple[1]
                couples[couple[1]] = couple[0]
            else:
                print(f"Erreur dans le couple {','.join(couple)}. Assurez-vous d'entrer deux noms.")


# Vérifier les couples initiaux
trouver_couples()

# Tirage au sort
random.shuffle(personnes)
for i in range(len(personnes)):
    current_person = personnes[i]
    next_person = personnes[(i + 1) % len(personnes)]

    # Vérifier si les deux personnes sont en couple
    while couples.get(current_person) == next_person:
        random.shuffle(personnes)
        next_person = personnes[(i + 1) % len(personnes)]

    print(f"{current_person} offre un cadeau à {next_person}")
"""

import tkinter as tk
import random

root = tk.Tk()
root.title("Tirage au sort des cadeaux")

# Fonction pour réaliser le tirage au sort
def tirage():
    personnes_list = personnes_entry.get().split(",")
    couples_list = couples_entry.get().split(";")

    personnes = [nom.strip() for nom in personnes_list]
    couples = {}

    for couple in couples_list:
        names = couple.split(",")
        if len(names) == 2:
            couples[names[0].strip()] = names[1].strip()
            couples[names[1].strip()] = names[0].strip()

    random.shuffle(personnes)
    results = []
    for i in range(len(personnes)):
        current_person = personnes[i]
        next_person = personnes[(i + 1) % len(personnes)]
        while couples.get(current_person) == next_person:
            random.shuffle(personnes)
            next_person = personnes[(i + 1) % len(personnes)]
        results.append(f"{current_person} offre un cadeau à {next_person}")

    result_label.config(text='\n'.join(results))

# Création des éléments d'interface
personnes_label = tk.Label(root, text="Entrez les noms des personnes séparés par des virgules :")
personnes_entry = tk.Entry(root)

couples_label = tk.Label(root, text="Entrez les couples séparés par des points-virgules (ex: Alice,Bob;Charlie,David) :")
couples_entry = tk.Entry(root)

tirage_button = tk.Button(root, text="Effectuer le tirage au sort", command=tirage)

result_label = tk.Label(root, text="", wraplength=400)

# Placement des éléments dans la fenêtre
personnes_label.pack()
personnes_entry.pack()
couples_label.pack()
couples_entry.pack()
tirage_button.pack()
result_label.pack()

root.mainloop()
