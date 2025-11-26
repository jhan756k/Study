"""
1. 할 일 추가 버튼
2. 할 일 엔트리
3. 마지막) 추가 삭제 버튼
4. 레이블 (할거 목록 순서대로 보여주기)
5. 체크박스 구현
"""
import tkinter as tk

window = tk.Tk()
window.title("할 일 목록")
window.geometry("300x550")

def make_string(tasks):
    label_text = ""
    for i in range(len(tasks)):
        label_text += (tasks[i])
        label_text += "\n"
    return label_text

def update_checkbox():
    for cb in checkbox:
        cb.destroy()
    checkbox.clear()

    for t in task:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(window, text=t, variable=var)
        cb.pack(anchor='w')
        checkbox.append(cb)

def btn_clicked():
    task.append(entry.get())
    label.config(text=make_string(task))
    update_checkbox()

def btn1_clicked():
    task.pop()
    label.config(text=make_string(task))
    update_checkbox()

def btn2_clicked():
    task.pop(int(entry1.get()))
    label.config(text=make_string(task))
    update_checkbox()

task = []
checkbox = []

entry = tk.Entry(window, width=15)
entry.pack()

btn = tk.Button(window, text="할 일 추가", command= btn_clicked)
btn.pack()

label = tk.Label(window, text="")
# label.pack()

btn1 = tk.Button(window, text="삭제", command= btn1_clicked)
btn1.pack()

entry1 = tk.Entry(window, width=15)
entry1.pack()

btn2 = tk.Button(window, text="삭제", command=btn2_clicked)
btn2.pack()

window.mainloop()
