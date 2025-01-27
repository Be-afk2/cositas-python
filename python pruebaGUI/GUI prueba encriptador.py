from tkinter import *
raiz=Tk()
raiz.config(bg="black")
#--------frame---------
frame1=Frame(width=200,height=200)
frame1.config(bg="black")
frame1.pack()

#------botojes inicio-----------
botoninicio=Button(frame1)
botoninicio.config(text="traspasar",pady=5,padx=5)
botoninicio.grid(row=1,column=1)

botoninicio=Button(frame1)
botoninicio.config(text="info",pady=5,padx=5)
botoninicio.grid(row=2,column=1)

botoninicio=Button(frame1)
botoninicio.config(text="salir",pady=5,padx=5)
botoninicio.grid(row=3,column=1)
raiz.mainloop()