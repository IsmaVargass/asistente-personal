"""
main.py
Punto de entrada de "Mi Asistente Personal".

Controla el flujo de ejecución por consola mediante un menú interactivo,
submenús temáticos y gestión de datos en memoria.

Unidad: UD02 - Funciones en Python
Asignatura: Programación IA (2º DAW)
"""

import sys
from datetime import datetime

# Importamos las funciones de lógica desde el archivo hermano funciones.py
from funciones import (
    pedir_numero,
    pedir_entero,
    pedir_texto,
    pedir_opcion_menu,
    calcular_precio_final,
    desglosar_ticket,
    sumar_gastos,
    calcular_presupuesto_restante,
    repartir_cuenta,
    resumen_gastos,
    convertir_temperatura,
    convertir_tiempo,
    convertir_distancia,
    añadir_contacto,
    buscar_contactos,
    eliminar_contacto,
    ordenar_contactos,
    registrar_producto,
    buscar_producto,
    actualizar_stock,
    obtener_alertas_stock_bajo,
    calcular_factorial,
    calcular_fibonacci,
    calcular_mcd,
    calcular_estadisticas_completas,
    filtrar_lista_numeros
)


# ==============================================================================
# SUBMENÚS POR ÁREA TEMÁTICA
# ==============================================================================

def submenu_compras():
    """Submenú interactivo para la gestión de compras y cálculo de tickets."""
    while True:
        print("\n" + "=" * 50)
        print("🛒 GESTIÓN DE COMPRAS")
        print("=" * 50)
        print("1. Calcular precio final (descuento e IVA)")
        print("2. Desglose detallado de ticket de compra")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 🏷️ CÁLCULO DE PRECIO FINAL ---")
            precio = pedir_numero("Introduce el precio base (€): ", minimo=0.0)
            descuento = pedir_numero("Introduce el % de descuento (0 a 100): ", minimo=0.0, maximo=100.0)
            iva = pedir_numero("Introduce el % de IVA (ej: 21, 10, 4): ", minimo=0.0)
            
            total = calcular_precio_final(precio, descuento, iva)
            print(f"\n✅ Precio final a pagar: {total:.2f} €")
            
        elif opcion == "2":
            print("\n--- 🧾 DESGLOSE DETALLADO DEL TICKET ---")
            precio = pedir_numero("Introduce el importe base de la compra (€): ", minimo=0.0)
            descuento = pedir_numero("Introduce el % de descuento (Enter para 0%): ", minimo=0.0, maximo=100.0)
            iva = pedir_numero("Introduce el % de IVA aplicado (Enter para 21%): ", minimo=0.0)
            
            base, imp_desc, imp_iva, total = desglosar_ticket(precio, descuento, iva)
            print("\n" + "-" * 35)
            print("         TICKET DE COMPRA          ")
            print("-" * 35)
            print(f"  Base imponible:     {base:>10.2f} €")
            print(f"  Descuento ({descuento:.0f}%):    -{imp_desc:>10.2f} €")
            print(f"  IVA ({iva:.0f}%):            +{imp_iva:>10.2f} €")
            print("-" * 35)
            print(f"  TOTAL A PAGAR:      {total:>10.2f} €")
            print("-" * 35)


