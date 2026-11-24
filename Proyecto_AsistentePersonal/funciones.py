"""
funciones.py
Módulo de lógica de negocio y funciones de "Mi Asistente Personal".

Contiene todas las funciones independientes y reutilizables del proyecto,
organizadas por secciones temáticas.

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

from datetime import datetime


# ==============================================================================
# SECCIÓN 1: UTILIDADES DE VALIDACIÓN Y ENTRADA DE DATOS
# Estas funciones blindan el programa contra entradas erróneas del usuario.
# Usan bucles while y bloques try/except para que el asistente NUNCA 'pete'.
# ==============================================================================

def pedir_numero(mensaje, minimo=None, maximo=None):
    """
    Solicita un número decimal o entero al usuario por teclado y valida su rango.
    Repite la petición hasta que el usuario introduzca un valor válido.
    
    Parámetros:
        mensaje (str): Texto explicativo que se muestra al usuario.
        minimo (float/int, opcional): Valor mínimo permitido (inclusivo).
        maximo (float/int, opcional): Valor máximo permitido (inclusivo).
        
    Devuelve:
        float: El número válido introducido por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()
        # Permitimos coma o punto como separador decimal para comodidad del usuario
        entrada = entrada.replace(",", ".")
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"  ❌ Error: El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ❌ Error: El valor no puede ser superior a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ❌ Entrada inválida: Por favor, escribe un número (ej: 12.50).")


def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita un número entero al usuario por teclado y valida su rango.
    
    Parámetros:
        mensaje (str): Texto mostrado al usuario.
        minimo (int, opcional): Valor entero mínimo permitido.
        maximo (int, opcional): Valor entero máximo permitido.
        
    Devuelve:
        int: El número entero introducido.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"  ❌ Error: Debe ser un entero mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ❌ Error: Debe ser un entero menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ❌ Entrada inválida: Por favor, escribe un número entero sin decimales.")


def pedir_texto(mensaje, permitir_vacio=False):
    """
    Solicita una cadena de texto al usuario evitando entradas vacías o solo espacios.
    
    Parámetros:
        mensaje (str): Texto de la pregunta.
        permitir_vacio (bool): Si es True, permite pulsar Enter sin escribir nada.
        
    Devuelve:
        str: El texto limpio introducido por el usuario.
    """
    while True:
        texto = input(mensaje).strip()
        if not texto and not permitir_vacio:
            print("  ❌ Este campo es obligatorio. No lo dejes en blanco.")
            continue
        return texto


def pedir_opcion_menu(opciones_validas):
    """
    Pide al usuario que elija una opción válida de un menú.
    
    Parámetros:
        opciones_validas (list/tuple/set): Colección de opciones permitidas (ej: ['1','2','3']).
        
    Devuelve:
        str: La opción válida elegida.
    """
    opciones_str = [str(op) for op in opciones_validas]
    while True:
        opcion = input("👉 Elige una opción: ").strip()
        if opcion in opciones_str:
            return opcion
        print(f"  ❌ Opción no reconocida. Debe ser una de las siguientes: {', '.join(opciones_str)}")


# ==============================================================================
# SECCIÓN 2: GESTIÓN DE COMPRAS
# Cálculo de precios con descuento e IVA, y desglose completo del ticket.
# ==============================================================================

def calcular_precio_final(precio, descuento=0, iva=21):
    """
    Calcula el precio final aplicando un descuento sobre la base y luego el IVA.
    Usa parámetros opcionales con valores por defecto (descuento=0%, IVA=21%).
    
    Parámetros:
        precio (float): Precio base en euros (>= 0).
        descuento (float): Porcentaje de descuento (entre 0 y 100).
        iva (float): Porcentaje de IVA a aplicar (>= 0).
        
    Devuelve:
        float: Precio total redondeado a 2 decimales, o -1.0 si los datos son inválidos.
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    precio_con_descuento = precio * (1 - (descuento / 100))
    total = precio_con_descuento * (1 + (iva / 100))
    return round(total, 2)


def desglosar_ticket(precio, descuento=0, iva=21):
    """
    Genera el desglose completo de un ticket de compra.
    Devuelve VARIOS RESULTADOS en una TUPLA: (base, descuento_euros, iva_euros, total).
    
    Parámetros:
        precio (float): Precio base.
        descuento (float): Porcentaje de descuento (0 a 100).
        iva (float): Porcentaje de IVA.
        
    Devuelve:
        tuple: (base, importe_descuento, importe_iva, total)
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return (0.0, 0.0, 0.0, 0.0)
        
    importe_descuento = round(precio * (descuento / 100), 2)
    base_imponible = round(precio - importe_descuento, 2)
    importe_iva = round(base_imponible * (iva / 100), 2)
    total = round(base_imponible + importe_iva, 2)
    
    return (round(precio, 2), importe_descuento, importe_iva, total)


