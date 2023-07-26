import json


class Juego:
    def __init__(self, titulo, genero, plataforma, anio):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**juego) for juego in data]
