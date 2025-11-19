import csv

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str = None):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __str__(self):
        return f"Usuario({self.nombre}, {self.edad} años, {self.genero})"


class GestorUsuarios:

    def __init__(self,):
        self._usuarios = []  # Lista interna donde guardamos objetos Usuario
        #self._cargar_datos_de_ejemplo()  # Cargamos usuarios de prueba

    def _cargar_datos_de_ejemplo(self):
        """Método privado que carga 2–3 usuarios de ejemplo."""
        u1 = Usuario("Ana", 28, "F")
        u2 = Usuario("Carlos", 35, "M")
        u3 = Usuario("Lucía", 22, "F")

        self._usuarios.extend([u1, u2, u3])

    def listar(self):
        return self._usuarios

    def agregar(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def guardar_csv(self, ruta="usuarios.csv"):
        """Guarda la lista de usuarios en un archivo CSV."""
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            # Cabecera
            escritor.writerow(["nombre", "edad", "genero", "avatar"])

            # Datos
            for u in self._usuarios:
                escritor.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta="usuarios.csv"):
        """Carga usuarios desde un CSV. Limpia la lista antes."""
        self._usuarios.clear()

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)

                # Saltar cabecera
                next(lector)

                for fila in lector:
                    try:
                        nombre, edad, genero, avatar = fila
                        usuario = Usuario(nombre, int(edad), genero, avatar)
                        self._usuarios.append(usuario)
                    except Exception as e:
                        print(f"Línea corrupta ignorada: {fila} -> {e}")

        except FileNotFoundError:
            print("Archivo CSV no encontrado. Se iniciará con la lista vacía.")