

def element_dasn_liste(e,l):
    """ for element in l:
       if e.lower()==element.lower():
            return True"""

    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower


noms = ["Jean","sophie","Martin","Christophe","Zoe","Marin"]
noms1 = ["Jean","ruddy","Martine","Christophe","Zoeeee","Marin"]
noms2 = ["J","ruddy","Mart","Christ","Zo","Mar"]

if element_dasn_liste("jEan",noms):
    print("Jean est la")
else:
    print("jean n est pas la")

# Nombre total de caractere
# For / len

nbre_caractere=0
for n in noms:
    nbre_caractere+=len(n)
print(nbre_caractere)

#completion / somme (sum)

nbre_noms1_liste=[len(n) for n in noms1]
print(sum(nbre_noms1_liste))

#join / len
print(len("".join(noms2)))



a = [1, 2, 3]
b = [4, 5, 6]

c = a.extend(b)
print(c)

