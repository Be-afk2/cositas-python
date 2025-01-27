from tkinter import *
raiz=Tk()  #crear la ventana (raiz) puede tener cualquier nombre

raiz.title("CovsJ") # le da titulo

raiz.iconbitmap(r"C:\Users\cleoe\Desktop\benja\pruebaGUI\cubune.ico") # cambiar el icono

#raiz.geometry("350x350") #cambiar el ancho

raiz.config(bg="black") #cambiar el color del fondo

raiz.resizable(1,1)  #ancho,alto     width,height      permite que no se pueda cambiar el ancho ni el alto

miframe=Frame()  #crar una ventana nueva

miframe.pack(side="bottom", anchor="s")

miframe.config(bd="35")
miframe.config(relief="groove") #cambia los vordes 

miframe.config(bg="red") #cambiar de color a la nueva ventana

miframe.config(cursor="pirate")
miframe.config(width="650",height="350") #darle tamaño a la nueva ventana que esta debtro de raiz
raiz.mainloop() #siempre al ultimo

