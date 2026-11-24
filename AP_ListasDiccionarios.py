"""
AP_ListasDiccionarios.py
Práctica de funciones que trabajan con colecciones: listas y diccionarios.

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

# ==============================================================================
# CONTACTOS (Lista de diccionarios: {"nombre", "telefono", "email"})
# ==============================================================================

def añadir_contacto(agenda, nombre, telefono, email):
    """
    Añade un nuevo contacto a la agenda si el nombre no está ya registrado.
    
    Parámetros:
        agenda (list): Lista de diccionarios con los contactos existentes.
        nombre (str): Nombre del contacto (no puede estar vacío).
        telefono (str): Teléfono de contacto.
        email (str): Correo electrónico.
        
    Devuelve:
        bool: True si se añadió con éxito, False si ya existía o los datos son inválidos.
    """
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return False
        
    # Comprobamos si ya existe alguien con ese mismo nombre (sin distinguir mayúsculas)
    for c in agenda:
        if c["nombre"].strip().lower() == nombre_limpio.lower():
            # Ya existe un contacto con ese nombre: evitamos duplicados
            return False
            
    # Creamos el nuevo diccionario con los datos del contacto
    nuevo_contacto = {
        "nombre": nombre_limpio,
        "telefono": telefono.strip(),
        "email": email.strip()
    }
    agenda.append(nuevo_contacto)
    return True


def buscar_contacto(agenda, texto_buscar):
    """
    Busca contactos cuyo nombre contenga el texto buscado (búsqueda flexible).
    
    Parámetros:
        agenda (list): Lista de contactos.
        texto_buscar (str): Subcadena a buscar en el nombre.
        
    Devuelve:
        list: Lista con los diccionarios de contactos que coinciden.
    """
    texto = texto_buscar.strip().lower()
    coincidencias = []
    
    for c in agenda:
        # 'in' comprueba si la subcadena está dentro del nombre
        if texto in c["nombre"].lower():
            coincidencias.append(c)
            
    return coincidencias


def ordenar_contactos(agenda):
    """
    Devuelve una NUEVA lista de contactos ordenada alfabéticamente por nombre.
    No modifica la lista original (principio de inmutabilidad).
    
    Parámetros:
        agenda (list): Lista de contactos.
        
    Devuelve:
        list: Nueva lista ordenada por nombre en orden ascendente (A-Z).
    """
    # Usamos sorted() con una función normal para extraer la clave de ordenación
    def obtener_nombre(contacto):
        return contacto["nombre"].lower()
        
    return sorted(agenda, key=obtener_nombre)


# ==============================================================================
# INVENTARIO DE PRODUCTOS (Lista de diccionarios: {"nombre", "precio", "stock"})
# ==============================================================================

def registrar_producto(inventario, nombre, precio, stock):
    """
    Registra un producto en el inventario comprobando que no esté repetido
    y que el precio y stock sean valores válidos (>= 0).
    
    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto.
        precio (float/int): Precio unitario en euros (>= 0).
        stock (int): Unidades disponibles (>= 0).
        
    Devuelve:
        bool: True si el registro fue exitoso, False si ya existía o los datos son incorrectos.
    """
    nombre_limpio = nombre.strip()
    if not nombre_limpio or precio < 0 or stock < 0:
        return False
        
    # Verificamos si ya existe
    for p in inventario:
        if p["nombre"].strip().lower() == nombre_limpio.lower():
            return False
            
    producto = {
        "nombre": nombre_limpio,
        "precio": round(float(precio), 2),
        "stock": int(stock)
    }
    inventario.append(producto)
    return True


def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre exacto (case-insensitive).
    
    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a localizar.
        
    Devuelve:
        dict: Diccionario del producto encontrado, o None si no existe.
    """
    nombre_buscar = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == nombre_buscar:
            return p
    return None


def actualizar_stock(inventario, nombre, cantidad):
    """
    Incrementa (entrada de almacén) o decrementa (venta) el stock de un producto.
    No permite que el stock resultante sea negativo.
    
    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a modificar.
        cantidad (int): Unidades a sumar (positivo) o restar (negativo).
        
    Devuelve:
        tuple: (exito, stock_actual, mensaje)
               - exito (bool): True si se pudo actualizar, False en caso contrario.
               - stock_actual (int): Cantidad que queda en stock.
               - mensaje (str): Explicación del resultado.
    """
    prod = buscar_producto(inventario, nombre)
    if prod is None:
        return (False, -1, f"El producto '{nombre}' no existe en el inventario.")
        
    nuevo_stock = prod["stock"] + cantidad
    if nuevo_stock < 0:
        # Stock insuficiente para la venta
        return (False, prod["stock"], f"Stock insuficiente: se intentó retirar {abs(cantidad)} pero solo hay {prod['stock']}.")
        
    prod["stock"] = nuevo_stock
    return (True, nuevo_stock, f"Stock actualizado con éxito a {nuevo_stock} unidades.")


