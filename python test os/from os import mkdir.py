from os import mkdir
import pathlib
numero=int(1)
ubicacion=str(pathlib.Path(__file__).parent.absolute())
print("--------------",ubicacion,"-----------------")

while numero<=10:
    numero=str(numero)
    mkdir(ubicacion+"\carpeta"+numero)
    numero=int(numero)
    numero=numero+1

    