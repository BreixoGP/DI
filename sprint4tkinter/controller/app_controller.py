import customtkinter as ctk
from view.main_view import app, scrollable, panel

class Controller:
    def __init__(self, app, scrollable, panel):
        self.app = app
        self.scrollable = scrollable
        self.panel = panel
        self.usuarios = []

def salir(self):
        self.app.destroy()
