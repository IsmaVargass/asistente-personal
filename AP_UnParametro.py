"""
AP_UnParametro.py
Práctica de funciones que reciben un único parámetro (argumento).

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""


def calcular_iva(precio):
    """
    Calcula el importe del IVA estándar (21%) aplicado a un precio base.
    
    Parámetros:
        precio (float/int): El precio base en euros. Debe ser mayor o igual a 0.
        
    Devuelve:
        float: El valor monetario del IVA redondeado a 2 decimales.
               Devuelve -1.0 si el precio introducido es negativo.
    """
    # Término técnico: 'precio' es el PARÁMETRO (la variable que espera la función).
    # Cuando llamamos a la función con calcular_iva(100), el número 100 es el ARGUMENTO (el valor real).
    
    # Validación: un precio no puede ser negativo en una compra normal
    if precio < 0:
        # En vez de romper el programa con un error, avisamos devolviendo un valor centinela (-1)
        return -1.0
        
    # Calculamos el 21% y redondeamos con round() a dos decimales
    iva = round(precio * 0.21, 2)
    return iva


def celsius_a_fahrenheit(grados_celsius):
    """
    Convierte una temperatura en grados Celsius a grados Fahrenheit.
    
    Parámetros:
        grados_celsius (float/int): Temperatura en Celsius.
        
    Devuelve:
        float: Temperatura equivalente en Fahrenheit redondeada a 2 decimales.
    """
    # Fórmula clásica de física: F = (C * 9/5) + 32
    # El cero absoluto en Celsius es -273.15 ºC.
    fahrenheit = round((grados_celsius * 9 / 5) + 32, 2)
    return fahrenheit


def minutos_a_horas(minutos):
    """
    Convierte una cantidad de minutos a su equivalente en horas (formato decimal).
    
    Parámetros:
        minutos (float/int): Cantidad de minutos a convertir.
        
    Devuelve:
        float: Horas resultantes. Devuelve -1.0 si los minutos son negativos.
    """
    # Si nos pasan un tiempo negativo no tiene sentido cronológico aquí
    if minutos < 0:
        return -1.0
        
    # Dividimos entre 60 para pasar a horas (ej: 90 minutos -> 1.5 horas)
    horas = round(minutos / 60, 2)
    return horas


def km_a_millas(kilometros):
    """
    Convierte una distancia dada en kilómetros a millas terrestres.
    
    Parámetros:
        kilometros (float/int): Distancia en km (debe ser mayor o igual a 0).
        
    Devuelve:
        float: Distancia en millas redondeada a 3 decimales. Devuelve -1.0 si es negativo.
    """
    if kilometros < 0:
        return -1.0
        
    # Factor de conversión oficial: 1 km = 0.621371 millas
    FACTOR_MILLAS = 0.621371
    millas = round(kilometros * FACTOR_MILLAS, 3)
    return millas


def es_par(numero):
    """
    Determina si un número entero es par o impar.
    
    Parámetros:
        numero (int): Número a comprobar.
        
    Devuelve:
        bool: True si el número es par, False si es impar o no entero.
    """
    # Verificamos primero que sea de tipo int (entero)
    if not isinstance(numero, int):
        return False
        
    # Usamos el operador módulo (%) que nos da el resto de la división entre 2.
    # Si el resto es 0, significa que es divisible exactamente por 2 (es par).
    return numero % 2 == 0


def validar_numero_positivo(numero):
    """
    Comprueba si un valor numérico es estrictamente positivo (mayor que 0).
    
    Parámetros:
        numero (float/int): Valor a verificar.
        
    Devuelve:
        bool: True si es mayor que cero, False en caso contrario.
    """
    # Comprobación booleana sencilla y limpia
    return numero > 0


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE AP_UnParametro.py <<<\n")

    # 1. Pruebas de calcular_iva
    print("--- 1. Pruebas: calcular_iva(precio) ---")
    precio_normal = 100.0
    print(f"IVA de {precio_normal}€: {calcular_iva(precio_normal)}€ (Esperado: 21.0€)")
    precio_cero = 0.0
    print(f"IVA de {precio_cero}€ (caso límite): {calcular_iva(precio_cero)}€ (Esperado: 0.0€)")
    precio_negativo = -50.0
    print(f"IVA de {precio_negativo}€ (caso error): {calcular_iva(precio_negativo)} (Esperado: -1.0)")

    # 2. Pruebas de celsius_a_fahrenheit
    print("\n--- 2. Pruebas: celsius_a_fahrenheit(grados_celsius) ---")
    print(f"0 ºC a Fahrenheit (congelación agua): {celsius_a_fahrenheit(0)} ºF (Esperado: 32.0 ºF)")
    print(f"100 ºC a Fahrenheit (ebullición agua): {celsius_a_fahrenheit(100)} ºF (Esperado: 212.0 ºF)")
    print(f"-40 ºC a Fahrenheit (punto de cruce): {celsius_a_fahrenheit(-40)} ºF (Esperado: -40.0 ºF)")

    # 3. Pruebas de minutos_a_horas
    print("\n--- 3. Pruebas: minutos_a_horas(minutos) ---")
    print(f"90 minutos: {minutos_a_horas(90)} horas (Esperado: 1.5 horas)")
    print(f"0 minutos: {minutos_a_horas(0)} horas (Esperado: 0.0 horas)")
    print(f"-15 minutos (error): {minutos_a_horas(-15)} (Esperado: -1.0)")

    # 4. Pruebas de km_a_millas
    print("\n--- 4. Pruebas: km_a_millas(kilometros) ---")
    print(f"10 km a millas: {km_a_millas(10)} millas (Esperado: ~6.214 millas)")
    print(f"0 km a millas: {km_a_millas(0)} millas (Esperado: 0.0 millas)")
    print(f"-5 km a millas (error): {km_a_millas(-5)} (Esperado: -1.0)")

    # 5. Pruebas de es_par
    print("\n--- 5. Pruebas: es_par(numero) ---")
    print(f"¿Es 4 par?: {es_par(4)} (Esperado: True)")
    print(f"¿Es 7 par?: {es_par(7)} (Esperado: False)")
    print(f"¿Es 0 par? (caso límite): {es_par(0)} (Esperado: True)")
    print(f"¿Es -8 par? (negativo): {es_par(-8)} (Esperado: True)")
    print(f"¿Es 4.5 par? (caso erróneo, no entero): {es_par(4.5)} (Esperado: False)")

    # 6. Pruebas de validar_numero_positivo
    print("\n--- 6. Pruebas: validar_numero_positivo(numero) ---")
    print(f"¿Es 25 positivo?: {validar_numero_positivo(25)} (Esperado: True)")
    print(f"¿Es 0 positivo? (límite): {validar_numero_positivo(0)} (Esperado: False)")
    print(f"¿Es -10 positivo?: {validar_numero_positivo(-10)} (Esperado: False)")

    print("\n>>> TODAS LAS PRUEBAS DE AP_UnParametro.py COMPLETADAS CON ÉXITO <<<")
