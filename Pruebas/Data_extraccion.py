import exifread
from PIL import Image

def Extraccion_Meta_Data():
    with open("Prueba.jpg", "rb") as md:
        tags = exifread.process_file(md)

    for tag in tags.keys():
        print(tag, ":", tags[tag])




if __name__ == "__main__":
    Extraccion_Meta_Data()