def submenu_economia(datos_gastos):
    """
    Submenú para el control económico, gastos y reparto de cuentas.
    
    Parámetros:
        datos_gastos (dict): Diccionario con el presupuesto y la lista de gastos.
    """
    while True:
        print("\n" + "=" * 50)
        print("💰 GESTIÓN ECONÓMICA")
        print("=" * 50)
        print(f"Presupuesto actual: {datos_gastos['presupuesto']:.2f} €")
        print("1. Registrar nuevo(s) gasto(s)")
        print("2. Consultar presupuesto restante")
        print("3. Resumen y estadísticas de gastos")
        print("4. Repartir cuenta entre varias personas")
        print("5. Configurar nuevo presupuesto inicial")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 💸 REGISTRAR GASTO ---")
            cantidad = pedir_entero("¿Cuántos gastos quieres registrar hoy? ", minimo=1)
            nuevos = []
            for i in range(cantidad):
                g = pedir_numero(f"  Gasto #{i+1} (€): ", minimo=0.01)
                nuevos.append(g)
            # Usamos *args para sumar
            total_nuevos = sumar_gastos(*nuevos)
            datos_gastos["gastos"].extend(nuevos)
            print(f"✅ Se han registrado {cantidad} gastos por un total de {total_nuevos:.2f} €.")
            
        elif opcion == "2":
            print("\n--- 📊 SALDO Y PRESUPUESTO RESTANTE ---")
            saldo, porcentaje = calcular_presupuesto_restante(
                datos_gastos["presupuesto"],
                *datos_gastos["gastos"]
            )
            print(f"  • Presupuesto asignado: {datos_gastos['presupuesto']:.2f} €")
            print(f"  • Total gastado acumulado: {sumar_gastos(*datos_gastos['gastos']):.2f} € ({porcentaje:.1f}%)")
            if saldo >= 0:
                print(f"  • 🟢 Saldo disponible: {saldo:.2f} €")
            else:
                print(f"  • 🔴 ¡ALERTA DE DÉFICIT! Has sobrepasado el presupuesto en {abs(saldo):.2f} €")
                
        elif opcion == "3":
            print("\n--- 📈 RESUMEN DE GASTOS REGISTRADOS ---")
            if not datos_gastos["gastos"]:
                print("  ℹ️ Todavía no hay gastos registrados.")
            else:
                total, media, mayor, menor = resumen_gastos(datos_gastos["gastos"])
                print(f"  • Total de gastos realizados: {len(datos_gastos['gastos'])}")
                print(f"  • Gasto total acumulado: {total:.2f} €")
                print(f"  • Gasto medio: {media:.2f} €")
                print(f"  • Gasto más elevado: {mayor:.2f} €")
                print(f"  • Gasto más reducido: {menor:.2f} €")
                
        elif opcion == "4":
            print("\n--- 🍕 REPARTIR CUENTA / BOTE COMÚN ---")
            total_cuenta = pedir_numero("Importe total de la cuenta (€): ", minimo=0.01)
            comensales = pedir_entero("Número de personas para pagar: ", minimo=1)
            cuota, resto = repartir_cuenta(total_cuenta, comensales)
            print(f"\n✅ Cada persona debe pagar: {cuota:.2f} €")
            if resto != 0:
                print(f"ℹ️ Ajuste por redondeo de céntimos: {resto:+.2f} €")
                
        elif opcion == "5":
            print("\n--- 🎯 CONFIGURAR PRESUPUESTO ---")
            nuevo_pres = pedir_numero("Introduce el nuevo presupuesto (€): ", minimo=1.0)
            datos_gastos["presupuesto"] = nuevo_pres
            print(f"✅ Presupuesto actualizado a {nuevo_pres:.2f} €.")


