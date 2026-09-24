class Retangulo :
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return self.altura + self.altura + self.largura + self.largura

retangulo1 = Retangulo(4,8)
retangulo2 = Retangulo(8, 12)

print(f"Retangulo 1: {retangulo1.largura} x {retangulo1.altura}")
print(f"Area: {retangulo1.calcular_area()} | Perimetro: {retangulo1.calcular_perimetro()}")
print("=" *24)
print(f"Retangulo 2: {retangulo2.largura} x {retangulo2.altura}")
print(f"Area: {retangulo2.calcular_area()} | Perimetro: {retangulo2.calcular_perimetro()}")