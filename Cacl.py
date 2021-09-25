from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
import math
import sys

root = Tk()
root.geometry('950x650')
root.title("Калькулька")
bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3", "=", "x^n",
"0", ".", "+-", "C",
"Exit", "Pi", "sin", "cos",
"(",")","n!","x^(1/2)","e^x"]

r=1
c=0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    tk.Button(root, text=i, command = cmd, height = 6, width = 8, font=("Calibri",10)).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33, font=("Calibri", 45), bg="#000000", fg="#FFFFFF", disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=0)
calc_entry.grid(row = 0, column = 0, columnspan = 5, sticky= 'ew')

#oop
#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END,"Первый символ не цифра" )
            messagebox.showerror("Ошибка!Вы ввели не номер!")
#исчесления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))    
        except:
            calc_entry.delete(0, END)
            calc_entry.insert(END,"Ошибка!")
            messagebox.showerror("Ошибка!", "Проверьте корректность введённых данных")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "+-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass                    
    elif key == "Pi":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    elif key == "x^2":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" +str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" +str(math.cos(int(calc_entry.get())))) 
    elif key == "n!":
        calc_entry.insert(END, "=" +str(math.factorial(int(calc_entry.get()))))       
    elif key == "x^(1/2)":
        calc_entry.insert(END, "^(1/2)")
        calc_entry.insert(END, "=" +str(math.sqrt(int(int(calc_entry.get())))))   
    elif key == "x^n":
        stepen = Tk()
        stepen.title("Ввод степени")
        calc_stepen = Entry(stepen, width = 20)
        calc_stepen.grid(row = 0, column = 0, columnspan = 1)
        tk.Button(stepen, text="Готово", command = lambda: [funcApow(calc_entry,calc_stepen), funcB(stepen)] , height = 3, width = 8, font=("Calibri",10)).grid(row = 1, column = 0)  
    elif key == "e^x":
        exp = Tk()
        exp.title("Ввод степени экспоненты")
        calc_exp = Entry(exp, width = 20)
        calc_exp.grid(row = 0, column = 0, columnspan = 1)
        tk.Button(exp, text="Готово", command = lambda: [funcAexp(calc_entry,calc_exp), funcB(exp)] , height = 3, width = 8, font=("Calibri",10)).grid(row = 1, column = 0)              
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")    
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

def funcApow(self,belf):
    #self.insert(END," ^ "+str(belf.get()))
    p = math.pow(int(self.get()),int(belf.get()))
    self.insert(END," ^ "+str(belf.get()))
    self.insert(END, "=" +str(p))
def funcAexp(self,belf):
    self.insert(END, "e^" +str(belf.get()))
    self.insert(END, " = " +str(math.exp(int(belf.get()))))      
def funcB(gelf):
    gelf.after(1,gelf.destroy)   

       


root.mainloop()
