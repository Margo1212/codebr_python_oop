class Uppercase():

    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Wpisz coś: ")
        return self.string

    def printString(self):
        string1=self.string.upper()
        return string1

string1 = Uppercase()
string1.getString()
string1.printString()
print(string1.printString())