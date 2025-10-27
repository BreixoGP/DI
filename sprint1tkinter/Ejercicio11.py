import tkinter as tk
def actualizar_valor(val):
    label.config(text=f"Valor: {val}")
root=tk.Tk()
root.geometry("300x200")
root.title("Ejercicio 11")
scale=tk.Scale(root,from_=0, to=100,orient='horizontal',command=actualizar_valor)
scale.pack(pady=20)
label=tk.Label(root,text="Valor: 0")
label.pack(pady=10)
root.mainloop()