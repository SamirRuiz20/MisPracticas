import sqlite3


conexion = sqlite3.connect("misProductos.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE MISPRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), seccion VARCHAR(20))")



productos = [
    ("Leche", "Lacteo"),
    ("Pan", "Panaderia"),
    ("Gaseosas", "Bebidas")
]

cursor.executemany("INSERT INTO MISPRODUCTOS VALUES(NULL, ?, ?)", productos)

conexion.commit()

conexion.close() 