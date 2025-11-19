from model.usuario_model import Usuario


class GestorUsuarios:

    def __init__(self,):
        self._usuarios = []  # Lista interna donde guardamos objetos Usuario
        self._cargar_datos_de_ejemplo()  # Cargamos usuarios de prueba

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