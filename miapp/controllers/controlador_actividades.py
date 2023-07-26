class ControladorActividades:
    def __init__(self, app, modelo_actividad):
        self.app = app
        self.modelo_actividad = modelo_actividad  #aca paso la lista de objetos de todas las actividades


    def regresar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def obtener_actividades(self, destino):
    	return self.modelo_actividad  #devuelvo la lista de actividades como objetos

    def obtener_actividades_destino(self, indice):
        actividades_por_destino = []
        for actividad in self.modelo_actividad: #modelo_actividad tiene la lista de todas las actividades 
            if actividad.destino_id == indice:
                actividades_por_destino.append(actividad)
        return actividades_por_destino	

