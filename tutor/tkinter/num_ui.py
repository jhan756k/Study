import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("숫자 맞추기 (GUI)")
window.geometry("420x220")

answer = random.randint(1, 1000)
tries = 0

info = tk.Label(window, text="숫자를 맞춰보세요! (1 ~ 1000)", font=("Arial", 12))
info.pack(pady=(10, 5))

entry = tk.Entry(window, width=12, font=("Arial", 14))
entry.pack()

submit_btn = tk.Button(window, text="제출", width=10)
submit_btn.pack(pady=6)

feedback = tk.Label(window, text="", font=("Arial", 11))
feedback.pack()

attempt_label = tk.Label(window, text="시도: 0", font=("Arial", 10))
attempt_label.pack(pady=(6, 4))

bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=6)

def start_new_game():
    global answer, tries
    answer = random.randint(1, 1000)
    tries = 0
    attempt_label.config(text="시도: 0")
    feedback.config(text="새 게임 시작! 숫자를 맞춰보세요.")
    entry.config(state="normal")
    submit_btn.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus()

def submit_guess():
    global tries, answer
    s = entry.get().strip()
    if s == "":
        feedback.config(text="숫자를 입력하세요.")
        return
    try:
        guess = int(s)
    except ValueError:
        feedback.config(text="유효한 숫자를 입력하세요.")
        return

    tries += 1
    attempt_label.config(text=f"시도: {tries}")

    if guess < answer:
        feedback.config(text=f"정해진 숫자는 {guess}보다 큽니다.")
        entry.delete(0, tk.END)
    elif guess > answer:
        feedback.config(text=f"정해진 숫자는 {guess}보다 작습니다.")
        entry.delete(0, tk.END)
    else:
        feedback.config(text="맞습니다!")
        messagebox.showinfo("정답", f"정답입니다! {tries}번 만에 맞혔습니다.")
        entry.config(state="disabled")
        submit_btn.config(state="disabled")

submit_btn.config(command=submit_guess)

new_game_btn = tk.Button(bottom_frame, text="새 게임", width=12, command=start_new_game)
new_game_btn.pack(side="left", padx=8)

quit_btn = tk.Button(bottom_frame, text="종료", width=12, command=window.destroy)
quit_btn.pack(side="right", padx=8)

window.mainloop()
