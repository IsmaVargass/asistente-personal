"""
ap_listas_diccionarios.py
Módulo para el manejo de colecciones: listas y diccionarios en memoria.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""


def añadir_contacto(agenda, nombre, telefono, email):
    """
    Registra un nuevo contacto en la agenda asegurando que no existan nombres duplicados.
    
    Parámetros:
        agenda (list): Lista de diccionarios con contactos existentes.
        nombre (str): Nombre del contacto.
        telefono (str): Teléfono asociado.
        email (str): Correo electrónico.
        
    Retorna:
        bool: True si el contacto fue registrado, False si ya existía o los datos son inválidos.
    """
    nom = nombre.strip()
    if not nom:
        return False
        
    for c in agenda:
        if c["nombre"].strip().lower() == nom.lower():
            return False
            
    agenda.append({
        "nombre": nom,
        "telefono": telefono.strip(),
        "email": email.strip()
    })
    return True


def buscar_contacto(agenda, criterio):
    """
    Localiza contactos que coincidan parcialmente con un criterio de búsqueda.
    
    Parámetros:
        agenda (list): Lista de contactos.
        criterio (str): Subcadena de búsqueda.
        
    Retorna:
        list: Lista de diccionarios que coinciden con el criterio.
    """
    crit = criterio.strip().lower()
    return [c for c in agenda if crit in c["nombre"].lower()]


def ordenar_contactos(agenda):
    """
    Retorna una nueva lista de contactos ordenada alfabéticamente por nombre.
    No altera la lista original.
    
    Parámetros:
        agenda (list): Colección de contactos.
        
    Retorna:
        list: Colección ordenada ascendentemente.
    """
    return sorted(agenda, key=lambda c: c["nombre"].lower())


def registrar_producto(inventario, nombre, precio, stock):
    """
    Incorpora un producto al catálogo controlando precio y existencias no negativas.
    
    Parámetros:
        inventario (list): Catálogo de productos.
        nombre (str): Denominación del producto.
        precio (float | int): Precio unitario (>= 0).
        stock (int): Unidades en almacén (>= 0).
        
    Retorna:
        bool: True si se registró con éxito, False si ya existe o hay datos no válidos.
    """
    nom = nombre.strip()
    if not nom or precio < 0 or stock < 0:
        return False
        
    for p in inventario:
        if p["nombre"].strip().lower() == nom.lower():
            return False
            
    inventario.append({
        "nombre": nom,
        "precio": round(float(precio), 2),
        "stock": int(stock)
    })
    return True


def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre exacto (insensible a mayúsculas).
    
    Parámetros:
        inventario (list): Catálogo de productos.
        nombre (str): Nombre a buscar.
        
    Retorna:
        dict | None: Diccionario del producto o None si no se encuentra.
    """
    nom = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == nom:
            return p
    return None


def actualizar_stock(inventario, nombre, cantidad):
    """
    Modifica las unidades de stock (entradas o salidas).
    Bloquea la operación si la salida provocaría un balance de stock negativo.
    
    Parámetros:
        inventario (list): Catálogo de productos.
        nombre (str): Nombre del producto a actualizar.
        cantidad (int): Valor a sumar (positivo) o restar (negativo).
        
    Retorna:
        tuple[bool, int, str]: (exito, stock_actual, mensaje_descriptivo).
    """
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        return (False, -1, f"El producto '{nombre}' no existe en el catálogo.")
        
    nuevo_stock = producto["stock"] + cantidad
    if nuevo_stock < 0:
        return (False, producto["stock"], f"Stock insuficiente: existencias actuales ({producto['stock']}).")
        
    producto["stock"] = nuevo_stock
    return (True, nuevo_stock, f"Stock actualizado a {nuevo_stock} unidades.")


def obtener_productos_sin_stock(inventario):
    """
    Filtra los productos cuyas existencias sean iguales a cero.
    
    Parámetros:
        inventario (list): Catálogo de productos.
        
    Retorna:
        list: Lista de productos agotados.
    """
    return [p for p in inventario if p["stock"] == 0]


def filtrar_mayores_que(numeros, limite):
    """
    Filtra una lista numérica conservando únicamente valores que superen el límite.
    """
    return [n for n in numeros if n > limite]


def eliminar_duplicados(lista):
    """
    Elimina elementos repetidos conservando el orden de aparición original.
    """
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_listas_diccionarios.py")
    
    # Agenda
    agenda = []
    añadir_contacto(agenda, "Ismael Vargas", "600123456", "ismael@correo.com")
    añadir_contacto(agenda, "Beatriz Ramos", "611987654", "beatriz@correo.com")
    print(f"Agenda registrada: {len(agenda)} contactos.")
    
    # Inventario
    inventario = []
    registrar_producto(inventario, "Monitor 4K", 299.99, 5)
    registrar_producto(inventario, "Teclado Mecánico", 79.50, 0)
    
    ok, stock_act, msg = actualizar_stock(inventario, "Monitor 4K", -2)
    print(f"Venta de 2 monitores: {msg}")
    
    ok_err, _, msg_err = actualizar_stock(inventario, "Monitor 4K", -10)
    print(f"Intento de sobreventa: {msg_err}")
    
    agotados = obtener_productos_sin_stock(inventario)
    print(f"Productos agotados: {[p['nombre'] for p in agotados]}")
    
    # Listas
    datos = [1, 2, 2, 3, 4, 4, 5]
    print(f"Sin duplicados: {eliminar_duplicados(datos)}")
    
    print("[TEST] Pruebas de ap_listas_diccionarios.py finalizadas con éxito.\n")
