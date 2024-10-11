import customtkinter as ctk
import tkcalendar.calendar_
from utils.colorsHex import *  # Colores utilizados dentro de la carpeta "utils"
from tkinter import messagebox, PhotoImage
import tkcalendar
from datetime import datetime
import sqlite3
from CTkListbox import *

ctk.set_appearance_mode("dark")

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
            cursor.execute("SELECT name, lastname, typeuser FROM users WHERE id = ? AND password = ?", (id, password))
            usuario = cursor.fetchone()
            if usuario:
                name, lastname, typeuser = usuario
                print("Usuario encontrado. Acceso concedido.")
                messagebox.showinfo(title="Asesorias UABC", message=f"Bienvenido {name} {lastname}")
                self.loginFrame.grid_forget()  # Ocultar el frame de login
                self.indexWindow(id)  # Llamar a la función para mostrar la ventana de índice
                return True
            else:
                print("Usuario o contraseña incorrectos.")
                messagebox.showinfo(title="Asesorias UABC", message="Usuario o contraseña incorrectos")
                return False
    
    # Función del botón para volver a la pantalla anterior (del registro al login)
    def goBack(self):
        print("Botón de volver presionado")
        self.signUpFrame.grid_forget()
        self.loginFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        self.update_idletasks()
    
    # Pagina principal
    def indexWindow(self, id):
        print("Ventana de indice para el alumno")
        print(id)
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT typeuser FROM users WHERE id = ?", (id,))
            typeuser = cursor.fetchone()[0] # El [0] es para que acceda solo a la tupla e imprima unicamente la palabra del tipo de usuario
            print(typeuser)
        # Crear el nuevo frame de índice
        self.indexFrame = ctk.CTkFrame(self)
        self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew") 
        
        self.scheduleAppointmentButton = ctk.CTkLabel(self.indexFrame,
                                                        text="Universidad Autonoma de Baja California - Sistema de asesorias",
                                                        font=('Arial', 30, 'bold'),
                                                        text_color='white',
                                                        fg_color='transparent')
        self.scheduleAppointmentButton.pack(pady=100)
         # Botón para agendar cita dentro del indexFrame
        if typeuser == "Alumno":
            print("Se mostro en pantalla el objeto boton para registrar asesoria para alumnos")
            self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                        text="Agendar asesoria",
                                                        font=('Arial', 15, 'bold'),
                                                        fg_color=pbGreen1,
                                                        hover_color=pbGreen2,
                                                        command= lambda: self.scheduleAppointmentWindow(id))
            self.scheduleAppointmentButton.pack(pady=(20, 10))
        if typeuser == "Maestro":
            print("Se mostro en pantalla el objeto boton para escoger materias para maestros")
            self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                        text="Activar materias",
                                                        font=('Arial', 15, 'bold'),
                                                        fg_color=pbGreen1,
                                                        hover_color=pbGreen2,
                                                        command= lambda: self.selectSubjects())
            self.scheduleAppointmentButton.pack(pady=(20, 10))

        self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                    text="Ver asesorias registradas",
                                                    font=('Arial', 15, 'bold'),
                                                    fg_color=pbGreen1,
                                                    hover_color=pbGreen2,
                                                    command=lambda: self.viewAppointments(id, typeuser))
        self.scheduleAppointmentButton.pack(pady=(20, 10))
    
        # Actualizar la ventana para que los cambios se reflejen
        self.update_idletasks()
    
    # Pagina para agendar cita
    def scheduleAppointmentWindow(self, id):
        print("Se accedio a la ventana de agendar cita")
        
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
        
        self.returnToindexWindowButton = ctk.CTkButton(self.scheduleFrame,
                                                            text="Volver",
                                                            font=('Arial',12,"bold"),
                                                            fg_color=pbRed1,
                                                            hover_color=pbRed2,
                                                            command= lambda: self.returnToindexWindow())
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton = ctk.CTkButton(self.scheduleFrame,
                                                            text="Agendar cita",
                                                            font=('Arial',12,"bold"),
                                                            fg_color=pbGreen1,
                                                            hover_color=pbGreen2,
                                                            command=lambda: saveSchedule(id, 
                                                                                         self.selectTeacherCombobox.get(), 
                                                                                         self.calendar.get_date(), 
                                                                                         self.scheduleDescriptionTextbox.get("1.0", "end")))
        self.returnToindexWindowButton.pack(pady=50, padx=(50,10), side='left',anchor="nw", expand=True)
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton.pack(pady=50,padx=(50), side='right', expand=True, anchor='e')

    def returnToindexWindow(self):
        print("Se volvio al index")
        self.scheduleFrame.grid_forget()
        self.calendarFrame.grid_forget()
        self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        # Forzar la actualización de la interfaz
        self.update_idletasks()

    def update_selected_day(self, event=None):
        selected_date = self.calendar.get_date()
        self.selectedDayVar.set(f"Día seleccionado: {selected_date}")
        print(f"Fecha seleccionada: {selected_date}")

    def viewAppointments(self, id, typeuser):
        print("Se presiono el boton de ver asesorias pendientes")
        self.indexFrame.grid_forget()
        #
        self.viewAppointmentsFrame = ctk.CTkFrame(self)
        self.viewAppointmentsFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        self.viewAppointmentsLabel = ctk.CTkLabel(self.viewAppointmentsFrame,
                                                  text=f"Citas registradas de {id}",
                                                  font=("Arial",20,"bold"))
        self.viewAppointmentsLabel.pack(pady=(20,10))

        if typeuser == "Alumno": # Pantalla para los alumnos
            print("Se desplego la pantalla para alumnos")
            showAccepteedListBool = acceptedAppointmentsForAlumns(id)
            pendientAppointmentList = loadPendientAppointmentsForStudent(id)
            if pendientAppointmentList == []:
                pendientAppointmentList = ["No hay asesorias registrados"]
                pendientAppointmentListBool = False
            else:
                pendientAppointmentListBool = True

            self.viewAppointmentsPendientCombobox = ctk.CTkComboBox(self.viewAppointmentsFrame,
                                                                    state="readonly",
                                                                    values=pendientAppointmentList,
                                                                    width=500)
            self.viewAppointmentsPendientCombobox.pack(pady=20)
            
            if pendientAppointmentListBool:
                self.deleteAppointmentButton = ctk.CTkButton(self.viewAppointmentsFrame,
                                                             text="Eliminar cita",
                                                             font=("Arial", 12, "bold"),
                                                             fg_color=pbRed1,
                                                             hover_color=pbRed2,
                                                             command=lambda: (deleteAppointment(self.viewAppointmentsPendientCombobox.get()),
                                                                            self.viewAppointmentsFrame.grid_forget(),
                                                                            self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                            self.update_idletasks()))
                self.deleteAppointmentButton.pack(pady=20) 
            if showAccepteedListBool:

                self.listboxAcceptedAppointments = ctk_listbox.CTkListbox(self.viewAppointmentsFrame)
                self.listboxAcceptedAppointments.pack(fill="both", expand=True, padx=200, pady=10)
                
                acceptedAppointmentList = loadAcceptedAppointmentsForStudent(id)
                
                for appointment in acceptedAppointmentList:
                    self.listboxAcceptedAppointments.insert("end", appointment)

                self.wdwGoToIndexFromAppointments = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text='Volver',
                                                                font=("Arial",12,"bold"),
                                                                command= lambda: (self.viewAppointmentsFrame.grid_forget(),
                                                                                    self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                    self.update_idletasks()))
                self.eliminateAppointmentAlreadyAccepted = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                        text="Eliminar cita",
                                                                        font=("Arial", 12, "bold"),
                                                                        fg_color=pbRed1,
                                                                        hover_color=pbRed2,
                                                                        command= lambda: (deleteAppointment(self.listboxAcceptedAppointments.get()),
                                                                                                            self.viewAppointmentsFrame.grid_forget(),
                                                                                                            self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                                            self.update_idletasks()))
                self.wdwGoToIndexFromAppointments.pack(pady=20, side='left', padx=(370,50)) 
                self.eliminateAppointmentAlreadyAccepted.pack(pady=20, side='left', padx=(50,0))
            else: 
                self.wdwGoToIndexFromAppointments = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text='Volver',
                                                                font=("Arial",12,"bold"),
                                                                command= lambda: (self.viewAppointmentsFrame.grid_forget(),
                                                                                    self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                    self.update_idletasks()))
                self.wdwGoToIndexFromAppointments.pack(pady=20)
                    
        if typeuser == "Maestro": # Pantalla para los maestros
            print("Se desplego la pantalla para maestros")
            pendientAppointmentList = loadPendientAppointmentsForTeachers(id)
            acceptedAppointmentList = loadAcceptedAppointmentsForTeachers(id)
            if pendientAppointmentList == []:
                pendientAppointmentList = ["No hay asesorias registrados"]
                pendientAppointmentListBool = False
            else:
                pendientAppointmentListBool = True

            self.viewAppointmentsPendientCombobox = ctk.CTkComboBox(self.viewAppointmentsFrame,
                                                                    state="readonly",
                                                                    values=pendientAppointmentList,
                                                                    width=500)
            self.viewAppointmentsPendientCombobox.pack(pady=(10,20))
            
            if pendientAppointmentListBool:
                self.buttonslalaFrame = ctk.CTkFrame(self.viewAppointmentsFrame,
                                                     fg_color='transparent')
                self.buttonslalaFrame.pack()
                self.deleteAppointmentButton = ctk.CTkButton(self.buttonslalaFrame,
                                                             text="Eliminar cita",
                                                             font=("Arial", 12, "bold"),
                                                             fg_color=pbRed1,
                                                             hover_color=pbRed2,
                                                             command=lambda: (deleteAppointment(self.viewAppointmentsPendientCombobox.get()),
                                                                            self.viewAppointmentsFrame.grid_forget(),
                                                                            self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                            self.update_idletasks()))
                self.acceptAppointmentButton = ctk.CTkButton(self.buttonslalaFrame,
                                                             text="Aceptar cita",
                                                             font=("Arial", 12, "bold"),
                                                             fg_color=pbGreen1,
                                                             hover_color=pbGreen2,
                                                             command=lambda: (acceptAppointment(self.viewAppointmentsPendientCombobox.get()),
                                                                            self.viewAppointmentsFrame.grid_forget(),
                                                                            self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                            self.update_idletasks()))
                

                self.deleteAppointmentButton.pack(side='left',pady=(0,10), anchor="n",padx=(10))
                self.acceptAppointmentButton.pack(side='left',pady=(0,10), anchor="n",padx=(10))
                
                self.labelForListbox = ctk.CTkLabel(self.viewAppointmentsFrame,
                                                    text="Asesorias aceptadas: ",
                                                    font=("Arial",15,"bold"))
                self.labelForListbox.pack(pady=10)
                
            if acceptedAppointmentsForTeachers(id):
                self.labelForListbox = ctk.CTkLabel(self.viewAppointmentsFrame,
                                                    text="Asesorias aceptadas: ",
                                                    font=("Arial",15,"bold"))
                self.labelForListbox.pack(pady=10)

                self.acceptedAppointments = ctk_listbox.CTkListbox(self.viewAppointmentsFrame)
                self.acceptedAppointments.pack(fill="both", expand=True, padx=200, pady=10)
                
                for appointment in acceptedAppointmentList:
                    self.acceptedAppointments.insert("end", appointment)

                self.wdwGoToIndexFromAppointments = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text='Volver',
                                                                font=("Arial",12,"bold"),
                                                                command= lambda: (self.viewAppointmentsFrame.grid_forget(),
                                                                                    self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                    self.update_idletasks()))
                self.eliminateAppointmentAlreadyAccepted = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                        text="Eliminar cita",
                                                                        font=("Arial", 12, "bold"),
                                                                        fg_color=pbRed1,
                                                                        hover_color=pbRed2,
                                                                        command= lambda: (deleteAppointment(self.acceptedAppointments.get()),
                                                                                                            self.viewAppointmentsFrame.grid_forget(),
                                                                                                            self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                                            self.update_idletasks()))
                self.wdwGoToIndexFromAppointments.pack(pady=20, side='left', padx=(370,50)) 
                self.eliminateAppointmentAlreadyAccepted.pack(pady=20, side='left', padx=(50,0))
            else: 
                self.wdwGoToIndexFromAppointments = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text='Volver',
                                                                font=("Arial",12,"bold"),
                                                                command= lambda: (self.viewAppointmentsFrame.grid_forget(),
                                                                                    self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                    self.update_idletasks()))
                self.wdwGoToIndexFromAppointments.pack(pady=20)
            
