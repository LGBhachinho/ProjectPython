


# EXERCICE LISTE demander nom des personnes

# Demander nom et age
# boucler a l infini sauf si champs vide
"""
noms=[]

while True:
    nom=input("Quel est ton nom? : ")
    if nom == "":
        break
    noms.append(nom)

print("Le nom des personnes sont :")
noms.sort()  #tre par ordre alphabetique A-Z  a-z
for i in noms:
    print(i)
  """

# Exercice Liste ALGO : Valeur la plus petite
nom_chauffeur = ["Ruddy", "toto", "tata","titi","fefzef","gfregrg","ezfezf"]
distance_valeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
noms_et_distance=[("ruddy",1.2), ("titi",0.2), ("toto",4.2)]

#V2

nom_et_distance_min=noms_et_distance[0]
for nom_et_distance in noms_et_distance:
    if nom_et_distance[1]< nom_et_distance_min[1]:
        nom_et_distance_min=nom_et_distance
print("distance minimal",nom_et_distance_min[1]," No du chauffeur ",nom_et_distance_min[0])

#V1

"""for distance in distance_valeur_km:
    if distance < distance_min:
        distance_min=distance"""
#index min
index_min = 0
distance_min =distance_valeur_km[0]

for i in range (len(distance_valeur_km)):
    distance=distance_valeur_km[i]
    if distance < distance_min:
        distance_min=distance
        index_min=i
print("La distance minimal est: ",distance_min)
print("l index min est ",index_min)
print(nom_chauffeur[index_min])





