"""
funciones.py
Biblioteca central de funciones lógicas y matemáticas de Mi Asistente Personal.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""


# ------------------------------------------------------------------------------
# 1. Utilidades de validación y entrada de datos
# ------------------------------------------------------------------------------

def pedir_numero(mensaje, minimo=None, maximo=None):
    """
    Solicita un valor numérico por consola y valida que cumpla con los límites especificados.
    Garantiza que el programa no termine con excepciones de tipo ValueError.
    
    Parámetros:
        mensaje (str): Texto indicador para la solicitud del dato.
        minimo (float | int, opcional): Límite inferior permitido.
        maximo (float | int, opcional): Límite superior permitido.
        
    Retorna:
        float: Número validado introducido por el usuario.
    """
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"Error: El valor no puede ser inferior a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: El valor no puede ser superior a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida: Introduce un valor numérico (ejemplo: 12.50).")


def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita un número entero por consola validando su formato y rango.
    
    Parámetros:
        mensaje (str): Texto indicador.
        minimo (int, opcional): Límite inferior.
        maximo (int, opcional): Límite superior.
        
    Retorna:
        int: Entero validado.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"Error: Debe ser un entero mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: Debe ser un entero menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida: Introduce un número entero sin decimales.")


def pedir_texto(mensaje, permitir_vacio=False):
    """
    Solicita una cadena de texto impidiendo entradas vacías por defecto.
    
    Parámetros:
        mensaje (str): Texto de la pregunta.
        permitir_vacio (bool): Determina si se admiten cadenas en blanco.
        
    Retorna:
        str: Texto saneado.
    """
    while True:
        texto = input(mensaje).strip()
        if not texto and not permitir_vacio:
            print("Campo obligatorio. No puede quedar en blanco.")
            continue
        return texto


def pedir_opcion_menu(opciones_validas):
    """
    Solicita una opción de menú asegurando que pertenezca al conjunto permitido.
    
    Parámetros:
        opciones_validas (iterable): Colección de opciones aceptadas.
        
    Retorna:
        str: Opción seleccionada.
    """
    validas_str = [str(op) for op in opciones_validas]
    while True:
        opcion = input("Selecciona una opción: ").strip()
        if opcion in validas_str:
            return opcion
        print(f"Opción no válida. Opciones disponibles: {', '.join(validas_str)}")


# ------------------------------------------------------------------------------
# 2. Gestión de compras y facturación
# ------------------------------------------------------------------------------

def calcular_precio_final(precio, descuento=0, iva=21):
    """
    Calcula el precio final aplicando descuento y posterior recargo de IVA.
    
    Parámetros:
        precio (float): Base imponible (>= 0).
        descuento (float, opcional): Descuento porcentual (0 a 100).
        iva (float, opcional): Tipo impositivo de IVA.
        
    Retorna:
        float: Precio final redondeado a dos decimales.
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    base_rebajada = precio * (1 - (descuento / 100))
    total = base_rebajada * (1 + (iva / 100))
    return round(total, 2)


