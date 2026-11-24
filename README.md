# Mi Asistente Personal en Python

**Proyecto:** Programación IA (2026/27) — iLERNA  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Autor:** Ismael Vargas ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 Descripción del Proyecto

**Mi Asistente Personal** es una aplicación modular desarrollada en Python 3 (versión 3.10 o superior) empleando exclusivamente la librería estándar del lenguaje. Su objetivo es estructurar y resolver tareas cotidianas mediante funciones reutilizables organizadas en 8 áreas operativas:

1. **Gestión de compras:** Facturación con descuentos, tipos impositivos de IVA y desglose comercial del ticket.
2. **Gestión económica:** Control presupuestario, registro dinámico de gastos con `*args` y reparto equitativo de cuentas.
3. **Conversores de unidades:** Motor de conversión de temperaturas (C, F, K), tiempos (s, m, h, d) y distancias (m, km, mi, ft).
4. **Agenda de contactos:** Registro en listas de diccionarios, búsqueda insensible a mayúsculas, eliminación y ordenación alfabética mediante lambdas.
5. **Gestión de inventario:** Control de existencias (bloqueo de stock negativo) y alertas automáticas de reposición.
6. **Utilidades matemáticas:** Algoritmos recursivos para Factorial, sucesión de Fibonacci y Máximo Común Divisor (Euclides).
7. **Análisis de información:** Tratamiento estadístico descriptivo (media, mediana, moda, mínimo y máximo) y filtrado funcional.
8. **Salir:** Cierre limpio del hilo de ejecución con captura de interrupciones de teclado (`Ctrl + C`).

---

## 📁 Estructura del Proyecto

El repositorio está organizado de forma limpia y profesional, agrupando el código fuente en `src/`, las prácticas independientes en `src/scripts/` y la documentación técnica en `docs/`:

```text
asistente-personal/
├── docs/
│   ├── UD02_AsistentePython_IsmaelVargas.pdf # Memoria técnica oficial en formato Tesis Académica
│   └── DocuAsistente.pdf                    # Manual técnico exhaustivo de especificación
├── src/
│   ├── main.py                              # Programa principal interactivo de consola
│   ├── main_gui.py                          # Extensión complementaria con interfaz gráfica (Tkinter)
│   ├── funciones.py                         # Biblioteca central de lógica y servicios de cálculo
│   └── scripts/
│       ├── AP_SinParametros.py              # Práctica: Funciones sin parámetros
│       ├── AP_UnParametro.py                # Práctica: Funciones con un único parámetro
│       ├── AP_VariosParametros.py           # Práctica: Múltiples parámetros, opcionales, *args, **kwargs y tuplas
│       ├── AP_ListasDiccionarios.py         # Práctica: Gestión de colecciones en memoria
│       ├── AP_Recursividad.py               # Práctica: Algoritmos recursivos y caso base
│       └── APLambda.py                      # Práctica: Funciones anónimas con sorted, filter y map
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Instrucciones de Ejecución

### Requisitos
- Python 3.10 o superior instalado.
- Sin dependencias externas de terceros (no requiere `pip install`, usa biblioteca estándar).

### 1. Ejecución del Asistente por Consola (Programa Principal)
Desde la raíz del proyecto:
```bash
python src/main.py
```
*(Permite navegar por los 8 módulos obligatorios del enunciado e incluye la opción 9 para lanzar la interfaz gráfica).*

### 2. Ejecución Directa de la Interfaz Gráfica (Tkinter)
Desde la raíz del proyecto:
```bash
python src/main_gui.py
```

### 3. Ejecución de los Módulos de Práctica Independientes
Desde la raíz del proyecto, cada archivo puede ejecutarse directamente para comprobar su batería de pruebas unitarias:
```bash
python src/scripts/AP_SinParametros.py
python src/scripts/AP_UnParametro.py
python src/scripts/AP_VariosParametros.py
python src/scripts/AP_ListasDiccionarios.py
python src/scripts/AP_Recursividad.py
python src/scripts/APLambda.py
```

---

## 📊 Matriz de Cumplimiento de Requisitos Técnicos

| Requisito Oficial | Función en Código | Ubicación | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Al menos una función sin parámetros** | `obtener_fecha_hora()`, `mostrar_bienvenida()` | `src/scripts/AP_SinParametros.py`, `src/funciones.py` | Genera y retorna marcas temporales del sistema sin depender de entradas externas. |
| **Al menos una función con varios parámetros** | `calcular_precio_con_descuento_e_iva(p, d, i)` | `src/scripts/AP_VariosParametros.py`, `src/funciones.py` | Maneja múltiples parámetros obligatorios posicionales. |
| **Función con parámetros opcionales** | `calcular_precio_final(precio, descuento=0, iva=21)` | `src/scripts/AP_VariosParametros.py`, `src/funciones.py` | Incorpora valores por defecto parametrizados. |
| **Función con `*args`** | `sumar_gastos(*gastos)`, `calcular_media(*numeros)` | `src/scripts/AP_VariosParametros.py`, `src/funciones.py` | Empaqueta un número indeterminado de argumentos posicionales en una tupla iterable. |
| **Función con `**kwargs`** | `mostrar_ficha(**datos)` | `src/scripts/AP_VariosParametros.py` | Empaqueta argumentos con nombre en un diccionario clave-valor. |
| **Función que devuelva varios resultados** | `desglosar_ticket(...)`, `repartir_cuenta(...)` | `src/scripts/AP_VariosParametros.py`, `src/funciones.py` | Retorna múltiples resultados empaquetados en tuplas desempaquetables. |
| **Función recursiva con caso base** | `calcular_factorial(n)`, `calcular_fibonacci(n)`, `calcular_mcd(a, b)` | `src/scripts/AP_Recursividad.py`, `src/funciones.py` | Algoritmos con caso base explícito para evitar desbordamiento del call stack. |
| **Al menos dos funciones Lambda** | `ordenar_contactos` (`sorted`), `obtener_alertas_stock_bajo` (`filter`) | `src/scripts/APLambda.py`, `src/funciones.py` | Programación funcional de orden superior para filtrado y ordenación inline. |
| **Validaciones y gestión de errores** | `pedir_numero()`, `pedir_entero()`, `actualizar_stock()` | `src/funciones.py` | Captura de `ValueError`, bloqueo de stock negativo y salida controlada ante `Ctrl+C`. |
| **Menú interactivo continuo** | `main()` con bucle `while True` | `src/main.py` | Flujo continuo con submenús temáticos y opción de salida limpia. |

---

## 📑 Documentación Técnica Oficial

Los entregables formales del proyecto se encuentran en la carpeta `docs/`:
- **[docs/UD02_AsistentePython_IsmaelVargas.pdf](docs/UD02_AsistentePython_IsmaelVargas.pdf):** Memoria técnica académica en formato de tesis formal (8 páginas completas con portada, índice, abstract, análisis algorítmico y referencias).
- **[docs/DocuAsistente.pdf](docs/DocuAsistente.pdf):** Manual técnico exhaustivo de especificación y arquitectura.
