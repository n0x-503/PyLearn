import math
def area_circunferencia():
    raio = float(input("Raio: "))
    area = math.pi * raio**2
    circunferencia = 2 * math.pi * raio
    print(f"Area: {round(area, 4)}")
    print(f"Circunferencia: {round(circunferencia, 4)}")

def calc_hipotenusa():
    cateto_a = float(input("Cateto a: "))
    cateto_b = float(input("Cateto b:"))
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    print(f"Hipotenusa: {round(hipotenusa, 4)}")

area_circunferencia()
calc_hipotenusa()