# ==============================================================================
# SECCIÓN 3: GESTIÓN ECONÓMICA
# Presupuesto restante, suma con *args, reparto de cuenta (tupla) y resumen.
# ==============================================================================

def sumar_gastos(*gastos):
    """
    Suma una cantidad variable de gastos mediante *args.
    
    Parámetros:
        *gastos (float/int): Lista variable de importes monetarios.
        
    Devuelve:
        float: Total acumulado de gastos positivos.
    """
    total = 0.0
    for g in gastos:
        if g > 0:
            total += g
    return round(total, 2)


def calcular_presupuesto_restante(presupuesto_inicial, *gastos):
    """
    Calcula cuánto dinero queda del presupuesto inicial tras descontar los gastos.
    
    Parámetros:
        presupuesto_inicial (float): Presupuesto total disponible.
        *gastos (float): Gastos a restar.
        
    Devuelve:
        tuple: (saldo_restante, porcentaje_gastado)
    """
    if presupuesto_inicial <= 0:
        return (0.0, 100.0)
        
    total_gastado = sumar_gastos(*gastos)
    saldo_restante = round(presupuesto_inicial - total_gastado, 2)
    porcentaje = round((total_gastado / presupuesto_inicial) * 100, 2)
    return (saldo_restante, porcentaje)


def repartir_cuenta(total, personas):
    """
    Divide un total entre comensales y devuelve (cuota_individual, resto_centimos).
    
    Parámetros:
        total (float): Importe a pagar.
        personas (int): Número de personas (>= 1).
        
    Devuelve:
        tuple: (cuota, resto)
    """
    if total <= 0 or personas <= 0:
        return (0.0, 0.0)
        
    cuota = round(total / personas, 2)
    resto = round(total - (cuota * personas), 2)
    return (cuota, resto)


def resumen_gastos(lista_gastos):
    """
    Genera un informe con total, media, gasto mayor y menor de una lista.
    
    Parámetros:
        lista_gastos (list): Lista de importes numéricos.
        
    Devuelve:
        tuple: (total, media, mayor, menor)
               Devuelve (0.0, 0.0, 0.0, 0.0) si la lista está vacía.
    """
    if not lista_gastos:
        return (0.0, 0.0, 0.0, 0.0)
        
    total = round(sum(lista_gastos), 2)
    media = round(total / len(lista_gastos), 2)
    mayor = round(max(lista_gastos), 2)
    menor = round(min(lista_gastos), 2)
    return (total, media, mayor, menor)


# ==============================================================================
# SECCIÓN 4: CONVERSORES DE UNIDADES
# Temperaturas, tiempos y distancias usando diccionarios de factores para no
# repetir código (principio DRY).
# ==============================================================================

def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre Celsius (C), Fahrenheit (F) y Kelvin (K).
    
    Parámetros:
        valor (float): Grados a convertir.
        origen (str): 'C', 'F' o 'K'.
        destino (str): 'C', 'F' o 'K'.
        
    Devuelve:
        float: Temperatura convertida, o None si las unidades no son válidas.
    """
    orig = origen.upper().strip()
    dest = destino.upper().strip()
    
    # Paso 1: Convertimos cualquier origen a Celsius como unidad pivote
    if orig == "C":
        celsius = valor
    elif orig == "F":
        celsius = (valor - 32) * 5 / 9
    elif orig == "K":
        celsius = valor - 273.15
    else:
        return None
        
    # Paso 2: Convertimos de Celsius a la unidad destino
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
    Convierte una cantidad de tiempo entre segundos (s), minutos (m), horas (h) y días (d).
    Usa un diccionario de factores respecto al segundo como unidad base.
    
    Parámetros:
        valor (float): Cantidad a convertir (>= 0).
        unidad_origen (str): 's', 'm', 'h' o 'd'.
        unidad_destino (str): 's', 'm', 'h' o 'd'.
        
    Devuelve:
        float: Valor convertido, o -1.0 si es inválido.
    """
    if valor < 0:
        return -1.0
        
    factores_segundos = {
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 86400
    }
    
    u_orig = unidad_origen.lower().strip()
    u_dest = unidad_destino.lower().strip()
    
    if u_orig not in factores_segundos or u_dest not in factores_segundos:
        return -1.0
        
    # Convertimos a segundos y luego a la unidad de destino
    segundos = valor * factores_segundos[u_orig]
    resultado = segundos / factores_segundos[u_dest]
    return round(resultado, 4)


