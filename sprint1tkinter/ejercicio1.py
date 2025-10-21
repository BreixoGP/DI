import tkinter as tk

# Función que cambia el texto de la tercera etiqueta
def cambiar_texto():
    etiqueta3.config(text="Texto cambiado")

ventana = tk.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("300x200")

etiqueta1 = tk.Label(ventana, text="Bienvenid@!")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(ventana, text="Breixo Gonzalez Pena")
etiqueta2.pack(pady=10)

etiqueta3 = tk.Label(ventana, text="Texto original")
etiqueta3.pack(pady=10)

boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()