import math

class Forma:
    def area(self):
        return

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio **2
    def __str__(self):
        return f"Circulo Area: {self.area():.2f}"
class Quadrado(Forma):
    def __init__(self, lados):
        self.lados = lados
    def area(self):
        return self.lados ** 2
    def __str__(self):
        return f"Quadrado Area: {self.area()}"

formas =[Circulo(5), Quadrado(10), Circulo(10), Quadrado(20), Circulo(7),
         Quadrado(15), Circulo(8), Quadrado(12), Circulo(12), Quadrado(30)]
for i in formas:
    print(i)