def convertir_distancia(valor, unidad_origen, unidad_destino):
    """
    Convierte distancias entre metros (m), kilómetros (km), millas (mi) y pies (ft).
    Usa el metro como unidad pivote.
    
    Parámetros:
        valor (float): Distancia (>= 0).
        unidad_origen (str): 'm', 'km', 'mi' o 'ft'.
        unidad_destino (str): 'm', 'km', 'mi' o 'ft'.
        
    Devuelve:
        float: Distancia convertida, o -1.0 si hay error.
    """
    if valor < 0:
        return -1.0
        
    factores_metros = {
        "m": 1.0,
        "km": 1000.0,
        "mi": 1609.344,
        "ft": 0.3048
    }
    
    u_orig = unidad_origen.lower().strip()
    u_dest = unidad_destino.lower().strip()
    
    if u_orig not in factores_metros or u_dest not in factores_metros:
        return -1.0
        
    metros = valor * factores_metros[u_orig]
    resultado = metros / factores_metros[u_dest]
    return round(resultado, 4)


# ==============================================================================
# SECCIÓN 5: AGENDA DE CONTACTOS
# Funciones para gestionar contactos representados como diccionarios.
# ==============================================================================

def añadir_contacto(agenda, nombre, telefono, email):
    """
    Añade un contacto a la agenda evitando duplicados por nombre.
    """
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return False
        
    for c in agenda:
        if c["nombre"].strip().lower() == nombre_limpio.lower():
            return False
            
    agenda.append({
        "nombre": nombre_limpio,
        "telefono": telefono.strip(),
        "email": email.strip()
    })
    return True


def buscar_contactos(agenda, criterio):
    """
    Busca contactos cuyo nombre, teléfono o email contengan el criterio de búsqueda.
    """
    crit = criterio.strip().lower()
    coincidencias = []
    for c in agenda:
        if (crit in c["nombre"].lower() or 
            crit in c["telefono"].lower() or 
            crit in c["email"].lower()):
            coincidencias.append(c)
    return coincidencias


def eliminar_contacto(agenda, nombre):
    """
    Elimina un contacto de la agenda por su nombre exacto.
    Devuelve True si lo encontró y eliminó, False si no existía.
    """
    nombre_buscar = nombre.strip().lower()
    for i, c in enumerate(agenda):
        if c["nombre"].strip().lower() == nombre_buscar:
            del agenda[i]
            return True
    return False


def ordenar_contactos(agenda):
    """
    Devuelve una nueva lista ordenada alfabéticamente por nombre usando sorted() y lambda.
    """
    return sorted(agenda, key=lambda c: c["nombre"].lower())


# ==============================================================================
# SECCIÓN 6: GESTIÓN DE PRODUCTOS
# Registro, búsqueda, actualización de stock y alertas con filter() + lambda.
# ==============================================================================

def registrar_producto(inventario, nombre, precio, stock):
    """
    Registra un nuevo producto en el inventario.
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
    Busca un producto por nombre exacto (insensible a mayúsculas).
    """
    nom = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == nom:
            return p
    return None


def actualizar_stock(inventario, nombre, cantidad):
    """
    Modifica el stock sumando o restando unidades sin permitir valores negativos.
    Devuelve tupla (exito, nuevo_stock, mensaje).
    """
    prod = buscar_producto(inventario, nombre)
    if prod is None:
        return (False, -1, f"El producto '{nombre}' no existe.")
        
    nuevo_stock = prod["stock"] + cantidad
    if nuevo_stock < 0:
        return (False, prod["stock"], f"Stock insuficiente. Solo quedan {prod['stock']} unidades.")
        
    prod["stock"] = nuevo_stock
    return (True, nuevo_stock, f"Stock actualizado a {nuevo_stock} unidades.")


def obtener_alertas_stock_bajo(inventario, limite=5):
    """
    Filtra los productos con existencias iguales o inferiores al límite usando filter() y lambda.
    """
    return list(filter(lambda p: p["stock"] <= limite, inventario))


# ==============================================================================
# SECCIÓN 7: UTILIDADES MATEMÁTICAS (RECURSIVAS)
# Factorial, Fibonacci y MCD implementados con recursividad pura y segura.
# ==============================================================================