# Funcion que guarda la cita
def saveSchedule(idAlumn, idTeacher, date, scheduleDescription):
    print("Se presiono el boton de guardar cita")
    idTeacher = idTeacher.split(" - ")[-1] # Convertir idTeacher a solo la matricula
    print(f'Matricula del profesor escogido: {idTeacher}')
    print(f'Dia escogido: {date}')
    print(f'Descripcion de la asesoria: {scheduleDescription}')
    state = "Pendiente"
    scheduleId = f"{idAlumn}{idTeacher}{date}"
    try:
        with sqlite3.connect("database.db") as uabcDatabase:
            # Nota: Poner logica aqui por si ya encuentra un id igual que no registre la cita
            cursor = uabcDatabase.cursor()
            cursor.execute("INSERT INTO scheduleList (scheduleId, idAlumn, idTeacher, date, scheduleDescription, state) VALUES (?, ?, ?, ?, ?, ?)", 
                           (scheduleId, idAlumn, idTeacher, date, scheduleDescription, state))
            print("Asesoria guardada con exito")
            messagebox.showinfo(title="Asesorias UABC", message=f"Has registrado con exito la asesoria el dia {date}")
    except sqlite3.Error as e:
        print("Error")
        messagebox.showinfo(title="Asesorias UABC", message="Ha ocurrido un error, por favor revisa la informacion ingresada")

