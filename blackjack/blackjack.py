

#blackjack mot maskinen. Laget før jeg lærte om objekter

from random import randint

startspoeng = 100                   #Definering av starts saldo
def blackjack(saldo):
    if saldo == 0:                  #Game over hvis saldo erlik 0
        print("Game Over")
        quit()

    fil = open("blackjack\kortikortstokk.csv")        #åpning av fil, forså å legge hver kodelinje inn i en tom liste
    kortstokk = []
    for x in fil:
        kortstokk.append(int(x))

    dinHånd = []                    #definering av ulike variabler og lister
    maskinHånd = []
    spesiellHånd1 = []
    spesiellHånd2 = []
    spillerSum = 0
    maskinSum = 0
    pottotal = 0

    def leggSaldo(x):                #returnerer en ny sum for din saldo (etter trukket fra veddemål)
        nySaldo = saldo - x
        return nySaldo

    def trekk_kort():                  
        nummer1 = randint(0, len(kortstokk))        #definerer et tilfeldig nummer fra 0 til len(kortstokk).
        if nummer1 == len(kortstokk):               #1 om tallet er siste tallet i range, siden tallet ikke kan brukes som gyldig indeks.
            nummer1 -= 1
        kort1 = kortstokk[nummer1]                  #henter verdi for kort1 ut fra kortstokk sin indeks, definert tilfeldig
        del kortstokk[nummer1]                      #fjerner elementet i lista, slik at det ikke kan bli valgt igjen
        nummer2 = randint(0, len(kortstokk))
        if nummer2 == len(kortstokk):                       #repeat...
            nummer2 -= 1
        kort2 = kortstokk[nummer2]
        del kortstokk[nummer2]
        listeMedKort = []  
        listeMedKort.append(kort1)                  #appender begge tall i tom liste og returnerer lista
        listeMedKort.append(kort2)
        return listeMedKort
    
    def trekk_et_til_kort(x, y):
        nummer3 = randint(0, len(kortstokk))        #funksjon som trekker kort på samme måte som forrige gang, men
        if nummer3 == len(kortstokk):               # appender de i en alledere eksisterende liste
            nummer3 -= 1
        kort3 = kortstokk[nummer3]
        print(f"{y} trakk kortet: {kort3}")
        del kortstokk[nummer3]
        x.append(kort3)

    def veddemålpros(x):
        x = input("Legg til veddemål: ")
        x = int(x)
        if x > saldo or x<1:                        #Skjekker om oppgitt nummer er innenfor maks saldo og 1
            print("Ugyldig input.")
            veddemålpros(x)
        else:
            return x

    print(f"Din saldo: {saldo}")
    pottotal = veddemålpros(pottotal)
    saldo = leggSaldo(pottotal)
    dinHånd.append(trekk_kort())
    maskinHånd.append(trekk_kort())
    spillerSum = dinHånd[0][0] + dinHånd[0][1]          #Definerer summen av elementene i listene
    maskinSum = maskinHånd[0][0] + maskinHånd[0][1]


    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    print(f"*   Potten står nå på {pottotal}p.") 
    print(" ")
    print(f"*   Dine kort: *{dinHånd[0][0]} , *{dinHånd[0][1]}        ")
    print(f"*   Maskinens kort: *{maskinHånd[0][0]}, *?          ")
    print(" ")

    start_runde2 = input("Tast inn 'h' for å trekke et kort, 'd' for å dobble, eller 'Enter' for å fortsette: ")
    if start_runde2 == "d":         #dobbler pottotal
        pottotal += pottotal
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"*   Potten står nå på {pottotal}p.") 
    while start_runde2 == "h":      #appender et til tilfeldig element fra kortstokk med funksjonen trekk_et_til_kort().
        trekk_et_til_kort(spesiellHånd1, "Du")
        start_runde2 = input("Tast inn 'h' for å trekke et kort eller 'Enter' for å fortsette: ")

    for e in dinHånd[0]:                #gjør om de to innviklede listene til 1 sammenhengende liste til brukeren
            spesiellHånd1.append(e)
    spillerSum = 0
    for e in spesiellHånd1:             #for-løkke som skjekker elementer i lista og plusser dem sammen
        spillerSum += e


    for e in spesiellHånd1:             #Om spiller har trukket en 11 (Ace), vil den ha mulighet til å velge om den skal være 1
        if e == 11:
            aceSpør = input("1 eller 11?: ")
            if aceSpør=="1":
                spillerSum -= 10
                spesiellHånd1.remove(e)
                spesiellHånd1.append(1)
                    
                    


    if spillerSum > 21:                 #Generelle blackjack regler for om maskin eller spiller vinner:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"* Maskinen vinner.")
        blackjack(saldo)
    elif spillerSum == 21:
        saldo += pottotal*2
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"* BlackJack! Spiller vinner.")
        blackjack(saldo)
    elif maskinSum > spillerSum and maskinSum > 16 and maskinSum != 22:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"Maskinens kort: *{maskinHånd[0][0]}, *{maskinHånd[0][1]}          ")
        print(f"Maskinen vinner.")
        blackjack(saldo)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    print(f"Din sum ligger nå på: {spillerSum}           >>>>>> Kort: {spesiellHånd1}")
    print(f"Maskinens sum ligger nå på: {maskinSum}      >>>>>> Kort: [{maskinHånd[0][0]}, {maskinHånd[0][1]}]")
    print(" ")
    input("Trykk enter for å fortsette: ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def maskinfunc(z):      #funksjon som gir maskinen mulighet til å trekke et til kort om dens sum er under 17.
        while z < 17:
            trekk_et_til_kort(spesiellHånd2, "Maskinen")
            for e in spesiellHånd2:
                z += e
    if spillerSum > maskinSum:
        maskinfunc(maskinSum)
    for e in maskinHånd[0]:         #definerer maskinens hånd til 1 egen liste
        spesiellHånd2.append(e)
    

    def acePros():                      #Prosedyre som skjekker om maskinen har trukket et Ace (11), og beregner om den burde
        maskinSum = 0                   # gjøre om dette kortet til 1. 
        for e in spesiellHånd2:
            maskinSum += e
        if ((spillerSum > maskinSum and 11 in spesiellHånd2) and maskinSum<17):
            for e in spesiellHånd2:         
                if e == 11:
                    spesiellHånd2.remove(e)
                    spesiellHånd2.append(1)
                    maskinfunc(maskinSum)
            acePros()
        elif ((spillerSum > maskinSum and 1 in spesiellHånd2) and maskinSum<17):
            for e in spesiellHånd2:
                if e == 1:
                    maskinfunc(maskinSum)
            acePros()
        elif (maskinSum>21 and 11 in spesiellHånd2):
            for e in spesiellHånd2:
                if e == 11:
                    spesiellHånd2.remove(e)
                    spesiellHånd2.append(1)
                    maskinfunc(maskinSum)
            acePros()
        elif (maskinSum>16 and 11 in spesiellHånd2) and spillerSum>maskinSum:
            for e in spesiellHånd2:
                if e == 11:
                    spesiellHånd2.remove(e)
                    spesiellHånd2.append(1)
                    maskinfunc(maskinSum)
            acePros()
        else:
            pass
    acePros()


    maskinSum = 0                   #Definerer en siste gang summene til spiller og maskin
    for e in spesiellHånd2:
        maskinSum += e
    spillerSum = 0
    for e in spesiellHånd1:
        spillerSum += e


    print(f"Maskinens sum ligger nå på: {maskinSum}")       #Ulike utfall:
    if maskinSum >= spillerSum and maskinSum < 22:
        print(f"* Maskinen vinner.")
        blackjack(saldo)
    elif maskinSum == spillerSum:
        print(f"* Maskinen vinner.")
        blackjack(saldo)
    else:
        saldo += pottotal*2
        print(f"* Spiller vinner.")
        blackjack(saldo)                  #Nytt spill begynner. Tar inn saldo som parameter

blackjack(startspoeng)          #Spill begynner med blackjack().