def submenu_conversores():
    """Submenú interactivo para conversiones de temperatura, tiempo y distancia."""
    while True:
        print("\n" + "=" * 50)
        print("🔄 CONVERSORES DE UNIDADES")
        print("=" * 50)
        print("1. Convertir Temperatura (Celsius, Fahrenheit, Kelvin)")
        print("2. Convertir Tiempo (Segundos, Minutos, Horas, Días)")
        print("3. Convertir Distancia (Metros, Km, Millas, Pies)")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 🌡️ CONVERSOR DE TEMPERATURA ---")
            valor = pedir_numero("Introduce el valor de temperatura: ")
            print("Unidades disponibles: C (Celsius), F (Fahrenheit), K (Kelvin)")
            origen = pedir_texto("Unidad de origen (C/F/K): ").upper()
            destino = pedir_texto("Unidad de destino (C/F/K): ").upper()
            resultado = convertir_temperatura(valor, origen, destino)
            if resultado is not None:
                print(f"✅ Resultado: {valor} º{origen} = {resultado} º{destino}")
            else:
                print("❌ Unidad no válida. Usa C, F o K.")
                
        elif opcion == "2":
            print("\n--- ⏱️ CONVERSOR DE TIEMPO ---")
            valor = pedir_numero("Introduce la cantidad de tiempo: ", minimo=0.0)
            print("Unidades: s (segundos), m (minutos), h (horas), d (días)")
            origen = pedir_texto("Unidad de origen (s/m/h/d): ").lower()
            destino = pedir_texto("Unidad de destino (s/m/h/d): ").lower()
            resultado = convertir_tiempo(valor, origen, destino)
            if resultado != -1.0:
                print(f"✅ Resultado: {valor} {origen} = {resultado} {destino}")
            else:
                print("❌ Unidad de tiempo no válida.")
                
        elif opcion == "3":
            print("\n--- 📏 CONVERSOR DE DISTANCIA ---")
            valor = pedir_numero("Introduce la distancia: ", minimo=0.0)
            print("Unidades: m (metros), km (kilómetros), mi (millas), ft (pies)")
            origen = pedir_texto("Unidad de origen (m/km/mi/ft): ").lower()
            destino = pedir_texto("Unidad de destino (m/km/mi/ft): ").lower()
            resultado = convertir_distancia(valor, origen, destino)
            if resultado != -1.0:
                print(f"✅ Resultado: {valor} {origen} = {resultado} {destino}")
            else:
                print("❌ Unidad de distancia no válida.")


def submenu_contactos(agenda):
    """
    Submenú interactivo para gestionar la agenda de contactos.
    
    Parámetros:
        agenda (list): Lista de contactos en memoria.
    """
    while True:
        print("\n" + "=" * 50)
        print("👥 AGENDA DE CONTACTOS")
        print("=" * 50)
        print(f"Contactos registrados: {len(agenda)}")
        print("1. Listar todos los contactos")
        print("2. Añadir nuevo contacto")
        print("3. Buscar contacto")
        print("4. Ordenar contactos alfabéticamente (A-Z)")
        print("5. Eliminar un contacto")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 📋 LISTA DE CONTACTOS ---")
            if not agenda:
                print("  ℹ️ La agenda está vacía.")
            else:
                for i, c in enumerate(agenda, 1):
                    print(f"  {i}. {c['nombre']} | 📞 {c['telefono']} | ✉️ {c['email']}")
                    
        elif opcion == "2":
            print("\n--- ➕ AÑADIR CONTACTO ---")
            nombre = pedir_texto("Nombre y apellidos: ")
            telefono = pedir_texto("Teléfono: ")
            email = pedir_texto("Correo electrónico: ")
            if añadir_contacto(agenda, nombre, telefono, email):
                print(f"✅ Contacto '{nombre}' añadido con éxito.")
            else:
                print(f"❌ Ya existe un contacto registrado con el nombre '{nombre}'.")
                
        elif opcion == "3":
            print("\n--- 🔍 BUSCAR CONTACTO ---")
            criterio = pedir_texto("Introduce nombre, teléfono o email a buscar: ")
            encontrados = buscar_contactos(agenda, criterio)
            if not encontrados:
                print(f"  ℹ️ No se encontraron coincidencias para '{criterio}'.")
            else:
                print(f"  Se encontraron {len(encontrados)} coincidencia(s):")
                for c in encontrados:
                    print(f"  • {c['nombre']} - Tel: {c['telefono']} - Email: {c['email']}")
                    
        elif opcion == "4":
            print("\n--- 🔤 ORDENAR AGENDA (A-Z) ---")
            if not agenda:
                print("  ℹ️ La agenda está vacía.")
            else:
                # Ordenamos usando la función lambda definida en funciones.py
                agenda[:] = ordenar_contactos(agenda)
                print("✅ Agenda ordenada correctamente:")
                for c in agenda:
                    print(f"  • {c['nombre']} ({c['telefono']})")
                    
        elif opcion == "5":
            print("\n--- 🗑️ ELIMINAR CONTACTO ---")
            nombre = pedir_texto("Nombre del contacto a borrar: ")
            if eliminar_contacto(agenda, nombre):
                print(f"✅ Contacto '{nombre}' eliminado de la agenda.")
            else:
                print(f"❌ No se encontró ningún contacto con el nombre '{nombre}'.")


