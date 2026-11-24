"""
ap_sin_parametros.py
Módulo de funciones sin parámetros de entrada.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""

from datetime import datetime
import random


def mostrar_bienvenida():
    """
    Imprime en consola el mensaje de bienvenida y la presentación del asistente.
    
    No recibe parámetros ni retorna ningún valor (None).
    """
    print("Iniciando Mi Asistente Personal...")
    print("Herramienta de consola para cálculos cotidianos y gestión de datos.")


def mostrar_menu_principal():
    """
    Muestra en pantalla el listado de opciones disponibles en el sistema.
    """
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestión de compras (descuentos e IVA)")
    print("2. Gestión económica (presupuesto, gastos y reparto)")
    print("3. Conversores (temperaturas, tiempos y distancias)")
    print("4. Agenda de contactos (búsqueda y ordenación)")
    print("5. Gestión de existencias e inventario")
    print("6. Utilidades matemáticas recursivas (Factorial, Fibonacci, MCD)")
    print("7. Análisis de información y filtrado de datos")
    print("8. Salir del programa")


def obtener_fecha_hora():
    """
    Obtiene la marca temporal actual del sistema con formato legible.
    
    Retorna:
        str: Fecha y hora en formato 'DD/MM/AAAA HH:MM:SS'.
    """
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y %H:%M:%S")


def obtener_consejo_del_dia():
    """
    Selecciona un principio de ingeniería de software al azar.
    
    Retorna:
        str: Consejo técnico seleccionado de una lista predefinida.
    """
    consejos = [
        "Aplica el principio DRY: define la lógica una sola vez y reutilízala.",
        "Separa la interfaz de usuario de las funciones de cálculo.",
        "Valida siempre las entradas para garantizar la robustez del sistema.",
        "Utiliza nombres de identificadores que describan fielmente su función.",
        "Asegúrate de comprobar los casos límite (colecciones vacías, ceros y negativos)."
    ]
    return random.choice(consejos)


def mostrar_despedida():
    """
    Muestra el mensaje de cierre y finalización de la sesión.
    """
    print("\nSesión finalizada. Gracias por utilizar el asistente.")


def pedir_nombre_usuario():
    """
    Solicita el nombre del usuario por teclado, saneando espacios innecesarios.
    
    Retorna:
        str: Nombre saneado o 'Usuario' si no se introdujo texto.
    """
    entrada = input("Introduce tu nombre: ").strip()
    return entrada if entrada else "Usuario"


if __name__ == "__main__":
    print("[TEST] Ejecutando pruebas unitarias de ap_sin_parametros.py")
    
    # Prueba 1: Bienvenida
    mostrar_bienvenida()
    
    # Prueba 2: Fecha y hora
    fecha = obtener_fecha_hora()
    print(f"Timestamp generado: {fecha} (Tipo: {type(fecha).__name__})")
    
    # Prueba 3: Consejo
    print(f"Consejo obtenido: {obtener_consejo_del_dia()}")
    
    # Prueba 4: Menú
    mostrar_menu_principal()
    
    # Prueba 5: Despedida
    mostrar_despedida()
    
    print("[TEST] Pruebas de ap_sin_parametros.py finalizadas con éxito.\n")
