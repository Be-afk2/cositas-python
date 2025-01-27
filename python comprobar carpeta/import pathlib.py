import pathlib
from pathlib import Path
from os import mkdir

ubicacion=str(pathlib.Path(__file__).parent.absolute())

def verificar_archivos(ubicacion):
    if Path(ubicacion+"\carpeta_contenedora").exists()==True:
        print("carpeta ya existe ")
    else:
        mkdir(ubicacion+"\carpeta_contenedora")
        print("carpeta creada") 
    if Path(ubicacion+"\carpeta_contenedora"+"\historialc.txt").exists()==True:
        print("historial c si existe ")
    else:
        historialc=open(ubicacion+"\carpeta_contenedora"+"\historialc.txt","a")
        print("historial creado")   
   
verificar_archivos(ubicacion)