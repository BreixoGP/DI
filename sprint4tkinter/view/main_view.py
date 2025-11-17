import customtkinter as ctk

class MainView(ctk.CTkFrame):

    def __init__(self,master):
        super().__init__(master)
        self.grid(sticky="nsew")
        #expandirse y ocupar todo el root
        self.pack(expand=True, fill="both")
        #Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        #lista de usuarios
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #detalle usuario
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        #labels
        self.label_nombre = ctk.CTkLabel(self.frame, text="Nombre: ")
        self.label_nombre.pack(anchor="w", pady=5)

        self.label_edad = ctk.CTkLabel(self.frame, text="Edad: ")
        self.label_edad.pack(anchor="w", pady=5)

        self.label_genero = ctk.CTkLabel(self.frame, text="Género: ")
        self.label_genero.pack(anchor="w", pady=5)

        self.label_avatar = ctk.CTkLabel(self.frame, text="Avatar: ")
        self.label_avatar.pack(anchor="w", pady=5)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        # Crear botones dinámicamente
        for i, usuario in enumerate(usuarios):
            boton = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            boton.pack(fill="x", padx=5, pady=3)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
        self.label_avatar.configure(text=f"Avatar: {usuario.avatar}")
