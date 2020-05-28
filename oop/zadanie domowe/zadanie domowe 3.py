# Napisz klasę Python o nazwie Koło skonstruowaną za pomocą
# promienia i dwóch metod, które obliczą obszar i obwód koła

class Kolo():
    def __init__(self, promien1):
        self.promien = promien1

    def obszar(self):
        pi = 3.14
        obszar1 = pi * self.promien ** 2
        return obszar1

    def obwod(self):
        pi = 3.14
        obwod1 = (2 * pi) * self.promien
        return obwod1


obszar1= Kolo(3)
obwod1 = Kolo(3)

print("Obwod kola = ", obwod1.obwod())
print("Obszar kola = ", obszar1.obszar())
