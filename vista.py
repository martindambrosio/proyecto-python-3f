import tkinter as tk
from tkinter import ttk, messagebox
from modelo.consultas_dao import listar_alumnos, guardar_alumno, editar_alumno, borrar_alumno, Alumno

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1200, height=800)
        self.root = root
        self.id_alumno = None
        self.pack()

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.crear_tabla()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido = tk.Label(self, text="Apellido:")
        self.label_apellido.config(font=('Arial', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)

        self.label_mail = tk.Label(self, text="Mail:")
        self.label_mail.config(font=('Arial', 12, 'bold'))
        self.label_mail.grid(row=2, column=0, padx=10, pady=10)

        self.label_direccion = tk.Label(self, text="direccion:")
        self.label_direccion.config(font=('Arial', 12, 'bold'))
        self.label_direccion.grid(row=3, column=0, padx=10, pady=10)

        self.label_id_curso = tk.Label(self, text="ID del curso:")
        self.label_id_curso.config(font=('Arial', 12, 'bold'))
        self.label_id_curso.grid(row=4, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.apellido)
        self.entry_apellido.config(width=50)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        self.mail = tk.StringVar()
        self.entry_mail = tk.Entry(self, textvariable=self.mail)
        self.entry_mail.config(width=50)
        self.entry_mail.grid(row=2, column=1, padx=10, pady=10)

        self.direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.direccion)
        self.entry_direccion.config(width=50)
        self.entry_direccion.grid(row=3, column=1, padx=10, pady=10)
        
        self.id_curso = tk.StringVar()
        self.entry_id_curso = tk.Entry(self, textvariable=self.id_curso)
        self.entry_id_curso.config(width=50)
        self.entry_id_curso.grid(row=4, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10)

    def guardar_campos(self):
        alumno = Alumno(
            nombre=self.nombre.get(),
            apellido=self.apellido.get(),
            mail=self.mail.get(),
            direccion=self.direccion.get(),
            idCurso=int(self.id_curso.get())
        )

        try:
            if self.id_alumno is None:
                guardar_alumno(alumno)
            else:
                editar_alumno(alumno, self.id_alumno)
            self.bloquear_campos()
            self.mostrar_tabla()
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_mail.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_id_curso.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_id_curso.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.apellido.set('')
        self.mail.set('')
        self.direccion.set('')
        self.id_curso.set('')
        self.id_alumno = None

    def crear_tabla(self):
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Apellido', 'Mail','Direccion', 'ID Curso', 'Curso', 'Turno'))
        self.tabla.grid(row=6, column=0, columnspan=8, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=8, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='Mail')
        self.tabla.heading('#4', text='Direccion')
        self.tabla.heading('#5', text='ID Curso')
        self.tabla.heading('#6', text='Curso')
        self.tabla.heading('#7', text='Turno')

    def mostrar_tabla(self):
        self.lista_a = listar_alumnos()
        self.tabla.delete(*self.tabla.get_children())

        for a in self.lista_a:
            self.tabla.insert('', 'end', text=a['id'], values=(a['nombre'], a['apellido'], a['mail'], a['direccion'], a['idCurso'], a['curso'], a['turno']))


def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)

    # Menú principal
    barra.add_cascade(label='Inicio', menu=menu_inicio)
    barra.add_cascade(label='Consultas', menu=menu_inicio)
    barra.add_cascade(label='Acerca de..', menu=menu_inicio2)
    barra.add_cascade(label='Ayuda', menu=menu_inicio2)

    # Submenú
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    # Submenú ayuda
    menu_inicio2.add_command(label='Contactanos')
    menu_inicio2.add_command(label='Documentación')
    menu_inicio2.add_command(label='Ayuda en línea')

# Crear y ejecutar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Gestión de Alumnos')

    barrita_menu(root)
    app = Frame(root=root)
    app.mainloop()
