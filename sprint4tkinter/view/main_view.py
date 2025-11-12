import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Registro de usuarios")
app.geometry("800x400")  # ancho mayor para que quepan ambos paneles

# scrollable
scrollable = ctk.CTkScrollableFrame(app, label_text="Lista de usuarios")
scrollable.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

# Panel de previsualización
panel = ctk.CTkFrame(app, corner_radius=10)
panel.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

