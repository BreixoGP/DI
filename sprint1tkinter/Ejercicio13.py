import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 30
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="green", outline="black")

def limpiar_canvas(event):
    if event.char.lower() == "c":
        canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio13")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", dibujar_circulo)

root.bind("<Key>", limpiar_canvas)

root.mainloop()
