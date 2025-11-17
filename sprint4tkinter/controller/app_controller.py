import customtkinter as ctk
from view.main_view import app, scrollable, panel

class Controller:
    def __init__(self, app, scrollable, panel):
        self.app = app
        self.scrollable = scrollable
        self.panel = panel
        self.usuarios = []

    def listar_usuarios(self):
        # agrega botones dinámicos para cada usuario
        for i in self.usuarios:
            boton = ctk.CTkButton(self.scrollable, text=i, command=lambda i=i: self.seleccionar(i))
            boton.pack(padx=10, pady=5, fill="x")

    def seleccionar(self, usuario):
        # limpia panel y muestra usuario seleccionado
        for w in self.panel.winfo_children():
            w.destroy()
        label = ctk.CTkLabel(self.panel, text=f"Seleccionado: {usuario}")
        label.pack(padx=20, pady=20)

    def salir(self):
        self.app.destroy()
