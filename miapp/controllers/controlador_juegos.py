class ControladorJuegos:
    def __init__(self, app, modelo_juego):
        self.app = app
        self.modelo_juego = modelo_juego

    def obtener_juegos(self):
        return self.modelo_juego

    def seleccionar_juego(self):
        """
        Obtiene el índice del juego seleccionado y llama a la vista de
        información para mostrar la información del juego.
        """
        indice = self.app.vista_juegos.obtener_juego_seleccionado()
        if indice is not None:
            juego = self.modelo_juego[indice]
            self.app.vista_info.mostrar_info_juego(juego)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