def submenu_productos(inventario):
    """
    Submenú interactivo para inventario y existencias.
    
    Parámetros:
        inventario (list): Lista de productos en memoria.
    """
    while True:
        print("\n" + "=" * 50)
        print("📦 GESTIÓN DE PRODUCTOS E INVENTARIO")
        print("=" * 50)
        print(f"Total productos en catálogo: {len(inventario)}")
        print("1. Listar inventario completo")
        print("2. Registrar nuevo producto")
        print("3. Buscar producto")
        print("4. Actualizar existencias (entradas/salidas)")
        print("5. Alerta de productos con stock bajo (<= 5)")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 📋 CATÁLOGO DE PRODUCTOS ---")
            if not inventario:
                print("  ℹ️ El inventario está vacío.")
            else:
                print(f"{'Producto':<25} | {'Precio (€)':<10} | {'Stock':<6}")
                print("-" * 47)
                for p in inventario:
                    print(f"{p['nombre']:<25} | {p['precio']:>10.2f} | {p['stock']:>6}")
                    
        elif opcion == "2":
            print("\n--- ➕ REGISTRAR PRODUCTO ---")
            nombre = pedir_texto("Nombre del producto: ")
            precio = pedir_numero("Precio unitario (€): ", minimo=0.01)
            stock = pedir_entero("Unidades iniciales en stock: ", minimo=0)
            if registrar_producto(inventario, nombre, precio, stock):
                print(f"✅ Producto '{nombre}' registrado correctamente.")
            else:
                print(f"❌ Ya existe un producto con el nombre '{nombre}' o los datos son inválidos.")
                
        elif opcion == "3":
            print("\n--- 🔍 BUSCAR PRODUCTO ---")
            nombre = pedir_texto("Nombre del producto: ")
            p = buscar_producto(inventario, nombre)
            if p:
                print(f"✅ Encontrado: {p['nombre']} | Precio: {p['precio']:.2f} € | Stock: {p['stock']} unidades")
            else:
                print(f"❌ El producto '{nombre}' no se encuentra en el inventario.")
                
        elif opcion == "4":
            print("\n--- 🔄 ACTUALIZAR STOCK ---")
            nombre = pedir_texto("Nombre del producto: ")
            p = buscar_producto(inventario, nombre)
            if not p:
                print(f"❌ El producto '{nombre}' no existe.")
                continue
            print(f"  Stock actual de '{p['nombre']}': {p['stock']} unidades.")
            print("  (Escribe un número positivo para entrada de almacén, o negativo para venta)")
            cantidad = pedir_entero("Cantidad a modificar: ")
            ok, nuevo_st, msg = actualizar_stock(inventario, nombre, cantidad)
            if ok:
                print(f"✅ {msg}")
            else:
                print(f"❌ {msg}")
                
        elif opcion == "5":
            print("\n--- ⚠️ ALERTA DE STOCK BAJO ---")
            limite = pedir_entero("Umbral de stock para la alerta (por defecto 5): ", minimo=0)
            alertas = obtener_alertas_stock_bajo(inventario, limite)
            if not alertas:
                print(f"  🟢 Todo en orden: ningún producto tiene {limite} o menos unidades.")
            else:
                print(f"  ⚠️ ¡Atención! Hay {len(alertas)} producto(s) que necesitan reposición:")
                for p in alertas:
                    print(f"    • {p['nombre']}: solo quedan {p['stock']} unidades (Precio: {p['precio']:.2f} €)")


