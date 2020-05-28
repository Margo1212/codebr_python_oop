# Implementacja objektowa

class Konto:
    def __init__(self, stan_początkowy, imie, nazwisko, numer):
        print("Jestem metoda__init__ ")
        # atrybut objektu
        self.stan = stan_początkowy
        # Atrybut objectu o nazwie stan
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        if self.stan >= kwota:
            self.stan -= kwota
            return kwota
        else:
            raise Exception('Nie ma wystarczajacej kwoty na koncie.')

    def pokaz_detale(self):
        string = f"{self.imie} {self.nazwisko}  {self.numer} {self.stan}"
        return string

    def przelej(self, kwota, konto_odbiorcy):
        zmienna = self.wyplac(kwota)
        konto_odbiorcy.wplac(zmienna)


konto = Konto(0, 'Margo', 'Sirachenko', 12345567)
print(konto)
print(konto.pokaz_detale())
konto.wplac(100)
print(konto.pokaz_detale())

print(konto.stan)
konto1 = Konto(100, 'Kamil', 'Sirachenko', 12345567)
konto.przelej(50, konto1)
print(konto.pokaz_detale())
print(konto1.pokaz_detale())
