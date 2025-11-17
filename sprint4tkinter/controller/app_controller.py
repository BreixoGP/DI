import customtkinter as ctk

from model.GestorUsuarios import GestorUsuarios
from view.main_view import MainView


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