import sqlite3

subjectsList = [
    "Programacion", "Requerimientos", "Lenguaje C", "Python", "Paradigmas", "Algebra", "Ingles", "Redes", 
    "Bases de Datos", "Seguridad Informática", "Sistemas Operativos", "Diseño de Software", 
    "Estructuras de Datos", "Arquitectura de Computadoras", "Desarrollo Web", "Metodologías Ágiles", 
    "Cálculo", "Inteligencia Artificial", "Machine Learning", "Desarrollo Móvil", 
    "Análisis de Algoritmos", "Cloud Computing", "Criptografía", "Matemáticas Discretas", 
    "Big Data", "Microcontroladores", "Visión por Computadora", "Robótica", 
    "Programación Funcional", "Automatización", "DevOps", "Ciencia de Datos", 
    "Blockchain", "Compiladores", "Realidad Virtual", "Redes Neuronales"
]
x=1
with sqlite3.connect("database.db") as uabcDatabase:
    for subject in subjectsList:
        print("")
        cursor = uabcDatabase.cursor()
        cursor.execute("INSERT INTO subjects (subjectId, subjectName) VALUES (?, ?)",(x,subject, ))
        x += 1