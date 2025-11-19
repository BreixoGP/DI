import csv

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str = None):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __str__(self):
        return f"Usuario({self.nombre}, {self.edad} años, {self.genero})"
