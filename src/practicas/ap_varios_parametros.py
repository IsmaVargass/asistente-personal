"""
ap_varios_parametros.py
Módulo de funciones con múltiples parámetros, valores por defecto,
argumentos variables (*args, **kwargs) y retornos múltiples.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""


def calcular_precio_con_descuento_e_iva(precio, descuento, iva):
    """
    Calcula el precio final aplicando un descuento y posteriormente el IVA.
    Demuestra el uso de múltiples parámetros posicionales obligatorios.
    
    Parámetros:
        precio (float | int): Precio base (>= 0).
        descuento (float | int): Porcentaje de descuento (0 a 100).
        iva (float | int): Porcentaje de IVA (>= 0).
        
    Retorna:
        float: Precio final calculado, o -1.0 en caso de valores no válidos.
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    base_con_descuento = precio * (1 - (descuento / 100))
    precio_total = base_con_descuento * (1 + (iva / 100))
    return round(precio_total, 2)


def calcular_precio_final(precio, descuento=0, iva=21):
    """
    Calcula el precio final con valores por defecto para agilizar la invocación.
    
    Parámetros:
        precio (float | int): Precio base obligatorio.
        descuento (float | int, opcional): Descuento porcentual (por defecto 0).
        iva (float | int, opcional): Porcentaje de IVA (por defecto 21).
        
    Retorna:
        float: Total calculado redondeado a 2 decimales.
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    base_rebajada = precio * (1 - (descuento / 100))
    total = base_rebajada * (1 + (iva / 100))
    return round(total, 2)


def sumar_gastos(*gastos):
    """
    Acumula una serie indeterminada de importes monetarios utilizando *args.
    Los argumentos posicionales se reciben empaquetados en una tupla.
    
    Parámetros:
        *gastos (float | int): Serie variable de importes numéricos.
        
    Retorna:
        float: Suma total de los gastos positivos.
    """
    total = 0.0
    for gasto in gastos:
        if gasto > 0:
            total += gasto
    return round(total, 2)


def calcular_media(*numeros):
    """
    Calcula la media aritmética de una serie de números variable con *args.
    Controla casos límite de invocación vacía para evitar división por cero.
    
    Parámetros:
        *numeros (float | int): Colección variable de números.
        
    Retorna:
        float: Media aritmética, o 0.0 si la serie está vacía.
    """
    if not numeros:
        return 0.0
    return round(sum(numeros) / len(numeros), 2)


def mostrar_ficha(**datos):
    """
    Formatea pares clave-valor recibidos mediante argumentos con nombre (**kwargs).
    Internamente se reciben como un diccionario.
    
    Parámetros:
        **datos: Atributos clave=valor.
        
    Retorna:
        str: Cadena formateada para presentación de datos.
    """
    if not datos:
        return "Ficha sin datos registrados."
        
    lineas = ["FICHA DE REGISTRO:"]
    for clave, valor in datos.items():
        lineas.append(f"  - {clave.capitalize()}: {valor}")
    return "\n".join(lineas)


def repartir_cuenta(total, personas):
    """
    Divide un importe entre un número de comensales.
    Retorna múltiples resultados empaquetados en una tupla: (cuota, resto).
    
    Parámetros:
        total (float | int): Importe total a liquidar.
        personas (int): Número de participantes (debe ser >= 1).
        
    Retorna:
        tuple[float, float]: (cuota_individual, resto_centimos).
    """
    if total <= 0 or personas <= 0:
        return (0.0, 0.0)
        
    cuota = round(total / personas, 2)
    descuadre = round(total - (cuota * personas), 2)
    return (cuota, descuadre)


def estadisticas_basicas(lista_numeros):
    """
    Calcula simultáneamente el mínimo, máximo y media de una colección.
    
    Parámetros:
        lista_numeros (list): Lista de enteros o decimales.
        
    Retorna:
        tuple[float, float, float]: (minimo, maximo, media).
    """
    if not lista_numeros:
        return (0.0, 0.0, 0.0)
        
    return (min(lista_numeros), max(lista_numeros), round(sum(lista_numeros) / len(lista_numeros), 2))


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_varios_parametros.py")
    
    # Parámetros posicionales
    p1 = calcular_precio_con_descuento_e_iva(100, 10, 21)
    print(f"Base 100€, desc 10%, IVA 21%: {p1}€ (Esperado: 108.9€)")
    
    # Parámetros por defecto
    p_def = calcular_precio_final(100)
    print(f"Base 100€ con valores por defecto: {p_def}€ (Esperado: 121.0€)")
    
    # *args
    suma = sumar_gastos(10.5, 20.0, 5.25)
    print(f"Suma de gastos: {suma}€ (Esperado: 35.75€)")
    print(f"Media de notas (8, 9, 7): {calcular_media(8, 9, 7)}")
    
    # **kwargs
    ficha = mostrar_ficha(nombre="Ismael Vargas", proyecto="Asistente Personal", version="1.0")
    print(ficha)
    
    # Retorno múltiple (tupla)
    cuota, resto = repartir_cuenta(100.0, 3)
    print(f"Reparto de 100€ entre 3 -> Cuota: {cuota}€, Resto: {resto}€")
    
    min_v, max_v, med_v = estadisticas_basicas([12, 5, 8, 20, 15])
    print(f"Estadísticas -> Min: {min_v}, Max: {max_v}, Media: {med_v}")
    
    print("[TEST] Pruebas de ap_varios_parametros.py finalizadas con éxito.\n")
