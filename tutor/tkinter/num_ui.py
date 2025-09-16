import tkinter as tk
from tkinter import messagebox
import random

# --- 초기 설정 ---
window = tk.Tk()
window.title("숫자 맞추기 (GUI)")
window.geometry("420x220")
window.resizable(False, False)

# 정답과 시도 수 (초기 게임 시작)
answer = random.randint(1, 1000)
tries = 0

# --- 위젯 배치 ---
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

# 하단 버튼 프레임 (새 게임, 종료)
bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=6)

def start_new_game():
    """새 게임 시작: 정답 재설정, 카운트 초기화, 입력 초기화"""
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
    """입력값 검증 및 정답 판정"""
    global tries, answer
    s = entry.get().strip()
    if s == "":
        feedback.config(text="숫자를 입력하세요.")
        return
    # 숫자 변환 안전처리
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
        feedback.config(text="맞습니다! 🎉")
        messagebox.showinfo("정답", f"정답입니다! {tries}번 만에 맞혔습니다.")
        # 정답 후 입력 막기 (원하면 자동 새 게임으로 바꿀 수 있음)
        entry.config(state="disabled")
        submit_btn.config(state="disabled")

# 버튼 연결
submit_btn.config(command=submit_guess)

new_game_btn = tk.Button(bottom_frame, text="새 게임", width=12, command=start_new_game)
new_game_btn.pack(side="left", padx=8)

quit_btn = tk.Button(bottom_frame, text="종료", width=12, command=window.destroy)
quit_btn.pack(side="right", padx=8)

# 엔터키로 제출되도록 바인딩 (Entry 포커스가 없어도 작동)
window.bind('<Return>', lambda event: submit_guess())

# 시작 시 포커스
entry.focus()

# --- 메인 루프 ---
window.mainloop()
