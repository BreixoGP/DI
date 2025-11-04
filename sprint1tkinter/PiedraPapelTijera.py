import tkinter as tk
from tkinter import messagebox
import random


class PiedraPapelTijeraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        self.root.geometry("500x400")

        self.opciones = ["Piedra", "Papel", "Tijera"]
        self.jugador_puntos = tk.IntVar(value=0)
        self.maquina_puntos = tk.IntVar(value=0)
        self.mensaje = tk.StringVar(value="Haz tu elección para comenzar.")
        self.eleccion_jugador = tk.StringVar(value="-")
        self.eleccion_maquina = tk.StringVar(value="-")

        # --- INTERFAZ ---
        titulo = tk.Label(self.root, text="Piedra - Papel - Tijera")
        titulo.pack(pady=10)

        # Marcador
        marcador_frame = tk.Frame(self.root)
        marcador_frame.pack(pady=10)

        tk.Label(marcador_frame, text="Jugador:").grid(row=0, column=0, padx=10)
        tk.Label(marcador_frame, textvariable=self.jugador_puntos).grid(row=1, column=0)

        tk.Label(marcador_frame, text="Máquina:").grid(row=0, column=2, padx=10)
        tk.Label(marcador_frame, textvariable=self.maquina_puntos).grid(row=1, column=2)

        # Elecciones actuales
        estado_frame = tk.Frame(self.root)
        estado_frame.pack(pady=10)

        tk.Label(estado_frame, text="Tú elegiste:").grid(row=0, column=0, padx=20)
        tk.Label(estado_frame, textvariable=self.eleccion_jugador).grid(row=1, column=0)

        tk.Label(estado_frame, text="La máquina eligió:").grid(row=0, column=1, padx=20)
        tk.Label(estado_frame, textvariable=self.eleccion_maquina).grid(row=1, column=1)

        # Mensaje de estado
        tk.Label(self.root, textvariable=self.mensaje).pack(pady=10)

        # Botones de jugada
        botones_frame = tk.Frame(self.root)
        botones_frame.pack(pady=10)

        tk.Button(botones_frame, text="Piedra", width=10, command=lambda: self.jugar("Piedra")).pack(side="left", padx=10)
        tk.Button(botones_frame, text="Papel", width=10, command=lambda: self.jugar("Papel")).pack(side="left", padx=10)
        tk.Button(botones_frame, text="Tijera", width=10, command=lambda: self.jugar("Tijera")).pack(side="left", padx=10)

        # Botones inferiores
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)

        tk.Button(control_frame, text="Nuevo Juego", command=self.nuevo_juego).pack(side="left", padx=10)
        tk.Button(control_frame, text="Salir", command=self.root.destroy).pack(side="left", padx=10)

    def jugar(self, eleccion):
        if self.jugador_puntos.get() >= 3 or self.maquina_puntos.get() >= 3:
            messagebox.showinfo("Juego terminado", "Nuevo juego.")
            return

        maquina = random.choice(self.opciones)

        self.eleccion_jugador.set(eleccion)
        self.eleccion_maquina.set(maquina)

        resultado = self.determinar_ganador(eleccion, maquina)

        if resultado == "empate":
            self.mensaje.set(f"Empate: ambos eligieron {eleccion}.")
        elif resultado == "jugador":
            self.jugador_puntos.set(self.jugador_puntos.get() + 1)
            self.mensaje.set(f"¡Ganaste esta ronda! {eleccion} vence a {maquina}.")
        else:
            self.maquina_puntos.set(self.maquina_puntos.get() + 1)
            self.mensaje.set(f"La máquina gana esta ronda. {maquina} vence a {eleccion}.")

        # Comprobar si alguien ganó
        self.comprobar_final()

    def determinar_ganador(self, jugador, maquina):
        if jugador == maquina:
            return "empate"
        elif (jugador == "Piedra" and maquina == "Tijera") or \
             (jugador == "Papel" and maquina == "Piedra") or \
             (jugador == "Tijera" and maquina == "Papel"):
            return "jugador"
        else:
            return "maquina"

    def comprobar_final(self):
        if self.jugador_puntos.get() == 3:
            messagebox.showinfo("Victoria", "¡Has ganado la partida!")
            self.mensaje.set("¡Eres el campeón! Pulsa 'Nuevo Juego' para volver a jugar.")
        elif self.maquina_puntos.get() == 3:
            messagebox.showinfo("Derrota", "La máquina ha ganado la partida.")
            self.mensaje.set("Has perdido... Pulsa 'Nuevo Juego' para intentarlo de nuevo.")

    def nuevo_juego(self):
        self.jugador_puntos.set(0)
        self.maquina_puntos.set(0)
        self.mensaje.set("Nuevo juego iniciado")
        self.eleccion_jugador.set("-")
        self.eleccion_maquina.set("-")

# --- Ejecución principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()
