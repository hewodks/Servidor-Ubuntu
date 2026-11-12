import exiftool
import sqlite3
import hashlib
from pathlib import Path

"""Rutas de Archivos Entrada"""

#Convertimos este archivo en el main de rutas recibiendo el nombre de raiz_utils
Raiz_utils = Path(__file__).parent

#Apuntamos desde el archivo main hacia la carpeta de interes (Carpeta_fotos) para extraer las fotos 1p1
Archivo_fotos = Raiz_utils / "Carpeta_Fotos_Entrada"

#prueba de foto exacta
#ruta = Archivo_fotos / "Prueba.jpg"

"""Rutas de Archivo Almacen"""

Raiz_utils_Almacen = Path(__file__).parent

Archivo_Almacen = Raiz_utils_Almacen / "Carpeta_Fotos_Almacen"


#def Extraccion_Meta_Data_vol():
#"""Te extrae todos los datos"""
#    with exiftool.ExifToolHelper() as exi:
#        lol = exi.get_metadata(Archivo_fotos)
#        for info in lol:
#             for clave, valor in info.items():
#                 print(f"{clave}, {valor}")


def Hash_foto_video(Word_to_Hash):
    global Hash_complete 
    Hash_complete = hashlib.sha256(Word_to_Hash.encode("utf-8")).hexdigest()

    #
    return Hash_complete


global tag_final
def Extraccion_Meta_Data():

    """Van los metadatos extraidos de la foto a procesar"""
    tags_extraccion = [ #deben ir las etiquetas que se deben extraer y coincidir con la sql
        "File:FileName", #filename
        "hash", #Name_Storage
        "File:MIMEType", #Media_type
        "File:FileType", #Media_type_fast
        #"File:FileSize", #file_size 
        #"File:FileSize"#"La fecha de subida del archivo en la nube"
        #"EXIF:DateTimeOriginal", #fecha que se tomo la foto
        #"ruta de la miniatura"
        #"Duration" #duracion del video 
        #"EXIF:Model",
    ]


    fotos_pendientes = []
    Extenciones = {".jpg"}

    for i in Archivo_fotos.iterdir():
         if i.is_file():
            if i.suffix.lower() in Extenciones:
                 fotos_pendientes.append(i)

    for foto_individual in fotos_pendientes:
        tag_final = []
        

        with exiftool.ExifToolHelper() as exi:

            extraccion_Meta = exi.get_tags([foto_individual], tags_extraccion)

        for info in extraccion_Meta:
            for tags in tags_extraccion:
                
                no_disponible = "No cuenta con Valor"
                if "hash" in tags:
                    tag_final.append(Hash_foto_video("lol"))
                
                else:
                    valor_2 = info.get(tags)#, no_disponible)
                    tag_final.append(valor_2)
        print(tag_final)                      

        return tag_final



def Conexion_sql():
    conn = sqlite3.connect("Prueba_tags.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            """CREATE TABLE prueba(
                    Filename TEXT,
                    DatetimeOriginal DATETIME,
                    Model TEXT,
                    prueba TEXT
                    )"""
        )
        conn.commit()
        conn.close()
    except:
        sqlite3.OperationalError()
        print("La tabla existe :( y hay conexion")

def Meta_data_envio_datos_a_db(metas):
    conn = sqlite3.connect("Prueba_tags.db")
    cursor = conn.cursor()
    Data_Meta = metas
    instruccion = f"INSERT INTO prueba VALUES (?, ?, ?, ?)"
    print(Data_Meta)
    cursor.execute(instruccion, Data_Meta)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #Extraccion_Meta_Data_vol()
    Datos = Extraccion_Meta_Data()
    print(Datos)
    #Conexion_sql()
    #Meta_data_envio_datos_a_db(Datos)
    