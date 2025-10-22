import tkinter as tk
def cambiarColor():
    root.config(bg=color.get())

root = tk.Tk()
root.geometry("300x300")
root.title("Ejercicio 5")

color=tk.StringVar()
color.set("Rojo")

radio_1=tk.Radiobutton(root,text="Rojo",variable=color,value="red",command=cambiarColor)
radio_1.pack(pady=10)

radio_2=tk.Radiobutton(root,text="Verde",variable=color,value="green",command=cambiarColor)
radio_2.pack(pady=10)

radio_3=tk.Radiobutton(root,text="Azul",variable=color,value="blue",command=cambiarColor)
radio_3.pack(pady=10)




root.mainloop()