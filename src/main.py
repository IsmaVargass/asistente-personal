"""
main.py
Punto de entrada interactivo de Mi Asistente Personal.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""

import sys
from datetime import datetime

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


# ------------------------------------------------------------------------------
# Submenús temáticos
# ------------------------------------------------------------------------------

def submenu_compras():
    """Gestión de cálculo de precios y facturación."""
    while True:
        print("\n--- GESTIÓN DE COMPRAS ---")
        print("1. Calcular precio final (descuento e IVA)")
        print("2. Desglose detallado de ticket de compra")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            precio = pedir_numero("Precio base (€): ", minimo=0.0)
            descuento = pedir_numero("Descuento porcentual (0 a 100): ", minimo=0.0, maximo=100.0)
            iva = pedir_numero("IVA aplicable (%): ", minimo=0.0)
            total = calcular_precio_final(precio, descuento, iva)
            print(f"Total final a liquidar: {total:.2f} €")
            
        elif opcion == "2":
            precio = pedir_numero("Importe base (€): ", minimo=0.0)
            descuento = pedir_numero("Descuento (%): ", minimo=0.0, maximo=100.0)
            iva = pedir_numero("Tipo de IVA (%): ", minimo=0.0)
            base, imp_desc, imp_iva, total = desglosar_ticket(precio, descuento, iva)
            
            print("\n" + "-" * 32)
            print("       DESGLOSE DE TICKET       ")
            print("-" * 32)
            print(f"  Base imponible:   {base:>10.2f} €")
            print(f"  Descuento:       -{imp_desc:>10.2f} €")
            print(f"  Cuota IVA:       +{imp_iva:>10.2f} €")
            print("-" * 32)
            print(f"  TOTAL:            {total:>10.2f} €")
            print("-" * 32)


def submenu_economia(datos_gastos):
    """Control financiero, presupuestario y liquidación de cuentas."""
    while True:
        print("\n--- GESTIÓN ECONÓMICA ---")
        print(f"Presupuesto configurado: {datos_gastos['presupuesto']:.2f} €")
        print("1. Registrar nuevo(s) gasto(s)")
        print("2. Consultar balance y saldo restante")
        print("3. Informe estadístico de gastos")
        print("4. Repartir cuenta entre comensales")
        print("5. Actualizar presupuesto inicial")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            cantidad = pedir_entero("Número de gastos a registrar: ", minimo=1)
            nuevos = []
            for i in range(cantidad):
                g = pedir_numero(f"  Importe gasto {i+1} (€): ", minimo=0.01)
                nuevos.append(g)
            total_nuevos = sumar_gastos(*nuevos)
            datos_gastos["gastos"].extend(nuevos)
            print(f"Registrados {cantidad} gasto(s) por un valor de {total_nuevos:.2f} €.")
            
        elif opcion == "2":
            saldo, porcentaje = calcular_presupuesto_restante(datos_gastos["presupuesto"], *datos_gastos["gastos"])
            gastado = sumar_gastos(*datos_gastos["gastos"])
            print(f"Presupuesto: {datos_gastos['presupuesto']:.2f} € | Gastado: {gastado:.2f} € ({porcentaje:.1f}%)")
            if saldo >= 0:
                print(f"Saldo disponible: {saldo:.2f} €")
            else:
                print(f"Déficit presupuestario: {abs(saldo):.2f} € por encima del límite.")
                
        elif opcion == "3":
            if not datos_gastos["gastos"]:
                print("No hay gastos registrados en el sistema.")
            else:
                tot, med, may, men = resumen_gastos(datos_gastos["gastos"])
                print(f"Total acumulado: {tot:.2f} € | Media: {med:.2f} € | Máximo: {may:.2f} € | Mínimo: {men:.2f} €")
                
        elif opcion == "4":
            total_cuenta = pedir_numero("Importe total de la cuenta (€): ", minimo=0.01)
            personas = pedir_entero("Número de comensales: ", minimo=1)
            cuota, resto = repartir_cuenta(total_cuenta, personas)
            print(f"Cuota por persona: {cuota:.2f} €")
            if resto != 0:
                print(f"Ajuste por redondeo: {resto:+.2f} €")
                
        elif opcion == "5":
            nuevo = pedir_numero("Nuevo presupuesto base (€): ", minimo=1.0)
            datos_gastos["presupuesto"] = nuevo
            print(f"Presupuesto actualizado a {nuevo:.2f} €.")


def submenu_conversores():
    """Conversores de unidades físicas y temporales."""
    while True:
        print("\n--- CONVERSORES DE UNIDADES ---")
        print("1. Temperatura (C, F, K)")
        print("2. Tiempo (s, m, h, d)")
        print("3. Distancia (m, km, mi, ft)")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "3", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            valor = pedir_numero("Valor térmico: ")
            orig = pedir_texto("Unidad origen (C/F/K): ").upper()
            dest = pedir_texto("Unidad destino (C/F/K): ").upper()
            res = convertir_temperatura(valor, orig, dest)
            if res is not None:
                print(f"Resultado: {valor} º{orig} = {res} º{dest}")
            else:
                print("Unidad no reconocida. Opciones: C, F o K.")
                
        elif opcion == "2":
            valor = pedir_numero("Cantidad de tiempo: ", minimo=0.0)
            orig = pedir_texto("Unidad origen (s/m/h/d): ").lower()
            dest = pedir_texto("Unidad destino (s/m/h/d): ").lower()
            res = convertir_tiempo(valor, orig, dest)
            if res != -1.0:
                print(f"Resultado: {valor} {orig} = {res} {dest}")
            else:
                print("Unidad no válida. Opciones: s, m, h, d.")
                
        elif opcion == "3":
            valor = pedir_numero("Distancia: ", minimo=0.0)
            orig = pedir_texto("Unidad origen (m/km/mi/ft): ").lower()
            dest = pedir_texto("Unidad destino (m/km/mi/ft): ").lower()
            res = convertir_distancia(valor, orig, dest)
            if res != -1.0:
                print(f"Resultado: {valor} {orig} = {res} {dest}")
            else:
                print("Unidad no válida. Opciones: m, km, mi, ft.")


def submenu_contactos(agenda):
    """Mantenimiento y consulta de la agenda de contactos."""
    while True:
        print(f"\n--- AGENDA DE CONTACTOS ({len(agenda)} registros) ---")
        print("1. Listar contactos")
        print("2. Registrar nuevo contacto")
        print("3. Buscar contactos")
        print("4. Ordenar alfabéticamente (A-Z)")
        print("5. Eliminar contacto")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            if not agenda:
                print("Agenda vacía.")
            else:
                for idx, c in enumerate(agenda, 1):
                    print(f"{idx}. {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']}")
                    
        elif opcion == "2":
            nom = pedir_texto("Nombre y apellidos: ")
            tel = pedir_texto("Teléfono: ")
            email = pedir_texto("Email: ")
            if añadir_contacto(agenda, nom, tel, email):
                print(f"Contacto '{nom}' añadido correctamente.")
            else:
                print(f"No se pudo añadir: Ya existe un contacto con el nombre '{nom}'.")
                
        elif opcion == "3":
            crit = pedir_texto("Término de búsqueda: ")
            res = buscar_contactos(agenda, crit)
            if not res:
                print("No se encontraron coincidencias.")
            else:
                print(f"{len(res)} coincidencia(s) encontrada(s):")
                for c in res:
                    print(f"- {c['nombre']} ({c['telefono']})")
                    
        elif opcion == "4":
            if not agenda:
                print("Agenda vacía.")
            else:
                agenda[:] = ordenar_contactos(agenda)
                print("Agenda ordenada alfabéticamente.")
                for c in agenda:
                    print(f"- {c['nombre']}")
                    
        elif opcion == "5":
            nom = pedir_texto("Nombre del contacto a eliminar: ")
            if eliminar_contacto(agenda, nom):
                print(f"Contacto '{nom}' eliminado.")
            else:
                print(f"No se localizó ningún contacto con el nombre '{nom}'.")


def submenu_productos(inventario):
    """Gestión de inventario y existencias."""
    while True:
        print(f"\n--- GESTIÓN DE PRODUCTOS ({len(inventario)} artículos) ---")
        print("1. Listar catálogo completo")
        print("2. Registrar nuevo producto")
        print("3. Buscar producto")
        print("4. Actualizar existencias (entradas/salidas)")
        print("5. Consultar alertas de stock bajo")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "3", "4", "5", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            if not inventario:
                print("Catálogo vacío.")
            else:
                print(f"{'Producto':<26} | {'Precio (€)':<10} | {'Stock':<6}")
                print("-" * 48)
                for p in inventario:
                    print(f"{p['nombre']:<26} | {p['precio']:>10.2f} | {p['stock']:>6}")
                    
        elif opcion == "2":
            nom = pedir_texto("Nombre del producto: ")
            prec = pedir_numero("Precio unitario (€): ", minimo=0.01)
            stock = pedir_entero("Unidades iniciales: ", minimo=0)
            if registrar_producto(inventario, nom, prec, stock):
                print(f"Producto '{nom}' registrado correctamente.")
            else:
                print("Error: Ya existe un producto con esa denominación.")
                
        elif opcion == "3":
            nom = pedir_texto("Nombre a buscar: ")
            p = buscar_producto(inventario, nom)
            if p:
                print(f"Localizado: {p['nombre']} | Precio: {p['precio']:.2f} € | Stock: {p['stock']} uds.")
            else:
                print(f"El producto '{nom}' no figura en el catálogo.")
                
        elif opcion == "4":
            nom = pedir_texto("Nombre del producto: ")
            p = buscar_producto(inventario, nom)
            if not p:
                print(f"El producto '{nom}' no existe.")
                continue
            print(f"Existencias actuales de '{p['nombre']}': {p['stock']} unidades.")
            cant = pedir_entero("Variación de stock (positivo=entrada, negativo=salida): ")
            ok, nuevo_st, msg = actualizar_stock(inventario, nom, cant)
            print(msg)
            
        elif opcion == "5":
            umbral = pedir_entero("Umbral de alerta (por defecto 5): ", minimo=0)
            alertas = obtener_alertas_stock_bajo(inventario, umbral)
            if not alertas:
                print(f"No hay artículos con existencias iguales o inferiores a {umbral}.")
            else:
                print(f"{len(alertas)} producto(s) en umbral crítico:")
                for p in alertas:
                    print(f"- {p['nombre']}: {p['stock']} uds restantes.")


def submenu_matematicas():
    """Utilidades matemáticas con algoritmos recursivos."""
    while True:
        print("\n--- UTILIDADES MATEMÁTICAS RECURSIVAS ---")
        print("1. Factorial de un número (n!)")
        print("2. n-ésimo término de la sucesión de Fibonacci")
        print("3. Máximo Común Divisor (Euclides)")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "3", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            n = pedir_entero("Número entero (0 a 20): ", minimo=0, maximo=20)
            print(f"Resultado: {n}! = {calcular_factorial(n)}")
            
        elif opcion == "2":
            n = pedir_entero("Posición solicitada (0 a 30): ", minimo=0, maximo=30)
            print(f"Resultado: Fibonacci({n}) = {calcular_fibonacci(n)}")
            
        elif opcion == "3":
            a = pedir_entero("Primer número: ")
            b = pedir_entero("Segundo número: ")
            print(f"Resultado: MCD({a}, {b}) = {calcular_mcd(a, b)}")


def submenu_analisis():
    """Análisis estadístico y filtrado de datos."""
    while True:
        print("\n--- ANÁLISIS DE INFORMACIÓN Y FILTRADO ---")
        print("1. Estadísticas descriptivas de una muestra")
        print("2. Filtrado de listas con funciones lambda")
        print("0. Volver al menú principal")
        
        opcion = pedir_opcion_menu(["1", "2", "0"])
        if opcion == "0":
            break
            
        if opcion == "1":
            cant = pedir_entero("Cantidad de elementos de la muestra: ", minimo=1)
            datos = [pedir_numero(f"  Elemento {i+1}: ") for i in range(cant)]
            media, mediana, moda, minimo, maximo = calcular_estadisticas_completas(datos)
            
            print("\n" + "-" * 32)
            print("     INFORME ESTADÍSTICO        ")
            print("-" * 32)
            print(f"  Media:     {media:>10.2f}")
            print(f"  Mediana:   {mediana:>10.2f}")
            print(f"  Moda:      {moda:>10}")
            print(f"  Mínimo:    {minimo:>10}")
            print(f"  Máximo:    {maximo:>10}")
            print("-" * 32)
            
        elif opcion == "2":
            cant = pedir_entero("Cantidad de números a introducir: ", minimo=1)
            datos = [pedir_numero(f"  Elemento {i+1}: ") for i in range(cant)]
            
            print("Criterios de filtrado:")
            print("1. Números pares")
            print("2. Números impares")
            print("3. Mayores que un umbral")
            print("4. Menores que un umbral")
            op_f = pedir_opcion_menu(["1", "2", "3", "4"])
            
            if op_f == "1":
                res = filtrar_lista_numeros([int(x) for x in datos], "pares")
                print(f"Pares: {res}")
            elif op_f == "2":
                res = filtrar_lista_numeros([int(x) for x in datos], "impares")
                print(f"Impares: {res}")
            elif op_f == "3":
                umb = pedir_numero("Umbral inferior: ")
                res = filtrar_lista_numeros(datos, "mayores", umb)
                print(f"Mayores que {umb}: {res}")
            elif op_f == "4":
                umb = pedir_numero("Umbral superior: ")
                res = filtrar_lista_numeros(datos, "menores", umb)
                print(f"Menores que {umb}: {res}")


# ------------------------------------------------------------------------------
# Función principal
# ------------------------------------------------------------------------------

def main():
    """Función de arranque e inicialización del asistente."""
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

    print("==================================================================")
    print("                    MI ASISTENTE PERSONAL                         ")
    print(f"       Autor: Ismael Vargas | Sesión: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}       ")
    print("==================================================================")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de compras (descuentos e IVA)")
        print("2. Gestión económica (presupuesto y gastos)")
        print("3. Conversores de unidades")
        print("4. Agenda de contactos")
        print("5. Gestión de inventario de productos")
        print("6. Utilidades matemáticas recursivas")
        print("7. Análisis de información y filtros")
        print("8. Salir")
        
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
            print("\nSesión finalizada. Aplicación cerrada correctamente.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupción de ejecución por usuario (Ctrl+C). Finalizando programa.")
        sys.exit(0)
