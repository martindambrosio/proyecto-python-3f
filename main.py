import tkinter as tk
from cliente.vista import Frame,barrita_menu

def main(): 
    ventana = tk.Tk()
    ventana.title('Gestión de Cursos y Alumnos de Escuela de Artes CREATO')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(False,False)

    barrita_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()