def desglosar_ticket(precio, descuento=0, iva=21):
    """
    Genera el desglose contable de una transacción.
    Retorna una tupla con (base, importe_descuento, importe_iva, total).
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return (0.0, 0.0, 0.0, 0.0)
        
    importe_descuento = round(precio * (descuento / 100), 2)
    base_imponible = round(precio - importe_descuento, 2)
    importe_iva = round(base_imponible * (iva / 100), 2)
    total = round(base_imponible + importe_iva, 2)
    
    return (round(precio, 2), importe_descuento, importe_iva, total)


# ------------------------------------------------------------------------------
# 3. Gestión económica y presupuestos
# ------------------------------------------------------------------------------

def sumar_gastos(*gastos):
    """
    Suma una cantidad indeterminada de gastos positivos recibidos en una tupla (*args).
    """
    total = 0.0
    for g in gastos:
        if g > 0:
            total += g
    return round(total, 2)


def calcular_presupuesto_restante(presupuesto_inicial, *gastos):
    """
    Calcula el balance presupuestario restante y el porcentaje consumido.
    Retorna una tupla: (saldo_restante, porcentaje_gastado).
    """
    if presupuesto_inicial <= 0:
        return (0.0, 100.0)
        
    total_gastado = sumar_gastos(*gastos)
    saldo_restante = round(presupuesto_inicial - total_gastado, 2)
    porcentaje = round((total_gastado / presupuesto_inicial) * 100, 2)
    return (saldo_restante, porcentaje)


def repartir_cuenta(total, personas):
    """
    Calcula la cuota exacta por persona y el posible descuadre de céntimos.
    Retorna (cuota_individual, resto_centimos).
    """
    if total <= 0 or personas <= 0:
        return (0.0, 0.0)
        
    cuota = round(total / personas, 2)
    resto = round(total - (cuota * personas), 2)
    return (cuota, resto)


def resumen_gastos(lista_gastos):
    """
    Calcula agregados estadísticos sobre una colección de gastos:
    Retorna (total, media, maximo, minimo).
    """
    if not lista_gastos:
        return (0.0, 0.0, 0.0, 0.0)
        
    total = round(sum(lista_gastos), 2)
    media = round(total / len(lista_gastos), 2)
    mayor = round(max(lista_gastos), 2)
    menor = round(min(lista_gastos), 2)
    return (total, media, mayor, menor)


# ------------------------------------------------------------------------------
# 4. Conversores de unidades
# ------------------------------------------------------------------------------

def convertir_temperatura(valor, origen, destino):
    """
    Convierte magnitudes térmicas entre Celsius (C), Fahrenheit (F) y Kelvin (K).
    """
    orig, dest = origen.upper().strip(), destino.upper().strip()
    
    if orig == "C":
        celsius = valor
    elif orig == "F":
        celsius = (valor - 32) * 5 / 9
    elif orig == "K":
        celsius = valor - 273.15
    else:
        return None
        
    if dest == "C":
        res = celsius
    elif dest == "F":
        res = (celsius * 9 / 5) + 32
    elif dest == "K":
        res = celsius + 273.15
    else:
        return None
        
    return round(res, 2)


def convertir_tiempo(valor, unidad_origen, unidad_destino):
    """
    Convierte intervalos temporales entre segundos (s), minutos (m), horas (h) y días (d).
    Utiliza el segundo como factor base.
    """
    if valor < 0:
        return -1.0
        
    factores = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    orig, dest = unidad_origen.lower().strip(), unidad_destino.lower().strip()
    
    if orig not in factores or dest not in factores:
        return -1.0
        
    segundos = valor * factores[orig]
    return round(segundos / factores[dest], 4)


def convertir_distancia(valor, unidad_origen, unidad_destino):
    """
    Convierte distancias entre metros (m), kilómetros (km), millas (mi) y pies (ft).
    Utiliza el metro como factor base.
    """
    if valor < 0:
        return -1.0
        
    factores = {"m": 1.0, "km": 1000.0, "mi": 1609.344, "ft": 0.3048}
    orig, dest = unidad_origen.lower().strip(), unidad_destino.lower().strip()
    
    if orig not in factores or dest not in factores:
        return -1.0
        
    metros = valor * factores[orig]
    return round(metros / factores[dest], 4)


# ------------------------------------------------------------------------------
# 5. Agenda de contactos
# ------------------------------------------------------------------------------

def añadir_contacto(agenda, nombre, telefono, email):
    """
    Registra un contacto asegurando unicidad por nombre.
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


def buscar_contactos(agenda, criterio):
    """
    Filtra contactos que coincidan con el criterio en nombre, teléfono o email.
    """
    crit = criterio.strip().lower()
    return [c for c in agenda if (crit in c["nombre"].lower() or 
                                  crit in c["telefono"].lower() or 
                                  crit in c["email"].lower())]


def eliminar_contacto(agenda, nombre):
    """
    Elimina un contacto por coincidencia de nombre exacto.
    """
    nom = nombre.strip().lower()
    for i, c in enumerate(agenda):
        if c["nombre"].strip().lower() == nom:
            del agenda[i]
            return True
    return False


def ordenar_contactos(agenda):
    """
    Retorna una nueva lista de contactos ordenada alfabéticamente (A-Z) mediante lambda.
    """
    return sorted(agenda, key=lambda c: c["nombre"].lower())


