import tkinter as tk


class VistaJuegos(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la lista de juegos.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.titulo = tk.Label(self, text="Lista de Juegos")
        self.titulo.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el evento de doble clic a la función seleccionar_juego
        self.listbox.bind("<Double-Button-1>", self.seleccionar_juego)

        self.listbox.pack(pady=10)
        self.actualizar_juegos()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)

    def actualizar_juegos(self):
        """
        Actualiza la lista de juegos con los juegos obtenidos del controlador.
        """
        juegos = self.controlador.obtener_juegos()
        self.listbox.delete(0, tk.END)
        for juego in juegos:
            self.listbox.insert(tk.END, juego.titulo)

    def obtener_juego_seleccionado(self):
        """
        Retorna el índice del juego seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_juego(self, event):
        """
        Obtiene el índice del juego seleccionado y llama al controlador para
        mostrar la información del juego.
        """
        self.controlador.seleccionar_juego()
