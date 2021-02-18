# Procedimiento para poder probar y seguir desarrollando la aplicacion.

Pasos para poder Replicar comportamiento en computador local (algunos de estos pueden ser hechos antes o despues, pero se recomiendo hacerlos segun se indica.)

1. Crear Environment de desarrollo de python (yo personalmente creo un environment en [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  * 'conda create --name mydjangoenv django' (version de django 3.1.5 y python 3.9.1)
  * para activar el environment: 'activate mydjangoenv'
2. Instalar las siguientes librerias en el environment:
  * Para los cifrados de las contraseñas de los usuarios: 
   * 'pip install bcrypt'
   * 'pip install django[argon2]'
  * Para poder usar MySQL como base de datos en Django: [mas documentacion sobre esto](https://data-flair.training/blogs/django-database/) (solo desde el paso IV hacia adelante ya que para manejar la base de datos usaremos MYSQL Workbench que viene instalado en el paqeye de servicios MySQL en el paso 3 de este README)
   * 'pip install mysqlclient
3. Instalar todos los servicios de MySQL [MySQL 8.0.23](https://dev.mysql.com/downloads/installer/), [Tutorial](https://youtu.be/enRpneJLVrU)
  * Conectarse al servidor de la base de datos a travez de MySQL Workbench
  * crear base de datos llamada 'codelco_prueba'
4. Migrar datos desde app a base de datos
  * Ir a la carpeta con todos los archivos del proyecto descargados (la que contenga manage.py) con el evironment activo.
  * ejecutar los siguientes comandos para que la aplicacion cree las tablas correspondientes en la base de datos.
    * 'python manage.py migrate'
    * 'python  manage.py makemigrations app_uno'
    * 'python manage.py migrate'
5. Probar si funciona (con el evironment activo en la carpeta que contiene 'manage.py'):
  * 'python manage.py runserver'

