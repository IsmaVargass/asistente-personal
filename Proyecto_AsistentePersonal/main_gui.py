"""
main_gui.py
Interfaz gráfica de usuario (GUI) para Mi Asistente Personal.
Módulo complementario desarrollado con la biblioteca nativa tkinter.

Asignatura: Programación IA
Centro: iLERNA
Autor: Ismael Vargas
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Reutilización directa de la biblioteca central de funciones lógicas
from funciones import (
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


class AsistentePersonalGUI:
    """Clase controladora de la interfaz gráfica de Mi Asistente Personal."""

    def __init__(self, root):
        self.root = root
        self.root.title("Mi Asistente Personal — Ismael Vargas (iLERNA)")
        self.root.geometry("820x620")
        self.root.minsize(750, 550)

        # Estado en memoria de la aplicación
        self.contactos_db = [
            {"nombre": "Carlos Gómez", "telefono": "600112233", "email": "carlos@gmail.com"},
            {"nombre": "Ana Ruiz", "telefono": "611223344", "email": "ana.ruiz@hotmail.com"},
            {"nombre": "Beatriz López", "telefono": "622334455", "email": "bea@empresa.es"}
        ]
        
        self.inventario_db = [
            {"nombre": "Ratón Inalámbrico", "precio": 18.50, "stock": 15},
            {"nombre": "Teclado Mecánico RGB", "precio": 54.99, "stock": 4},
            {"nombre": "Monitor 27 Pulgadas", "precio": 189.00, "stock": 3},
            {"nombre": "Cable HDMI 2.1", "precio": 9.99, "stock": 25},
            {"nombre": "Alfombrilla Gaming", "precio": 12.00, "stock": 0}
        ]
        
        self.gastos_db = [45.50, 18.90, 120.00, 32.10]
        self.presupuesto_base = 600.0

        # Configuración de estilos ttk
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Encabezado formal
        header_frame = tk.Frame(self.root, bg="#0f172a", height=60)
        header_frame.pack(fill="x", side="top")
        
        lbl_title = tk.Label(
            header_frame, 
            text="MI ASISTENTE PERSONAL", 
            font=("Inter", 14, "bold"), 
            fg="#f8fafc", 
            bg="#0f172a"
        )
        lbl_title.pack(anchor="w", padx=20, pady=(10, 0))
        
        lbl_sub = tk.Label(
            header_frame, 
            text="Sistema Modular de Gestión y Algoritmia • Autor: Ismael Vargas (iLERNA)", 
            font=("Inter", 9), 
            fg="#94a3b8", 
            bg="#0f172a"
        )
        lbl_sub.pack(anchor="w", padx=20, pady=(0, 10))

        # Cuaderno de pestañas temáticas (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        # Construcción de pestañas
        self._tab_compras()
        self._tab_economia()
        self._tab_conversores()
        self._tab_contactos()
        self._tab_inventario()
        self._tab_matematicas()
        self._tab_analisis()

    # 1. Pestaña de Compras
    def _tab_compras(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Compras")

        lbl_sec = ttk.Label(tab, text="Facturación y Desglose de Ticket", font=("Inter", 11, "bold"))
        lbl_sec.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        ttk.Label(tab, text="Precio base (€):").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_precio = ttk.Entry(tab, width=20)
        self.ent_precio.grid(row=1, column=1, sticky="w", pady=5)
        self.ent_precio.insert(0, "100.0")

        ttk.Label(tab, text="Descuento (%):").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_desc = ttk.Entry(tab, width=20)
        self.ent_desc.grid(row=2, column=1, sticky="w", pady=5)
        self.ent_desc.insert(0, "10.0")

        ttk.Label(tab, text="IVA aplicable (%):").grid(row=3, column=0, sticky="w", pady=5)
        self.ent_iva = ttk.Entry(tab, width=20)
        self.ent_iva.grid(row=3, column=1, sticky="w", pady=5)
        self.ent_iva.insert(0, "21.0")

        btn_calc = ttk.Button(tab, text="Generar Ticket Desglosado", command=self._calcular_ticket)
        btn_calc.grid(row=4, column=0, columnspan=2, pady=15, sticky="w")

        self.txt_ticket = tk.Text(tab, height=8, width=45, font=("JetBrains Mono", 9), bg="#f8fafc", relief="solid", bd=1)
        self.txt_ticket.grid(row=5, column=0, columnspan=2, sticky="w")

    def _calcular_ticket(self):
        try:
            p = float(self.ent_precio.get().replace(",", "."))
            d = float(self.ent_desc.get().replace(",", "."))
            i = float(self.ent_iva.get().replace(",", "."))
            base, imp_d, imp_i, tot = desglosar_ticket(p, d, i)
            
            res = (
                f"-----------------------------------------\n"
                f"           TICKET DESGLOSADO             \n"
                f"-----------------------------------------\n"
                f"  Base imponible:          {base:>10.2f} €\n"
                f"  Descuento aplicado:     -{imp_d:>10.2f} €\n"
                f"  Cuota de IVA:           +{imp_i:>10.2f} €\n"
                f"-----------------------------------------\n"
                f"  TOTAL LIQUIDADO:         {tot:>10.2f} €\n"
                f"-----------------------------------------"
            )
            self.txt_ticket.delete("1.0", tk.END)
            self.txt_ticket.insert(tk.END, res)
        except ValueError:
            messagebox.showerror("Error de entrada", "Introduce valores numéricos válidos.")

    # 2. Pestaña de Economía
    def _tab_economia(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Economía")

        ttk.Label(tab, text="Control Presupuestario y Gastos", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 10))

        self.lbl_estado_presupuesto = ttk.Label(tab, text="", font=("Inter", 10))
        self.lbl_estado_presupuesto.pack(anchor="w", pady=5)

        frame_input = ttk.Frame(tab)
        frame_input.pack(anchor="w", pady=10)

        ttk.Label(frame_input, text="Registrar nuevo gasto (€):").pack(side="left", padx=(0, 5))
        self.ent_nuevo_gasto = ttk.Entry(frame_input, width=15)
        self.ent_nuevo_gasto.pack(side="left", padx=5)

        btn_add = ttk.Button(frame_input, text="Añadir Gasto", command=self._añadir_gasto)
        btn_add.pack(side="left", padx=5)

        self.txt_resumen_gastos = tk.Text(tab, height=6, width=55, font=("JetBrains Mono", 9), bg="#f8fafc", relief="solid", bd=1)
        self.txt_resumen_gastos.pack(anchor="w", pady=10)

        self._actualizar_vista_economia()

    def _añadir_gasto(self):
        try:
            val = float(self.ent_nuevo_gasto.get().replace(",", "."))
            if val <= 0:
                messagebox.showwarning("Atención", "El importe del gasto debe ser mayor que 0.")
                return
            self.gastos_db.append(val)
            self.ent_nuevo_gasto.delete(0, tk.END)
            self._actualizar_vista_economia()
        except ValueError:
            messagebox.showerror("Error", "Introduce un número válido.")

    def _actualizar_vista_economia(self):
        saldo, pct = calcular_presupuesto_restante(self.presupuesto_base, *self.gastos_db)
        total_g = sumar_gastos(*self.gastos_db)
        tot, med, may, men = resumen_gastos(self.gastos_db)

        self.lbl_estado_presupuesto.config(
            text=f"Presupuesto: {self.presupuesto_base:.2f} €  |  Gastado: {total_g:.2f} € ({pct:.1f}%)  |  Saldo: {saldo:.2f} €"
        )
        info = (
            f"Informe Económico:\n"
            f"• Total gastos registrados: {len(self.gastos_db)}\n"
            f"• Gasto medio: {med:.2f} €\n"
            f"• Gasto máximo: {may:.2f} €  |  Mínimo: {men:.2f} €"
        )
        self.txt_resumen_gastos.delete("1.0", tk.END)
        self.txt_resumen_gastos.insert(tk.END, info)

    # 3. Pestaña de Conversores
    def _tab_conversores(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Conversores")

        ttk.Label(tab, text="Motor de Conversión de Magnitudes (DRY)", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 15))

        f_temp = ttk.LabelFrame(tab, text=" Temperatura ", padding=10)
        f_temp.pack(fill="x", pady=5)
        self.ent_temp_val = ttk.Entry(f_temp, width=10)
        self.ent_temp_val.insert(0, "25")
        self.ent_temp_val.pack(side="left", padx=5)
        self.cmb_temp_o = ttk.Combobox(f_temp, values=["C", "F", "K"], width=4, state="readonly")
        self.cmb_temp_o.set("C")
        self.cmb_temp_o.pack(side="left", padx=5)
        ttk.Label(f_temp, text="a").pack(side="left", padx=5)
        self.cmb_temp_d = ttk.Combobox(f_temp, values=["C", "F", "K"], width=4, state="readonly")
        self.cmb_temp_d.set("F")
        self.cmb_temp_d.pack(side="left", padx=5)
        btn_c_temp = ttk.Button(f_temp, text="Convertir", command=self._convertir_temperatura)
        btn_c_temp.pack(side="left", padx=10)
        self.lbl_res_temp = ttk.Label(f_temp, text="Resultado: --", font=("Inter", 9, "bold"))
        self.lbl_res_temp.pack(side="left", padx=10)

        f_dist = ttk.LabelFrame(tab, text=" Distancia ", padding=10)
        f_dist.pack(fill="x", pady=10)
        self.ent_dist_val = ttk.Entry(f_dist, width=10)
        self.ent_dist_val.insert(0, "10")
        self.ent_dist_val.pack(side="left", padx=5)
        self.cmb_dist_o = ttk.Combobox(f_dist, values=["km", "m", "mi", "ft"], width=4, state="readonly")
        self.cmb_dist_o.set("km")
        self.cmb_dist_o.pack(side="left", padx=5)
        ttk.Label(f_dist, text="a").pack(side="left", padx=5)
        self.cmb_dist_d = ttk.Combobox(f_dist, values=["km", "m", "mi", "ft"], width=4, state="readonly")
        self.cmb_dist_d.set("mi")
        self.cmb_dist_d.pack(side="left", padx=5)
        btn_c_dist = ttk.Button(f_dist, text="Convertir", command=self._convertir_distancia)
        btn_c_dist.pack(side="left", padx=10)
        self.lbl_res_dist = ttk.Label(f_dist, text="Resultado: --", font=("Inter", 9, "bold"))
        self.lbl_res_dist.pack(side="left", padx=10)

    def _convertir_temperatura(self):
        try:
            val = float(self.ent_temp_val.get().replace(",", "."))
            res = convertir_temperatura(val, self.cmb_temp_o.get(), self.cmb_temp_d.get())
            self.lbl_res_temp.config(text=f"Resultado: {res:.2f} º{self.cmb_temp_d.get()}")
        except ValueError:
            messagebox.showerror("Error", "Valor térmico no válido.")

    def _convertir_distancia(self):
        try:
            val = float(self.ent_dist_val.get().replace(",", "."))
            res = convertir_distancia(val, self.cmb_dist_o.get(), self.cmb_dist_d.get())
            self.lbl_res_dist.config(text=f"Resultado: {res:.4f} {self.cmb_dist_d.get()}")
        except ValueError:
            messagebox.showerror("Error", "Valor numérico no válido.")

    # 4. Pestaña de Contactos
    def _tab_contactos(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Contactos")

        ttk.Label(tab, text="Agenda de Contactos en Memoria", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 10))

        frame_top = ttk.Frame(tab)
        frame_top.pack(fill="x", pady=5)

        ttk.Label(frame_top, text="Buscar:").pack(side="left", padx=(0, 5))
        self.ent_buscar_c = ttk.Entry(frame_top, width=20)
        self.ent_buscar_c.pack(side="left", padx=5)
        ttk.Button(frame_top, text="Filtrar", command=self._filtrar_contactos).pack(side="left", padx=5)
        ttk.Button(frame_top, text="Ordenar A-Z (Lambda)", command=self._ordenar_contactos_ui).pack(side="left", padx=5)
        ttk.Button(frame_top, text="Restablecer", command=self._cargar_contactos).pack(side="left", padx=5)

        # Treeview de contactos
        self.tree_c = ttk.Treeview(tab, columns=("nombre", "telefono", "email"), show="headings", height=8)
        self.tree_c.heading("nombre", text="Nombre y Apellidos")
        self.tree_c.heading("telefono", text="Teléfono")
        self.tree_c.heading("email", text="Correo Electrónico")
        self.tree_c.pack(fill="both", expand=True, pady=10)

        self._cargar_contactos()

    def _cargar_contactos(self, lista=None):
        for item in self.tree_c.get_children():
            self.tree_c.delete(item)
        datos = lista if lista is not None else self.contactos_db
        for c in datos:
            self.tree_c.insert("", "end", values=(c["nombre"], c["telefono"], c["email"]))

    def _ordenar_contactos_ui(self):
        self.contactos_db = ordenar_contactos(self.contactos_db)
        self._cargar_contactos()

    def _filtrar_contactos(self):
        crit = self.ent_buscar_c.get().strip()
        filtrados = buscar_contactos(self.contactos_db, crit)
        self._cargar_contactos(filtrados)

    # 5. Pestaña de Inventario
    def _tab_inventario(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Inventario")

        ttk.Label(tab, text="Gestión de Catálogo y Control de Existencias", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 10))

        frame_top = ttk.Frame(tab)
        frame_top.pack(fill="x", pady=5)
        ttk.Button(frame_top, text="Ver Alertas de Stock Bajo (<= 5)", command=self._filtrar_alertas_stock).pack(side="left", padx=5)
        ttk.Button(frame_top, text="Mostrar Todo el Catálogo", command=self._cargar_inventario).pack(side="left", padx=5)

        self.tree_p = ttk.Treeview(tab, columns=("nombre", "precio", "stock"), show="headings", height=8)
        self.tree_p.heading("nombre", text="Producto")
        self.tree_p.heading("precio", text="Precio (€)")
        self.tree_p.heading("stock", text="Stock Disponible")
        self.tree_p.pack(fill="both", expand=True, pady=10)

        self._cargar_inventario()

    def _cargar_inventario(self, lista=None):
        for item in self.tree_p.get_children():
            self.tree_p.delete(item)
        datos = lista if lista is not None else self.inventario_db
        for p in datos:
            self.tree_p.insert("", "end", values=(p["nombre"], f"{p['precio']:.2f} €", f"{p['stock']} uds"))

    def _filtrar_alertas_stock(self):
        alertas = obtener_alertas_stock_bajo(self.inventario_db, 5)
        self._cargar_inventario(alertas)
        messagebox.showinfo("Filtro Aplicado", f"Se encontraron {len(alertas)} productos con existencias en nivel crítico (<= 5).")

    # 6. Pestaña de Matemáticas Recursivas
    def _tab_matematicas(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Matemáticas")

        ttk.Label(tab, text="Algoritmos Recursivos Puros", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 15))

        f_fact = ttk.LabelFrame(tab, text=" Factorial (n!) ", padding=10)
        f_fact.pack(fill="x", pady=5)
        ttk.Label(f_fact, text="Entero n:").pack(side="left", padx=5)
        self.ent_fact = ttk.Entry(f_fact, width=6)
        self.ent_fact.insert(0, "5")
        self.ent_fact.pack(side="left", padx=5)
        ttk.Button(f_fact, text="Calcular", command=self._calc_factorial).pack(side="left", padx=10)
        self.lbl_res_fact = ttk.Label(f_fact, text="Resultado: --", font=("Inter", 9, "bold"))
        self.lbl_res_fact.pack(side="left", padx=10)

        f_fibo = ttk.LabelFrame(tab, text=" Fibonacci (n <= 30) ", padding=10)
        f_fibo.pack(fill="x", pady=5)
        ttk.Label(f_fibo, text="Posición n:").pack(side="left", padx=5)
        self.ent_fibo = ttk.Entry(f_fibo, width=6)
        self.ent_fibo.insert(0, "7")
        self.ent_fibo.pack(side="left", padx=5)
        ttk.Button(f_fibo, text="Calcular", command=self._calc_fibonacci).pack(side="left", padx=10)
        self.lbl_res_fibo = ttk.Label(f_fibo, text="Resultado: --", font=("Inter", 9, "bold"))
        self.lbl_res_fibo.pack(side="left", padx=10)

        f_mcd = ttk.LabelFrame(tab, text=" Máximo Común Divisor (Euclides) ", padding=10)
        f_mcd.pack(fill="x", pady=5)
        ttk.Label(f_mcd, text="A:").pack(side="left", padx=5)
        self.ent_mcd_a = ttk.Entry(f_mcd, width=8)
        self.ent_mcd_a.insert(0, "48")
        self.ent_mcd_a.pack(side="left", padx=5)
        ttk.Label(f_mcd, text="B:").pack(side="left", padx=5)
        self.ent_mcd_b = ttk.Entry(f_mcd, width=8)
        self.ent_mcd_b.insert(0, "18")
        self.ent_mcd_b.pack(side="left", padx=5)
        ttk.Button(f_mcd, text="Calcular", command=self._calc_mcd).pack(side="left", padx=10)
        self.lbl_res_mcd = ttk.Label(f_mcd, text="Resultado: --", font=("Inter", 9, "bold"))
        self.lbl_res_mcd.pack(side="left", padx=10)

    def _calc_factorial(self):
        try:
            n = int(self.ent_fact.get())
            res = calcular_factorial(n)
            self.lbl_res_fact.config(text=f"Resultado: {n}! = {res}")
        except ValueError:
            messagebox.showerror("Error", "Introduce un entero válido.")

    def _calc_fibonacci(self):
        try:
            n = int(self.ent_fibo.get())
            if n > 30:
                messagebox.showwarning("Límite de seguridad", "Por seguridad de ejecución recursiva, n debe ser <= 30.")
                return
            res = calcular_fibonacci(n)
            self.lbl_res_fibo.config(text=f"Resultado: F({n}) = {res}")
        except ValueError:
            messagebox.showerror("Error", "Introduce un entero válido.")

    def _calc_mcd(self):
        try:
            a = int(self.ent_mcd_a.get())
            b = int(self.ent_mcd_b.get())
            res = calcular_mcd(a, b)
            self.lbl_res_mcd.config(text=f"Resultado: MCD({a}, {b}) = {res}")
        except ValueError:
            messagebox.showerror("Error", "Introduce enteros válidos.")

    # 7. Pestaña de Análisis Estadístico
    def _tab_analisis(self):
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Análisis")

        ttk.Label(tab, text="Análisis Estadístico Descriptivo", font=("Inter", 11, "bold")).pack(anchor="w", pady=(0, 10))

        ttk.Label(tab, text="Introduce números separados por comas:").pack(anchor="w", pady=2)
        self.ent_datos_stat = ttk.Entry(tab, width=50)
        self.ent_datos_stat.insert(0, "10, 20, 20, 30, 40, 50")
        self.ent_datos_stat.pack(anchor="w", pady=5)

        ttk.Button(tab, text="Calcular Estadísticas Completas", command=self._calc_estadisticas).pack(anchor="w", pady=5)

        self.lbl_res_stat = ttk.Label(tab, text="", font=("JetBrains Mono", 10), justify="left")
        self.lbl_res_stat.pack(anchor="w", pady=10)

    def _calc_estadisticas(self):
        try:
            raw = self.ent_datos_stat.get().split(",")
            nums = [float(x.strip()) for x in raw if x.strip()]
            if not nums:
                messagebox.showwarning("Atención", "Introduce al menos un número.")
                return
            med, medn, mod, mn, mx = calcular_estadisticas_completas(nums)
            res = (
                f"Resultados Estadísticos:\n"
                f"• Media:   {med:.2f}\n"
                f"• Mediana: {medn:.2f}\n"
                f"• Moda:    {mod}\n"
                f"• Mínimo:  {mn}\n"
                f"• Máximo:  {mx}"
            )
            self.lbl_res_stat.config(text=res)
        except ValueError:
            messagebox.showerror("Error", "Asegúrate de separar números válidos por comas.")


def iniciar_gui():
    """Función de arranque independiente para la interfaz gráfica."""
    root = tk.Tk()
    app = AsistentePersonalGUI(root)
    root.mainloop()


if __name__ == "__main__":
    iniciar_gui()
