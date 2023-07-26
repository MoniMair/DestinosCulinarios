import json
from models.actividad import Actividad

class Destino:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo,
                 popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
        self.actividades = []


    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]



    #actividad es un objeto
    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        

    def obtener_actividades_por_destino(self, destino_id):
        actividades_por_destino = []
        for actividad in lista_de_actividades:  # Suponiendo que tienes una lista llamada lista_de_actividades con todas las instancias de Actividad
            if actividad.destino_id == destino_id:
                actividades_por_destino.append(actividad)
        return actividades_por_destino    

