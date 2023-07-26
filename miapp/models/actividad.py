import json

class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio



    #transforma el objeto a formato json
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]        


    #@classmethod es un decorador q define un metodo de clase,
    #actua sobre la clase (cls por convencion), no sobre la instancia
    #en este caso recibe la clase cls y una cadeja json (datos_json)
    #el metodo de_jsoncrea una instancia de destino a partir de la cadena pasada
    #return cls crea una instancia de la clase destino usando el diccionario
    #datos como argumentos para el constructor init de la clase 
    # @classmethod
    # def de_json(cls, datos_json):
    #     datos = json.loads(datos_json)
    #     return cls(**datos)

    @staticmethod
    def cargar_actividades(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Local.de_json(json.dumps(dato)) for dato in datos]




# # Método cargar_actividades cargará los datos del archivo JSON y creará una lista de objetos Actividad
# actividades = Actividad.cargar_actividades("actividades.json")

# # Ahora podemos trabajar con la lista de actividades creada
# for actividad in actividades:
#     print(f"Nombre de la actividad: {actividad.nombre}")
#     print(f"ID del destino asociado: {actividad.destino_id}")
#     print(f"Hora de inicio: {actividad.hora_inicio}")
#     print("--------------------------")