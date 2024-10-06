# operaciones.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    
    # calculos.py

from operaciones import suma, resta, producto, division

# Ejemplos de uso
a = 10
b = 5
c = "texto"  # Ejemplo de tipo de dato no válido
d = 0  # Ejemplo de división por cero

print("Suma:", suma(a, b))           # 10 + 5
print("Resta:", resta(a, b))         # 10 - 5
print("Producto:", producto(a, b))   # 10 * 5
print("División:", division(a, b))   # 10 / 5

# Pruebas con valores no válidos
print("Suma con texto:", suma(a, c)) # Error: Tipo de dato no válido
print("División por cero:", division(a, d)) # Error: No es posible dividir entre cero