# Recuperar la lista de profesores que hay
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

# Cargar asesorias en estado: Pendiente para alumno
def loadPendientAppointmentsForStudent(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT state, idTeacher, date, scheduleID FROM scheduleList WHERE idAlumn = ? AND state = 'Pendiente'", (id,))
        loadQuery = cursor.fetchall()
        formatted_appointments = [f"Estado: {state}, Matricula del profesor: {teacher}, Fecha: {date}, scheduleID: {scheduleID}" for state, teacher, date, scheduleID in loadQuery]
        print(f"Lista de asesorias pendientes recuperadas:")
        for i in formatted_appointments:
            print(f'{i}')
        return formatted_appointments

# Cargar asesorias en estado: Aceptado para el alumno    
def loadAcceptedAppointmentsForStudent(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT state, idTeacher, date, scheduleID FROM scheduleList WHERE idAlumn = ? AND state = 'Aceptado'", (id,))
        loadQuery = cursor.fetchall()
        formatted_appointments = [f"Estado: {state}, Matricula del profesor: {teacher}, Fecha: {date}, scheduleID: {scheduleID}" for state, teacher, date, scheduleID in loadQuery]
        print(f"Lista de asesorias aceptadas recuperadas:")
        for i in formatted_appointments:
            print(f'{i}')
        return formatted_appointments

# Cargar asesorias en estado: Pendiente para el maestro  
def loadPendientAppointmentsForTeachers(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT state, idAlumn, date, scheduleID FROM scheduleList WHERE idTeacher = ? AND state = 'Pendiente'", (id,))
        loadQuery = cursor.fetchall()
        formatted_appointments = [f"Estado: {state}, Matricula del alumno: {alumn}, Fecha: {date}, scheduleID: {scheduleID}" for state, alumn, date, scheduleID in loadQuery]
        print(f"Lista de asesorias pendientes recuperadas:")
        for i in formatted_appointments:
            print(f'{i}')
        return formatted_appointments

# Cargar asesorias en estado: Aceptado para el maestro      
def loadAcceptedAppointmentsForTeachers(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT state, idAlumn, date, scheduleID FROM scheduleList WHERE idTeacher = ? AND state = 'Aceptado'", (id,))
        loadQuery = cursor.fetchall()
        formatted_appointments = [f"Estado: {state}, Matricula del alumno: {alumn}, Fecha: {date}, scheduleID: {scheduleID}" for state, alumn, date, scheduleID in loadQuery]
        print(f"Lista de asesorias aceptadas recuperadas:")
        for i in formatted_appointments:
            print(f'{i}')
        return formatted_appointments

# Eliminar cita a partir del ID (EL STRING TIENE QUE TENER AL FINAL EL ID)
def deleteAppointment(varToExtractScheduleID):
    scheduleID = extractScheduleId(varToExtractScheduleID)
    print(f"Se presiono el boton para eliminar la cita con ID: {scheduleID}")
    if scheduleID == None:
        messagebox.showinfo(title="Asesorias UABC", message=f"No seleccionaste ningun elemento")
        return
    try:
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("DELETE FROM scheduleList WHERE scheduleId = ?", (scheduleID,))
            print("Asesoria eliminada con exito")
            messagebox.showinfo(title="Asesorias UABC", message=f"Has eliminado con exito la asesoria con ID {scheduleID}")
    except sqlite3.Error as e:
        messagebox.showinfo(title="Asesorias UABC", message=f"Ha ocurrido un error")
        print("Error")

# Funcion para extraer el ID de la cita de un string   
def extractScheduleId(cadena):
    # Dividimos la cadena por comas y espacios
    partes = cadena.split(', ')
    
    # Buscamos la parte que comienza con "scheduleID:"
    for parte in partes:
        if parte.startswith("scheduleID:"):
            # Retornamos solo el valor del scheduleID
            return parte.split(': ')[1]
    
    # Si no encontramos el scheduleID, retornamos None
    return None

# Funcion para cambiar el estado de una cita a aceptado
def acceptAppointment(varToExtractScheduleID):  
    print("El maestro presiono el boton para aceptar la cita")
    scheduleID = extractScheduleId(varToExtractScheduleID)
    try:
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("UPDATE scheduleList SET state = 'Aceptado' WHERE scheduleId = ?;", (scheduleID,))
            print("Asesoria aceptada con exito")
            messagebox.showinfo(title="Asesorias UABC", message=f"Se ha aceptado la asesoria {scheduleID}")
    except sqlite3.Error as e:
        messagebox.showinfo(title="Asesorias UABC", message=f"Ha ocurrido un error {scheduleID}")
        print("Error")
    ###

# Saber si el maestro tiene citas aceptadas (SOLO TRUE O FALSE)
def acceptedAppointmentsForTeachers(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT idAlumn FROM scheduleList WHERE idTeacher = ? AND state = 'Aceptado'", (id, ))
        aceppted = cursor.fetchone()
        if aceppted:
            print("El usuario tiene citas aceptadas")
            return True
        else:
            print("El usuario no tiene citas aceptadas")
            return False

# Saber si el alumno tiene citas aceptadas (SOLO TRUE O FALSE)
def acceptedAppointmentsForAlumns(id):
    with sqlite3.connect("database.db") as uabcDatabase:
        cursor = uabcDatabase.cursor()
        cursor.execute("SELECT idAlumn FROM scheduleList WHERE idAlumn = ? AND state = 'Aceptado'", (id, ))
        aceppted = cursor.fetchone()
        if aceppted:
            print("El usuario tiene citas aceptadas")
            return True
        else:
            print("El usuario no tiene citas aceptadas")
            return False

app = mainApp()
app.mainloop()