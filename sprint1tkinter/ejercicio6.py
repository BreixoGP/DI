import tkinter as tk
def seleccionar():
    seleccion=listbox.curselection()
    elementos=[listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Seleccionaste: {','.join(elementos)}")

root = tk.Tk()
root.geometry("300x300")

lista=["Manzana","Banana","Naranja"]

listbox=tk.Listbox(root)
for item in lista:
    listbox.insert(tk.END, item)
listbox.pack(padx=10)

boton=tk.Button(root, text="Mostrar", command=seleccionar)
boton.pack(padx=10)
etiqueta=tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack(padx=10)
etiqueta.pack(padx=10)

root.mainloop()