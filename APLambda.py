"""
APLambda.py
Práctica de funciones lambda (anónimas) y su uso con sorted(), filter() y map().

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

# ==============================================================================
# ¿QUÉ ES UNA FUNCIÓN LAMBDA? (Para defender ante el profesor)
#
# Una función lambda es una función ANÓNIMA (sin nombre) que se define en una
# única línea de código.
#
# Sintaxis:
#   lambda argumento1, argumento2: expresion_que_se_devuelve
#
# Características principales:
# 1. No lleva la palabra reservada 'def' ni la sentencia 'return'; devuelve
#    automáticamente el resultado de evaluar su única expresión.
# 2. Es exactamente el equivalente a las 'arrow functions' de JavaScript:
#    Python:     (lambda x: x * 2)
#    JavaScript: (x => x * 2)
#
# ¿CUÁNDO USAR LAMBDA VS DEF?
# - Usa LAMBDA: Para operaciones sencillas y de un solo uso, especialmente como
#   parámetro 'key' en sorted() o en funciones de orden superior como filter() y map().
# - Usa DEF: Cuando la función requiere múltiples líneas, bucles, estructuras
#   try/except, o cuando se va a reutilizar en varias partes del programa.
# ==============================================================================


# 1. Lambda asignada a variable para cálculo de IVA (ejemplo didáctico de sintaxis)
# Recibe precio e iva opcional (por defecto 21%)
calcular_iva_lambda = lambda precio, iva=21: round(precio * (iva / 100), 2)

# 2. Lambda para convertir grados Celsius a Fahrenheit
celsius_a_fahrenheit_lambda = lambda c: round((c * 9 / 5) + 32, 2)


def ordenar_contactos_por_nombre(contactos):
    """
    Ordena una lista de diccionarios de contactos alfabéticamente por su nombre
    utilizando sorted() con una función lambda como criterio de ordenación.
    
    Parámetros:
        contactos (list): Lista de diccionarios {"nombre", "telefono", "email"}.
        
    Devuelve:
        list: Nueva lista ordenada de la A a la Z sin alterar la original.
    """
    # La lambda extrae el nombre en minúsculas de cada diccionario para ordenar sin importar mayúsculas
    return sorted(contactos, key=lambda c: c["nombre"].lower())


def ordenar_contactos_por_telefono(contactos):
    """
    Ordena los contactos numéricamente por su teléfono usando sorted() y lambda.
    """
    return sorted(contactos, key=lambda c: c["telefono"])


def filtrar_productos_stock_bajo(inventario, limite=5):
    """
    Filtra los productos que tienen existencias iguales o inferiores al límite
    utilizando la función filter() de Python junto con una lambda.
    
    Parámetros:
        inventario (list): Lista de diccionarios {"nombre", "precio", "stock"}.
        limite (int): Umbral de stock para considerar que está bajo (por defecto 5).
        
    Devuelve:
        list: Lista con los productos filtrados.
    """
    # filter() aplica la condición booleana de la lambda a cada producto
    # Convertimos el resultado de filter a list() porque filter devuelve un iterador
    productos_bajo_stock = list(filter(lambda p: p["stock"] <= limite, inventario))
    return productos_bajo_stock


def aplicar_descuento_a_precios(precios, porcentaje_descuento):
    """
    Aplica un descuento porcentual a toda una lista de precios utilizando
    la función map() de Python y una función lambda.
    
    Parámetros:
        precios (list): Lista de precios originales en euros.
        porcentaje_descuento (float/int): Porcentaje a rebajar (ej: 15 para 15%).
        
    Devuelve:
        list: Nueva lista de precios con el descuento ya aplicado y redondeados a 2 decimales.
    """
    # map() aplica la transformación de la lambda a cada elemento de la lista 'precios'
    factor = 1 - (porcentaje_descuento / 100)
    precios_rebajados = list(map(lambda p: round(p * factor, 2), precios))
    return precios_rebajados


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE APLambda.py <<<\n")

    # 1. Prueba de lambdas directas (IVA y Temperatura)
    print("--- 1. Lambdas sencillas ---")
    p = 100.0
    print(f"IVA de {p}€ al 21%: {calcular_iva_lambda(p)}€")
    print(f"IVA de {p}€ al 10% (reducido): {calcular_iva_lambda(p, 10)}€")
    
    temp_c = 25.0
    print(f"{temp_c} ºC a Fahrenheit: {celsius_a_fahrenheit_lambda(temp_c)} ºF")

    # 2. Prueba de ordenación con sorted() y lambda
    print("\n--- 2. Ordenación con sorted() y lambda ---")
    agenda_desordenada = [
        {"nombre": "Zoe Marín", "telefono": "655998877", "email": "zoe@correo.com"},
        {"nombre": "Alberto Gil", "telefono": "611002233", "email": "alberto@correo.com"},
        {"nombre": "marta salas", "telefono": "644112233", "email": "marta@correo.com"},
        {"nombre": "Beatriz Cruz", "telefono": "622445566", "email": "beatriz@correo.com"}
    ]
    
    agenda_por_nombre = ordenar_contactos_por_nombre(agenda_desordenada)
    print("Contactos ordenados por nombre (A-Z, insensible a mayúsculas):")
    for c in agenda_por_nombre:
        print(f"  • {c['nombre']} - Tel: {c['telefono']}")

    # 3. Prueba de filtrado con filter() y lambda
    print("\n--- 3. Filtrado con filter() y lambda (stock bajo) ---")
    catalogo = [
        {"nombre": "Portátil i7", "precio": 799.0, "stock": 2},
        {"nombre": "Ratón Óptico", "precio": 12.5, "stock": 25},
        {"nombre": "Teclado RGB", "precio": 35.0, "stock": 4},
        {"nombre": "Auriculares", "precio": 29.9, "stock": 0},
        {"nombre": "Webcam 1080p", "precio": 45.0, "stock": 18}
    ]
    
    alerta_stock = filtrar_productos_stock_bajo(catalogo, limite=5)
    print("Productos con stock en alerta (<= 5 unidades):")
    for p in alerta_stock:
        print(f"  ⚠️ {p['nombre']}: solo quedan {p['stock']} unidades.")

    # 4. Prueba de transformación con map() y lambda
    print("\n--- 4. Transformación con map() y lambda (descuentos) ---")
    precios_originales = [10.0, 25.50, 49.99, 100.0, 199.95]
    descuento_black_friday = 20  # 20%
    precios_finales = aplicar_descuento_a_precios(precios_originales, descuento_black_friday)
    
    print(f"Precios originales: {precios_originales}")
    print(f"Precios con {descuento_black_friday}% de descuento: {precios_finales}")

    print("\n>>> TODAS LAS PRUEBAS DE APLambda.py COMPLETADAS CON ÉXITO <<<")
