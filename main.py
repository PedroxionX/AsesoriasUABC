import customtkinter as ctk
import tkcalendar.calendar_
from utils.colorsHex import *  # Colores utilizados dentro de la carpeta "utils"
from tkinter import messagebox, PhotoImage
import tkcalendar
from datetime import datetime
import sqlite3
import tkinter as tk

ctk.set_appearance_mode("system")

class mainApp(ctk.CTk):
    # Inicializacion
    def __init__(self):
        """ = = = Configuracion de la ventana = = = """
        super().__init__()
        self.geometry("1100x700")  # Tamaño de la ventana
        self.title("Asesorias UABC")
        icon = PhotoImage(file="ico/ico.png")
        self.iconphoto(False, icon)  # Establecer el icono de la ventana
        
        """ = = = Inicio de widgets = = = """
        # Frame principal de login
        self.loginFrame = ctk.CTkFrame(self)
        self.loginFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        
        # Label "Inicio sesion"
        self.labelLogIn = ctk.CTkLabel(self.loginFrame, 
                                        text="Inicio de sesion",
                                        font=('Arial', 24, 'bold'))
        self.labelLogIn.pack(pady=20)

        # Labels "Matricula:", "Contraseña:" y sus respectivos Entry
        self.labelUser = ctk.CTkLabel(self.loginFrame, 
                                       text="Matricula:",
                                       font=('Arial', 15, 'bold'))
        self.labelUser.pack(pady=10)
        self.entryUser = ctk.CTkEntry(self.loginFrame)
        self.entryUser.pack(pady=10)

        self.labelPassword = ctk.CTkLabel(self.loginFrame, 
                                           text="Contraseña:",
                                           font=('Arial', 15, 'bold'))
        self.labelPassword.pack(pady=10)
        self.entryPassword = ctk.CTkEntry(self.loginFrame,
                                           show="*")
        self.entryPassword.pack(pady=10)

        # Botones "Iniciar sesion" y "registrar"
        self.buttonLogIn = ctk.CTkButton(self.loginFrame, text="Iniciar sesion",
                                          font=('Arial', 15, 'bold'),
                                          fg_color=pbGreen1,
                                          hover_color=pbGreen2,
                                          command=lambda: self.logIn(self.entryUser.get(), self.entryPassword.get()))
        self.buttonLogIn.pack(pady=(10, 50))

        self.labelPassword = ctk.CTkLabel(self.loginFrame, text="Si aún no estás registrado:",
                                           font=('Arial', 15, 'bold'))
        self.labelPassword.pack(pady=10)

        self.buttonRegister = ctk.CTkButton(self.loginFrame,text="Registrar",
                                             font=('Arial', 15, 'bold'),
                                             fg_color=pbRed1,
                                             hover_color=pbRed2,
                                             command=self.signUp)
        self.buttonRegister.pack(pady=10)

        # Configuración de las filas y columnas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.loginFrame.grid_rowconfigure(0, weight=1)
        self.loginFrame.grid_columnconfigure(0, weight=1)
    # SignUp
    def signUp(self):
        print("Se presionó el botón de registrar usuario")
        self.loginFrame.grid_forget()  # Ocultar el frame de login
        
        # Frame principal de signUp
        self.signUpFrame = ctk.CTkFrame(self)
        self.signUpFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        
        # Label de arriba
        self.signUpLabel = ctk.CTkLabel(self.signUpFrame,
                                        text="Registrar usuario",
                                        font=("Arial", 25, "bold"))
        self.signUpLabel.pack(pady=20)

        """ = = = Frame con los datos a ingresar para completar el registro = = = """
        # Frame interno para ingresar los datos
        dataFrame = ctk.CTkFrame(self.signUpFrame)
        dataFrame.pack(pady=20, expand=True)

        # Nombre
        nameFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        nameFrame.pack(pady=5)
        self.nameLabel = ctk.CTkLabel(nameFrame, 
                                       text="Nombre:",
                                       font=("Arial", 15, "bold"))
        self.nameEntry = ctk.CTkEntry(nameFrame)

        self.nameLabel.pack(side="left", padx=10, pady=5)
        self.nameEntry.pack(side="right", padx=10, pady=5)

        # Apellido
        lastNameFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        lastNameFrame.pack(pady=10)
        self.lastNameLabel = ctk.CTkLabel(lastNameFrame,
                                           text="Apellido:",
                                           font=("Arial", 15, "bold"))
        self.lastNameEntry = ctk.CTkEntry(lastNameFrame)

        self.lastNameLabel.pack(side="left", padx=10, pady=5)
        self.lastNameEntry.pack(side="left", padx=10, pady=5)

        # id
        idFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        idFrame.pack(pady=10)
        self.idLabel = ctk.CTkLabel(idFrame,
                                     text="Matricula:",
                                     font=("Arial", 15, "bold"))
        self.idEntry = ctk.CTkEntry(idFrame)

        self.idLabel.pack(side="left", padx=10, pady=5)
        self.idEntry.pack(side="left", padx=10, pady=5)

        # email
        emailFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        emailFrame.pack(pady=10)
        self.emailLabel = ctk.CTkLabel(emailFrame,
                                        text="e-mail:",
                                        font=("Arial", 15, "bold"))
        self.emailEntry = ctk.CTkEntry(emailFrame)

        self.emailLabel.pack(side="left", padx=10, pady=5)
        self.emailEntry.pack(side="left", padx=10, pady=5)

        # Password
        passwordFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        passwordFrame.pack(pady=10)
        self.passwordLabel = ctk.CTkLabel(passwordFrame,
                                           text="Contraseña:",
                                           font=("Arial", 15, "bold"))
        self.passwordEntry = ctk.CTkEntry(passwordFrame, show="*")

        self.passwordLabel.pack(side="left", padx=10, pady=5)
        self.passwordEntry.pack(side="left", padx=10, pady=5)

        # Tipo de cuenta
        usertypesList = ["Alumno", "Maestro"]  # lista de roles disponibles
        typeuserFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        typeuserFrame.pack(pady=10)
        self.typeuserLabel = ctk.CTkLabel(typeuserFrame,
                                           text="Tipo de cuenta:",
                                           font=("Arial", 15, "bold"))
        self.typeuserCombobox = ctk.CTkComboBox(typeuserFrame,
                                                 state="readonly",
                                                 values=usertypesList)

        self.typeuserLabel.pack(side="left", padx=10, pady=5)
        self.typeuserCombobox.pack(side="left", padx=10, pady=5)

        # Botones registrar y volver
        buttonsFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        buttonsFrame.pack(pady=10)
        
        self.RegisterButton = ctk.CTkButton(buttonsFrame,
                                             text="Registrar",
                                             font=("Arial", 12, "bold"),
                                             command=lambda: self.registerUser(self.idEntry.get(), 
                                                                                self.passwordEntry.get(), 
                                                                                self.typeuserCombobox.get(), 
                                                                                self.nameEntry.get(), 
                                                                                self.lastNameEntry.get(), 
                                                                                self.emailEntry.get()))

        self.goBackButton = ctk.CTkButton(buttonsFrame,
                                           text="Volver",
                                           font=("Arial", 12, "bold"),
                                           fg_color=pbRed1,
                                           hover_color=pbRed2,
                                           command=self.goBack)
        self.RegisterButton.pack(side="left", padx=10, pady=5)
        self.goBackButton.pack(side="left", padx=10, pady=5)
    # Función del botón para registrar
    def registerUser(self, id, password, typeuser, name, lastname, email):
        print("Se presionó el botón de registrar usuario")
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
            existing_user = cursor.fetchone()

            if existing_user is None:
                print("No se encontró otro usuario con esa matrícula, se podrá agregar.")
                cursor.execute("INSERT INTO users (id, password, typeuser, name, lastname, email) VALUES (?, ?, ?, ?, ?, ?)", 
                               (id, password, typeuser, name, lastname, email))

                if cursor.rowcount > 0:
                    print("Usuario registrado exitosamente.")
                    messagebox.showinfo(title="Asesorias UABC", message="Usuario registrado con éxito")
                else:
                    print("Error al registrar usuario.")
                    messagebox.showinfo(title="Asesorias UABC", message="Error al registrar usuario")
            else:
                print("Ya existe un usuario con esa matrícula.")
                messagebox.showinfo(title="Asesorias UABC", message="Ya existe un usuario con esa matrícula. Por favor ingresa otra.")
    # LogIn
    def logIn(self, id, password):
        print("Se presionó el botón para hacer un inicio de sesión")
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT name, lastname FROM users WHERE id = ? AND password = ?", (id, password))
            usuario = cursor.fetchone()
            if usuario:
                name, lastname = usuario
                print("Usuario encontrado. Acceso concedido.")
                messagebox.showinfo(title="Asesorias UABC", message=f"Bienvenido {name} {lastname}")
                self.loginFrame.grid_forget()  # Ocultar el frame de login
                self.indexWindowAlumn(id)  # Llamar a la función para mostrar la ventana de índice
                return True
            else:
                print("Usuario o contraseña incorrectos.")
                messagebox.showinfo(title="Asesorias UABC", message="Usuario o contraseña incorrectos")
                return False
    # Función del botón para volver a la pantalla anterior
    def goBack(self):
        print("Botón de volver presionado")
        self.signUpFrame.grid_forget()
        self.loginFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        self.update_idletasks()
    # Pagina principal
    def indexWindowAlumn(self, id):
        print("Ventana de indice para el alumno")
        print(id)
        # Crear el nuevo frame de índice
        self.indexFrame = ctk.CTkFrame(self)
        self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        
        # Botón para agendar cita dentro del indexFrame
        self.scheduleAppointmentButton = ctk.CTkLabel(self.indexFrame,
                                                    text="Universidad Autonoma de Baja California - Sistema de asesorias",
                                                    font=('Arial', 30, 'bold'),
                                                    text_color='white',
                                                    fg_color='transparent')
        self.scheduleAppointmentButton.pack(pady=100)
        self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                    text="Agendar asesoria",
                                                    font=('Arial', 15, 'bold'),
                                                    fg_color=pbGreen1,
                                                    hover_color=pbGreen2,
                                                    command= lambda: self.scheduleAppointmentWindow(id))
        self.scheduleAppointmentButton.pack(pady=(20, 10))
        self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                    text="Ver asesorias registradas",
                                                    font=('Arial', 15, 'bold'),
                                                    fg_color=pbGreen1,
                                                    hover_color=pbGreen2)
        self.scheduleAppointmentButton.pack(pady=(20, 10))
    
        # Actualizar la ventana para que los cambios se reflejen
        self.update_idletasks()
    # Pagina para agendar cita
    def scheduleAppointmentWindow(self, id):
        print("Se accedió a la ventana de agendar cita")
        
        # Ocultar el frame anterior
        if hasattr(self, 'indexFrame'):
            self.indexFrame.grid_forget()

        # Crear el nuevo frame de crear cita
        self.scheduleFrame = ctk.CTkFrame(self)
        self.scheduleFrame.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        self.scheduleFrame.grid_columnconfigure(0, weight=1)
        self.scheduleFrame.grid_rowconfigure(0, weight=1)

        # Frame del calendario
        self.calendarFrame = ctk.CTkFrame(self.scheduleFrame)
        self.calendarFrame.pack(padx=(50, 0), pady=(50), side="left", anchor="nw", fill='y')
        # Crear el calendario
        self.calendar = tkcalendar.Calendar(self.calendarFrame, 
                                            selectmode='day', 
                                            year=2023, 
                                            month=10, 
                                            day=4,
                                            font=("Arial", 14, "bold"),  # Cambiar tamaño de fuente
                                            borderwidth=2, 
                                            relief="solid",  # Agregar borde
                                            selectbackground=pbGreen1,  # Cambiar color de selección
                                            selectforeground="white",
                                            showothermonthdays=False,
                                            normalforeground=pbGreen1,
                                            showweeknumbers=False,
                                            headersforeground='white')  
        self.calendar.pack(pady=20, padx=20, expand=True, fill='both')

        # Configurar el callback para el evento de selección de fecha
        self.calendar.bind("<<CalendarSelected>>", self.update_selected_day)

        # Inicializar la variable StringVar
        self.selectedDayVar = ctk.StringVar()
        self.selectedDayVar.set(f"Día seleccionado: {self.calendar.get_date()}")

        # Recuperar la lista de profesores de la base de datos y en caso de que este vacia hacerselo saber al usuario
        teachersListVar = teacherList()

        if teachersListVar == []:
            teachersRegistered = False
            teachersListVar = ["No hay profesores registrados"]

        # Crear y mostrar el label con la fecha seleccionada
        self.selectedDayLabel = ctk.CTkLabel(self.scheduleFrame,
                                             textvariable=self.selectedDayVar,
                                             font=("Arial", 20, "bold"))
        self.selectedDayLabel.pack(pady=(60, 30),padx=50, anchor="nw")
        self.selectTeacherCombobox = ctk.CTkComboBox(self.scheduleFrame,
                                                     state="readonly",
                                                     values=teachersListVar)
        self.selectTeacherCombobox.pack(pady=10,padx=50, anchor="nw")
        self.textBoxLabel = ctk.CTkLabel(self.scheduleFrame,
                                         text='Escribe aqui una descripcion sobre tu asesoria:',
                                         font=("Arial", 15, "bold"))
        self.textBoxLabel.pack(pady=(30),padx=50, anchor="nw")
        self.scheduleDescriptionTextbox = ctk.CTkTextbox(self.scheduleFrame, wrap='word')
        self.scheduleDescriptionTextbox.pack(pady=0,padx=(50,50), expand=True, fill='both')
        
        self.returnToIndexWindowAlumnButton = ctk.CTkButton(self.scheduleFrame,
                                                            text="Volver",
                                                            font=('Arial',12,"bold"),
                                                            fg_color=pbRed1,
                                                            hover_color=pbRed2,
                                                            command= lambda: self.returnToIndexWindowAlumn())
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton = ctk.CTkButton(self.scheduleFrame,
                                                            text="Agendar cita",
                                                            font=('Arial',12,"bold"),
                                                            fg_color=pbGreen1,
                                                            hover_color=pbGreen2,
                                                            command=lambda: saveSchedule(id))
        self.returnToIndexWindowAlumnButton.pack(pady=50, padx=(50,10), side='left',anchor="nw", expand=True)
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton.pack(pady=50,padx=(50), side='right', expand=True, anchor='e')
        
    def returnToIndexWindowAlumn(self):
        print("Se volvio al index")
        self.scheduleFrame.grid_forget()
        self.calendarFrame.grid_forget()
        self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        # Forzar la actualización de la interfaz
        self.update_idletasks()

    def update_selected_day(self, event):
        selected_date = self.calendar.get_date()
        self.selectedDayVar.set(f"Día seleccionado: {selected_date}")
        print(f"Fecha seleccionada: {selected_date}")

