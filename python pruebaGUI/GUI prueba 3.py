from tkinter import *
raiz=Tk()
miframe=Frame(raiz,width=1200,height=600)
miframe.pack()
miframe.config(bg="white")
raiz.config(bg="gray")

texto=Entry(miframe) #crear cuadro de texto
texto.grid(row=0,column=1)
texto.config(show="*")

texto1=Label(miframe,text="nombre:",padx=10,pady=10,) #padx/y para seprar del cuadro contenedor
texto1.grid(row=0,column=0)

textoingresar=Label(miframe,text="ingresar")
textoingresar.grid(row=1,column=1)
raiz.mainloop()