import tkinter as tk
from models.juego import Juego
from models.destino import Destino
from models.actividad import Actividad
from views.vista_inicio import VistaInicio
from views.vista_juegos import VistaJuegos
from views.vista_destinos import VistaDestinos
from views.vista_info import VistaInfo
from views.vista_actividades import VistaActividades
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_juegos import ControladorJuegos
from controllers.controlador_destinos import ControladorDestinos
from controllers.controlador_info import ControladorInfo
from controllers.controlador_actividades import ControladorActividades


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Aplicación de Actividades en Destinos")
        self.geometry("330x300")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        juegos = Juego.cargar_de_json("data/juegos.json")
        destinos = Destino.cargar_de_json("data/destinos.json")
        actividades = Actividad.cargar_de_json("data/actividades.json")

        controlador_inicio = ControladorInicio(self)
        controlador_juegos = ControladorJuegos(self, juegos)
        controlador_destinos = ControladorDestinos(self, destinos)
        controlador_info = ControladorInfo(self)
        controlador_actividades = ControladorActividades(self, actividades)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_juegos = VistaJuegos(self, controlador_juegos)
        self.vista_destinos = VistaDestinos(self, controlador_destinos)
        self.vista_info = VistaInfo(self, controlador_info)
        self.vista_actividades = VistaActividades(self, controlador_actividades)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_juegos)
        self.ajustar_frame(self.vista_destinos)
        self.ajustar_frame(self.vista_info)
        self.ajustar_frame(self.vista_actividades)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
