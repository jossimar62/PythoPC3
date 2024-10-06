import math

# Clase Circulo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Clase Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

# Función para validar que los datos ingresados sean números válidos y positivos
def validar_entrada(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Entrada inválida, por favor ingresa un número.")

# Función principal del menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            radio = validar_entrada("Ingresa el radio del círculo: ")
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")

        elif opcion == '2':
            base = validar_entrada("Ingresa la base del rectángulo: ")
            altura = validar_entrada("Ingresa la altura del rectángulo: ")
            rectangulo = Rectangulo(base, altura)
            print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        elif opcion == '3':
            lado = validar_entrada("Ingresa el lado del cuadrado: ")
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 4.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
