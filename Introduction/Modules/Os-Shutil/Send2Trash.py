""" 
Librería send2trash

La librería send2trash permite enviar archivos y carpetas
a la Papelera de reciclaje en lugar de eliminarlos de forma
permanente. Esto la convierte en una opción mucho más segura 
que os.remove() o shutil.rmtree(), ya que los elementos pueden 
recuperarse si fueron eliminados por error. Su uso es muy sencillo
mediante la función send2trash(), siendo ideal para aplicaciones 
donde la seguridad de los datos del usuario es importante.
"""
from send2trash import send2trash

send2trash(r"Files/Curso.txt")
print("El archivo fue enviado a la Papelera de reciclaje.")
