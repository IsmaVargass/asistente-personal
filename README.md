# Mi Asistente Personal en Python

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-0%20(Librer%C3%ADa%20Est%C3%A1ndar)-success.svg)](https://docs.python.org/3/library/)
[![Interfaces](https://img.shields.io/badge/Interfaces-Consola%20%2B%20GUI%20(Tkinter)-orange.svg)](#-interfaz-gr%C3%A1fica-de-escritorio-gui-con-tkinter---m%C3%B3dulo-extra)
[![Unit Tests](https://img.shields.io/badge/Tests%20Unitarios-100%25%20Aprobados-brightgreen.svg)](#3-ejecuci%C3%B3n-de-las-pr%C3%A1cticas-aut%C3%B3nomas)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Proyecto:** Mi Asistente Personal  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Autor:** Ismael Vargas ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 1. Descripción y Justificación del Proyecto

**Mi Asistente Personal** es una aplicación desarrollada en Python 3 que resuelve tareas cotidianas mediante un catálogo estructurado de funciones reutilizables. Frente a alternativas más sencillas (como una calculadora básica o un conversor aislado), este proyecto integra múltiples áreas funcionales en un único sistema modular:

1. **Gestión de compras:** Cálculo de facturación comercial con descuentos e IVA, junto con el desglose del ticket.
2. **Gestión económica:** Control presupuestario, suma dinámica de una lista variable de gastos con `*args` y reparto equitativo de cuentas.
3. **Conversores de unidades:** Motor de conversión de temperaturas (Celsius, Fahrenheit, Kelvin), tiempo (segundos, minutos, horas, días) y distancias (metros, kilómetros, millas, pies).
4. **Agenda de contactos:** Almacenamiento en listas de diccionarios, búsqueda insensible a mayúsculas, eliminación y ordenación alfabética mediante lambdas.
5. **Gestión de inventario:** Control de existencias (bloqueo de stock negativo) y alertas automáticas de reposición reactiva.
6. **Utilidades matemáticas:** Algoritmos recursivos para Factorial ($n!$), sucesión de Fibonacci y Máximo Común Divisor (Algoritmo de Euclides).
7. **Análisis de información:** Estadística descriptiva (media, mediana, moda, mínimo y máximo) y filtrado funcional con `filter()`.
8. **Salir:** Cierre limpio del hilo de ejecución con captura de interrupciones de teclado (`Ctrl + C`).

---

## 📁 2. Estructura del Repositorio

El proyecto mantiene una estructura modular y ordenada:

```text
asistente-personal/
├── docs/
│   ├── UD02_AsistentePython_IsmaelVargas.pdf  # Informe visual para presentar el proyecto (10 págs.)
│   └── DocuAsistente.pdf                     # Guía técnica paso a paso y manual de proyecto (8 págs.)
├── src/
│   ├── funciones.py                          # Biblioteca central: 26 funciones puras (sin I/O acoplado)
│   ├── main.py                               # Consola interactiva continua (Módulos 1 al 8 + Opción 9)
│   ├── main_gui.py                           # Interfaz Gráfica de Escritorio completa (Tkinter / ttk)
│   └── scripts/                              # Prácticas autónomas independientes con pruebas unitarias
│       ├── AP_SinParametros.py               # Funciones sin parámetros y reloj del sistema
│       ├── AP_UnParametro.py                 # Funciones con 1 parámetro y búsqueda en catálogo
│       ├── AP_VariosParametros.py            # Parámetros opcionales, tuplas, *args y **kwargs
│       ├── AP_ListasDiccionarios.py          # Gestión de colecciones en memoria (agenda e inventario)
│       ├── AP_Recursividad.py                # Algoritmos recursivos y caso base (Factorial, Fibonacci, Euclides)
│       └── APLambda.py                       # Expresiones lambda, sorted(), filter() y map()
├── .gitignore                                # Exclusión de temporales y bytecode (__pycache__)
├── LICENSE                                   # Licencia libre MIT
└── README.md                                 # Ficha técnica y manual del proyecto
```

---

## 🚀 3. Instrucciones de Ejecución

### Requisitos
- Python 3.10 o superior instalado.
- Cero dependencias externas (utiliza únicamente la biblioteca estándar de Python: `datetime`, `math`, `tkinter`).

### 1. Ejecución del Asistente por Consola (Programa Principal)
Desde la raíz del proyecto:
```bash
python src/main.py
```
*(Permite navegar por los 8 módulos de consola e incluye la opción 9 para iniciar la interfaz gráfica).*

### 2. Ejecución Directa de la Interfaz Gráfica (Tkinter)
Desde la raíz del proyecto:
```bash
python src/main_gui.py
```

### 3. Ejecución de las Prácticas Autónomas
Cada archivo en `src/scripts/` contiene su propia batería de pruebas unitarias ejecutables de forma independiente:
```bash
python src/scripts/AP_SinParametros.py
python src/scripts/AP_UnParametro.py
python src/scripts/AP_VariosParametros.py
python src/scripts/AP_ListasDiccionarios.py
python src/scripts/AP_Recursividad.py
python src/scripts/APLambda.py
```

---

## 🖥️ 4. Interfaz Gráfica de Escritorio (GUI con Tkinter) — Módulo Extra

### ¿Por qué la hemos implementado?
- **Demostración de Desacoplamiento:** Muestra que la biblioteca de cálculo `src/funciones.py` está totalmente aislada de la consola. La interfaz gráfica reutiliza el 100% de las funciones sin haber tenido que modificar su lógica.
- **Accesibilidad y Usabilidad:** Ofrece una experiencia visual e intuitiva con formularios, desplegables, tablas con scroll y avisos modales.

### ¿Cómo la hemos implementado?
- Construida íntegramente con `tkinter` y su subsistema temático moderno `tkinter.ttk`.
- Organizada mediante un panel de pestañas (`ttk.Notebook`) para cada módulo temático.
- Tablas interactivas con barras de scroll vertical (`ttk.Treeview`) para la agenda y el inventario.
- Diálogos modales nativos (`messagebox`) para confirmaciones, alertas de reposición y errores de formato.

---

## 📊 5. Matriz de Requisitos Técnicos

| Requisito | Función en Código | Ubicación | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Función sin parámetros** | `obtener_fecha_hora()` | `AP_SinParametros.py`<br>`src/funciones.py` | Lee la marca temporal del sistema con `datetime.now()` sin requerir entradas externas. |
| **Función con varios parámetros** | `calcular_precio_con_descuento_e_iva(p, d, i)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Exige parámetros obligatorios posicionales para el cálculo comercial. |
| **Parámetros opcionales (defaults)** | `calcular_precio_final(precio, descuento=0, iva=21)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Asigna valores por defecto que permiten invocar la función con 1, 2 o 3 argumentos. |
| **Función con `*args`** | `sumar_gastos(*gastos)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Empaqueta una cantidad dinámica de importes numéricos en una tupla iterable. |
| **Función con `**kwargs`** | `mostrar_ficha(**datos)` | `AP_VariosParametros.py` | Recibe pares clave-valor arbitrarios para formatear datos en diccionarios. |
| **Función con retorno múltiple** | `desglosar_ticket(...)`<br>`repartir_cuenta(...)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Devuelve tuplas estructuradas de 4 y 2 resultados respectivamente. |
| **Función recursiva con caso base** | `calcular_factorial(n)`<br>`calcular_fibonacci(n)`<br>`calcular_mcd(a, b)` | `AP_Recursividad.py`<br>`src/funciones.py` | Algoritmos con caso base explícito que frenan la pila de llamadas (Call Stack). |
| **Funciones Lambda** | `ordenar_contactos` (`sorted`)<br>`obtener_alertas_stock_bajo` (`filter`) | `APLambda.py`<br>`src/funciones.py` | Programación funcional: ordenación A-Z insensible a mayúsculas y filtrado de stock crítico. |
| **Validaciones defensivas** | `pedir_numero()`, `pedir_entero()` | `src/funciones.py`<br>`src/main.py` | Captura de `ValueError`, reemplazo de coma decimal y bloqueo de stock negativo. |
| **Menú interactivo continuo** | `main()` con bucle `while True` | `src/main.py` | Bucle continuo con submenús, navegación fluida y salida controlada. |

---

## 📑 6. Documentación en la Carpeta `docs/`

1. **[docs/UD02_AsistentePython_IsmaelVargas.pdf](docs/UD02_AsistentePython_IsmaelVargas.pdf):**  
   **Informe visual para presentar el proyecto (10 páginas).** Diseñado de forma esquemática y gráfica (iconos, tarjetas, trazas de recursión, mockups de terminal y de GUI, tablas y poco texto plano) para exponerlo de manera clara.
2. **[docs/DocuAsistente.pdf](docs/DocuAsistente.pdf):**  
   **Guía técnica paso a paso y manual de proyecto (8 páginas).** Documento de referencia para el desarrollador: bitácora de cómo se construyó cada fase, qué tenemos entre manos, catálogo completo de APIs y guion para defender el proyecto en 3 minutos.

---

## ⚖️ Licencia y Autoría

Desarrollado por **Ismael Vargas Duque**.  
Distribuido bajo licencia de código abierto **MIT License**. Consulta el archivo `LICENSE` para más detalles.