def submenu_matematicas():
    """Submenú interactivo para utilidades matemáticas recursivas."""
    while True:
        print("\n" + "=" * 50)
        print("🧮 UTILIDADES MATEMÁTICAS RECURSIVAS")
        print("=" * 50)
        print("1. Calcular Factorial de un número (n!)")
        print("2. Calcular n-ésimo término de Fibonacci")
        print("3. Calcular Máximo Común Divisor (MCD - Algoritmo de Euclides)")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- ⚡ FACTORIAL RECURSIVO ---")
            n = pedir_entero("Introduce un número entero (0 a 20): ", minimo=0, maximo=20)
            res = calcular_factorial(n)
            print(f"✅ {n}! = {res}")
            print(f"ℹ️ Explicación: {n}! es el producto de todos los enteros desde 1 hasta {n}.")
            
        elif opcion == "2":
            print("\n--- 🌀 FIBONACCI RECURSIVO ---")
            n = pedir_entero("Introduce la posición a calcular (0 a 30): ", minimo=0, maximo=30)
            res = calcular_fibonacci(n)
            print(f"✅ Término #{n} de Fibonacci = {res}")
            print("ℹ️ Nota: Limitamos a n=30 porque la versión recursiva pura realiza millones de llamadas.")
            
        elif opcion == "3":
            print("\n--- 📐 MÁXIMO COMÚN DIVISOR (EUCLIDES) ---")
            a = pedir_entero("Primer número entero: ")
            b = pedir_entero("Segundo número entero: ")
            res = calcular_mcd(a, b)
            print(f"✅ MCD({a}, {b}) = {res}")


