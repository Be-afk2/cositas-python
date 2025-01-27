from tkinter import *
raiz=Tk()
raiz.config(bg="#d5dbdb",bd=5,relief="sunken")
raiz.iconbitmap(r"C:\Users\cleoe\Desktop\benja\pruebaGUI\cubune.ico")
#----frame--------

frame1=Frame(raiz)
frame1.pack()
frame1.config(bg="grey")
#----pantalla-----
numeropantalla=StringVar()
pantalla=Entry(frame1)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="black",justify="right",fg="#03f943",)

#----bototesfila1------
botonn7=Button(frame1,text="7",width="3",height="2")
botonn7.grid(row=2,column=1)
botonn8=Button(frame1,text="8",width="3",height="2")
botonn8.grid(row=2,column=2)
botonn9=Button(frame1,text="9",width="3",height="2")
botonn9.grid(row=2,column=3)
botonndiv=Button(frame1,text="/",width="3",height="2")
botonndiv.grid(row=2,column=4)
#----bototesfila2------

botonn4=Button(frame1,text="4",width="3",height="2")
botonn4.grid(row=3,column=1)
botonn5=Button(frame1,text="5",width="3",height="2")
botonn5.grid(row=3,column=2)
botonn6=Button(frame1,text="6",width="3",height="2")
botonn6.grid(row=3,column=3)
botonX=Button(frame1,text="X",width="3",height="2")
botonX.grid(row=3,column=4)

#----bototesfila3------

botonn1=Button(frame1,text="1",width="3",height="2")
botonn1.grid(row=4,column=1)
botonn2=Button(frame1,text="2",width="3",height="2")
botonn2.grid(row=4,column=2)
botonn3=Button(frame1,text="3",width="3",height="2")
botonn3.grid(row=4,column=3)
botonres=Button(frame1,text="-",width="3",height="2")
botonres.grid(row=4,column=4)

#----bototesfila4------

botonn0=Button(frame1,text="0",width="3",height="2")
botonn0.grid(row=5,column=2)
botoncoma=Button(frame1,text=".",width="3",height="2")
botoncoma.grid(row=5,column=1)
botonigual=Button(frame1,text="=",width="3",height="2")
botonigual.grid(row=5,column=3)
botonsuma=Button(frame1,text="+",width="3",height="2")
botonsuma.grid(row=5,column=4)

raiz.mainloop()