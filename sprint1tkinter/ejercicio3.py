import  tkinter as tk
def saludar():
    etiquetaSaludo.config(text=f"Hola mr {entrada.get()}")

root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x300")

etiquetaMensaje = tk.Label(root, text="Introduce tu nombre")
etiquetaMensaje.pack(pady=10)

entrada=tk.Entry(root)
entrada.pack(pady=5)

etiquetaSaludo = tk.Label(root, text="Introduce tu saludo")
etiquetaSaludo.pack(pady=10)

botonSaludo = tk.Button(root, text="Saludar", command=saludar)
botonSaludo.pack(pady=10)

root.mainloop()