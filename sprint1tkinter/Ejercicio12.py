import tkinter as tk
from tkinter import ttk, messagebox


def añadir_usuario():
    nombre = entry_nombre.get().strip()
    edad = int(scale_edad.get())
    genero = genero_var.get()

    if not nombre:
        messagebox.showwarning("Error", "El nombre no puede estar vacío.")
        return

    usuario = f"{nombre} - {edad} años - {genero}"
    listbox.insert(tk.END, usuario)
    entry_nombre.delete(0, tk.END)
    genero_var.set("Otro")
    scale_edad.set(0)

def eliminar_usuario():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione un usuario para eliminar.")
        return
    listbox.delete(seleccion)
def guardar_lista():
    total = listbox.size()
    messagebox.showinfo("Guardar Lista", f"Se han guardado {total} usuarios correctamente.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Lista de usuarios cargada correctamente.")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Ejercicio12")
root.geometry("500x600")



# Menú


menubar = tk.Menu(root)
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=menubar)

# Frame del formulario

frame_form = tk.LabelFrame(root, text="Datos del Usuario", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=10)

# Nombre
tk.Label(frame_form, text="Nombre:").pack(anchor="w")
entry_nombre = tk.Entry(frame_form, width=30)
entry_nombre.pack(fill="x", pady=5)

# Edad
label_edad=tk.Label(frame_form, text="Edad:").pack(anchor="w")
scale_edad = tk.Scale(frame_form, from_=0, to=100, orient="horizontal")
scale_edad.pack(fill="x", pady=5)

# Género
tk.Label(frame_form, text="Género:").pack(anchor="w", pady=(5,0))
genero_var = tk.StringVar(value="Otro")

frame_genero = tk.Frame(frame_form)
frame_genero.pack(pady=5, anchor="w")

ttk.Radiobutton(frame_genero, text="Masculino", variable=genero_var, value="Masculino").pack(side="left", padx=5)
ttk.Radiobutton(frame_genero, text="Femenino", variable=genero_var, value="Femenino").pack(side="left", padx=5)
ttk.Radiobutton(frame_genero, text="Otro", variable=genero_var, value="Otro").pack(side="left", padx=5)

# Lista de usuarios

frame_lista = tk.LabelFrame(root, text="Usuarios Registrados", padx=5, pady=5)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
listbox.pack(fill="both", expand=True)

scrollbar.config(command=listbox.yview)

# Botones inferiores

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="Añadir", command=añadir_usuario).pack(side="left", padx=10)
ttk.Button(frame_botones, text="Eliminar", command=eliminar_usuario).pack(side="left", padx=10)
ttk.Button(frame_botones, text="Salir", command=salir).pack(side="left", padx=10)


root.mainloop()
