import mysql.connector
from mysql.connector import errorcode
from decouple import config

class Database:
    def __init__(self):
        self.host = config('DATABASE_HOST') # Reemplaza por el host del MySQL que obtuviste
        self.user = config('DATABASE_USER') # Reemplaza por tu usuario de MySQL
        self.password = config('DATABASE_PASSWORD') # Reemplaza por tu contraseña de MySQL
        self.name = config('DATABASE_NAME') # Reemplaza por el nombre de tu base de datos

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.name
            )
            print('Conexión a la base de datos exitosa!')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o contraseña incorrectos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no existe")
            else:
                print(err)

    def disconnect(self):
        self.cnx.close()
