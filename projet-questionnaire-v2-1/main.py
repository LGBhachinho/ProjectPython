# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions


"""
    titre = question[0]
    choix = question[1]
    choix_bonne_reponse = question[2]
"""

def poser_question(question):
    global score
    choix = question[1]
    choix_bonne_reponse = question[2]
 #   titre_question, r1, r2, r3, r4, choix_bonne_reponse
    print("QUESTION")
    print("  " + question[0])

    for i in range(len(choix)):
        print(i+1,"- ", choix[i])
    print()
    reponse_str = input("Votre réponse compris entre 1 et" + str(len(choix)) +" : ")
    reponse_int=int(reponse_str)

    if choix[reponse_int-1].lower() == choix_bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
