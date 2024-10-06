def solicitar_calificaciones():
    while True:
        entrada = input("Introduce las calificaciones separadas por comas: ")
        # Eliminar espacios en blanco y dividir la cadena
        calificaciones_str = entrada.replace(" ", "").split(',')
        
        try:
            # Convertir cada calificación a entero
            calificaciones = [int(calificacion) for calificacion in calificaciones_str]
            print("Calificaciones ingresadas:", calificaciones)
            break  # Salir del bucle si todo es correcto
            
        except ValueError:
            print("Error: Asegúrate de ingresar solo números enteros separados por comas. Inténtalo de nuevo.")

# Ejecutar la función
solicitar_calificaciones()