import tkinter as tk
from tkinter.font import Font

#importar este

class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Destinos Culinarios", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=12)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Podrás ver las actividades en cada Destino Culinarios.",
            font=descripcion_font,
            wraplength=300,
        )
        self.descripcion.grid(row=1, column=0, pady=50)

        # Crea el botón para ir a juegos y lo agrega a la vista
        self.boton_destinos = tk.Button(
            self, text="Ir a los Destinos Culinarios", command=self.controlador.mostrar_destinos
        )
        self.boton_destinos.grid(row=2, column=0, pady=10)
