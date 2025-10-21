import tkinter as tk
def actualizar():
    aficiones = []
    if leer.get():
        aficiones.append("Leer")
    if deporte.get():
        aficiones.append("Deporte")
    if musica.get():
        aficiones.append("Música")

    if aficiones:
        texto = "Aficiones seleccionadas: " + ", ".join(aficiones)
    else:
        texto = "Seleccione sus aficiones"

    resultado.config(text=texto)

root = tk.Tk()
root.title("ejercicio 4")
root.geometry("300x300")

leer = tk.IntVar()
deporte = tk.IntVar()
musica = tk.IntVar()

resultado=tk.Label(root, text="Seleccione sus aficiones")
resultado.pack(pady=10)

checkButton1 = tk.Checkbutton(root, text="Leer",variable=leer,command=actualizar)
checkButton1.pack(pady=10)
checkButton2 = tk.Checkbutton(root, text="Deporte",variable=deporte,command=actualizar)
checkButton2.pack(pady=10)
checkButton3 = tk.Checkbutton(root, text="Música",variable=musica,command=actualizar)
checkButton3.pack(pady=10)





root.mainloop()





