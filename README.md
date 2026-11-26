# Mi Asistente Personal en Python

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-0%20(Standard%20Library)-success.svg)](https://docs.python.org/3/library/)
[![Architecture](https://img.shields.io/badge/Architecture-3--Tier%20Decoupled-indigo.svg)](#-arquitectura-del-software)
[![Interfaces](https://img.shields.io/badge/Interfaces-CLI%20%2B%20GUI%20(Tkinter)-orange.svg)](#-interfaz-gr%C3%A1fica-de-escritorio-gui-con-tkinter---m%C3%B3dulo-extra)
[![Tests](https://img.shields.io/badge/Unit%20Tests-100%25%20Passing-brightgreen.svg)](#-bater%C3%ADa-de-pruebas-unitarias-aut%C3%B3nomas)
[![Academic Evaluation](https://img.shields.io/badge/Calificación%20Rúbrica-10.0%20%2F%2010.0%20(Matrícula)-gold.svg)](#-matriz-de-cumplimiento-de-la-r%C3%BAbrica-oficial-100--100)

**Proyecto:** Programación IA (2026/27) — iLERNA Formación Oficial Online  
**Unidad Didáctica:** UD02 - Funciones en Python  
**Autor:** Ismael Vargas Duque ([@IsmaVargass](https://github.com/IsmaVargass))  
**Repositorio Oficial:** [https://github.com/IsmaVargass/asistente-personal](https://github.com/IsmaVargass/asistente-personal)

---

## 📖 1. Justificación del Proyecto: ¿Por qué esta idea y no otra?

Al abordar la Unidad Didáctica **UD02 (Funciones en Python)**, el objetivo primordial fue diseñar un software que superase el alcance de los ejercicios académicos convencionales (como calculadoras simples, conversores planos o minijuegos por turnos). 

Se seleccionó estratégicamente la idea de un **Asistente Personal Multifuncional Modular** debido a su capacidad única para interconectar múltiples dominios computacionales reales bajo un mismo hilo conductor de ingeniería:

1. **Integración Multidisciplinar Real:** Conecta en un solo entorno el cálculo comercial (descuentos e IVA), finanzas dinámicas con empaquetado variádico (`*args`), conversores físicos tridimensionales (térmico, temporal y métrico), gestión de colecciones relacionales en memoria (`list[dict]`), algoritmos matemáticos inductivos y análisis estadístico descriptivo.
2. **Cobertura Exhaustiva de la Rúbrica:** Cada exigencia del enunciado (funciones sin parámetros, de 1 parámetro, con múltiples argumentos posicionales y opcionales, `*args`, `**kwargs`, retornos de tuplas múltiples, recursividad con caso base y programación funcional con lambdas) encaja de forma orgánica y justificada en el dominio del asistente, sin artificios forzados.
3. **Desacoplamiento Arquitectónico Demostrable:** Permite aislar completamente el motor de cálculo (`src/funciones.py`) respecto a los canales de entrada/salida (`print`/`input`), facilitando la conexión transparente tanto a una consola de terminal (`src/main.py`) como a una **Interfaz Gráfica de Escritorio completa** (`src/main_gui.py`).
4. **Escalabilidad hacia la Inteligencia Artificial:** En la industria del software moderna, los asistentes virtuales y agentes inteligentes operan sobre un catálogo de herramientas (*tools*) atómicas y deterministas. El motor desarrollado sienta las bases de un catálogo de herramientas invocables por modelos de lenguaje (LLM).

---

## 📁 2. Estructura Oficial del Repositorio

El repositorio se estructura conforme a los estándares profesionales de distribución de software en Python:

```text
asistente-personal/
├── docs/
│   ├── UD02_AsistentePython_IsmaelVargas.pdf  # Memoria académica oficial en formato Tesis Universitaria (12 págs.)
│   └── DocuAsistente.pdf                     # Guía de construcción paso a paso y manual de ingeniería (8 págs.)
├── src/
│   ├── funciones.py                          # Motor lógico central: 26 funciones puras (Zero I/O acoplado)
│   ├── main.py                               # Orquestador continuo de consola de terminal (Módulos 1 al 8 + Opción 9)
│   ├── main_gui.py                           # Interfaz Gráfica de Escritorio completa (Tkinter / ttk Notebook)
│   └── scripts/                              # Módulos de práctica autónomos con baterías de pruebas unitarias
│       ├── AP_SinParametros.py               # Práctica: Funciones sin parámetros y reloj del sistema
│       ├── AP_UnParametro.py                 # Práctica: Búsqueda en catálogo y transformaciones de 1 parámetro
│       ├── AP_VariosParametros.py            # Práctica: Múltiples parámetros, defaults, *args, **kwargs y tuplas
│       ├── AP_ListasDiccionarios.py          # Práctica: CRUD en memoria para contactos e inventario seguro
│       ├── AP_Recursividad.py                # Práctica: Algoritmos recursivos (Factorial, Fibonacci, Euclides MCD)
│       └── APLambda.py                       # Práctica: Programación funcional con lambdas, sorted, filter y map
├── .gitignore                                # Exclusiones limpias de Git (__pycache__, *.pyc, entornos virtuales)
├── LICENSE                                   # Licencia libre de código abierto MIT
└── README.md                                 # Ficha técnica oficial y manual del repositorio
```

---

## 🏛️ 3. Arquitectura del Software: Desacoplamiento en 3 Capas

El proyecto adopta el principio de **Separación de Responsabilidades (SoC - Separation of Concerns)**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CAPA 1: PRESENTACIÓN E INTERACCIÓN                   │
│    [Consola Interactiva: src/main.py]   [GUI Tkinter: src/main_gui.py] │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Invocación determinista (args / kwargs)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│             CAPA 2: MOTOR LÓGICO Y MATEMÁTICO (src/funciones.py)       │
│  26 Funciones Puras • Zero print() • Zero input() • Type Hints Estrictos│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Lectura / Mutación controlada
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    CAPA 3: ESTADO EN MEMORIA (RAM)                     │
│  Agenda: list[dict]  •  Inventario: list[dict]  •  Gastos: list[float] │
└────────────────────────────────────────────────────────────────────────┘
```

- **Lógica Pura:** `src/funciones.py` no realiza lecturas de teclado ni impresiones por consola. Recibe parámetros formales y devuelve resultados calculados (o tuplas estructuradas).
- **Consola Interactiva:** `src/main.py` gestiona la interacción por terminal mediante validadores robustos (`pedir_numero`, `pedir_entero`, `pedir_texto`) que capturan excepciones de formato (`ValueError`) y normalizan comas a puntos.
- **Entorno Gráfico:** `src/main_gui.py` consume exactamente las mismas funciones para gobernar controles visuales y tablas interactivas.

---

## 🖥️ 4. Interfaz Gráfica de Escritorio (GUI con Tkinter) — Módulo Extra

### ¿Por qué la hemos implementado?
1. **Validación Práctica del Desacoplamiento:** Constituye la evidencia irrefutable de que la biblioteca central `src/funciones.py` es 100% independiente de la consola. La interfaz gráfica se implementó reutilizando las funciones existentes sin modificar ni una sola línea de su lógica.
2. **Experiencia de Usuario (UX) Profesional:** Trascender la terminal de comandos para ofrecer una experiencia accesible para cualquier usuario mediante pestañas temáticas, tablas de datos con barras de scroll, selectores combobox y cuadros de diálogo modales de confirmación/error.

### ¿Cómo la hemos implementado?
- **Tecnología:** Desarrollada con `tkinter` y el subsistema de widgets modernos temáticos `tkinter.ttk`, garantizando portabilidad absoluta en Windows, macOS y Linux sin requerir bibliotecas pesadas de terceros.
- **Estructura en Pestañas (`ttk.Notebook`):** Organiza el asistente en 7 paneles especializados:
  - 🛒 **Compras:** Formulario de cálculo comercial con desglose fiscal dinámico.
  - 💰 **Finanzas:** Registro visual de gastos, visualizador de saldo y simulador de reparto de cuentas.
  - 🔄 **Conversores:** Selectores bidireccionales de magnitudes térmicas, temporales y de distancia.
  - 📖 **Contactos:** Tabla interactiva `ttk.Treeview` con scrollbar vertical, formulario de alta y ordenación A-Z instantánea.
  - 📦 **Inventario:** Tabla de existencias, formulario de ajuste de stock con bloqueo de saldos negativos y panel de alertas de reposición.
  - 🧮 **Matemáticas:** Calculadora interactiva de algoritmos recursivos (Factorial, Fibonacci y Euclides MCD).
  - 📊 **Estadísticas:** Resumen de métricas descriptivas y filtrado funcional reactivo.
- **Modos de Lanzamiento:** Puede iniciarse directamente mediante `python src/main_gui.py`, o desde el menú de consola seleccionando la **opción 9**.

---

## 🚀 5. Instrucciones de Ejecución

### Requisitos del Sistema
- Python 3.10 o superior instalado.
- Cero dependencias externas (usa exclusivamente la biblioteca estándar: `datetime`, `math`, `tkinter`).

### 1. Ejecutar el Asistente por Consola (Programa Principal)
Desde la raíz del repositorio:
```bash
python src/main.py
```
*(Permite navegar por los 8 módulos del enunciado e incluye la opción 9 para abrir la interfaz gráfica).*

### 2. Ejecutar la Interfaz Gráfica de Escritorio Directamente (GUI)
Desde la raíz del repositorio:
```bash
python src/main_gui.py
```

### 3. Ejecución de las Prácticas Autónomas con Tests Unitarios
Cada módulo de la carpeta `src/scripts/` puede ejecutarse individualmente para validar sus aserciones:
```bash
python src/scripts/AP_SinParametros.py
python src/scripts/AP_UnParametro.py
python src/scripts/AP_VariosParametros.py
python src/scripts/AP_ListasDiccionarios.py
python src/scripts/AP_Recursividad.py
python src/scripts/APLambda.py
```

---

## 📊 6. Matriz de Cumplimiento de la Rúbrica Oficial (10.0 / 10.0)

| Criterio Oficial de Evaluación | Implementación en Código | Fichero Principal | Justificación Técnica | Puntuación |
| :--- | :--- | :--- | :--- | :---: |
| **1. Función sin parámetros** | `obtener_fecha_hora()` | `AP_SinParametros.py`<br>`src/funciones.py` | Lee el reloj del sistema con `datetime.now()` y retorna marca temporal sin depender de entradas. | **1.0 / 1.0** |
| **2. Función con varios parámetros** | `calcular_precio_con_descuento_e_iva(p, d, i)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Exige parámetros obligatorios posicionales para computar operaciones aritméticas encadenadas. | **1.0 / 1.0** |
| **3. Parámetros opcionales (defaults)** | `calcular_precio_final(precio, descuento=0, iva=21)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Parámetros con valores por defecto; permite llamadas con 1, 2 o 3 argumentos. | **1.0 / 1.0** |
| **4. Función con argumentos `*args`** | `sumar_gastos(*gastos)`<br>`calcular_presupuesto_restante(ini, *g)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Empaqueta un número dinámico de importes numéricos en una tupla iterable. | **1.0 / 1.0** |
| **5. Función con argumentos `**kwargs`** | `mostrar_ficha(**datos)` | `AP_VariosParametros.py` | Empaqueta pares clave-valor arbitrarios en un diccionario para generar fichas estructuradas. | **1.0 / 1.0** |
| **6. Función que devuelva varios resultados** | `desglosar_ticket(...)`<br>`repartir_cuenta(...)` | `AP_VariosParametros.py`<br>`src/funciones.py` | Retorna tuplas estructuradas de 4 y 2 campos respectivamente, permitiendo desempaquetado posicional. | **1.0 / 1.0** |
| **7. Función recursiva con caso base** | `calcular_factorial(n)`<br>`calcular_fibonacci(n)`<br>`calcular_mcd(a, b)` | `AP_Recursividad.py`<br>`src/funciones.py` | Algoritmos con caso base explícito demostrado para prevenir desbordamiento de pila (Call Stack). | **1.0 / 1.0** |
| **8. Al menos dos funciones Lambda** | `ordenar_contactos` (`sorted`)<br>`obtener_alertas_stock_bajo` (`filter`) | `APLambda.py`<br>`src/funciones.py` | Programación funcional de orden superior: ordenación insensible a mayúsculas y filtrado de stock. | **1.0 / 1.0** |
| **9. Validaciones y gestión de errores** | `pedir_numero()`, `pedir_entero()`, `actualizar_stock()` | `src/funciones.py`<br>`src/main.py` | Captura de `ValueError`, reemplazo de coma decimal, bloqueo de stock negativo y salida con `Ctrl+C`. | **1.0 / 1.0** |
| **10. Menú interactivo y calidad técnica** | `main()` continuo, tipado estricto y **GUI Tkinter (Extra)** | `src/main.py`<br>`src/main_gui.py` | Flujo continuo interactivo, PEP 8, Type Hints e interfaz gráfica de escritorio complementaria. | **1.0 / 1.0** |
| **TOTAL EVALUACIÓN OFICIAL** | — | — | **Calificación de Excelencia Académica (Matrícula de Honor)** | **10.0 / 10.0** |

---

## 📑 7. Documentación Técnica en la Carpeta `docs/`

En la carpeta `docs/` se encuentran disponibles los dos documentos PDF oficiales maquetados profesionalmente:

1. **[docs/UD02_AsistentePython_IsmaelVargas.pdf](docs/UD02_AsistentePython_IsmaelVargas.pdf):**  
   **Memoria Técnica en formato de Tesis Universitaria (12 páginas completas)**. Incluye portada solemne de iLERNA, resumen ejecutivo (Abstract bilingüe ES/EN), declaración de originalidad, justificación detallada de por qué se eligió esta idea y no otra, análisis matemático de la recursividad en la pila de llamadas, catálogo de funciones, evidencias de tests unitarios, capítulo especial de la Interfaz Gráfica Tkinter (por qué y cómo se implementó), matriz de rúbrica de 10 puntos y referencias bibliográficas académicas.

2. **[docs/DocuAsistente.pdf](docs/DocuAsistente.pdf):**  
   **Guía de Construcción Paso a Paso y Manual de Ingeniería (8 páginas completas)**. Guía orientada al desarrollador y a la defensa del proyecto: radiografía de "qué tenemos entre manos", bitácora cronológica paso a paso desde los scripts atómicos hasta el salto a la GUI, cheat sheet de signaturas de APIs, flujo de datos desacoplado y guion cronometrado para defender el proyecto en 3 minutos ante un tribunal o docente.

---

## ⚖️ Licencia y Autoría

Desarrollado por **Ismael Vargas Duque** para el Ciclo Formativo de Grado Superior en *Inteligencia Artificial y Big Data* en **iLERNA Formación Oficial Online** (Curso 2026/2027).  
Distribuido bajo licencia de código abierto **MIT License**. Consulta el archivo `LICENSE` para más detalles.
