import customtkinter as ctk

from model.GestorUsuarios import GestorUsuarios
from view.main_view import MainView, AddUserView


class AppController:
    def __init__(self,root):
        self.root=root
        self.model = GestorUsuarios()
        self.view = MainView(root)
        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios,self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario_seleccionado = self.model.listar()[indice]
        self.view.mostrar_detalles_usuario(usuario_seleccionado)
    def abrir_ventana_añadir(self):
        # Snippet para controller/app_controller.py en abrir_ventana_añadir
        add_view = AddUserView(self.master)
        # Le decimos al botón "Guardar": "Cuando te pulsen, llama a 'añadir_usuario'
        # del controlador y pásale una referencia a ti misma (add_view)".
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))
    def añadir_usuario(self, add_view):
        add_view.get_data()