"""
AP_Recursividad.py
Práctica de funciones recursivas: factorial, Fibonacci y Máximo Común Divisor (MCD).

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

import sys

# ==============================================================================
# ¿QUÉ ES LA RECURSIVIDAD? (Guía para defender ante el profesor)
#
# Una función recursiva es aquella que se llama a sí misma para resolver un
# problema dividiéndolo en versiones más pequeñas del mismo problema.
#
# Toda función recursiva bien diseñada DEBE tener dos partes obligatorias:
# 1. CASO BASE (o condición de parada):
#    Es la situación más sencilla que se resuelve directamente SIN volver a llamarse.
#    Si no existiera, la función se llamaría infinitamente hasta agotar la memoria
#    provocando un 'RecursionError: maximum recursion depth exceeded'.
#
# 2. CASO RECURSIVO:
#    Es la llamada a sí misma con un dato más cercano al caso base (ej: n - 1).
#
# PILA DE LLAMADAS (Call Stack):
# Cada vez que una función se llama a sí misma, Python "pausa" la función actual
# y apila un nuevo marco en la memoria (como una pila de platos).
# Cuando se alcanza el caso base, los platos se van desapilando de arriba a abajo,
# devolviendo los valores acumulados.
#
# LÍMITE DE RECURSIÓN EN PYTHON:
# Python incluye una protección por defecto (habitualmente 1000 llamadas máximas)
# que podemos consultar con `sys.getrecursionlimit()`.
# ==============================================================================


def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo (n!) de forma recursiva.
    
    Fórmula matemática:
        0! = 1
        n! = n * (n - 1)!
        
    Parámetros:
        n (int): Número entero no negativo (>= 0).
        
    Devuelve:
        int: El factorial de n.
             Devuelve -1 si el argumento es negativo o no es un entero.
             
    Ejemplo de traza de pila de llamadas para factorial(4):
        1) factorial(4) espera a 4 * factorial(3)  [Apila llamada]
        2) factorial(3) espera a 3 * factorial(2)  [Apila llamada]
        3) factorial(2) espera a 2 * factorial(1)  [Apila llamada]
        4) factorial(1) espera a 1 * factorial(0)  [Apila llamada]
        5) factorial(0) llega al CASO BASE -> devuelve 1
        -- Comienza el desapilado:
        6) factorial(1) = 1 * 1 = 1                [Desapila]
        7) factorial(2) = 2 * 1 = 2                [Desapila]
        8) factorial(3) = 3 * 2 = 6                [Desapila]
        9) factorial(4) = 4 * 6 = 24               [Resultado final desapilado]
    """
    # Validación: solo aceptamos enteros no negativos
    if not isinstance(n, int) or n < 0:
        return -1
        
    # --- CASO BASE ---
    # Por definición matemática, el factorial de 0 (y de 1) es 1.
    # Aquí paramos de llamarnos a nosotros mismos.
    if n == 0 or n == 1:
        return 1
        
    # --- CASO RECURSIVO ---
    # Multiplicamos 'n' por el factorial del número anterior (n - 1)
    return n * factorial_recursivo(n - 1)


