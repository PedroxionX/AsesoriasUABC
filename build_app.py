import PyInstaller.__main__
import os
import shutil
import sys

# Obtén la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define las rutas de los archivos y directorios
main_file = os.path.join(current_dir, 'main.py')
utils_dir = os.path.join(current_dir, 'utils')
ico_file = os.path.join(current_dir, 'ico', 'your_icon.ico')  # Asegúrate de que este es el nombre correcto de tu archivo de icono
database_file = os.path.join(current_dir, 'database.db')

# Crea la lista de argumentos para PyInstaller
pyinstaller_args = [
    '--name=TuAplicacion',
    '--windowed',
    '--onedir',
    f'--add-data={utils_dir}:utils',
    f'--add-data={database_file}:.',
    f'--icon={ico_file}',
    '--hidden-import=customtkinter',
    '--hidden-import=tkinter',
    '--hidden-import=PIL',
    '--hidden-import=PIL._imagingtk',
    '--hidden-import=PIL._tkinter_finder',
    '--hidden-import=sqlite3',
    '--debug=all',
    main_file
]

# Ejecuta PyInstaller
PyInstaller.__main__.run(pyinstaller_args)

# Copia el archivo .app a la raíz del proyecto
dist_dir = os.path.join(current_dir, 'dist')
app_name = 'TuAplicacion.app'
source_app = os.path.join(dist_dir, app_name)
destination_app = os.path.join(current_dir, app_name)

if os.path.exists(destination_app):
    shutil.rmtree(destination_app)

shutil.copytree(source_app, destination_app)

print(f"La aplicación ha sido creada en: {destination_app}")
"""
# Después de copiar la aplicación
images_dir = os.path.join(current_dir, 'images')  # Ajusta esto a la ubicación real de tus imágenes
if os.path.exists(images_dir):
    dest_images_dir = os.path.join(destination_app, 'Contents', 'MacOS', 'images')
    shutil.copytree(images_dir, dest_images_dir)"""