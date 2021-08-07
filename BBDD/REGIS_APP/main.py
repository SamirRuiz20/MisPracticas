'''

APP DE REGISTRO De Postulantes A UN Respectivo Empleo .

Las Vacantes Son Para :
- Personal Administrativo (Administracion)
- Medicina (Medico(a))
- Seguridad (Vigilantes)

PROBLEMA :

Se necesita de una app que logre registrar a distinto postulantes almacenando
en una base de datos sqlite su numero de DNI , NOMBRE, EDAD, A QUE POSTULA, 
AÑOS DE EXPERIENCIA Ordenados Ascendentemente PARA que un postulante sea apto
debe tener no menos de 5 años de experiencia .

CARACTERISTICAS DE LA APP :

- Almacenar los Postulantes
- Consultar SI UN Postulante ya esta registrado con su DNI
- MOSTRAR UNA LISTA DE LOS POSTULANTES Aptos 
- Mostrar Una Lista de postulantes para MEDICINA
- Mostrar lista DE Postulantes Para Vigilancia 
- Mostrar Lista De Postulantes Para Administracion 
- Mostrar Informcion De Un Usuario Introduciendo Su DNI si ESTA REGISTRADO .

'''



import os
import sqlite3
import time


#CREA UNA UN ARCHIVO.DB SI NO EXISTE .
def crearbbdd() :

    conexion = sqlite3.connect("Postulantes.db")

    cursor = conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS POSTULANTES"\
      "(NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), EDAD INTEGER, \
          POSTULANTE VARCHAR(50), EXPERIENCIA INTEGER, DNI VARCHAR(8) PRIMARY KEY, APTO VARCHAR(2))"
       )

    conexion.commit()


    conexion.close()




#INSERTA UNA NUEVA FILA EN LA BBDD CON LOS DATOS DE LA LISTA POR PARAMETRO
def insertValues( lista = []) :

    try :

        conexion = sqlite3.connect("Postulantes.db")

        cusor = conexion.cursor()

        cusor.executemany("INSERT INTO POSTULANTES VALUES(?, ?, ?, ?, ?, ?, ?)", [tuple(lista)])  

        conexion.commit()


    except sqlite3.IntegrityError :

        return "INSERT_ERROR!"


    finally :

        conexion.close()




#ACTUALIZA UNO O VARIOS CAMPOS DE LA BASE DE DATOS DONDE SE ENCUENTRE EL DNI PASADO POR PARAMETRO, COMPLETANDO EL CAMPO CON LA LISTA .
def updateValues(dni, lista = []) :


    try :

        conexion = sqlite3.connect("Postulantes.db")


        cursor = conexion.cursor()
        cursor.execute(f"UPDATE POSTULANTES SET NOMBRE=?, APELLIDO=?, EDAD=?, POSTULANTE=?, EXPERIENCIA=?, DNI=?, APTO=? WHERE DNI='{dni}'", lista)

        conexion.commit()

    finally :

        conexion.close()




#CONSULTA INFORMACION DE LA BASE DE DATOS CON LAS CONDICIONES QUE SE LES PASE AL PARAMETRO EJECUTAR
def consultBBDD(ejecutar= None) :


    try :

        conexion = sqlite3.connect("Postulantes.db")

        cursor = conexion.cursor()

        cursor.execute(ejecutar) 



        info = cursor.fetchall()

        if len(info) != 0 :

            return info

        else :

            return None

    
    finally :

        conexion.close()






def menuMAIN() :

    while True :

        os.system("cls")

        print(f"{'MENU':^60}")
        print("\n"*2)
        print(" 1 - Registrar Postulante .")
        print(" 2 - Consultar Postulante .")
        print(" 3 - Listar Todos Los Postulantes .")
        print(" 4 - Listar Postulantes A Medicina .")
        print(" 5 - Listar Postulantes A Vigilancia .")
        print(" 6 - Listar Postulantes A Administracion .")

        print("\n"*2)

        opcion = (input(" Por Favor escoge una opcion ->  ")) 

        if opcion in ('1', '2', '3', '4', '5', '6') :

            return opcion

        input(f"{'ENTER Para intentar de nuevo':.^60}")




