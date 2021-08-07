import sqlite3



#creo mi primera base de datos
conexion = sqlite3.connect("miBase.db")


#creo mi primer cursor 
cursor = conexion.cursor()


#creamos nuestra primer tabla
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
    "(nombre VARCHAR(100), edad INTEGER , email VARCHAR(100))")

conexion.commit()


#cierro la base de datos
conexion.close()


