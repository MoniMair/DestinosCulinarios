class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_juegos(self):
        self.app.cambiar_frame(self.app.vista_juegos)

    def mostrar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)        

    def mostrar_actividades(self):
        self.app.cambiar_frame(self.app.vista_actividades)    
