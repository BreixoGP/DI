import csv

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str = None):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __str__(self):
        return f"Usuario({self.nombre}, {self.edad} años, {self.genero})"

    def guardar_csv(self,ruta_archivo=None):#con none se guarda en la carpeta del proyecto
            """
            Guarda una lista de objetos Usuario en un archivo CSV.
            usuarios: lista de objetos Usuario
            ruta_archivo: path del CSV donde se guardarán los datos
            """
            # Abrimos el archivo en modo escritura
            with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)

                # Escribimos la cabecera
                escritor.writerow(["nombre", "edad", "genero", "avatar"])

                # Escribimos los datos de cada usuario
                for usuario in usuarios:
                    escritor.writerow([usuario.nombre, usuario.edad, usuario.genero, usuario.avatar])
