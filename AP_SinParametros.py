"""
AP_SinParametros.py
Práctica de funciones que no reciben parámetros (argumentos).

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

from datetime import datetime
import random


def mostrar_bienvenida():
    """
    Muestra en pantalla el mensaje de bienvenida y el título del asistente.
    No recibe parámetros.
    No devuelve ningún valor (retorna None).
    """
    # Imprimimos un encabezado bonito para que el usuario sepa que el programa ha arrancado
    print("=" * 60)
    print("   🤖 ¡BIENVENIDO A MI ASISTENTE PERSONAL EN PYTHON! 🤖   ")
    print("        Tu compañero diario de tareas y cálculos         ")
    print("=" * 60)


def mostrar_menu_principal():
    """
    Imprime por consola las opciones disponibles en el menú principal.
    No recibe parámetros.
    No devuelve nada (None).
    """
    # Mostramos la lista numerada de opciones que componen el proyecto
    print("\n--------- MENÚ PRINCIPAL ---------")
    print("1. Gestión de compras (precios, descuentos e IVA)")
    print("2. Gestión económica (presupuesto, gastos y cuentas)")
    print("3. Conversores (temperaturas, tiempos y distancias)")
    print("4. Agenda de contactos (búsqueda y ordenación)")
    print("5. Gestión de productos (inventario y existencias)")
    print("6. Utilidades matemáticas (factorial, Fibonacci, MCD)")
    print("7. Análisis de información (estadísticas y filtros)")
    print("8. Salir del programa")
    print("----------------------------------")


def obtener_fecha_hora():
    """
    Obtiene la fecha y la hora actual del sistema formateada.
    No recibe parámetros.
    Devuelve:
        str: Cadena con el formato 'DD/MM/AAAA HH:MM:SS'.
    """
    # Usamos el módulo datetime de la librería estándar para saber el momento exacto
    ahora = datetime.now()
    # strftime formatea la fecha: %d=día, %m=mes, %Y=año 4 dígitos, %H=hora, %M=minuto, %S=segundo
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
    return fecha_formateada


def mostrar_consejo_del_dia():
    """
    Devuelve un consejo aleatorio sobre buenas prácticas de programación.
    No recibe parámetros.
    Devuelve:
        str: Un consejo seleccionado al azar de una lista predefinida.
    """
    # Guardamos varios consejos en una lista normal de Python
    consejos = [
        "Aplica el principio DRY: Don't Repeat Yourself (no repitas código).",
        "Escribe funciones pequeñas que hagan una sola tarea y la hagan bien.",
        "Usa nombres de variables y funciones que expliquen claramente lo que hacen.",
        "Comenta tu código pensando en tu 'yo' del futuro o en tus compañeros.",
        "Valida siempre las entradas del usuario: nunca te fíes de lo que escribe.",
        "Prueba casos límite (listas vacías, ceros, negativos) antes de entregar."
    ]
    # random.choice elige un elemento al azar de la lista
    return random.choice(consejos)


def mostrar_despedida():
    """
    Muestra en pantalla un mensaje amistoso de cierre de la sesión.
    No recibe parámetros.
    No devuelve nada (None).
    """
    # Despedida limpia para avisar al usuario de que la ejecución ha finalizado correctamente
    print("\n" + "=" * 60)
    print("  👋 ¡Gracias por usar Mi Asistente Personal! ¡Hasta pronto!  ")
    print("=" * 60 + "\n")


def pedir_nombre_usuario():
    """
    Pide el nombre al usuario por teclado y elimina espacios sobrantes.
    Si el usuario pulsa Enter sin escribir nada, asigna un nombre por defecto ('Amigo/a').
    No recibe parámetros.
    Devuelve:
        str: El nombre limpio introducido por el usuario.
    """
    # input captura lo que teclea el usuario como texto (string)
    entrada = input("¿Cómo te llamas? ").strip()
    # strip() elimina espacios en blanco al principio y al final
    if not entrada:
        return "Amigo/a"
    return entrada


# ==============================================================================
# BLOQUE DE PRUEBAS (__main__)
# Este bloque solo se ejecuta si lanzamos este archivo directamente,
# no cuando otra parte del código lo importe.
# ==============================================================================
if __name__ == "__main__":
    print(">>> INICIANDO PRUEBAS DE AP_SinParametros.py <<<\n")

    # Prueba 1: Mostrar bienvenida
    print("--- Prueba 1: mostrar_bienvenida() ---")
    mostrar_bienvenida()

    # Prueba 2: Obtener fecha y hora
    print("\n--- Prueba 2: obtener_fecha_hora() ---")
    fecha_actual = obtener_fecha_hora()
    print(f"Fecha y hora devuelta por la función: {fecha_actual}")
    print(f"¿Tipo de dato retornado?: {type(fecha_actual)}")

    # Prueba 3: Mostrar consejo del día
    print("\n--- Prueba 3: mostrar_consejo_del_dia() ---")
    consejo = mostrar_consejo_del_dia()
    print(f"💡 Consejo de hoy: {consejo}")

    # Prueba 4: Mostrar menú principal
    print("\n--- Prueba 4: mostrar_menu_principal() ---")
    mostrar_menu_principal()

    # Prueba 5: Mostrar despedida
    print("\n--- Prueba 5: mostrar_despedida() ---")
    mostrar_despedida()

    print(">>> TODAS LAS PRUEBAS DE AP_SinParametros.py COMPLETADAS CON ÉXITO <<<")
