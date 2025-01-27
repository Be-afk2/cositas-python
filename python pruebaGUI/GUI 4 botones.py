from tkinter import *
raiz=Tk()
minombre=StringVar("")


miframe=Frame(raiz,width="500",height="500")
miframe.pack()
miframe.config(bg="white")

textonombre=Label(miframe,text="nombre :",padx=10,pady=10,) #padx/y para seprar del cuadro contenedor
textonombre.grid(row=0,column=0)
ingreasarnombre=Entry(miframe,textvariable=minombre,fg="black") #crear cuadro de texto
ingreasarnombre.grid(row=0,column=1)

textocontraseña=Label(miframe,text="contraseña:",padx=10,pady=10,) #padx/y para seprar del cuadro contenedor
textocontraseña.grid(row=1,column=0)
ingresocontraseña=Entry(miframe) #crear cuadro de texto
ingresocontraseña.grid(row=1,column=1)
ingresocontraseña.config(show="*")

textoapellido=Label(miframe,text="apellido:",padx=10,pady=10,) #padx/y para seprar del cuadro contenedor
textoapellido.grid(row=2,column=0)
ingresoapellido=Entry(miframe) #crear cuadro de texto
ingresoapellido.grid(row=2,column=1)

textodirecion=Label(miframe,text="direcion:",padx=10,pady=10,) #padx/y para seprar del cuadro contenedor
textodirecion.grid(row=3,column=0)
ingresodirecion=Entry(miframe) #crear cuadro de texto
ingresodirecion.grid(row=3,column=1)

textocomentario=Label(miframe,text="comentario")
textocomentario.grid(row=4,column=0,pady=5)
comentario=Text(miframe,width=16,height=5)
comentario.grid(row=4,column=1)

barracomentario=Scrollbar(miframe,command=comentario.yview)   #crear scrollbar
barracomentario.grid(row=4,column=3,sticky="nsew")  #sticky para que se adapte a la casilla comentario
comentario.config(yscrollcommand=barracomentario.set)    #para que la barra se pocicione donde se esta viendo en el comentario
def codigo():
    minombre.set("benja")   #def para escribir el nombre en el cuadro nombre
    
botonaceptar=Button(raiz,text="enviar",pady=5,command=codigo)
botonaceptar.pack()

raiz.mainloop()