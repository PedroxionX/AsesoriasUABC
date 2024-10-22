# Asesorias UABC
Sistema de registro de citas para asesorias de materias universitarias. Aplicacion hecha en Python para solicitar asesorias. El sistema cuenta con una base de datos en la que se maneja el registro de los usuarios (tanto alumnos como profesores) y el almacenamiento de las asesorias solicitadas.
## Requerimientos
- [x] Calendario
- [x] Lista de materias que imparte
- [x] Registro de usuarios y Log In
- [x] Apartado para agendar cita
- [x] Escoger semestre
- [x] Agendar mediante materia y horario
- [x] Que el maestro pueda ver la descripcion de la asesoria
## Librerias utilizadas
* Nativas (no ocupan instalacion)
  * sqlite3
  * os
  * webbrowser
* Externas (ocupan instalacion en el entorno virtual)
  * customtkinter - Mas widgets para TK https://customtkinter.tomschimansky.com/documentation/
  * CTkMessagebox - Caja con mensaje https://github.com/Akascape/CTkMessagebox
  * tkcalendar - Calendario de TKinter https://github.com/j4321/tkcalendar
  * CTkListbox # Listbox de CustomTkinter https://github.com/Akascape/CTkListbox
## Crear y activar entorno virtual (Unix)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt # Instalar todas las librerias utilizadas
```
## Crear binario ejecutable (Unix)
>[!NOTE]
> Primero necesitas haber instalado las librerias en tu entorno Python.
  1. Instalar pyinstaller
```bash
pip install pyinstaller
```
  2. Ejecutar build.py
```bash
python3 build.py
```
  3. Dirigirnos a la carpeta 'dist' donde encontraremos el binario ejecutable