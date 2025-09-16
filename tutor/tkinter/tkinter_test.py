import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Test")
window.geometry("400x300")


juwon = tk.Label(window, text="김주원")
juwon.pack()

entry = tk.Entry(window, width=25)
entry.pack()

def btn_clicked():
    t = entry.get()
    juwon.config(text=t)
    messagebox.showinfo("알림", "안녕하세요")
    messagebox.showerror("알림", "비밀번호가 틀렸습니다")

btn1 = tk.Button(window, text="눌러보세요", command=btn_clicked)
btn1.pack()

window.mainloop()