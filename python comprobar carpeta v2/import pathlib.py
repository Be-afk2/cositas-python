import pathlib
from pathlib import Path
from os import mkdir
ubicacion=str(pathlib.Path(__file__).parent.absolute())
def comprobar_carpeta(ubicacion):
    if Path(ubicacion+"\carpeta").exists()==True:
        print("carpeta ya creada ")
    else:
        print("archivos creados")   
        mkdir(ubicacion+"\carpta")
    if Path(ubicacion+"\carpeta"+"\historial.txt").exists()==True:
        print("txt ya creado")
    else:     
        archivo=open(ubicacion+"\carpeta"+"\historial.txt","a")
        print("txt creado")
comprobar_carpeta(ubicacion)        
        
archivo=open(ubicacion+"\carpeta"+"\historial.txt","a")
archivo.write("hola  ")
archivo.close()