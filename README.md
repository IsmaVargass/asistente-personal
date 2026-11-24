# Mi Asistente Personal en Python

**Proyecto:** Programación IA (2026/27) — iLERNA  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Autor:** Ismael Vargas ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 Descripción del Proyecto

**Mi Asistente Personal** es una aplicación modular desarrollada en Python 3 (versión 3.10 o superior) empleando exclusivamente la librería estándar del lenguaje. Su propósito es estructurar y resolver tareas cotidianas mediante funciones reutilizables organizadas en 8 áreas operativas:

1. **Gestión de compras:** Cálculo de precios netos con descuentos, IVA y desglose comercial del ticket.
2. **Gestión económica:** Control presupuestario, registro dinámico de gastos con `*args` y reparto equitativo de cuentas.
3. **Conversores de unidades:** Motor de conversión de temperaturas (C, F, K), tiempos (s, m, h, d) y distancias (m, km, mi, ft).
4. **Agenda de contactos:** Registro en listas de diccionarios, búsqueda insensible a mayúsculas, eliminación y ordenación alfabética mediante lambdas.
5. **Gestión de inventario:** Control de existencias (bloqueo de stock negativo) y alertas automáticas de reposición.
6. **Utilidades matemáticas:** Algoritmos recursivos para Factorial, sucesión de Fibonacci y Máximo Común Divisor (Euclides).
7. **Análisis de información:** Tratamiento estadístico descriptivo (media, mediana, moda, mínimo y máximo) y filtrado funcional.
8. **Salir:** Cierre limpio del hilo de ejecución con captura de interrupciones de teclado (`Ctrl + C`).

---

## 🎯 Arquitectura del Software

- **Principio DRY (Don't Repeat Yourself):** Toda la lógica de cómputo reside en funciones independientes y puras dentro de `src/funciones.py`.
- **Desacoplamiento I/O:** Las funciones de cálculo no contienen `print()` ni `input()`, garantizando que la misma lógica pueda ser consumida por la consola o por la interfaz gráfica.
- **Doble Interfaz (Consola y GUI):** 
  - `src/main.py`: Interfaz oficial por consola interactiva exigida en la rúbrica.
  - `src/main_gui.py`: Extensión gráfica de escritorio desarrollada en `tkinter` nativo.

---

## 📁 Estructura del Repositorio

```text
asistente-personal/
├── docs/
│   ├── UD02_AsistentePython_IsmaelVargas.pdf   # Memoria técnica oficial en formato académico / tesis
│   └── DocuAsistente.pdf                      # Manual técnico exhaustivo del sistema
├── src/
│   ├── main.py                                # Punto de entrada oficial por consola
│   ├── main_gui.py                            # Interfaz gráfica de escritorio (Tkinter)
│   ├── funciones.py                           # Biblioteca central de lógica y servicios
│   └── scripts/                               # Módulos temáticos independientes
│       ├── ap_sin_parametros.py
│       ├── ap_un_parametro.py
│       ├── ap_varios_parametros.py
│       ├── ap_listas_diccionarios.py
│       ├── ap_recursividad.py
│       └── ap_lambda.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Instrucciones de Ejecución

### Requisitos
- Python 3.10 o superior instalado.
- Sin dependencias externas de terceros (no requiere `pip install`).

### 1. Ejecución de la Consola Oficial (Programa Principal)
Desde la raíz del repositorio:
```bash
python src/main.py
```
*(Permite navegar por los 8 módulos obligatorios de la rúbrica, e incluye la opción 9 para lanzar la GUI si se desea).*

### 2. Ejecución Directa de la Interfaz Gráfica (Tkinter)
```bash
python src/main_gui.py
```

### 3. Ejecución de Suites de Pruebas Unitarias
```bash
python -m src.scripts.ap_sin_parametros
python -m src.scripts.ap_un_parametro
python -m src.scripts.ap_varios_parametros
python -m src.scripts.ap_listas_diccionarios
python -m src.scripts.ap_recursividad
python -m src.scripts.ap_lambda
python src/funciones.py
```

---

## 📊 Matriz de Cumplimiento de Requisitos Técnicos

| Requisito Oficial | Función en Código | Archivo | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Al menos una función sin parámetros** | `obtener_fecha_hora()`, `mostrar_bienvenida()` | `src/scripts/ap_sin_parametros.py`, `src/funciones.py` | Genera y retorna marcas temporales del sistema sin depender de entradas externas. |
| **Al menos una función con varios parámetros** | `calcular_precio_con_descuento_e_iva(p, d, i)` | `src/scripts/ap_varios_parametros.py`, `src/funciones.py` | Maneja múltiples parámetros obligatorios posicionales. |
| **Función con parámetros opcionales** | `calcular_precio_final(precio, descuento=0, iva=21)` | `src/scripts/ap_varios_parametros.py`, `src/funciones.py` | Incorpora valores por defecto parametrizados. |
| **Función con `*args`** | `sumar_gastos(*gastos)`, `calcular_media(*numeros)` | `src/scripts/ap_varios_parametros.py`, `src/funciones.py` | Empaqueta un número indeterminado de argumentos posicionales en una tupla iterable. |
| **Función con `**kwargs`** | `mostrar_ficha(**datos)` | `src/scripts/ap_varios_parametros.py` | Empaqueta argumentos con nombre en un diccionario clave-valor. |
| **Función que devuelva varios resultados** | `desglosar_ticket(...)`, `repartir_cuenta(...)` | `src/scripts/ap_varios_parametros.py`, `src/funciones.py` | Retorna múltiples resultados empaquetados en tuplas desempaquetables. |
| **Función recursiva con caso base** | `calcular_factorial(n)`, `calcular_fibonacci(n)`, `calcular_mcd(a, b)` | `src/scripts/ap_recursividad.py`, `src/funciones.py` | Algoritmos con caso base explícito para evitar desbordamiento del call stack. |
| **Al menos dos funciones Lambda** | `ordenar_contactos` (`sorted`), `obtener_alertas_stock_bajo` (`filter`) | `src/scripts/ap_lambda.py`, `src/funciones.py` | Programación funcional de orden superior para filtrado y ordenación inline. |
| **Validaciones y gestión de errores** | `pedir_numero()`, `pedir_entero()`, `actualizar_stock()` | `src/funciones.py` | Captura de `ValueError`, bloqueo de stock negativo y salida controlada ante `Ctrl+C`. |
| **Menú interactivo continuo** | `main()` con bucle `while True` | `src/main.py` | Flujo continuo con submenús temáticos y opción de salida limpia. |

---

## 📑 Documentación Técnica Oficial

Los entregables formales del proyecto se encuentran en la carpeta `docs/`:
- **[docs/UD02_AsistentePython_IsmaelVargas.pdf](docs/UD02_AsistentePython_IsmaelVargas.pdf):** Memoria técnica académica en formato de tesis formal (8 páginas completas con portada, índice, abstract, análisis algorítmico y referencias).
- **[docs/DocuAsistente.pdf](docs/DocuAsistente.pdf):** Manual técnico exhaustivo de especificación y arquitectura.
