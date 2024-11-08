from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Aprendiendo Tkinter"
        self.icon = "images/free-30-instagram-stories-icons53_122600.ico"
        self.size = "770x470"
        self.resizable = False
        
    def cargar(self):
        # Crearemos la ventana principal.
        ventana = Tk()  # El objeto TK() es el que nos permite crear la ventana.
        self.ventana = ventana

        # Título de la ventana
        ventana.title(self.title)

        # Icono de la ventana
        ventana.iconbitmap(self.icon)

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        # Añadir un texto a la ventana
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar y ejecutar el programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("Soy un texto")
programa.addTexto("Bienvenidos")
programa.addTexto("Aprendiendo Tkinter")
programa.addTexto("Con Python")
programa.addTexto("Nunca pares de aprender")
programa.mostrar()
