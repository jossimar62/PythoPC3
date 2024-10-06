class RECTANGULO:
    def _init_(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def _init_(self, lado):
        super()._init_(lado, lado)  # Llama al constructor de RECTANGULO con largo y ancho iguales

# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(4, 5)

# Crear un objeto de tipo CUADRADO
cuadrado = CUADRADO(3)

# Calcular y mostrar el área de cada figura
area_rectangulo = rectangulo.area()
area_cuadrado = cuadrado.area()

print(f"El área del rectángulo de largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area_rectangulo}")
print(f"El área del cuadrado de lado {cuadrado.largo} es: {area_cuadrado}")