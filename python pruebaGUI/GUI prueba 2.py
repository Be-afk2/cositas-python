from tkinter import *
raiz=Tk()
miframe=Frame(raiz,width="300",height="300")
miframe.config(bg="black")
miframe.pack()    
imagen=PhotoImage(file=r"C:\Users\cleoe\Desktop\benja\pruebaGUI\cubune1.png")                                    #este de abajo cmbia el fotmato y tamaño
Label(miframe,image=imagen).place(x=1,y=2)              #"hola",fg="White",bg="black",font=("Arial",12)) #crar una cadena de texto
 #permite colocar el texto medicante cordenadas
#se puede abreviar asi si no la usamos mas:Label(miframe,text="hola").place(x=50,y=100)

raiz.mainloop()