import PyInstaller.__main__
import os
import sys

# Obtener el directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir los archivos y carpetas a incluir
main_file = os.path.join(current_dir, 'main.py')
utils_dir = os.path.join(current_dir, 'utils')
ico_dir = os.path.join(current_dir, 'ico')

# Definir las opciones de PyInstaller
options = [
    main_file,
    '--name=AsesoríasUABC',
    '--onefile',
    f'--add-data={utils_dir}:utils',
    f'--add-data={ico_dir}:ico',
    '--icon=' + os.path.join(ico_dir, 'ico.png'),
    '--hidden-import=babel.numbers',
    '--hidden-import=tkcalendar',
    '--hidden-import=CTkListbox',
    '--debug=all',
    '--log-level=DEBUG',
]

# Ejecutar PyInstaller
PyInstaller.__main__.run(options)

print("La construcción de la aplicación ha finalizado.")