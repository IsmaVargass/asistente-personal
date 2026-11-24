"""
ap_lambda.py
Módulo de funciones anónimas (Lambda) y su integración con sorted, filter y map.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""

# Funciones lambda de evaluación directa
calcular_iva_lambda = lambda precio, iva=21: round(precio * (iva / 100), 2)
celsius_a_fahrenheit_lambda = lambda c: round((c * 9 / 5) + 32, 2)


def ordenar_contactos_por_nombre(contactos):
    """
    Ordena una lista de diccionarios alfabéticamente por la clave 'nombre'.
    Utiliza sorted() con una expresión lambda como clave de ordenación.
    """
    return sorted(contactos, key=lambda c: c["nombre"].lower())


def filtrar_productos_stock_bajo(inventario, limite=5):
    """
    Filtra los artículos que se encuentran por debajo o igual al umbral de existencias.
    Aplica filter() en combinación con una función lambda.
    """
    return list(filter(lambda p: p["stock"] <= limite, inventario))


def aplicar_descuento_a_precios(precios, porcentaje_descuento):
    """
    Transforma una colección de precios aplicando un porcentaje de descuento.
    Utiliza map() junto a una expresión lambda.
    """
    factor = 1 - (porcentaje_descuento / 100)
    return list(map(lambda p: round(p * factor, 2), precios))


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_lambda.py")
    
    # Lambdas directas
    print(f"IVA de 100€ (21%): {calcular_iva_lambda(100)}€")
    print(f"20 ºC a Fahrenheit: {celsius_a_fahrenheit_lambda(20)} ºF")
    
    # Ordenación con lambda
    contactos = [
        {"nombre": "Zoe Marín", "telefono": "655112233"},
        {"nombre": "Alberto Gil", "telefono": "611002233"},
        {"nombre": "Beatriz Cruz", "telefono": "622445566"}
    ]
    ordenados = ordenar_contactos_por_nombre(contactos)
    print(f"Contactos ordenados: {[c['nombre'] for c in ordenados]}")
    
    # Filtrado con lambda
    catalogo = [
        {"nombre": "Ratón", "stock": 12},
        {"nombre": "Teclado", "stock": 3},
        {"nombre": "Monitor", "stock": 1}
    ]
    alertas = filtrar_productos_stock_bajo(catalogo, limite=5)
    print(f"Stock bajo (<= 5): {[p['nombre'] for p in alertas]}")
    
    # Mapeo con lambda
    precios = [50.0, 100.0, 200.0]
    rebajas = aplicar_descuento_a_precios(precios, 15)
    print(f"Precios originales: {precios} -> Con 15% desc: {rebajas}")
    
    print("[TEST] Pruebas de ap_lambda.py finalizadas con éxito.\n")
