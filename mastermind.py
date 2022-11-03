

#random prosjekt fordi ville teste om jeg klarte det

class Mastermind():
    def __init__(self):
        self._farger = 0
        self._plasser = 0
        self._forsøk = 10
        self._riktig_liste = []
        self._gjette_liste = []
        self._sjekkede_farger = []
        self._fjernet_farger = []

    def hovedpros(self):
        if self._forsøk != 0:
            self.gjett_brikker()
            while (self._gjette_liste != self._riktig_liste) and (self._forsøk):
                self._forsøk -= 1
                self.hovedpros()
            print("Riktig svar!")
        else:
            print(f"Du tapte. Riktige brikker var: {self._riktig_liste}")

    def sett_brikker(self):
            sett_brikker = input("Skriv inn kode som skal gjettes (f.eks: 'rød,grønn,blå,gul'): ")
            self._riktig_liste = sett_brikker.split(",")
            self._sjekkede_farger = sett_brikker.split(",")
    def gjett_brikker(self):
            gjett_brikker = input("Gjett en rekke med farger (f.eks: rød,blå,gul,grønn): ")
            self._gjette_liste = gjett_brikker.split(",")

    def sjekk_brikker(self):
        self._farger = 0
        self._plasser = 0
        self._fjernet_farger = []

        for brikke1 in self._gjette_liste:
            i = -1
            for brikke2 in self._sjekkede_farger:
                i += 1
                if brikke1 == brikke2:
                    self._farger += 1
                    _fjernet_farge = self._sjekkede_farger.pop(i)
                    self._fjernet_farger.append(_fjernet_farge)
        for e in self._fjernet_farger:
            self._sjekkede_farger.append(e)

        for i in range(-1,3):
            if self._gjette_liste[i] == self._riktig_liste[i]:
                self._plasser += 1

        return f"Riktige farger: {self._farger} | Riktige plasser: {self._plasser}\nDu har {self._forsøk} forsøk igjen."

mastermind = Mastermind()
mastermind.sett_brikker()
mastermind.hovedpros()