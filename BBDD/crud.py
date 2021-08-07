import sqlite3


'''

Create = Crear
Read = Leer
Update = Actualizar
Delete = Eliminar

'''

conexion = sqlite3.connect("misProductos.db")

cursor = conexion.cursor()

#LEER
cursor.execute("SELECT * FROM MISPRODUCTOS WHERE ID='2'") 
NAME = "BALON" 

#ACTUALIZAR
cursor.execute(F'UPDATE MISPRODUCTOS SET nombre=?, seccion=? WHERE nombre="{NAME}"', ["BALONES", "CIRCULO"])  

#ELIMINAR
#cursor.execute('DELETE FROM MISPRODUCTOS WHERE ID="3"') 
productos = cursor.fetchall()

print(productos) 


conexion.commit()
conexion.close() 