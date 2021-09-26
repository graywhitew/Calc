from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
import math
import sys


#Setting.NewWindow(root,'950x650',"Калькулька")

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
        Calculator.C(calc_entry)
    elif key == "+-":
        Calculator.plusminus(calc_entry)                  
    elif key == "Pi":
        Calculator.Pi(calc_entry)
    elif key == "Exit":
        Calculator.Exit(root)
    elif key == "x^2":
        Calculator.Quadr(calc_entry)
    elif key == "sin":
        Calculator.Sin(calc_entry)
    elif key == "cos":
        Calculator.Cos(calc_entry)
    elif key == "n!":
        Calculator.Factorial(calc_entry)
    elif key == "x^(1/2)":
        Calculator.Sqrt(calc_entry)  
    elif key == "x^n":
        Calculator.Pow(calc_entry)
    elif key == "e^x":
        Calculator.Ex(calc_entry)    
    elif key == "(":
        Calculator.LeftBracket(calc_entry)
    elif key == ")":
        Calculator.RightBracket(calc_entry)   
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


class Calculator():
    def C(entry):
        entry.delete(0, END)
    def plusminus(entry):
        if "=" in entry.get():
            entry.delete(0, END)
        try:
            if entry.get()[0] == "-":
                entry.delete(0)
            else:
                entry.insert(0, "-")
        except IndexError:
            pass                    
    def Pi(entry):
        entry.insert(END, math.pi)
    def Exit(Table):
        Table.after(1,Table.destroy)
        sys.exit
    def Quadr(entry):
        entry.insert(END, "**")
    def Sin(entry):
        entry.insert(END, "=" +str(math.sin(int(entry.get()))))
    def Cos(entry):
        entry.insert(END, "=" +str(math.cos(int(entry.get())))) 
    def Factorial(entry):
        entry.insert(END, "=" +str(math.factorial(int(entry.get()))))       
    def Sqrt(entry):
        c=math.sqrt(int(int(entry.get())))
        entry.insert(END, "^(1/2)")
        entry.insert(END, "=" +str(c))   
    def Pow(entry):
        stepen = Tk()
        stepen.title("Ввод степени")
        calc_stepen = Entry(stepen, width = 20)
        calc_stepen.grid(row = 0, column = 0, columnspan = 1)
        tk.Button(stepen, text="Готово", command = lambda: [funcApow(entry,calc_stepen), funcB(stepen)] , height = 3, width = 8, font=("Calibri",10)).grid(row = 1, column = 0)  
    def Ex(entry):
        #Setting.NewWindow(exp,'950x650',"Калькулька")
        exp = Tk()
        exp.title("Ввод степени экспоненты")
        calc_exp = Entry(exp, width = 20)
        calc_exp.grid(row = 0, column = 0, columnspan = 1)
        tk.Button(exp, text="Готово", command = lambda: [funcAexp(entry,calc_exp), funcB(exp)] , height = 3, width = 8, font=("Calibri",10)).grid(row = 1, column = 0)              
    def LeftBracket(entry):
        entry.insert(END, "(")
    def RightBracket(entry):
        entry.insert(END, ")")    

class Setting:
    def NewWindow(screen,size,text):
        screen = Tk()
        screen.geometry(str(size))
        screen.title(str(text))




def funcApow(self,belf):
    p = math.pow(int(self.get()),int(belf.get()))
    self.insert(END," ^ "+str(belf.get()))
    self.insert(END, "=" +str(p))
def funcAexp(self,belf):
    self.insert(END, "e^" +str(belf.get()))
    self.insert(END, " = " +str(math.exp(int(belf.get()))))      
def funcB(gelf):
    gelf.after(1,gelf.destroy)   
    

root.mainloop()
