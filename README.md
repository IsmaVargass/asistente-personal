# 🤖 Mi Asistente Personal en Python

**Proyecto de Programación IA (2026/27) — iLERNA**  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Ciclo Formativo:** 2º Desarrollo de Aplicaciones Web (2DAW)  
**Autor:** Ismael Vargas Duque ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 Descripción del Proyecto

**Mi Asistente Personal** es una aplicación interactiva por consola desarrollada íntegramente en **Python 3 (versión 3.10 o superior)** sin librerías externas (únicamente utilizando la librería estándar). Su propósito es centralizar y automatizar operaciones cotidianas a través de un menú estructurado en 8 módulos temáticos:

1. **🛒 Gestión de compras:** Cálculo de precios finales con descuentos e IVA, junto con desglose de tickets.
2. **💰 Gestión económica:** Control de presupuestos, registro acumulativo de gastos con `*args` y reparto equitativo de cuentas.
3. **🔄 Conversores:** Conversión bidireccional de temperaturas ($^\circ\text{C}, ^\circ\text{F}, \text{K}$), tiempos ($\text{s}, \text{m}, \text{h}, \text{d}$) y distancias ($\text{m}, \text{km}, \text{mi}, \text{ft}$).
4. **👥 Agenda de contactos:** Registro, búsqueda insensible a mayúsculas, eliminación y ordenación alfabética mediante funciones Lambda.
5. **📦 Gestión de productos:** Inventario, control de existencias (entradas/salidas evitando stock negativo) y alertas automáticas de reposición (`filter` + Lambda).
6. **🧮 Utilidades matemáticas:** Algoritmos recursivos puros para Factorial, sucesión de Fibonacci y Máximo Común Divisor (MCD mediante Euclides).
7. **📊 Análisis de información:** Cálculo estadístico completo (media, mediana, moda, mínimo y máximo) y filtrado dinámico de colecciones con funciones anónimas.
8. **🚪 Salir:** Cierre seguro y limpio de la sesión.

---

## 🎯 ¿Por qué es importante este proyecto en 2º de DAW?