# ------------------------------------------------------------------------------
# 6. Gestión de inventario de productos
# ------------------------------------------------------------------------------

def registrar_producto(inventario, nombre, precio, stock):
    """
    Registra un nuevo producto en catálogo impidiendo duplicados y valores negativos.
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
    Busca un producto por su nombre exacto en el catálogo.
    """
    nom = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == nom:
            return p
    return None


def actualizar_stock(inventario, nombre, cantidad):
    """
    Actualiza existencias de un producto. Impide saldos negativos de stock.
    Retorna tupla: (exito, nuevo_stock, mensaje).
    """
    prod = buscar_producto(inventario, nombre)
    if prod is None:
        return (False, -1, f"El producto '{nombre}' no existe en el catálogo.")
        
    nuevo_stock = prod["stock"] + cantidad
    if nuevo_stock < 0:
        return (False, prod["stock"], f"Operación denegada: existencias insuficientes ({prod['stock']} uds).")
        
    prod["stock"] = nuevo_stock
    return (True, nuevo_stock, f"Existencias actualizadas a {nuevo_stock} unidades.")


def obtener_alertas_stock_bajo(inventario, limite=5):
    """
    Retorna los artículos con stock menor o igual al umbral mediante filter y lambda.
    """
    return list(filter(lambda p: p["stock"] <= limite, inventario))


# ------------------------------------------------------------------------------
# 7. Utilidades matemáticas recursivas
# ------------------------------------------------------------------------------

def calcular_factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    Caso base: n <= 1 -> 1
    Caso recursivo: n * factorial(n - 1)
    """
    if not isinstance(n, int) or n < 0:
        return -1
    if n in (0, 1):
        return 1
    return n * calcular_factorial(n - 1)


def calcular_fibonacci(n):
    """
    Calcula el término n de Fibonacci recursivamente.
    Se acota a n <= 30 para evitar el bloqueo del hilo de ejecución.
    """
    if not isinstance(n, int) or n < 0 or n > 30:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)


def calcular_mcd(a, b):
    """
    Calcula el Máximo Común Divisor mediante el algoritmo de Euclides recursivo.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return -1
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return calcular_mcd(b, a % b)


# ------------------------------------------------------------------------------
# 8. Análisis de información y filtrado de datos
# ------------------------------------------------------------------------------

def calcular_estadisticas_completas(lista_numeros):
    """
    Calcula media, mediana, moda, mínimo y máximo de una colección.
    Retorna una tupla: (media, mediana, moda, minimo, maximo).
    """
    if not lista_numeros:
        return (0.0, 0.0, 0.0, 0, 0)
        
    ordenados = sorted(lista_numeros)
    n = len(ordenados)
    
    media = round(sum(ordenados) / n, 2)
    
    if n % 2 == 1:
        mediana = ordenados[n // 2]
    else:
        mediana = round((ordenados[(n // 2) - 1] + ordenados[n // 2]) / 2, 2)
        
    frecuencias = {}
    for num in ordenados:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    moda = max(frecuencias, key=lambda k: frecuencias[k])
    
    return (media, mediana, moda, ordenados[0], ordenados[-1])


def filtrar_lista_numeros(lista_numeros, criterio, valor_corte=0):
    """
    Filtra una lista numérica aplicando filter() y lambdas según el criterio dado.
    """
    if not lista_numeros:
        return []
        
    criterios = {
        "pares": lambda x: x % 2 == 0,
        "impares": lambda x: x % 2 != 0,
        "mayores": lambda x: x > valor_corte,
        "menores": lambda x: x < valor_corte
    }
    
    filtro = criterios.get(criterio)
    return list(filter(filtro, lista_numeros)) if filtro else lista_numeros


if __name__ == "__main__":
    print("[TEST] Ejecutando verificación de funciones.py")
    t = desglosar_ticket(100, 10, 21)
    print(f"Desglose ticket: {t}")
    mcd = calcular_mcd(60, 24)
    print(f"MCD(60, 24): {mcd}")
    print("[TEST] Verificación completada con éxito.\n")
