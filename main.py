import sys
import os
import customtkinter as ctk
import tkcalendar.calendar_
import tkcalendar
from CTkListbox import *

from utils.colorsHex import *
from utils.databaseControl import *

from PIL import ImageTk

ctk.set_appearance_mode("dark")

def resource_path(relative_path):
    #Get absolute path to resource, works for dev and for PyInstaller 
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

connectDatabase() # Funcion para verificar si encuentra la base de datos, en caso de que no exista crea una vacia.

class mainApp(ctk.CTk):
    # Inicializacion y primera ventana
    def __init__(self):
        """ = = = Configuracion de la ventana = = = """
        super().__init__()
        self.geometry("1100x700")
        self.title("Asesorias UABC")

        if True:
            icon_path = resource_path(os.path.join("ico", "ico.png"))
            icon = ImageTk.PhotoImage(file=icon_path)
            self.iconphoto(False, icon)
        
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
    ###
    # SignUp
    def signUp(self):
        print("Se presionó el botón de registrar usuario")
        self.loginFrame.grid_forget()
        
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

        # Password confirm
        passwordConfirmFrame = ctk.CTkFrame(dataFrame, fg_color='transparent')
        passwordConfirmFrame.pack(pady=10)
        self.passwordConfirmLabel = ctk.CTkLabel(passwordConfirmFrame,
                                           text="Rep. Contraseña:",
                                           font=("Arial", 15, "bold"))
        self.passwordConfirmEntry = ctk.CTkEntry(passwordConfirmFrame, show="*")

        self.passwordConfirmLabel.pack(side="left", padx=10, pady=5)
        self.passwordConfirmEntry.pack(side="left", padx=10, pady=5)

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
                                             command=lambda: validateRegisterEntrys(self.idEntry.get(), 
                                                                            self.passwordEntry.get(),
                                                                            self.passwordConfirmEntry.get(), 
                                                                            self.typeuserCombobox.get(), 
                                                                            self.nameEntry.get(), 
                                                                            self.lastNameEntry.get(), 
                                                                            self.emailEntry.get()))

        self.goBackButton = ctk.CTkButton(buttonsFrame,
                                           text="Volver",
                                           font=("Arial", 12, "bold"),
                                           fg_color=pbRed1,
                                           hover_color=pbRed2,
                                           command= lambda: (self.signUpFrame.grid_forget(),
                                                             self.loginFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                             self.update_idletasks()))
        self.RegisterButton.pack(side="left", padx=10, pady=5)
        self.goBackButton.pack(side="left", padx=10, pady=5)
    ###
    # LogOut
    def logOut(self):
        print("Se cerro sesion")
        self.entryUser.delete(0, 'end')
        self.entryPassword.delete(0, 'end')
        self.indexFrame.grid_forget()
        self.loginFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew")
        self.update_idletasks()
    ###
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
                self.loginFrame.grid_forget()
                self.indexWindow(id, typeuser)
                return True
            else:
                print("Usuario o contraseña incorrectos.")
                messagebox.showinfo(title="Asesorias UABC", message="Usuario o contraseña incorrectos")
                return False
    ###
    # Pagina principal
    def indexWindow(self, id, typeuser):
        print(f"Ventana de indice para el {typeuser} con matricula {id}")
        # Crear el nuevo frame de índice
        self.indexFrame = ctk.CTkFrame(self)
        self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew") 
        
        self.scheduleAppointmentButton = ctk.CTkLabel(self.indexFrame,
                                                        text="Universidad Autonoma de Baja California - Sistema de asesorias",
                                                        font=('Arial', 30, 'bold'),
                                                        text_color='white',
                                                        fg_color='transparent')
        self.scheduleAppointmentButton.pack(pady=100)
        if typeuser == "Alumno":
            self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                        text="Agendar asesoria",
                                                        font=('Arial', 15, 'bold'),
                                                        fg_color=pbGreen1,
                                                        hover_color=pbGreen2,
                                                        command= lambda: self.scheduleAppointmentWindow(id))
            self.scheduleAppointmentButton.pack(pady=(20, 10))
        if typeuser == "Maestro":
            self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                        text="Activar materias",
                                                        font=('Arial', 15, 'bold'),
                                                        fg_color=pbGreen1,
                                                        hover_color=pbGreen2,
                                                        command= lambda: self.selectSubjects(id))
            self.scheduleAppointmentButton.pack(pady=(20, 10))

        self.scheduleAppointmentButton = ctk.CTkButton(self.indexFrame,
                                                    text="Ver asesorias registradas",
                                                    font=('Arial', 15, 'bold'),
                                                    fg_color=pbGreen1,
                                                    hover_color=pbGreen2,
                                                    command=lambda: self.viewAppointments(id, typeuser))
        self.scheduleAppointmentButton.pack(pady=(20, 10))

        self.logOutButton = ctk.CTkButton(self.indexFrame,
                                          text="Cerrar sesion",
                                          font=("Arial",12,"bold"),
                                          command= lambda: self.logOut(),
                                          fg_color=pbRed1,
                                          hover_color=pbRed2)
        self.logOutButton.pack(pady=(200,0))
        self.update_idletasks() # Usar esto siempre para que la ventana se refresque
    ###
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
                                            font=("Arial", 14, "bold"),
                                            borderwidth=2, 
                                            relief="solid",
                                            selectbackground=pbGreen1,
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
                                                     values=teachersListVar,
                                                     width=500)
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
                                                            command= lambda: (self.scheduleFrame.grid_forget(),
                                                                              self.calendarFrame.grid_forget(),
                                                                              self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                              self.update_idletasks()))
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton = ctk.CTkButton(self.scheduleFrame,
                                                            text="Agendar cita",
                                                            font=('Arial',12,"bold"),
                                                            fg_color=pbGreen1,
                                                            hover_color=pbGreen2,
                                                            command=lambda: windowForSemesterAndSubject(id,
                                                                                                        self.selectTeacherCombobox.get(),
                                                                                                        self.calendar.get_date(),
                                                                                                        self.scheduleDescriptionTextbox.get("1.0", "end")))
        self.returnToindexWindowButton.pack(pady=50, padx=(50,10), side='left',anchor="nw", expand=True)
        if teachersListVar != ["No hay profesores registrados"]:
            self.saveScheduleAlumnButton.pack(pady=50,padx=(50), side='right', expand=True, anchor='e')
    ###
    # Pagina para ver citas
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

        if typeuser == "Alumno":
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
        if typeuser == "Maestro":
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
                self.wdwGoToIndexFromAppointments.pack(pady=20, side='left', padx=(270,50)) 
                #
                self.viewDescriptionAppointment = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text="Ver descripcion",
                                                                font=("Arial", 12, "bold"),
                                                                command= lambda: viewDescription(extractScheduleId(self.acceptedAppointments.get())))
                self.viewDescriptionAppointment.pack(pady=20, side='left', padx=(30,50)) 
                #
                self.eliminateAppointmentAlreadyAccepted.pack(pady=20, side='left', padx=(50,0))
            else: 
                self.wdwGoToIndexFromAppointments = ctk.CTkButton(self.viewAppointmentsFrame,
                                                                text='Volver',
                                                                font=("Arial",12,"bold"),
                                                                command= lambda: (self.viewAppointmentsFrame.grid_forget(),
                                                                                    self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                                    self.update_idletasks()))
                self.wdwGoToIndexFromAppointments.pack(pady=20)
    ###
    # Pagina para dar de alta una materia
    def selectSubjects(self, id):
        print("Se presiono el boton para activar materias")
        self.indexFrame.grid_forget()
        
        self.selectSubjectsFrame = ctk.CTkFrame(self)
        self.selectSubjectsFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew") 
        
        self.selectSubjectsLabel = ctk.CTkLabel(self.selectSubjectsFrame,
                                                text="Escoge la materia que quieras activar",
                                                font=("Arial",20,"bold"))
        self.selectSubjectsLabel.pack(pady=20)

        self.unnactivatedSubjects = ctk_listbox.CTkListbox(self.selectSubjectsFrame)
        self.unnactivatedSubjects.pack(fill="both", expand=True, padx=200, pady=10)
        
        subjects = loadAllSubjects()
        for subject in subjects:
            self.unnactivatedSubjects.insert("end", subject)

        self.activateSubjectButton = ctk.CTkButton(self.selectSubjectsFrame,
                                                   text="Activar materia",
                                                   font=("Arial",12,"bold"),
                                                   fg_color=pbGreen1,
                                                   hover_color=pbGreen2,
                                                   command= lambda: activateSubject(id,self.unnactivatedSubjects.get()))

        self.returnFromSubjectsFrameButton = ctk.CTkButton(self.selectSubjectsFrame,
                                                   text="Volver",
                                                   font=("Arial",12,"bold"),
                                                   fg_color=pbRed1,
                                                   hover_color=pbRed2,
                                                   command= lambda: (self.selectSubjectsFrame.grid_forget(),
                                                                     self.indexFrame.grid(row=0, column=0, columnspan=2, rowspan=2, pady=50, sticky="nsew"),
                                                                     self.update_idletasks()))
        self.activateSubjectButton.pack(pady=20, side='left', padx=(400,20))
        self.returnFromSubjectsFrameButton.pack(pady=20, side = "left", padx=(20))
    # Funcion que actualiza el dia seleccionado
    def update_selected_day(self, event=None):
        selected_date = self.calendar.get_date()
        self.selectedDayVar.set(f"Día seleccionado: {selected_date}")
        print(f"Fecha seleccionada: {selected_date}")



app = mainApp()
app.mainloop()