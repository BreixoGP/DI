from tkinter import messagebox

import customtkinter as ctk

from model.usuario_model import Usuario
from model.usuario_model import GestorUsuarios
from view.main_view import MainView, AddUserView
from pathlib import Path

class AppController:
    def __init__(self,root):
        self.root=root
        self.model = GestorUsuarios()
        self.view = MainView(root)
        self.view.menu_archivo.add_command(label="Guardar CSV", command=self.guardar_usuarios)
        self.view.menu_archivo.add_command(label="Cargar CSV", command=self.cargar_usuarios)

        self.view.boton_añadir_usuario.configure(command=self.abrir_ventana_añadir)
        self.view.boton_salir.configure(command=root.destroy)
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"


        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios,self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario_seleccionado = self.model.listar()[indice]
        self.view.mostrar_detalles_usuario(usuario_seleccionado)

    def abrir_ventana_añadir(self):
        # Snippet para controller/app_controller.py en abrir_ventana_añadir
        add_view = AddUserView(self.root)
        # Le decimos al botón "Guardar": "Cuando te pulsen, llama a funcion 'añadir_usuario'
        # del controlador y pásale una referencia a ti misma (add_view)".
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))
        add_view.cancelar_button.configure(command=add_view.window.destroy)
    def añadir_usuario(self, add_view):
        datos=add_view.get_data()
        #validar edad
        try:
            edad = int(datos["edad"])
            if edad <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "La edad debe ser un número entero positivo.")
            return

        nuevo_usuario = Usuario(
            nombre=datos["nombre"],
            edad=edad,
            genero=datos["genero"],
            avatar=datos["avatar"]  # ruta del avatar
        )

        self.model.agregar(nuevo_usuario)
        self.refrescar_lista_usuarios()
        add_view.window.destroy()

    def guardar_usuarios(self):
        """Llama al modelo para guardar CSV."""
        try:
            self.model.guardar_csv()
            messagebox.showinfo("Éxito", "Usuarios guardados en usuarios.csv")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los usuarios.\n{e}")

    def cargar_usuarios(self):
        try:
            self.model.cargar_csv()
            self.refrescar_lista_usuarios()

            # Solo mostrar mensaje si el archivo existía
            if len(self.model.listar()) > 0:
                messagebox.showinfo("Carga completa", "Usuarios cargados desde CSV.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los usuarios.\n{e}")