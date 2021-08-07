import sqlite3
from sqlite3.dbapi2 import Cursor



#creo mi primera base de datos
conexion = sqlite3.connect("miBase.db")


#creo mi primer cursor 
cursor = conexion.cursor()


#creamos nuestra primer tabla
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
#   "(DNI VARCHAR(10)PRIMARY KEY, nombre VARCHAR(100), edad INTEGER , email VARCHAR(100))")

cursor.execute("INSERT INTO usuarios VALUES "\
    "('456323145', 'gabriel', 08, 'gabriel@gmail.com')")


conexion.commit()


#cierro la base de datos
conexion.close()


