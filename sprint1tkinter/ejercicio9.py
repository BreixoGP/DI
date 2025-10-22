import tkinter as tk
from tkinter import messagebox

def showMsg():
    messagebox.showinfo("Acerca de", "Este texto es un largo y extenso acerca de...")

root=tk.Tk()
root.geometry("400x400")


menubar=tk.Menu(root)
root.config(menu=menubar)

menuArchivo=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="Archivo",menu=menuArchivo)
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Salir",command=root.quit)
menuAyuda=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de",command=showMsg)

root.mainloop()