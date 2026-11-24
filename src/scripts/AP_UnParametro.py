"""
ap_un_parametro.py
Módulo de funciones con un único parámetro de entrada.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""


def calcular_iva(precio):
    """
    Calcula el importe correspondiente al IVA estándar (21%) sobre una base imponible.
    
    Parámetros:
        precio (float | int): Base imponible en euros (debe ser >= 0).
        
    Retorna:
        float: Cuota de IVA redondeada a 2 decimales, o -1.0 si el precio es negativo.
    """
    if precio < 0:
        return -1.0
    return round(precio * 0.21, 2)


def celsius_a_fahrenheit(grados_celsius):
    """
    Convierte una magnitud térmica de grados Celsius a Fahrenheit.
    
    Fórmula: F = (C * 9/5) + 32
    
    Parámetros:
        grados_celsius (float | int): Temperatura en Celsius.
        
    Retorna:
        float: Temperatura en Fahrenheit redondeada a 2 decimales.
    """
    return round((grados_celsius * 9 / 5) + 32, 2)


def minutos_a_horas(minutos):
    """
    Convierte una cantidad de minutos a formato decimal de horas.
    
    Parámetros:
        minutos (float | int): Intervalo de minutos (>= 0).
        
    Retorna:
        float: Horas equivalentes, o -1.0 si el valor de entrada es negativo.
    """
    if minutos < 0:
        return -1.0
    return round(minutos / 60, 2)


def km_a_millas(kilometros):
    """
    Convierte una distancia de kilómetros a millas terrestres.
    
    Factor de conversión: 1 km = 0.621371 millas
    
    Parámetros:
        kilometros (float | int): Distancia en kilómetros (>= 0).
        
    Retorna:
        float: Distancia en millas redondeada a 3 decimales, o -1.0 si es negativa.
    """
    if kilometros < 0:
        return -1.0
    return round(kilometros * 0.621371, 3)


def es_par(numero):
    """
    Evalúa la paridad de un número entero mediante el operador módulo.
    
    Parámetros:
        numero (int): Valor a evaluar.
        
    Retorna:
        bool: True si el número es divisible por 2, False en caso contrario.
    """
    if not isinstance(numero, int):
        return False
    return numero % 2 == 0


def validar_numero_positivo(numero):
    """
    Comprueba si un valor numérico es estrictamente mayor que cero.
    
    Parámetros:
        numero (float | int): Número a verificar.
        
    Retorna:
        bool: True si es positivo, False si es cero o negativo.
    """
    return numero > 0


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_un_parametro.py")
    
    # 1. IVA
    print(f"IVA de 100€: {calcular_iva(100)}€ (Esperado: 21.0€)")
    print(f"IVA de 0€ (límite): {calcular_iva(0)}€ (Esperado: 0.0€)")
    print(f"IVA de -25€ (erróneo): {calcular_iva(-25)} (Esperado: -1.0)")
    
    # 2. Temperatura
    print(f"0 ºC a Fahrenheit: {celsius_a_fahrenheit(0)} ºF (Esperado: 32.0 ºF)")
    print(f"100 ºC a Fahrenheit: {celsius_a_fahrenheit(100)} ºF (Esperado: 212.0 ºF)")
    
    # 3. Minutos a horas
    print(f"90 minutos: {minutos_a_horas(90)} h (Esperado: 1.5 h)")
    
    # 4. Distancia
    print(f"10 km a millas: {km_a_millas(10)} mi (Esperado: 6.214 mi)")
    
    # 5. Paridad
    print(f"¿Es 8 par?: {es_par(8)} (Esperado: True)")
    print(f"¿Es 7 par?: {es_par(7)} (Esperado: False)")
    
    # 6. Positivo
    print(f"¿Es 15 positivo?: {validar_numero_positivo(15)} (Esperado: True)")
    print(f"¿Es -5 positivo?: {validar_numero_positivo(-5)} (Esperado: False)")
    
    print("[TEST] Pruebas de ap_un_parametro.py finalizadas con éxito.\n")