1. **Principio DRY (*Don't Repeat Yourself*):** Las funciones permiten encapsular la lógica una sola vez y reutilizarla en múltiples puntos del programa, evitando código redundante y reduciendo errores.
2. **Modularidad y Arquitectura de Software:** Separar la lógica de negocio (`funciones.py`) de la interfaz de usuario (`main.py`) es el estándar en el desarrollo web y backend profesional (patrones MVC, APIs REST con FastAPI/Flask/Django o microservicios en Express/Spring).
3. **Pensamiento Lógico y Equivalencia con JavaScript:** El dominio de la **recursividad** y las funciones **Lambda** sienta las bases para las funciones flecha (*arrow functions*), así como el uso intensivo de métodos funcionales en frontend/backend como `map()`, `filter()` y `reduce()`.
4. **Robustez mediante Validación de Entradas:** Un software profesional nunca debe fallar abruptamente (*crash/traceback*) ante un dato imprevisto. El proyecto incorpora validaciones sistemáticas con `try/except` y bucles de control.

---

## 📁 Estructura del Repositorio

```text
asistente-personal/
├── .gitignore                    # Filtro de Git para archivos temporales de Python
├── LICENSE                       # Licencia del proyecto
├── README.md                     # Documentación completa y manual de usuario
├── AP_SinParametros.py           # Práctica 1: Funciones sin parámetros
├── AP_UnParametro.py             # Práctica 2: Funciones con un parámetro
├── AP_VariosParametros.py        # Práctica 3: Parámetros opcionales, *args, **kwargs y tuplas
├── AP_ListasDiccionarios.py      # Práctica 4: Manipulación de listas y diccionarios
├── AP_Recursividad.py            # Práctica 5: Factorial, Fibonacci y MCD recursivos
├── APLambda.py                   # Práctica 6: Funciones anónimas, sorted, filter y map
└── Proyecto_AsistentePersonal/
    ├── funciones.py              # Biblioteca modular de funciones del asistente
    └── main.py                   # Interfaz de consola y menús interactivos
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos
- Python 3.10 o superior instalado (`python --version`).
- No requiere dependencias externas (`pip install` no es necesario).

### Pasos para Ejecutar el Asistente Personal

1. Clonar o abrir la carpeta del repositorio en la terminal:
   ```bash
   cd C:\Users\ismaelvargasduque14\Desktop\asistente-personal
   ```

2. Entrar a la carpeta del proyecto principal y lanzar `main.py`:
   ```bash
   cd Proyecto_AsistentePersonal
   python main.py
   ```

### Ejecución de los Archivos de Práctica Independientes
Cada archivo incluye su propia suite de pruebas visibles al ejecutarse directamente:

```bash
python AP_SinParametros.py
python AP_UnParametro.py
python AP_VariosParametros.py
python AP_ListasDiccionarios.py
python AP_Recursividad.py
python APLambda.py
python Proyecto_AsistentePersonal/funciones.py
```

---

## 📊 Matriz de Cumplimiento de Requisitos Técnicos

A continuación se detalla dónde se cumple cada requisito exigido en la rúbrica oficial de evaluación:

| Requisito Técnico Obligatorio | Función Implementada | Archivo | Explicación Técnica |
| :--- | :--- | :--- | :--- |
| **Al menos una función sin parámetros** | `mostrar_bienvenida()`, `obtener_fecha_hora()` | `AP_SinParametros.py`, `funciones.py` | No recibe argumentos de entrada; retorna información formateada del sistema o avisos. |
| **Al menos una función con varios parámetros** | `calcular_precio_con_descuento_e_iva(precio, desc, iva)` | `AP_VariosParametros.py`, `funciones.py` | Recibe múltiples parámetros obligatorios posicionales. |
| **Función con parámetros opcionales** | `calcular_precio_final(precio, descuento=0, iva=21)` | `AP_VariosParametros.py`, `funciones.py` | Asigna valores por defecto (0% descuento, 21% IVA) si el usuario los omite. |
| **Función con `*args`** | `sumar_gastos(*gastos)`, `calcular_media(*numeros)` | `AP_VariosParametros.py`, `funciones.py` | Empaqueta un número indeterminado de argumentos posicionales en una tupla iterable. |
| **Función con `**kwargs`** | `mostrar_ficha(**datos)` | `AP_VariosParametros.py` | Empaqueta argumentos con nombre en un diccionario clave-valor. |
| **Función que devuelva varios resultados** | `desglosar_ticket(...)`, `repartir_cuenta(...)`, `calcular_estadisticas_completas(...)` | `AP_VariosParametros.py`, `funciones.py` | Retorna múltiples variables empaquetadas en una `tuple` que se desempaquetan en el llamador. |
| **Función recursiva con caso base** | `calcular_factorial(n)`, `calcular_fibonacci(n)`, `calcular_mcd(a, b)` | `AP_Recursividad.py`, `funciones.py` | Se llaman a sí mismas reduciendo el problema; incluyen caso base para evitar recursión infinita. |
| **Al menos dos funciones Lambda** | `ordenar_contactos` (`sorted`), `obtener_alertas_stock_bajo` (`filter`), `aplicar_descuento` (`map`) | `APLambda.py`, `funciones.py` | Funciones anónimas en una línea para ordenación, filtrado y mapeo de datos. |
| **Validaciones y gestión de errores** | `pedir_numero()`, `pedir_entero()`, `actualizar_stock()` | `funciones.py` | Captura `ValueError`, impide stock negativo, bloquea división por cero y previene crash por `Ctrl+C`. |
| **Menú interactivo continuo** | `main()` con `while True` y submenús | `Proyecto_AsistentePersonal/main.py` | Permite navegación cíclica por todas las secciones hasta elegir la opción de salida (8). |

---

## 🧪 Pruebas Realizadas y Casos Límite Verificados

Durante el desarrollo se han verificado sistemáticamente los siguientes escenarios mediante suites automatizadas:

1. **Casos Normales:**
   - Cálculo de ticket comercial con 10% descuento y 21% IVA sobre 100€ $\to$ Total: 108.90€.
   - Conversión de 25 ºC a Fahrenheit $\to$ 77.00 ºF.
   - MCD(48, 18) $\to$ 6.

2. **Casos Límite:**
   - `calcular_factorial(0)` $\to$ Retorna 1 (definición matemática del caso base).
   - `sumar_gastos()` sin argumentos $\to$ Retorna 0.0€ sin error.
   - `calcular_media()` con lista vacía $\to$ Retorna 0.0 (evita `ZeroDivisionError`).
   - `repartir_cuenta(100, 3)` $\to$ Cuota: 33.33€, resto/descuadre: +0.01€.

3. **Casos Erróneos y Control de Excepciones:**
   - Intentar registrar stock negativo o precios inferiores a 0 $\to$ Rechazado por validación.
   - Intentar vender más unidades de las existentes en stock $\to$ Operación denegada con aviso de existencias insuficientes.
   - Interrupción de teclado `Ctrl + C` en cualquier momento del menú $\to$ Capturada por `KeyboardInterrupt` cerrando el asistente amigablemente.

---

## 📌 Enlace al Repositorio en GitHub

El código fuente completo con su historial de commits se encuentra publicado en:  
🔗 **[https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)**
