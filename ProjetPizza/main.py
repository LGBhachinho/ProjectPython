
#Afficher liste pizza par ligne


def tri_personnalise(e):
    return len(e)

def afficher(collection,nbre=-1):
    print(f"-------LISTE DES PIZZA  ({len(collection)})------")

    collection.sort(reverse=True, key=tri_personnalise)
    if len(collection)==0:
        print("Acune Pizza")
        return
    if not nbre==-1:
        c = collection[0:nbre]
    else :
        c= collection
    #Afficher pizza 1 par ligne
    for i in c:
        print(i)
    print("Premiere pizza : " + c[0])
    print("Derniere pizza : " + c[-1])



pizzas=["4 fromages", "végétarienne", "Hawai", "Calzone"]
#vide=()
#Ajouter pizza utilisateur

#Pizza existe --> Bool
#True la pizza existe ---> print la pizza existe deja
#False elle n existe pas --> apend

def ajouter_pizzas_utilisateur(collection):
    pizza_ajouter=input("Quel pizza voulez vous ajouter ? :")
    if not pizza_ajouter in collection:
        collection.append(pizza_ajouter)
    else:
        print("Erreur pizza deja existante")


#lower() --> minuscule
#upper() --> majuscule

### Appel fonction
nbre_affiche=3
ajouter_pizzas_utilisateur(pizzas)
afficher(pizzas,3)