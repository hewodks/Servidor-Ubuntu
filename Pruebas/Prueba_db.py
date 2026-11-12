import sqlite3

"""Crear un base de datos sencilla"""
def createdb():
    conn = sqlite3.connect("Base_Prueba.db") #crearla
    conn.commit() #nose investigar
    conn.close() #cerrarla

def create_table():
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor() #ponerlo en modo editor creo 
    cursor.execute( #execute es para ejecutar los comandos sql
        """CREATE TABLE streamers (
                                nombre text,
                                suscriptores integer,
                                laiks integer
                                )"""
    )
    conn.commit()
    conn.close()

def insertar_info(nombre, suscriptores, likes):
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    #en el caso de insertar valores se sigue usando execute pero por facilidad se crea una variable con el INSERT
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {suscriptores}, {likes})" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def Inserta_Youtuber_Fav():
    yutuber = input("Ingresa tu yutuber: ")
    subs = int(input("ingresa los subs: "))
    likes = int(input("Ingresa los likes: "))

    print("Ingresando datos a la base de datos")

    insertar_info(yutuber, subs, likes)

def Read_rows():
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers "
    cursor.execute(instruccion)
    datos = cursor.fetchall() #nos sirve para asignar los datos que nos devolvera la tabla
    conn.commit()
    conn.close()
    print(datos)

def insertar_infos(streamerlist):
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    #en el caso de insertar valores se sigue usando execute pero por facilidad se crea una variable con el INSERT
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)" 
    cursor.executemany(instruccion, streamerlist) #se usa executemany si se necesita insertar varias informaciones
    conn.commit()
    conn.close()

Streamers_grand = [
    ("'", 9999999999, 67),
    ("george", 3453045, 3432),
    ("mi amol", 6345334534534, 67)
]

def Reads_only(field):
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC" #DESC es para ordenar de mayor a menor por defecto sin desc los ordena de menor a mayor
    cursor.execute(instruccion)
    datos = cursor.fetchall() #nos sirve para asignar los datos que nos devolvera la tabla
    conn.commit()
    conn.close()
    print(datos)

def Search():
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE suscriptores > 6000000000 ORDER BY suscriptores DESC" #like es solo si no encontramos el nombre nos sirve para buscarlo de diferentes maneras y encontrarlo
    #si queremos buscar a gente con numeros mayores ejemplo subs tengan mas de 600 y no mostrar lo q no cumplen es subs > 600
    cursor.execute(instruccion)
    datos = cursor.fetchall() #nos sirve para asignar los datos que nos devolvera la tabla
    conn.commit()
    conn.close()
    print(datos)

def update_fields():
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET suscriptores=999 WHERE nombre like 'vegeta777'" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def Delete_row():
    conn = sqlite3.connect("Base_Prueba.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE nombre like 'vegeta%'" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #Inserta_Youtuber_Fav()
    #insertar_infos(Streamers_grand)
    #Read_rows()
    #Reads_only("suscriptores")
    #Search()
    #update_fields()
    #Delete_row()
    pass
    #createdb()
    #create_table()
    #insertar_info(yutuber, subs, likes)