def calcular_promedios_temperatura(datos_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad durante un período de semanas.

    Args:
        datos_temperaturas (dict): Un diccionario donde las claves son nombres de ciudades
                                  y los valores son listas de temperaturas semanales.
                                  Ejemplo: {"Loja": [18, 20, 22, 21], "Quito": [15, 16, 17, 15]}

    Returns:
        dict: Un diccionario donde las claves son nombres de ciudades y los valores
              son las temperaturas promedio correspondientes.
              Devuelve un diccionario vacío si no hay datos de entrada.
              Devuelve None si los datos de entrada no son válidos.
    """

    # 1. Validación de los datos de entrada
    if not isinstance(datos_temperaturas, dict):
        print("Error: Los datos de entrada deben ser un diccionario.")
        return None

    # 2. Manejo del caso en que no hay datos
    if not datos_temperaturas:
        print("Advertencia: No se proporcionaron datos de temperaturas.  Devolviendo un diccionario vacío.")
        return {}

    promedios_por_ciudad = {}  # Diccionario para almacenar los promedios

    for ciudad, temperaturas_semanales in datos_temperaturas.items():
        # 3. Validación de cada ciudad y sus temperaturas
        if not isinstance(ciudad, str):
            print(f"Error: El nombre de la ciudad '{ciudad}' debe ser una cadena.")
            return None  # O podrías optar por saltar esta ciudad y continuar

        if not isinstance(temperaturas_semanales, list):
            print(f"Error: Las temperaturas para '{ciudad}' deben ser una lista.")
            return None

        if not temperaturas_semanales:
            print(f"Advertencia: No hay datos de temperatura para '{ciudad}'. Omitiendo el cálculo del promedio.")
            continue  # Saltar a la siguiente ciudad

        # 4. Convertir temperaturas a números y manejar errores
        temperaturas_numericas = []
        for temp in temperaturas_semanales:
            if isinstance(temp, (int, float)):
                temperaturas_numericas.append(float(temp))  # Convertir a float para mayor precisión
            else:
                print(f"Error: Temperatura inválida '{temp}' para la ciudad '{ciudad}'.  Debe ser un número.")
                return None #O podrías optar por saltar esta temperatura y continuar con las demás

        # 5. Cálculo del promedio
        try:
            promedio = sum(temperaturas_numericas) / len(temperaturas_numericas)
            promedios_por_ciudad[ciudad] = promedio  # Guarda el promedio en el diccionario
        except ZeroDivisionError:
            print(f"Error: No se pueden calcular promedios con una lista de temperaturas vacía para '{ciudad}'.")
            promedios_por_ciudad[ciudad] = None  # Asignar None o un valor por defecto apropiado

    return promedios_por_ciudad  # Devuelve el diccionario con los promedios

# ----------------------------------------------------------------------
# Ejemplo de uso (puedes descomentar para probar)
# ----------------------------------------------------------------------
datos_temperaturas = {
    "Loja": [18, 20, 22, 21],
    "Quito": [15, 16, 17, 15],
    "Guayaquil": [28, 30, 32, 31],
    "Cuenca": []  # Lista vacía para probar el manejo de errores
}

resultados = calcular_promedios_temperatura(datos_temperaturas)

if resultados:
    print(resultados)
