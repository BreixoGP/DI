import tkinter as tk
def crearCuadrado():
    canvas.create_rectangle(int(x.get()), int(y.get()),int(x2.get()) , int(y2.get()), fill="red")
def crearCirculo():
    canvas.create_oval(int(x.get()), int(y.get()),int(x2.get()) , int(y2.get()), fill="green")


root=tk.Tk()
root.geometry("600x700")

canvas=tk.Canvas(root, width=400, height=400,bg="white")
canvas.pack(padx=10)
etiqueta=tk.Label(text="Introduce cordenadas en pixel para dibujar")
etiqueta.pack(pady=10)
#entradas
x=tk.Entry(root)
x.pack(pady=5)
y=tk.Entry(root)
y.pack(pady=5)
x2=tk.Entry(root)
x2.pack(pady=5)
y2=tk.Entry(root)
y2.pack(pady=5)
botonRectangulo=tk.Button(root, text="Rectangulo", command=crearCuadrado)
botonRectangulo.pack(pady=5)
botonCirculo=tk.Button(root, text="Circulo",command=crearCirculo)
botonCirculo.pack(pady=5)

#figuras geometricas


root.mainloop()