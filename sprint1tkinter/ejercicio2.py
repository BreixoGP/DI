import  tkinter as tk
def mostrar_mensaje():
    etiqueta.config(text="Que divertido tkinter")

root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("300x150")

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=20)

boton_mensaje = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)


root.mainloop()