import tkinter as tk
from tkinter import ttk, messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio14")
        self.root.geometry("500x600")


        # --- Menú ---
        menubar = tk.Menu(self.root)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        self.root.config(menu=menubar)

        # --- Frame del formulario ---
        frame_form = tk.LabelFrame(self.root, text="Datos del Usuario", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=10)

        # Nombre
        tk.Label(frame_form, text="Nombre:").pack(anchor="w")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.pack(fill="x", pady=5)

        # Edad
        tk.Label(frame_form, text="Edad:").pack(anchor="w")
        self.scale_edad = tk.Scale(frame_form, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack(fill="x", pady=5)

        # Género
        tk.Label(frame_form, text="Género:").pack(anchor="w", pady=(5, 0))
        self.genero_var = tk.StringVar(value="Otro")

        frame_genero = tk.Frame(frame_form)
        frame_genero.pack(pady=5, anchor="w")

        ttk.Radiobutton(frame_genero, text="Masculino", variable=self.genero_var, value="Masculino").pack(side="left", padx=5)
        ttk.Radiobutton(frame_genero, text="Femenino", variable=self.genero_var, value="Femenino").pack(side="left", padx=5)
        ttk.Radiobutton(frame_genero, text="Otro", variable=self.genero_var, value="Otro").pack(side="left", padx=5)

        # --- Lista de usuarios ---
        frame_lista = tk.LabelFrame(self.root, text="Usuarios Registrados", padx=5, pady=5)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
        self.listbox.pack(fill="both", expand=True)

        scrollbar.config(command=self.listbox.yview)

        # --- Botones inferiores ---
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Añadir", command=self.añadir_usuario).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Salir", command=self.salir).pack(side="left", padx=10)

    # --- Métodos idénticos a los del ejercicio original ---
    def añadir_usuario(self):
        nombre = self.entry_nombre.get().strip()
        edad = int(self.scale_edad.get())
        genero = self.genero_var.get()

        if not nombre:
            messagebox.showwarning("Error", "El nombre no puede estar vacío.")
            return

        usuario = f"{nombre} - {edad} años - {genero}"
        self.listbox.insert(tk.END, usuario)
        self.entry_nombre.delete(0, tk.END)
        self.genero_var.set("Otro")
        self.scale_edad.set(0)

    def eliminar_usuario(self):
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un usuario para eliminar.")
            return
        self.listbox.delete(seleccion)

    def guardar_lista(self):
        total = self.listbox.size()
        messagebox.showinfo("Guardar Lista", f"Se han guardado {total} usuarios correctamente.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Lista de usuarios cargada correctamente.")

    def salir(self):
        self.root.destroy()


# --- Ejecución principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
