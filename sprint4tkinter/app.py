# app.py (Arranque mínimo)
import customtkinter as ctk

import model
import view
from controller.app_controller import AppController

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Registro de Usuarios (CTk + MVC)")
    app.geometry("800x500")


    controller = AppController(app) # El controlador inicia todo lo demás
    app.mainloop()