def submenu_analisis():
    """Submenú interactivo para estadísticas y filtros con lambdas."""
    while True:
        print("\n" + "=" * 50)
        print("📊 ANÁLISIS DE INFORMACIÓN Y FILTRADO")
        print("=" * 50)
        print("1. Introducir serie de números y ver estadísticas (media, mediana, moda, min, max)")
        print("2. Filtrar lista de números con Lambdas (pares, impares, mayores/menores)")
        print("0. Volver al menú principal")
        print("-" * 50)
        
        opcion = pedir_opcion_menu(["1", "2", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            print("\n--- 📈 ESTADÍSTICAS NUMÉRICAS COMPLETAS ---")
            cantidad = pedir_entero("¿Cuántos números vas a introducir?: ", minimo=1)
            datos = []
            for i in range(cantidad):
                num = pedir_numero(f"  Número #{i+1}: ")
                datos.append(num)
                
            media, mediana, moda, minimo, maximo = calcular_estadisticas_completas(datos)
            print("\n" + "-" * 35)
            print("         RESULTADOS ESTADÍSTICOS   ")
            print("-" * 35)
            print(f"  Muestra: {datos}")
            print(f"  • Media aritmética: {media:.2f}")
            print(f"  • Mediana:          {mediana:.2f}")
            print(f"  • Moda:             {moda}")
            print(f"  • Valor mínimo:     {minimo}")
            print(f"  • Valor máximo:     {maximo}")
            print("-" * 35)
            
        elif opcion == "2":
            print("\n--- 🔍 FILTRADO CON FUNCIONES LAMBDA ---")
            cantidad = pedir_entero("¿Cuántos números vas a introducir?: ", minimo=1)
            datos = []
            for i in range(cantidad):
                num = pedir_numero(f"  Número #{i+1}: ")
                datos.append(num)
                
            print("\nElige el criterio de filtrado:")
            print("  1. Solo pares (enteros)")
            print("  2. Solo impares (enteros)")
            print("  3. Mayores que un umbral")
            print("  4. Menores que un umbral")
            op_f = pedir_opcion_menu(["1", "2", "3", "4"])
            
            if op_f == "1":
                resultado = filtrar_lista_numeros([int(x) for x in datos], "pares")
                print(f"✅ Números pares: {resultado}")
            elif op_f == "2":
                resultado = filtrar_lista_numeros([int(x) for x in datos], "impares")
                print(f"✅ Números impares: {resultado}")
            elif op_f == "3":
                umbral = pedir_numero("Introduce el valor mínimo (umbral): ")
                resultado = filtrar_lista_numeros(datos, "mayores", umbral)
                print(f"✅ Números mayores que {umbral}: {resultado}")
            elif op_f == "4":
                umbral = pedir_numero("Introduce el valor máximo (umbral): ")
                resultado = filtrar_lista_numeros(datos, "menores", umbral)
                print(f"✅ Números menores que {umbral}: {resultado}")


# ==============================================================================
# FUNCIÓN PRINCIPAL (main)
# ==============================================================================

def main():
    """
    Función principal que arranca la aplicación de consola.
    Inicializa los datos de prueba en memoria y gestiona el bucle del menú principal.
    """
    # Datos de demostración iniciales (viven en main, no como globales en funciones.py)
    contactos_db = [
        {"nombre": "Carlos Gómez", "telefono": "600112233", "email": "carlos@gmail.com"},
        {"nombre": "Ana Ruiz", "telefono": "611223344", "email": "ana.ruiz@hotmail.com"},
        {"nombre": "Beatriz López", "telefono": "622334455", "email": "bea@empresa.es"}
    ]
    
    inventario_db = [
        {"nombre": "Ratón Inalámbrico", "precio": 18.50, "stock": 15},
        {"nombre": "Teclado Mecánico RGB", "precio": 54.99, "stock": 4},
        {"nombre": "Monitor 27 Pulgadas", "precio": 189.00, "stock": 3},
        {"nombre": "Cable HDMI 2.1", "precio": 9.99, "stock": 25},
        {"nombre": "Alfombrilla Gaming", "precio": 12.00, "stock": 0}
    ]
    
    control_gastos = {
        "presupuesto": 600.0,
        "gastos": [45.50, 18.90, 120.00, 32.10]
    }

    # Mensaje de bienvenida
    print("=" * 65)
    print("      🤖 MI ASISTENTE PERSONAL EN PYTHON (UD02 - 2º DAW) 🤖     ")
    print(f"             Sesión iniciada: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}             ")
    print("=" * 65)
    print("Hola. Soy tu asistente modular desarrollado con funciones en Python.")

    # Bucle interactivo principal
    while True:
        print("\n" + "=" * 65)
        print("                       MENÚ PRINCIPAL                            ")
        print("=" * 65)
        print("  1. 🛒 Gestión de compras (precios, descuentos e IVA)")
        print("  2. 💰 Gestión económica (presupuestos, gastos y cuentas)")
        print("  3. 🔄 Conversores (temperaturas, tiempos y distancias)")
        print("  4. 👥 Agenda de contactos (búsqueda y ordenación)")
        print("  5. 📦 Gestión de productos (inventario y existencias)")
        print("  6. 🧮 Utilidades matemáticas (factorial, Fibonacci y MCD)")
        print("  7. 📊 Análisis de información (estadísticas y filtros)")
        print("  8. 🚪 Salir del programa")
        print("=" * 65)
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "6", "7", "8"])
        
        if opcion == "1":
            submenu_compras()
        elif opcion == "2":
            submenu_economia(control_gastos)
        elif opcion == "3":
            submenu_conversores()
        elif opcion == "4":
            submenu_contactos(contactos_db)
        elif opcion == "5":
            submenu_productos(inventario_db)
        elif opcion == "6":
            submenu_matematicas()
        elif opcion == "7":
            submenu_analisis()
        elif opcion == "8":
            print("\n" + "=" * 65)
            print("  👋 ¡Hasta pronto! Gracias por utilizar Mi Asistente Personal.")
            print("=" * 65 + "\n")
            break


# Punto de entrada estándar del programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Si el usuario pulsa Ctrl+C, capturamos la señal para salir limpiamente
        print("\n\n⚠️ Ejecución interrumpida por el usuario (Ctrl + C). ¡Hasta la próxima!\n")
        sys.exit(0)
