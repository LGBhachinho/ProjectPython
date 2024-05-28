


import os
import time
import random


#Vous devez aussi gérer un score, initialement égal à 0, et qui s'incrémente de 1 à chaque bonne réponse.
#Quand l'utilisateur donne une mauvaise réponse, le programme s'arrête directement et affiche (exemple) :

#Mauvaise réponse, la séquence était : xxxx
#Votre score final : xx

####0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.
def nombre_magique(chiffre_al):
    if chiffre_al=="":
        a = str(random.randint(0, 9))
        b = str(random.randint(0, 9))
        c = str(random.randint(0, 9))
        d = str(random.randint(0, 9))
        chiffre_al=a+b+c+d
    else:
        a = str(random.randint(0, 9))
        chiffre_al=chiffre_al+a
    print("Retenez la sequence :")
    time.sleep(1)
    print(chiffre_al)
    time.sleep(3)
    os.system('cls')
    return chiffre_al

point=0
n=""
#nombre_magique(n)

#1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence
while True:
    n=nombre_magique(n)
    reponse = input("Entrer la reponse : ")
    if reponse == n:
        point +=1
        print(f"Bravo vous avez {point}  point ")
        time.sleep(1)
        os.system('cls')
        #nombre_magique(n)
        #continue
    else:
        print(f"Mauvaise réponse, la séquence était : {n} votre score final :  {point}  point ")
        break

#2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde

#3 - Afficher la séquence à mémoriser pendant 3 secondes

#4 - Nettoyer n'écran et demander la réponse à l'utilisateur

#5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1

#5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"