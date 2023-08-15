from tkinter import *
from tkinter import ttk
from datetime import *

root = Tk()
root.title("수열계산기")
root.geometry("600x850")
root.resizable(False,0)
root.iconbitmap('calc.ico')

def getfvalc():
    n1, n2, v1, v2 , 등차, 첫째항, 값 = 0, 0, 0, 0, 0, 0, 0
    
    listn1 = (numberenter1.get()).split(" ")
    listn2 = (numberenter2.get()).split(" ")

    n1 = int(listn1[0])
    v1 = int(listn1[1])
    n2 = int(listn2[0])
    v2 = int(listn2[1])
    
    등차 = ((v2 - v1) / (n2 - n1))
    첫째항 = (v1 - ((n1-1)*등차))

    번 = int(indexenter.get())

    값 = (첫째항 + ((번 - 1) * 등차))


    valuelabel.config(text="제 " + str(번) + "항은 " + str(값) + " 입니다.")
    showequation(첫째항, 등차)

def getfvalb():
    n1, n2, v1, v2 , 등비, 첫째항, 값 = 0, 0, 0, 0, 0, 0, 0

    listn1 = (numberenter1.get()).split(" ")
    listn2 = (numberenter2.get()).split(" ")

    n1 = int(listn1[0])
    v1 = int(listn1[1])
    n2 = int(listn2[0])
    v2 = int(listn2[1])
    
    등비 = ((v2 / v1)**(1 / (n2 - n1)))
    첫째항 = (v1 / ((등비) ** (n1 - 1)))

    번 = int(indexenter.get())

    값 = ((첫째항)*((등비)**(번-1)))

    valuelabel.config(text= "제 " + str(번) + "항은 " + str(값) + " 입니다.")

def getsigma():

    valist = (equationenter.get()).split(" ")
    
    a = int(valist[0])
    b = int(valist[1])
    c = int(valist[2])
    sp = int(valist[3])
    ep = int(valist[4])

    sigmasum = 0

    for rotaten in range(int(sp), int(ep) + 1):
        sigmasum += solve_equation(a, b, c, rotaten)

    sigmavalabel.config(text = sigmasum)
    sigmasum = 0
    
def solve_equation(x, y, z, n):
    return int(((n**2)*x) + ((n)*y) + (z))

def showequation(a, d):
    showequationlabel.config(text= str(int(d)) + "n" + " + " + str(int(a - d)))

def resetall():
    
    valuelabel.config(text="----------")
    sigmavalabel.config(text="----------")
    showequationlabel.config(text="----------")
    numberenter1.delete(0, END)
    numberenter2.delete(0, END)
    indexenter.delete(0, END)
    equationenter.delete(0, END)

numberenter1 = ttk.Entry(root, font="Lato 30", width=8)
numberenter1.grid(column=0, row = 0, padx = 40, pady = 10)

numberenter2 = ttk.Entry(root, font="Lato 30", width=8)
numberenter2.grid(column=2, row= 0, padx = 30)

indexenter = ttk.Entry(root, font="Lato 30", width=8)
indexenter.grid(column=0, row= 2, pady = 70)

equationenter = ttk.Entry(root, font="Lato 30", width=18)
equationenter.place(x = 40, y = 380)

enterbuttonnc = ttk.Button(root, text="등차값", width=10, command= getfvalc)
enterbuttonnc.grid(column=1, row = 2)

enterbuttonnb = ttk.Button(root, text="등비값", width=10, command= getfvalb)
enterbuttonnb.grid(column=2, row = 2)

equationenterbutton = ttk.Button(root, text="시그마", width=10, command= getsigma)
equationenterbutton.place(x = 500, y = 390)

valuelabel = ttk.Label(root, font="Lato 20", wraplength= 400, text="----------")
valuelabel.place(x=50, y = 250)

equationguidelabel = ttk.Label(root, font="Lato 20", text="[ㅁn^2 + ㅁn + ㅁ], [sigma ㅁ --> ㅁ]")
equationguidelabel.place(x  = 40, y = 440)

sigmavalabel = ttk.Label(root, font="Lato 20", text="----------")
sigmavalabel.place(x = 40, y = 500)

showequationlabel = ttk.Label(root, font ="Lato 20", text = "----------")
showequationlabel.place(x=40, y = 600)

resetbutton = ttk.Button(root, text="RESET", width=10, command= resetall)
resetbutton.place(x = 430, y = 250)

root.mainloop() 