#ITEM1 REGISTRAR POSTULANTE
def registraUser() :

    

    while True :

        lista = []
        error = None

        os.system("cls")

        print(f"{'REGISTRO DE POSTULANTES':^60}")
        print(f"{'_'*20:^60}")
        print("\n"*2)
        
        name = (input(" Cual Es Tu Nombre -> ")).strip()
        if not(name.isalpha()) or len(name) == 0 or name.isdigit() :

            error = repr("NOMBRE")


        apellido = (input(" Cuales Son Tus Apellidos -> ")).strip()
        if not(apellido.isalpha()) or len(apellido) == 0 or apellido.isdigit() :

            error = repr("APELLIDO")


        edad = (input(" Cual Es Tu Edad -> ")).strip()
        if edad.isalpha() or len(edad) == 0 or not(edad.isdigit()) or int(edad) <= 0 :

            error = repr("EDAD")

        postulacion = (input(" A Que Postulas ADMINISTRACION(A)-VIGILANTE(V)-MEDICINA(M) -> ")).upper().strip()
        if not(postulacion.isalpha()) or len(postulacion) == 0 or postulacion.isdigit() or postulacion not in ("A", "V", "M") :

            error = repr("POSTULACION")

        exper = (input(" Años De Experiencia -> ")).strip()
        if exper.isalpha() or len(exper) == 0 or not(exper.isdigit()) or int(exper) < 0 :

            error = repr("EXPERIENCIA")

        dni = input(" NUMERO DE DNI -> ").strip()
        if not(dni.isdigit()) or len(dni) != 8 :

            error = repr("DNI")

        
        print("\n"*2)

        if error is None :

            if postulacion == "A" :

                postulacion = "ADMINISTRACION"

            elif postulacion == "V" :

                postulacion = "VIGILANCIA"

            else :

                postulacion = "MEDICINA"


            apto = "Si" if int(exper) >= 5 else "No"
            
            lista.extend([name, apellido, int(edad), postulacion, (exper), (dni), apto ])

            insertar = insertValues(lista)

            while True : 

                print() 

                if insertar == "INSERT_ERROR!" :

                    print(f" EL DNI {dni} Ya Esta Registrado ...")
                    print("\n Deseas actualizar sus datos o cambiar nro De DNI")
                    rspta = input("\n (M)MODIFICAR - (C)CAMBIAR -> ").upper().strip()

                    if rspta == "M" :

                        updateValues(lista[-2], lista)

                        return

                    elif rspta == "C" :

                        while True :

                            dni = input(" NUMERO DE DNI -> ").strip()
                            if not(dni.isdigit()) or len(dni) != 8 :

                                print("  \nDNI NO VALIDO\n")
                                continue

                            else :

                                break

                        lista[-2] = dni    

                        insertar = insertValues(lista)

                        if insertar == "INSERT_ERROR!" :

                            continue

                        else :

                            return


                    else :

                        return


                else :

                    return





        print(f"{'EL VALOR PASADO A':^60}")
        print(f"{error:^60}")
        print(f"{'ES INVALIDO':^60}")
        input(f"{'ENTER PARA INTENTAR DE NUEVO':^60}")






#ITEM2 CONSULTAR INFORMACION DE UN POSTULANTE POR SU DNI
def consultINFO() :


    while True :


        os.system("cls")

        print(f"{' CONSULTAR INFORMACION ':.^60}")
        print("\n"*2)

        dni = (input(" Digita El Numero De DNI -> ")).strip()
        print()

        if not(dni.isdigit()) or len(dni) != 8 :

            print(f"{'NUMERO DE DNI NO VALIDO':^60}")
            input(f"{'ENTER PARA INTENTAR DE NUEVO':^60}")
            continue


        info = consultBBDD(f"SELECT * FROM POSTULANTES WHERE DNI='{dni}'") 

        if type(info) is list :

            campos = ["NOMBRE  ", "APELLIDO  ", "EDAD  ", "POSTULANTE A  ", "EXPERIENCIA  ", "DNI  ", "APTO  "]


            print(f"{'INFORMACION PARA EL DNI ':^60}")
            print(f"{dni!r:^60}") 


            print()

            for i in range(len(campos)) :

                print(f" {campos[i]:-<45}  {info[0][i]}") 


     
            input(f"{'ENTER Para Volver Al Menu':^60}")
            return

        else :

            print(f"{'EL DNI NO ESTA REGISTRADO':^60}")
            print()
            print(f"{' (V)VOLVER A MENU - (O)PROBAR OTRO DNI'}")
            opcion = (input(" Cual Es Tu Opcion -> ")).upper().strip()

            print()

            if opcion == "V" :

                return

            elif opcion == "O" :

                continue

            else :

                return






#ITEM3 LISTAR TODOS LOS POSTULANTES SIN EXCEPCION
def listPOST(post) :


    os.system("cls")

    if post == "M":

        values = consultBBDD("SELECT * FROM POSTULANTES WHERE POSTULANTE='MEDICINA'")

    elif post == "A":

        values = consultBBDD("SELECT * FROM POSTULANTES WHERE POSTULANTE='ADMINISTRACION'")

    elif post == "V" :

        values = consultBBDD("SELECT * FROM POSTULANTES WHERE POSTULANTE='VIGILANCIA'")

    else :

        values = consultBBDD("SELECT * FROM POSTULANTES")


    print() 

    if type(values) is list :

        dists = 15, 15, 5, 20, 15, 10, 6
        print(f"{'NOMBRE':^15}{'APELLIDO':^15}{'EDAD':^5}{'POSTULANTE':^20}{'EXPERIENCIA':^15}{'DNI':^10}{'APTO':^6}")
        print(f" {'-'*94}")

        for i in range(len(values)) :

            for j in range(len(dists)) :

                print(f"{values[i][j]:^{dists[j]}}", end= "")  

            print() 


        print() 

        input(f"{'ENTER Para Volver Al Menu':^60}")
        return

        
        

    else :

        return "AUN NO HAY POSTULANTES REGISTRADOS"

            




        


if not(os.path.exists("\Postulantes.db")) : 

    crearbbdd()



while True :

    OP = menuMAIN()

    if OP == "1" :

        registraUser()

    elif OP == "2" :

        consultINFO()

    elif OP == "3" :

        listPOST(None)

    elif OP == "4" :

        listPOST("M")

    elif OP == "5" :

        listPOST("V")

    elif OP == "6" :

        listPOST("A") 

    else :

        break