def obtener_productos_sin_stock(inventario):
    """
    Filtra y devuelve todos los productos con stock igual a 0.
    
    Parámetros:
        inventario (list): Lista de productos.
        
    Devuelve:
        list: Lista con los productos agotados.
    """
    agotados = []
    for p in inventario:
        if p["stock"] == 0:
            agotados.append(p)
    return agotados


# ==============================================================================
# FILTRADO Y PROCESAMIENTO DE LISTAS NUMÉRICAS
# ==============================================================================

def filtrar_mayores_que(numeros, limite):
    """
    Filtra una lista de números devolviendo solo aquellos que superan un umbral.
    
    Parámetros:
        numeros (list): Lista de números a evaluar.
        limite (float/int): Valor umbral de corte.
        
    Devuelve:
        list: Nueva lista con los números estrictamente mayores que el límite.
    """
    resultado = []
    for n in numeros:
        if n > limite:
            resultado.append(n)
    return resultado


def eliminar_duplicados(lista):
    """
    Elimina elementos repetidos de una lista conservando el orden de aparición original.
    
    Parámetros:
        lista (list): Lista con posibles elementos duplicados.
        
    Devuelve:
        list: Nueva lista con elementos únicos.
    """
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE AP_ListasDiccionarios.py <<<\n")

    # 1. Pruebas de Agenda de Contactos
    print("--- 1. Pruebas de Agenda de Contactos ---")
    agenda_demo = []
    print(f"Añadir 'Carlos Gómez': {añadir_contacto(agenda_demo, 'Carlos Gómez', '600112233', 'carlos@mail.com')}")
    print(f"Añadir 'Ana Ruiz': {añadir_contacto(agenda_demo, 'Ana Ruiz', '611223344', 'ana@mail.com')}")
    print(f"Añadir 'Beatriz López': {añadir_contacto(agenda_demo, 'Beatriz López', '622334455', 'bea@mail.com')}")
    # Intento de duplicado:
    print(f"Reintentar añadir 'carlos gómez' (duplicado): {añadir_contacto(agenda_demo, 'carlos gómez', '999', 'dup@mail.com')}")
    
    # Búsqueda
    print(f"Buscar 'ru': {[c['nombre'] for c in buscar_contacto(agenda_demo, 'ru')]}")
    
    # Ordenación
    agenda_ordenada = ordenar_contactos(agenda_demo)
    print("Agenda ordenada alfabéticamente:")
    for c in agenda_ordenada:
        print(f"  - {c['nombre']} ({c['telefono']})")

    # 2. Pruebas de Gestión de Inventario
    print("\n--- 2. Pruebas de Inventario de Productos ---")
    inventario_demo = []
    print(f"Registrar 'Ratón USB': {registrar_producto(inventario_demo, 'Ratón USB', 15.99, 10)}")
    print(f"Registrar 'Teclado Mecánico': {registrar_producto(inventario_demo, 'Teclado Mecánico', 49.99, 5)}")
    print(f"Registrar 'Monitor 24': {registrar_producto(inventario_demo, 'Monitor 24', 120.00, 0)}")
    # Intento de registrar con stock negativo:
    print(f"Registrar con stock negativo (error): {registrar_producto(inventario_demo, 'Cable HDMI', 5.0, -2)}")

    # Actualizar stock
    ok, nuevo_st, msg = actualizar_stock(inventario_demo, "Ratón USB", -3)
    print(f"Vender 3 ratones: Éxito={ok} | {msg}")
    
    ok_fallo, _, msg_fallo = actualizar_stock(inventario_demo, "Teclado Mecánico", -10)
    print(f"Intentar vender 10 teclados (solo hay 5): Éxito={ok_fallo} | {msg_fallo}")

    # Productos agotados
    sin_stock = obtener_productos_sin_stock(inventario_demo)
    print(f"Productos sin stock (agotados): {[p['nombre'] for p in sin_stock]}")

    # 3. Pruebas de Filtrado de Listas
    print("\n--- 3. Pruebas de Listas: Filtrar y Duplicados ---")
    datos = [10, 5, 20, 8, 20, 15, 5, 30]
    print(f"Lista original: {datos}")
    print(f"Mayores que 12: {filtrar_mayores_que(datos, 12)}")
    print(f"Sin duplicados (manteniendo orden): {eliminar_duplicados(datos)}")
    
    # Caso límite: lista vacía
    print(f"Filtrar lista vacía: {filtrar_mayores_que([], 10)}")
    print(f"Eliminar duplicados de lista vacía: {eliminar_duplicados([])}")

    print("\n>>> TODAS LAS PRUEBAS DE AP_ListasDiccionarios.py COMPLETADAS CON ÉXITO <<<")
