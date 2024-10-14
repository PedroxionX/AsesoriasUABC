import sqlite3
from tkinter import messagebox, PhotoImage
""" = = = Funciones extra = = = """
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
