import tkinter as tk
from tkinter import messagebox

# 로그인 페이지
'''
1. 로그인 페이지 레이블
2. id 엔트리 칸
3. 비밀번호 엔트리 칸
4. 입력 확인 버튼
5. 입력 시 맞았는지 틀렸는지 alert 창
'''

window = tk.Tk()
window.title("Test")
window.geometry("400x300")

loginpage = tk.Label(window, text="로그인 페이지")
loginpage.pack()

id = tk.Entry(window, width=25)
id.pack()

a = tk.Entry(window, width=25)
a.pack()

def btn_cilcked():
    if id.get() == "김주원" and a.get() == "비밀번호":
        messagebox.showinfo("알림", "안녕하세요")
    else:
        messagebox.showerror("알림", "비밀번호가 틀렸습니다")
btn1 = tk.Button(window,text="입력", command=btn_cilcked)
btn1.pack()

window.mainloop()