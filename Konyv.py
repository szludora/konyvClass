import random


class Konyv:
    def __init__(self):
        self.oldal = self.oldalszam()
        self.nyitva = False
        self.aktualis_oldal = 0

    def __str__(self):
        return f"A könyv oldalszáma: {self.oldal}, aktuális oldal: {self.aktualis_oldal}"

    @staticmethod
    def oldalszam():
        x = int(random.random()*101) + 50
        return x

    def kinyit(self):
        x = int(random.random() * (self.oldal+1)) + 1
        self.aktualis_oldal = x
        self.nyitva = True
        return x

    def bezar(self):
        self.nyitva = False
        return "Bezártad a könyvet"

    def porget(self, irany):
        """
        "j" - jobbra lapozás
        "b" - balra lapozás
        """

        if self.nyitva:
            if irany == "j":
                x = int(random.random()*(self.oldal-self.aktualis_oldal + 1)) + self.aktualis_oldal
                print(f"A {x}. oldalra lapoztál")
                self.aktualis_oldal = x
            elif irany == "b":
                x = int(random.random() * self.aktualis_oldal) + 1
                print(f"A {x}. oldalra lapoztál")
                self.aktualis_oldal = x
        else:
            print("Előbb ki kell nyitnod a könyvet")

    def lapoz(self, irany):
        """
        "j" - jobbra lapozás
        "b" - balra lapozás
        """
        if self.nyitva:

            if irany == "j":
                x = self.aktualis_oldal + 1
                print(f"A {x}. oldalra lapoztál")
                self.aktualis_oldal = x
            elif irany == "b":
                x = self.aktualis_oldal - 1
                print(f"A {x}. oldalra lapoztál")
                self.aktualis_oldal = x

            if self.aktualis_oldal == 1 or self.aktualis_oldal == self.oldal:
                self.bezar()
        else:
            print("Előbb ki kell nyitnod a könyvet")

    def nez(self):
        if self.nyitva:
            print(f"A könyv ki van nyitva a {self.aktualis_oldal}. oldalon.")
        else:
            print(f"A könyv be van zárva")
