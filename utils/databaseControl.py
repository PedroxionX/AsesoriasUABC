import sqlite3
from tkinter import messagebox
from customtkinter import CTkToplevel, CTkComboBox, CTkButton
from utils.colorsHex import *
import os

def connectDatabase():
    db_name = 'database.db'
    print("Se verificara si existe o no la base de datos")
    if not os.path.exists(db_name):
        print("Se creara la base de datos")
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # Crear tabla scheduleList
        cursor.execute('''CREATE TABLE scheduleList (
                            scheduleId TEXT PRIMARY KEY,
                            idAlumn INTEGER,
                            idTeacher INTEGER,
                            date TEXT,
                            scheduleDescription TEXT,
                            state TEXT
                          )''')
        # Crear tabla users
        cursor.execute('''CREATE TABLE users (
                            id NUMERIC PRIMARY KEY,
                            password TEXT,
                            typeuser TEXT,
                            name TEXT,
                            lastname TEXT,
                            email TEXT
                          )''')
        # Crear tabla subjects
        cursor.execute('''CREATE TABLE subjects (
                            subjectId INTEGER PRIMARY KEY,
                            subjectName TEXT
                          )''')
        # Crear tabla subjectTeachers
        cursor.execute('''CREATE TABLE subjectTeachers (
                            idTeacher INTEGER,
                            idSubject INTEGER
                          )''')
        conn.commit()
        conn.close()
        print(f"Base de datos '{db_name}' creada con éxito.")
    else:
        print(f"La base de datos '{db_name}' ya existe.")

# Llamar a la función para crear la base de datos si no existe

""" = = = Funciones para controlar la base de datos = = = """

def registerUser(id, password, typeuser, name, lastname, email):
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
    
# Funcion que guarda la cita
def saveSchedule(idAlumn, idTeacher, date, scheduleDescription):
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

# Cargar la lista con todas las materias existentes
def loadAllSubjects():
    with sqlite3.connect("database.db") as uabcDatabase:
        try:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT subjectId, subjectName FROM subjects")
            loadQuery = cursor.fetchall()
            subjects = [f"#{subjectId} - Materia : {subjectName}" for subjectId, subjectName in loadQuery]
            print("Se conecto de manera exitosa con la base de datos")
            print(f"Lista de materias recuperadas:")
            for i in subjects:
                print(f'{i}')
            return subjects
        except:
            print("Hubo un error al querer conectar con la base de datos")

# Activar materia
def activateSubject(id, stringToEdit):
    print(stringToEdit)
    subjectId = stringToEdit.split()[0].replace("#", "")
    subjectId = int(subjectId)
    print(f"Se activará la materia #{subjectId} para el maestro: {id}")
    with sqlite3.connect("database.db") as uabcDatabase:
        try:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT idTeacher FROM subjectTeachers WHERE idTeacher = ? AND idSubject = ?", (id, subjectId,))
            if cursor.fetchone():
                print("El profesor ya tenía dada de alta esta materia")
                messagebox.showinfo(title="Asesorias UABC", message="Ya tienes dada de alta esa materia")
            else:
                cursor.execute("INSERT INTO subjectTeachers (idTeacher, idSubject) VALUES (?, ?)", (id, subjectId,))
                messagebox.showinfo(title="Asesorias UABC", message=f"Se activo con exito la materia #{subjectId}")
                print("Se insertó de manera exitosa en la base de datos")
        except sqlite3.Error as e:
            print(f"Hubo un error al querer conectar con la base de datos: {e}")
    
# Validar datos de la asesoria
def validateAppointment(idTeacher):
    if idTeacher != '':
        print('Se valido la asesoria')
        return True
    else:
        messagebox.showinfo(title="Asesorias UABC", message=f"No has seleccionado a ningun profesor")
        print('No se valido la asesoria ya que no se selecciono ningun profesor')
        return False


def teacherSubjects(idTeacher):
    with sqlite3.connect("database.db") as uabcDatabase:
        try:
            cursor = uabcDatabase.cursor()
            query = """
            SELECT s.subjectName 
            FROM subjectTeachers st
            JOIN subjects s ON st.idSubject = s.subjectId
            WHERE st.idTeacher = ?
            """
            cursor.execute(query, (idTeacher,))
            subjects = cursor.fetchall()
            if subjects:
                print(f"Materias que imparte el profesor {idTeacher}:")
                for subject in subjects:
                    print(subject[0])
                return subjects
            else:
                print(f"El profesor con ID {idTeacher} no imparte materias.")
        except sqlite3.Error as e:
            print(f"Hubo un error al querer conectar con la base de datos: {e}")


