import tkinter as tk

root=tk.Tk()
root.geometry("200x100")
frame=tk.Frame(root,width=400,height=400)
frame.pack(fill=tk.BOTH,expand=True)

textframe=tk.Text(frame,wrap="none")
textframe.grid(row=0,column=0)
textframe.insert(
    "end","""La eterna discusión es cual es la mejor elección, si la tortilla de patatas con cebolla o sin cebolla, hoy vamos a preparar la versión con cebolla y con un truco genial"
          " que te voy a dar para que quede jugosa y nada seca.La tortilla de patatas teóricamente no lleva cebolla, eso dice su receta original, pero debemos de saber que las cosas van evolucionando y si la mayoría la tomamos con cebolla es porque la "
          "receta ha evolucionado y ese dulzor que le da la cebolla nos encanta.
           fsdddddddddgeggsbbfbfdbbf
           fdbfdbfdbdfbfdbfdbdfb
           fdbfdbdfbdbdbdfbfdbfdb
           fdbfdbfdbfdbfdbfdbfbdfb
           fdbfdbfdbfdbdbfdbdbdbd
           fdbdfbdbdfbdbdbdbd""")

scrollvert=tk.Scrollbar(frame,orient='vertical',command=textframe.yview)
scrollvert.grid(row=0,column=1,sticky="ns")
textframe.configure(yscrollcommand=scrollvert.set)

scrollside=tk.Scrollbar(frame,orient='horizontal',command=textframe.xview)
scrollside.grid(row=1,column=0,sticky="ew")
textframe.configure(xscrollcommand=scrollside.set)

frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)





root.mainloop()