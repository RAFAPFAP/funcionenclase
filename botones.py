from tkinter import *


def sumar():
    r.set(float (n1.get())+float (n2.get()))

root = Tk()

root.config(bd=15)

n1= StringVar()
n2= StringVar()
r= StringVar()
Label(root,text='Numero1').pack()
Entry(root,justify='center',textvariable=n1).pack()#numero 1
Label(root,text='Numero2').pack()
Entry(root,justify='center',textvariable=n2).pack()#numero 2
Label(root,text=' ').pack()
Button(root,text='Sumar',command=sumar).pack()
Label(root,text='\nResultado').pack()
Entry(root,justify='center',textvariable=r).pack()#resultado




root.mainloop()