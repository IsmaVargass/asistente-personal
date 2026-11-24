"""
ap_recursividad.py
Módulo de algoritmos recursivos: Factorial, Fibonacci y Máximo Común Divisor.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""

import sys


def factorial_recursivo(n):
    """
    Calcula el factorial de un entero no negativo de manera recursiva.
    
    Fórmula:
        0! = 1
        n! = n * (n - 1)!
        
    Parámetros:
        n (int): Entero no negativo (>= 0).
        
    Retorna:
        int: Factorial de n, o -1 si el argumento es inválido o negativo.
        
    Traza de ejecución en la pila de llamadas para factorial(4):
        factorial(4) -> 4 * factorial(3)
        factorial(3) -> 3 * factorial(2)
        factorial(2) -> 2 * factorial(1)
        factorial(1) -> 1 * factorial(0)
        factorial(0) -> 1 (Caso base alcanzado)
        Desapilado: 1 -> 1 -> 2 -> 6 -> 24
    """
    if not isinstance(n, int) or n < 0:
        return -1
        
    # Caso base
    if n in (0, 1):
        return 1
        
    # Caso recursivo
    return n * factorial_recursivo(n - 1)


def fibonacci_recursivo(n):
    """
    Calcula el término n-ésimo de la sucesión de Fibonacci.
    
    Parámetros:
        n (int): Posición solicitada (>= 0).
        
    Retorna:
        int: Valor del término, o -1 en caso de error.
        
    Nota técnica:
        La versión recursiva pura tiene una complejidad temporal O(2^n)
        debido a la ramificación de llamadas repetidas.
    """
    if not isinstance(n, int) or n < 0:
        return -1
        
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # Caso recursivo
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def mcd_recursivo(a, b):
    """
    Calcula el Máximo Común Divisor mediante el algoritmo de Euclides recursivo.
    
    Fórmula: MCD(a, b) = MCD(b, a % b)
    
    Parámetros:
        a (int): Primer operando entero.
        b (int): Segundo operando entero.
        
    Retorna:
        int: Máximo común divisor positivo, o -1 si los tipos son incorrectos.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return -1
        
    a, b = abs(a), abs(b)
    
    # Caso base: cuando el divisor llega a cero, el MCD es el dividendo
    if b == 0:
        return a
        
    # Caso recursivo
    return mcd_recursivo(b, a % b)


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_recursividad.py")
    print(f"Límite de recursión del intérprete: {sys.getrecursionlimit()} llamadas.")
    
    # Factorial
    print(f"Factorial de 0 (caso base): {factorial_recursivo(0)} (Esperado: 1)")
    print(f"Factorial de 4: {factorial_recursivo(4)} (Esperado: 24)")
    print(f"Factorial de 5: {factorial_recursivo(5)} (Esperado: 120)")
    print(f"Factorial de -3 (erróneo): {factorial_recursivo(-3)} (Esperado: -1)")
    
    # Fibonacci
    print(f"Fibonacci(0): {fibonacci_recursivo(0)} (Esperado: 0)")
    print(f"Fibonacci(7): {fibonacci_recursivo(7)} (Esperado: 13)")
    print(f"Fibonacci(10): {fibonacci_recursivo(10)} (Esperado: 55)")
    
    # MCD Euclides
    print(f"MCD(48, 18): {mcd_recursivo(48, 18)} (Esperado: 6)")
    print(f"MCD(100, 25): {mcd_recursivo(100, 25)} (Esperado: 25)")
    print(f"MCD(17, 13) (primos entre sí): {mcd_recursivo(17, 13)} (Esperado: 1)")
    
    print("[TEST] Pruebas de ap_recursividad.py finalizadas con éxito.\n")
