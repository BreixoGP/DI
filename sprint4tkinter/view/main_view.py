import customtkinter as ctk


class MainView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.grid(sticky="nsew")
        # expandirse y ocupar todo el root
        self.pack(expand=True, fill="both")
        # Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # NUEVA FILA PARA BOTONES (respeta todo lo demás)
        self.grid_rowconfigure(1, weight=0)

        # lista de usuarios
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # detalle usuario
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # labels
        self.label_nombre = ctk.CTkLabel(self.frame, text="Nombre: ")
        self.label_nombre.pack(anchor="w", pady=5)

        self.label_edad = ctk.CTkLabel(self.frame, text="Edad: ")
        self.label_edad.pack(anchor="w", pady=5)

        self.label_genero = ctk.CTkLabel(self.frame, text="Género: ")
        self.label_genero.pack(anchor="w", pady=5)

        self.label_avatar = ctk.CTkLabel(self.frame, text="Avatar: ")
        self.label_avatar.pack(anchor="w", pady=5)

        # botones abajo
        self.boton_añadir_usuario = ctk.CTkButton(self, text="Añadir Usuario",)
        self.boton_añadir_usuario.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.boton_salir = ctk.CTkButton(self, text="Salir")
        self.boton_salir.grid(row=1, column=1, sticky="e", padx=10, pady=10)

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


class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("500x650")
        self.window.grab_set()  #Esto la hace modal

        # Entradas
        label = ctk.CTkLabel(self.window, text="Nombre:")
        label.pack(pady=10)
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.pack(pady=10, padx=10)

        label = ctk.CTkLabel(self.window, text="Edad:")
        label.pack(pady=10)

        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.pack(pady=10, padx=10)

        # GÉNERO
        self.genero_var = ctk.StringVar(value="ninguno")

        label = ctk.CTkLabel(self.window, text="Género:")
        label.pack(pady=10)

        rb_masculino = ctk.CTkRadioButton(
            self.window, text="Masculino", variable=self.genero_var, value="M"
        )
        rb_masculino.pack(pady=5)

        rb_femenino = ctk.CTkRadioButton(
            self.window, text="Femenino", variable=self.genero_var, value="F"
        )
        rb_femenino.pack(pady=5)

        rb_otro = ctk.CTkRadioButton(
            self.window, text="Otro", variable=self.genero_var, value="O"
        )
        rb_otro.pack(pady=5)

        # AVATAR
        self.avatar_var = ctk.StringVar(value="ninguno")

        label = ctk.CTkLabel(self.window, text="Avatar:")
        label.pack(pady=10)

        avatar1 = ctk.CTkRadioButton(
            self.window, text="Avatar1", variable=self.avatar_var, value="C:\\Users\\Breixo\\manual-git\\sprint4tkinter\\assets\\avatar1.png"
        )
        avatar1.pack(pady=5)

        avatar2 = ctk.CTkRadioButton(
            self.window, text="Avatar2", variable=self.avatar_var, value="C:\\Users\\Breixo\\manual-git\\sprint4tkinter\\assets\\avatar2.png"
        )
        avatar2.pack(pady=5)

        avatar3 = ctk.CTkRadioButton(
            self.window, text="Avatar3", variable=self.avatar_var, value="C:\\Users\\Breixo\\manual-git\\sprint4tkinter\\assets\\avatar3.png"
        )
        avatar3.pack(pady=5)

        # Botones
        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(pady=10)

        self.cancelar_button = ctk.CTkButton(self.window, text="Cancelar")
        self.cancelar_button.pack(pady=10)

    def get_data(self):
        """Recoge los valores del formulario y los devuelve en un diccionario"""
        datos = {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get(),
        }
        return datos
