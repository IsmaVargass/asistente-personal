# Mi Asistente Personal en Python

**Proyecto:** Programación IA (2026/27) — iLERNA  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Autor:** Ismael Vargas ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 Descripción del Proyecto

**Mi Asistente Personal** es una aplicación modular por consola desarrollada íntegramente en Python 3 (versión 3.10 o superior), utilizando exclusivamente la librería estándar del lenguaje. Su objetivo es centralizar operaciones cotidianas a través de un menú interactivo estructurado en 8 módulos independientes:

1. **Gestión de compras:** Facturación con descuentos, tipos impositivos de IVA y desglose comercial del ticket.
2. **Gestión económica:** Control de presupuestos, registro acumulativo de gastos con `*args` y reparto equitativo de cuentas.
3. **Conversores de unidades:** Motor de conversión de temperaturas (C, F, K), tiempos (s, m, h, d) y distancias (m, km, mi, ft).
4. **Agenda de contactos:** Registro, búsqueda insensible a mayúsculas, eliminación y ordenación alfabética mediante funciones Lambda.
5. **Gestión de inventario:** Control de existencias (entradas/salidas bloqueando saldos negativos) y alertas automáticas de rotura de stock.
6. **Utilidades matemáticas:** Algoritmos recursivos puros para Factorial, sucesión de Fibonacci y Máximo Común Divisor (MCD mediante Euclides).
7. **Análisis de información:** Cálculo estadístico descriptivo (media, mediana, moda, mínimo y máximo) y filtrado funcional dinámico.
8. **Salir:** Cierre seguro y limpio del sistema con captura de interrupciones de teclado (`Ctrl + C`).

---

## 🎯 Arquitectura e Ingeniería del Software

- **Principio DRY (Don't Repeat Yourself):** Cada cálculo y transformación se declara una sola vez en funciones independientes y reutilizables.
- **Desacoplamiento I/O:** Las funciones de cálculo en `src/funciones.py` no realizan `print()` ni `input()`, garantizando su reutilización e integración en cualquier interfaz o API.
- **Modularidad:** Separación limpia del código fuente en `src/` y de la documentación formal en `docs/`.
- **Robustez y Gestión de Excepciones:** Validación de entradas mediante bucles de control y bloques `try/except ValueError` para prevenir caídas de ejecución.

---

## 📁 Estructura del Repositorio

```text
asistente-personal/
├── docs/
│   ├── UD02_AsistentePython_IsmaelVargas.pdf   # Presentación técnica oficial en diapositivas
│   └── DocuAsistente.pdf                      # Manual técnico exhaustivo del proyecto
├── src/
│   ├── main.py                                # Punto de entrada y menú interactivo
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
- Sin dependencias de terceros (no requiere `pip install`).

### Ejecución de la Aplicación Principal
Desde la raíz del repositorio:
```bash
python src/main.py
```

### Ejecución de Suites de Pruebas Unitarias
Cada módulo incluye su propio bloque de verificación ejecutable de forma aislada:
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
- **[docs/UD02_AsistentePython_IsmaelVargas.pdf](docs/UD02_AsistentePython_IsmaelVargas.pdf):** Presentación técnica oficial en diapositivas con evidencias de terminal real y desarrollo de los 7 puntos exigidos en la rúbrica.
- **[docs/DocuAsistente.pdf](docs/DocuAsistente.pdf):** Manual técnico del proyecto con desglose de funciones, arquitectura modular y verificación.
