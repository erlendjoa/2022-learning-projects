

from random import randint

def hovedpros():
    liste = []
    liste2 = []

    fil = open("privat/ordgjetting/ord.csv")
    ordliste = []
    for i in fil:
        lin = i.strip()
        ordliste.append(str(lin))

    riktig_ord = ordliste[randint(0,len(ordliste)-1)]
    for i in riktig_ord:
        liste.append(i)
    while len(liste) != 0:
        i = randint(0,len(liste)-1)
        liste2.append(liste[i])
        liste.pop(i)
    for i in liste2:
        print(f"{i}",end="")

    gjett_ord = input("\nGjett ord: ")
    if gjett_ord.upper() != riktig_ord.upper():
        print(f"Feil ord. Riktig ord var {riktig_ord}")
    else:
        print("Riktig ord!")
    print("\n")
    hovedpros()

hovedpros()