def funcionintermedia(idAlumn, idTeacher, date, scheduleDescription):
    if validateAppointment(idTeacher):
        semesterList = ["Primer semestre", "Segundo semestre", "Tercer semestre", "Cuarto semestre", "Quinto semestre", "Sexto semestre", "Septimo semestre", "Octavo semestre"]
        teacherSubjectsList = tupleToListBUGGG(teacherSubjects(int(idTeacher.split("- ")[1]))) # Esto es lo mas sucio que he hecho en mi vida
        print(f"Lista {teacherSubjectsList}")
        toplevel = CTkToplevel()
        toplevel.selectSubjectCombobox = CTkComboBox(toplevel,
                                                     values=teacherSubjectsList,
                                                     state="readonly")
        toplevel.selectSubjectCombobox.pack(pady=20, padx=50)

        toplevel.selectSemesterCombobox = CTkComboBox(toplevel,
                                                      values=semesterList)
        toplevel.selectSemesterCombobox.pack(pady=20, padx=50)
        toplevel.confirmButton = CTkButton(toplevel,
                                           text="Confirmar",
                                           font=("Arial",12,"bold"),
                                           fg_color=pbGreen1,
                                           hover_color=pbGreen2,
                                           command=lambda: saveSchedule(idAlumn, 
                                                                        idTeacher, 
                                                                        date, 
                                                                        f"{scheduleDescription} - Asesoria para la materia: {toplevel.selectSubjectCombobox.get()} - Alumno de: {toplevel.selectSemesterCombobox.get()}"))
        toplevel.confirmButton.pack(pady=20, padx=50)

def tupleToListBUGGG(lista_tuplas):
    if lista_tuplas == None:
        messagebox.showinfo(title="Asesorias UABC", message="El profesor que escogiste aun no tiene materias dadas de alta")
    else:
        return [item[0] for item in lista_tuplas]

def viewDescription(scheduleId):
    if scheduleId == "":
        print("El usuario no selecciono asesoria e intento recuperar la descripcion ")
        messagebox.showinfo(title="Asesorias UABC", message=f"Descripcion de la asesoria: {description[0]}")
    else:
        print(f"Se recuperará la descripción de la cita con ID: {scheduleId}")
        with sqlite3.connect("database.db") as uabcDatabase:
            cursor = uabcDatabase.cursor()
            cursor.execute("SELECT scheduleDescription FROM scheduleList WHERE scheduleId = ?", (scheduleId,))
            description = cursor.fetchone()
            print(f"La descripcion de la cita es: {description[0]}")
            messagebox.showinfo(title="Asesorias UABC", message=f"Descripcion de la asesoria: {description[0]}")

def validateRegisterEntrys(id, password, password2, typeuser, name, lastname, email):
    if name == "":
        print("El usuario no escribio su nombre")
        messagebox.showinfo(title="Asesorias UABC", message="No puedes dejar vacio el campo de nombre")
    elif lastname == "":
        print("El usuario no escribio su apellido")
        messagebox.showinfo(title="Asesorias UABC", message="No puedes dejar vacio el campo de apellido")
    elif id == "":
        print("El usuario no escribio su matricula")
        messagebox.showinfo(title="Asesorias UABC", message="No puedes dejar vacio el campo de matricula")
    elif email == "":
        print("El usuario no escribio su correo electronico")
        messagebox.showinfo(title="Asesorias UABC", message="No puedes dejar vacio el campo de correo electronico")
    elif password == "":
        print("El usuario no escribio su contraseña")
        messagebox.showinfo(title="Asesorias UABC", message="No puedes dejar vacio el campo de contraseña")
    elif password != password2:
        print("El usuario no escribio las dos contraseñas iguales")
        messagebox.showinfo(title="Asesorias UABC", message="Las contraseñas no coinciden")
    elif typeuser == "":
        print("El usuario no selecciono un tipo de usuario")
        messagebox.showinfo(title="Asesorias UABC", message="Selecciona un tipo de usuario")
    else:
        id = int(id)
        registerUser(id, password, typeuser, name, lastname, email)