def saveSchedule(idAlumn, ):
    print("Se presiono el boton de guardar cita")
    try:
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            profId = cursor.execute("SELECT * FROM users WHERE id")
            cursor.execute("INSERT INTO scheduleList (scheduleId, idAlumn, idTeacher, date) VALUES (?, ?, ?, ?)", ("", idAlumn, "", ""))
            # 
            cursor.execute("INSERT INTO scheduleList (scheduleId, idAlumn, idTeacher, date) VALUES (?, ?, ?, ?)", ("", idAlumn, "", ""))

    except sqlite3.Error as e:
        print("Error")
    
    print(id)

def teacherList():
    teachers = []
    try:
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            #Consulta SQL para seleccionar nombre y apellido de los maestros
            query = "SELECT name, lastname, id FROM users WHERE typeuser = 'Maestro'"
            cursor.execute(query)
                
            # Fetchall para obtener todos los resultados
            results = cursor.fetchall()
            # Combinar nombre y apellido en una sola cadena
            teachers = [f"{name} {lastname} - {id}" for name, lastname, id in results]
            
        print(f"Se recuperaron {len(teachers)} profesores de la base de datos")
        # Devolver la lista de nombres de maestros
        return teachers
    except sqlite3.Error as e:
        print(f"Error al recuperar los profesores de la base de datos: {e}")
        return []


app = mainApp()
app.mainloop()