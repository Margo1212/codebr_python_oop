# Napisz klasę Python o nazwie Prostokąt zbudowaną na podstawie
# długości i szerokości oraz metodę, która obliczy obszar
# prostokąta.

class Prostokat():
    def __init__(self, dlugosc1, szerokosc1):
        self.dlugosc=dlugosc1
        self.szerokosc=szerokosc1

    def obszar (self):
        obszar1 = self.dlugosc*self.szerokosc
        return obszar1

obszar1 = Prostokat(20, 30)
print(obszar1.obszar())