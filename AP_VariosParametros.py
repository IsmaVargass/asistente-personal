"""
AP_VariosParametros.py
Práctica de funciones con varios parámetros, parámetros opcionales, *args, **kwargs
y funciones que devuelven múltiples valores (tuplas).

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

# ==============================================================================
# CONCEPTOS CLAVE A TENER EN CUENTA (para defender ante el profesor):
# 1. PARÁMETRO: Variable que declaramos en la definición de la función 'def f(x):'.
# 2. ARGUMENTO: El valor real que le enviamos a la función al llamarla 'f(10)'.
# 3. ARGUMENTOS POSICIONALES: Se asignan por orden de aparición en la llamada.
# 4. ARGUMENTOS CON NOMBRE (Keyword Arguments): Se asignan indicando 'nombre=valor',
#    lo que permite alterar el orden.
# 5. *args: Permite recibir un número indeterminado de argumentos posicionales
#    empaquetados en una tupla.
# 6. **kwargs: Permite recibir un número indeterminado de argumentos con nombre
#    empaquetados en un diccionario.
# 7. RETORNO MÚLTIPLE: Python permite devolver varios valores separados por comas,
#    lo que internamente construye y retorna una TUPLA.
# ==============================================================================


def calcular_precio_con_descuento_e_iva(precio, descuento, iva):
    """
    Calcula el precio final aplicando primero un descuento y luego el IVA.
    Todos los parámetros son obligatorios (posicionales).
    
    Parámetros:
        precio (float/int): Precio base en euros (debe ser >= 0).
        descuento (float/int): Porcentaje de descuento (0 a 100).
        iva (float/int): Porcentaje de IVA a aplicar (>= 0).
        
    Devuelve:
        float: Precio final calculado y redondeado a 2 decimales.
               Devuelve -1.0 si algún valor no es válido.
    """
    # Validamos que los números tengan lógica comercial
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    # Paso 1: Aplicamos el descuento sobre la base
    precio_con_descuento = precio * (1 - (descuento / 100))
    # Paso 2: Aplicamos el IVA sobre el precio ya rebajado
    precio_final = precio_con_descuento * (1 + (iva / 100))
    
    return round(precio_final, 2)


def calcular_precio_final(precio, descuento=0, iva=21):
    """
    Calcula el precio final con parámetros opcionales (valores por defecto).
    Si el usuario no especifica descuento, se asume 0%.
    Si el usuario no especifica IVA, se asume el 21% (IVA general en España).
    
    Parámetros:
        precio (float/int): Precio base (obligatorio).
        descuento (float/int, opcional): Porcentaje de descuento (por defecto 0).
        iva (float/int, opcional): Porcentaje de IVA (por defecto 21).
        
    Devuelve:
        float: Precio final redondeado a 2 decimales, o -1.0 si es erróneo.
    """
    if precio < 0 or not (0 <= descuento <= 100) or iva < 0:
        return -1.0
        
    precio_rebajado = precio * (1 - (descuento / 100))
    total = precio_rebajado * (1 + (iva / 100))
    return round(total, 2)


def sumar_gastos(*gastos):
    """
    Suma una cantidad variable de gastos utilizando *args.
    *args empaqueta todos los argumentos posicionales que le pasemos en una tupla.
    
    Parámetros:
        *gastos (float/int): Cualquier número de cantidades monetarias (ej: 10, 25.5, 3.2).
        
    Devuelve:
        float: La suma total de los gastos válidos (redondeada a 2 decimales).
               Si algún gasto es negativo, se ignora avisando o se descarta.
    """
    # *args es una tupla iterable dentro de la función: podemos recorrerla con un for
    total = 0.0
    for gasto in gastos:
        # Solo sumamos si el valor es positivo
        if gasto > 0:
            total += gasto
    return round(total, 2)


def calcular_media(*numeros):
    """
    Calcula la media aritmética de una lista variable de números usando *args.
    
    Parámetros:
        *numeros (float/int): Números a promediar.
        
    Devuelve:
        float: Media aritmética redondeada a 2 decimales.
               Devuelve 0.0 si no se proporciona ningún número (evita división por cero).
    """
    # Caso límite: Si nos llaman sin argumentos 'calcular_media()', la tupla está vacía
    if len(numeros) == 0:
        # Evitamos hacer suma / 0, que provocaría un ZeroDivisionError
        return 0.0
        
    suma_total = sum(numeros)
    cantidad = len(numeros)
    media = suma_total / cantidad
    return round(media, 2)


def mostrar_ficha(**datos):
    """
    Muestra los datos de un usuario o entidad usando **kwargs.
    **kwargs empaqueta los argumentos con nombre en un DICCIONARIO clave-valor.
    
    Parámetros:
        **datos: Pares clave=valor (ej: nombre="Ana", edad=20, rol="Estudiante").
        
    Devuelve:
        str: Cadena formateada con la información recibida.
    """
    if not datos:
        return "Ficha vacía: no se han proporcionado datos."
        
    lineas = ["--- FICHA DE DATOS ---"]
    # items() recorre a la vez la clave y el valor del diccionario
    for clave, valor in datos.items():
        # capitalize() pone la primera letra en mayúscula para que quede presentable
        lineas.append(f"  • {clave.capitalize()}: {valor}")
    lineas.append("----------------------")
    
    # join une la lista de líneas en un único texto separado por saltos de línea
    return "\n".join(lineas)


def repartir_cuenta(total, personas):
    """
    Reparte una cuenta entre un número de comensales y calcula los céntimos restantes.
    Demuestra una función que devuelve VARIOS RESULTADOS mediante una TUPLA.
    
    Parámetros:
        total (float/int): Importe total de la cuenta en euros.
        personas (int): Número de personas que pagan (debe ser >= 1).
        
    Devuelve:
        tuple: (cuota_por_persona, resto_centimos)
               - cuota_por_persona (float): Lo que paga cada comensal redondeado a 2 decimales.
               - resto_centimos (float): Céntimos de descuadre debidos al redondeo.
               Devuelve (0.0, 0.0) si los parámetros son inválidos.
    """
    # Validaciones: la cuenta no puede ser negativa y las personas deben ser al menos 1
    if total <= 0 or personas <= 0:
        return (0.0, 0.0)
        
    # Calculamos la cuota exacta por persona redondeada hacia abajo a 2 decimales
    cuota = round(total / personas, 2)
    # Comprobamos si el total de multiplicar la cuota por las personas cuadra exactamente
    total_recaudado = round(cuota * personas, 2)
    diferencia = round(total - total_recaudado, 2)
    
    # Retornamos ambos valores: Python crea una tupla (cuota, diferencia)
    return (cuota, diferencia)


def estadisticas_basicas(lista_numeros):
    """
    Calcula el mínimo, máximo y la media de una lista de números.
    Devuelve múltiples resultados en una tupla: (minimo, maximo, media).
    
    Parámetros:
        lista_numeros (list): Colección de enteros o decimales.
        
    Devuelve:
        tuple: (minimo, maximo, media)
               Devuelve (0, 0, 0.0) si la lista está vacía.
    """
    # Caso límite: Lista vacía
    if not lista_numeros:
        return (0, 0, 0.0)
        
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    media = round(sum(lista_numeros) / len(lista_numeros), 2)
    
    return (minimo, maximo, media)


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE AP_VariosParametros.py <<<\n")

    # 1. Función con varios parámetros obligatorios
    print("--- 1. calcular_precio_con_descuento_e_iva ---")
    res1 = calcular_precio_con_descuento_e_iva(100, 10, 21)
    print(f"Base 100€, desc 10%, IVA 21%: {res1}€ (Esperado: 108.9€)")
    # Argumentos con nombre cambiando el orden:
    res_nom = calcular_precio_con_descuento_e_iva(iva=21, precio=100, descuento=10)
    print(f"Llamada con argumentos con nombre (desordenados): {res_nom}€")
    # Caso erróneo (descuento del 150%):
    res_err = calcular_precio_con_descuento_e_iva(100, 150, 21)
    print(f"Caso erróneo (descuento 150%): {res_err} (Esperado: -1.0)")

    # 2. Función con parámetros opcionales (valores por defecto)
    print("\n--- 2. calcular_precio_final (parámetros por defecto) ---")
    print(f"Solo precio (descuento=0, iva=21 por defecto): {calcular_precio_final(100)}€ (Esperado: 121.0€)")
    print(f"Con descuento 20% e IVA por defecto: {calcular_precio_final(100, 20)}€ (Esperado: 96.8€)")
    print(f"Con descuento 10% e IVA superreducido 4%: {calcular_precio_final(100, 10, 4)}€ (Esperado: 93.6€)")

    # 3. Función con *args (sumar_gastos y calcular_media)
    print("\n--- 3. Funciones con *args ---")
    total_g = sumar_gastos(12.50, 45.0, 3.20, 8.99)
    print(f"Suma de 4 gastos (12.50, 45.0, 3.20, 8.99): {total_g}€")
    print(f"Suma sin gastos 'sumar_gastos()': {sumar_gastos()}€ (Esperado: 0.0€)")
    
    media1 = calcular_media(10, 8, 9, 7)
    print(f"Media de notas (10, 8, 9, 7): {media1} (Esperado: 8.5)")
    media_vacia = calcular_media()
    print(f"Media sin datos (evita división por 0): {media_vacia} (Esperado: 0.0)")

    # 4. Función con **kwargs (mostrar_ficha)
    print("\n--- 4. Función con **kwargs (mostrar_ficha) ---")
    ficha1 = mostrar_ficha(nombre="Ana García", edad=21, ciclo="2º DAW", ciudad="Sevilla")
    print(ficha1)
    ficha_vacia = mostrar_ficha()
    print(ficha_vacia)

    # 5. Función que devuelve múltiples resultados (tupla) y desempaquetado
    print("\n--- 5. Retorno múltiple: repartir_cuenta ---")
    # Recibimos la tupla y la DESEMPAQUETAMOS en dos variables distintas
    cuota, sobrante = repartir_cuenta(100.0, 3)
    print(f"Cuenta 100€ entre 3 personas -> Cuota: {cuota}€ | Descuadre: {sobrante}€")
    
    # Caso límite: dividir entre 0 personas
    cuota_err, sobrante_err = repartir_cuenta(50.0, 0)
    print(f"Cuenta 50€ entre 0 personas -> Cuota: {cuota_err} | Descuadre: {sobrante_err}")

    print("\n--- 6. Retorno múltiple: estadisticas_basicas ---")
    notas = [7, 4, 9, 10, 6, 8]
    min_nota, max_nota, med_nota = estadisticas_basicas(notas)
    print(f"Notas: {notas} -> Mínimo: {min_nota}, Máximo: {max_nota}, Media: {med_nota}")

    print("\n>>> TODAS LAS PRUEBAS DE AP_VariosParametros.py COMPLETADAS CON ÉXITO <<<")
