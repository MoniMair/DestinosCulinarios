import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un juego.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.juego_label = tk.Label(self, text="")
        self.juego_label.pack(pady=50)
        self.juego_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de juegos",
            command=self.controlador.regresar_juegos,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_info_juego(self, juego):
        """
        Muestra la información del juego recibido como parámetro.
        """
        info = f"Título: {juego.titulo}\nGénero: {juego.genero}\nPlataforma: {juego.plataforma}\nAño: {juego.anio}"
        self.juego_label["text"] = info
