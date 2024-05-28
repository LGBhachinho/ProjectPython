# Epreuve de code "Convertisseur"

"""
1 pouce = 2.54 cm
1 cm = 0.394 pouces

Exemple :
Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)

Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en reprécisant l'unité)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme.
"""

"""
effectuer_conversion : Cette fonction convertit les unités unit1 vers unit2

Return :
 True : L'utilisateur ne veut plus convertir (sortir du programme)
 False : L'utilisateur a donné une valeur à convertir
"""
def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    # Menu : choix de la conversion
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("Votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")

while True:
    # Demander les valeurs à convertir à l'utilisateur
    if choix == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54):
            break
    if choix == "2":
        if demander_et_afficher_conversion("cm", "pouces", 0.394):
            break




