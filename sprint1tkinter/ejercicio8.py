import tkinter as tk
def changelabel():
    label2.config(text=str(entry.get()))
def eraselabel():
    label2.config(text="")

root=tk.Tk()
root.geometry("400x400")

label=tk.Label(root,text="Buenos dias Mr...")
label.pack(pady=10)
label2=tk.Label(root,text="XXXXXXX")
label2.pack(pady=10)
entry=tk.Entry(root)
entry.pack(pady=10)

frame=tk.Frame(root,bg="white")
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
boton1=tk.Button(frame,text="Saludar",command=changelabel)
boton1.pack(pady=10)
boton2=tk.Button(frame,text="Borrar",command=eraselabel)
boton2.pack(pady=10)



root.mainloop()
