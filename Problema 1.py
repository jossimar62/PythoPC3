def solicitar_fraccion():
    while True:
        entrada = input("Introduce una fracción en formato X/Y: ")
        try:
            x, y = map(int, entrada.split('/'))
            if y == 0:
                print("El denominador (Y) no puede ser cero. Inténtalo de nuevo.")
                continue
            if x < 0 or x > y:
                print("X debe ser menor o igual a Y. Inténtalo de nuevo.")
                continue
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            break  # Salir del bucle si todo es correcto
            
        except ValueError:
            print("Entrada no válida. Asegúrate de usar el formato X/Y con números enteros.")

# Ejecutar la función
solicitar_fraccion()