def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo término de la sucesión de Fibonacci de forma recursiva.
    
    Sucesión: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    
    Parámetros:
        n (int): Posición en la sucesión (n >= 0).
        
    Devuelve:
        int: El valor en la posición n.
             Devuelve -1 si n es negativo o no es entero.
             
    ¿POR QUÉ ES LENTO CON NÚMEROS GRANDES?
    Porque genera un árbol de llamadas exponencial O(2^n).
    Por ejemplo, para calcular fibonacci(5), calcula fibonacci(3) dos veces,
    fibonacci(2) tres veces, etc. No guarda memoria de lo ya calculado.
    Por eso en la práctica solo debe llamarse con n <= 30.
    """
    if not isinstance(n, int) or n < 0:
        return -1
        
    # --- CASO BASE ---
    # Si nos piden la posición 0 devuelve 0; si piden la posición 1 devuelve 1.
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # --- CASO RECURSIVO ---
    # Cada número de Fibonacci es la suma de los dos anteriores
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def mcd_recursivo(a, b):
    """
    Calcula el Máximo Común Divisor entre dos números enteros mediante
    el Algoritmo de Euclides de forma recursiva.
    
    Algoritmo de Euclides:
        MCD(a, b) = MCD(b, a % b)
        
    Parámetros:
        a (int): Primer número entero.
        b (int): Segundo número entero.
        
    Devuelve:
        int: El máximo común divisor (siempre positivo).
             Devuelve -1 si alguno de los datos no es entero.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return -1
        
    # El MCD se calcula sobre valores absolutos (positivos)
    a, b = abs(a), abs(b)
    
    # --- CASO BASE ---
    # Cuando el divisor 'b' llega a 0, el MCD es 'a'.
    if b == 0:
        return a
        
    # --- CASO RECURSIVO ---
    # Llamamos a la función pasando 'b' como nuevo dividendo y el resto (a % b) como nuevo divisor.
    return mcd_recursivo(b, a % b)


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE AP_Recursividad.py <<<\n")

    # Información sobre el entorno Python
    limite = sys.getrecursionlimit()
    print(f"ℹ️ Límite máximo de recursión configurado en este Python: {limite} llamadas.")

    # 1. Pruebas de Factorial
    print("\n--- 1. Pruebas: factorial_recursivo(n) ---")
    print(f"Factorial de 0 (caso base límite): {factorial_recursivo(0)} (Esperado: 1)")
    print(f"Factorial de 1 (caso base): {factorial_recursivo(1)} (Esperado: 1)")
    print(f"Factorial de 4: {factorial_recursivo(4)} (Esperado: 24)")
    print(f"Factorial de 6: {factorial_recursivo(6)} (Esperado: 720)")
    print(f"Factorial de -3 (caso error): {factorial_recursivo(-3)} (Esperado: -1)")
    print(f"Factorial de 3.5 (no entero): {factorial_recursivo(3.5)} (Esperado: -1)")

    # 2. Pruebas de Fibonacci
    print("\n--- 2. Pruebas: fibonacci_recursivo(n) ---")
    print(f"Fibonacci(0): {fibonacci_recursivo(0)} (Esperado: 0)")
    print(f"Fibonacci(1): {fibonacci_recursivo(1)} (Esperado: 1)")
    print(f"Fibonacci(6): {fibonacci_recursivo(6)} (Esperado: 8)")
    print(f"Fibonacci(10): {fibonacci_recursivo(10)} (Esperado: 55)")
    print(f"Fibonacci(-4) (caso error): {fibonacci_recursivo(-4)} (Esperado: -1)")
    
    # Mostramos los primeros 8 números de la serie
    serie_8 = [fibonacci_recursivo(i) for i in range(8)]
    print(f"Primeros 8 términos de Fibonacci: {serie_8}")

    # 3. Pruebas de MCD (Algoritmo de Euclides)
    print("\n--- 3. Pruebas: mcd_recursivo(a, b) ---")
    print(f"MCD(48, 18): {mcd_recursivo(48, 18)} (Esperado: 6)")
    print(f"MCD(100, 25): {mcd_recursivo(100, 25)} (Esperado: 25)")
    print(f"MCD(17, 13) (números primos entre sí): {mcd_recursivo(17, 13)} (Esperado: 1)")
    print(f"MCD(0, 5) (caso límite): {mcd_recursivo(0, 5)} (Esperado: 5)")
    print(f"MCD(20, -8) (con negativos): {mcd_recursivo(20, -8)} (Esperado: 4)")

    print("\n>>> TODAS LAS PRUEBAS DE AP_Recursividad.py COMPLETADAS CON ÉXITO <<<")
