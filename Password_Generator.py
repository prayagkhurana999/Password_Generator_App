from tkinter import *
from password_generator import PasswordGenerator       #imported PasswordGenerator class from this package

password=passwordGenerator()     #instanciating the class by object
password.minlen=10    #an attribute to set minimum length to 10
password.maxlen=20
password.minuchars=2
password.maxuchars=5

#password.generate()   # it will automatically generate password according to conditions that we have set

master=Tk()

master.title("Password Generator")
dis=Entry(master)
b=button(master,text="genrate",command=create,padx=40,pady=20)
clear=button(master,text="clear",command=delete1,padx=40,pady=20)
label1=label(master,text="password generator",font=("Helvetica",17,"black,italic"))

def create():
    result=password.generate()
    dis.insert(0,result)   

def delete1():
    dis.delete(0,END)            
    
label1.grid(row=0,coloumn=0)
dis.grid(row=1,coloumn=0)
b.grid(row=2,coloumn=0,columnspan=2)
clear.grid(row=3,coloumn=0,columnspan=2)





