# Tkinter
# Es un módulo para crear interfaces gráficas de usuario.

# Haremos from tkinter import * para importar todo el módulo.
from tkinter import *

# Crearemos la ventana principal.

ventana = Tk() # El objeto TK() es el que nos permite crear la ventana.

# Título de la ventana
ventana.title("Interfaz gráfica con Python y Tkinter")

# Icono de la ventana
ventana.iconbitmap("images/free-30-instagram-stories-icons53_122600.ico")

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana
ventana.resizable(0,0)

# Arrancar y mostrar la venana hasta que se cierre

ventana.mainloop()