def calcular_factorial(n):
    """
    Calcula el factorial de n recursivamente.
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
    Para evitar bloqueos de la consola limitamos n a un máximo razonable (30).
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
    Caso base: b == 0 -> a
    Caso recursivo: mcd(b, a % b)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return -1
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return calcular_mcd(b, a % b)


# ==============================================================================
# SECCIÓN 8: ANÁLISIS DE INFORMACIÓN (ESTADÍSTICAS Y FILTROS)
# Estadísticas completas y filtrado con funciones lambda y funciones de orden superior.
# ==============================================================================

def calcular_estadisticas_completas(lista_numeros):
    """
    Calcula media, mediana, moda, mínimo y máximo de una lista numérica.
    Devuelve múltiples resultados en una tupla: (media, mediana, moda, minimo, maximo).
    """
    if not lista_numeros:
        return (0.0, 0.0, 0.0, 0, 0)
        
    numeros_ordenados = sorted(lista_numeros)
    n = len(numeros_ordenados)
    
    # 1. Media
    media = round(sum(numeros_ordenados) / n, 2)
    
    # 2. Mediana
    if n % 2 == 1:
        mediana = numeros_ordenados[n // 2]
    else:
        mediana = round((numeros_ordenados[(n // 2) - 1] + numeros_ordenados[n // 2]) / 2, 2)
        
    # 3. Moda (el número más repetido)
    frecuencias = {}
    for num in numeros_ordenados:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    # Buscamos la clave con mayor frecuencia
    moda = max(frecuencias, key=lambda k: frecuencias[k])
    
    # 4. Mínimo y Máximo
    minimo = numeros_ordenados[0]
    maximo = numeros_ordenados[-1]
    
    return (media, mediana, moda, minimo, maximo)


def filtrar_lista_numeros(lista_numeros, criterio, valor_corte=0):
    """
    Filtra una lista de números según el criterio elegido utilizando filter() y lambda.
    
    Criterios disponibles:
        - 'pares': Números divisibles entre 2.
        - 'impares': Números no divisibles entre 2.
        - 'mayores': Mayores que valor_corte.
        - 'menores': Menores que valor_corte.
        
    Devuelve:
        list: Lista con los números que cumplen la condición.
    """
    if not lista_numeros:
        return []
        
    criterios_dict = {
        "pares": lambda x: x % 2 == 0,
        "impares": lambda x: x % 2 != 0,
        "mayores": lambda x: x > valor_corte,
        "menores": lambda x: x < valor_corte
    }
    
    funcion_filtro = criterios_dict.get(criterio)
    if not funcion_filtro:
        return lista_numeros
        
    return list(filter(funcion_filtro, lista_numeros))


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE funciones.py <<<\n")

    # 1. Compras
    base, desc, iva, total = desglosar_ticket(100, 10, 21)
    print(f"Desglose ticket (100€, desc 10%, IVA 21%) -> Base: {base}€, Desc: {desc}€, IVA: {iva}€, Total: {total}€")

    # 2. Economía
    resto, porc = calcular_presupuesto_restante(500, 50, 120, 30)
    print(f"Presupuesto inicial 500€, gastos 50, 120, 30 -> Saldo: {resto}€ (Gastado: {porc}%)")

    # 3. Conversores
    c_a_f = convertir_temperatura(25, "C", "F")
    print(f"25 ºC a Fahrenheit: {c_a_f} ºF")
    min_a_h = convertir_tiempo(90, "m", "h")
    print(f"90 minutos a horas: {min_a_h} h")
    km_a_mi = convertir_distancia(10, "km", "mi")
    print(f"10 km a millas: {km_a_mi} mi")

    # 4. Matemáticas recursivas
    print(f"Factorial de 5: {calcular_factorial(5)} (Esperado: 120)")
    print(f"Fibonacci de 7: {calcular_fibonacci(7)} (Esperado: 13)")
    print(f"MCD(60, 24): {calcular_mcd(60, 24)} (Esperado: 12)")

    # 5. Estadísticas y filtros
    muestra = [10, 20, 20, 30, 40, 50]
    med, medn, mod, mn, mx = calcular_estadisticas_completas(muestra)
    print(f"Estadísticas de {muestra} -> Media: {med}, Mediana: {medn}, Moda: {mod}, Min: {mn}, Max: {mx}")
    pares = filtrar_lista_numeros(muestra, "pares")
    print(f"Pares: {pares}")
    mayores_25 = filtrar_lista_numeros(muestra, "mayores", 25)
    print(f"Mayores de 25: {mayores_25}")

    print("\n>>> TODAS LAS PRUEBAS DE funciones.py COMPLETADAS CON ÉXITO <<<")
