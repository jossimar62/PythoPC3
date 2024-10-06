import math

class CIRCULO:
    def _init_(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(5)  # Radio de 5
circulo2 = CIRCULO(10)  # Radio de 10

# Calcular y mostrar el área de cada círculo
area_circulo1 = circulo1.area()
area_circulo2 = circulo2.area()

print(f"El área del círculo con radio {circulo1.radio} es: {area_circulo1:.2f}")
print(f"El área del círculo con radio {circulo2.radio} es: {area_circulo2:.2f}")