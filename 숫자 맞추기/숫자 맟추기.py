import tkinter as tk
import random
from tkinter import messagebox

def 새게임():
    global 정답, 시도수, 최소값, 최대값
    정답 = random.randint(1, 100)
    시도수 = 0
    최소값 = 1
    최대값 = 100
    결과["text"] = ""
    입력창.delete(0, tk.END)

def 확인():
    global 시도수, 최소값, 최대값
    try:
        입력값 = int(입력창.get())
    except:
        결과["text"] = "숫자만 입력해 주세요 🙈"
        return

    if 입력값 < 1 or 입력값 > 100:
        결과["text"] = "1부터 100 사이 숫자만 가능해요!"
        return

    시도수 += 1

    if 입력값 < 정답:
        최소값 = max(최소값, 입력값 + 1)
        결과["text"] = "조금 더 ↑ 큰 숫자에요!"
    elif 입력값 > 정답:
        최대값 = min(최대값, 입력값 - 1)
        결과["text"] = "조금 더 ↓ 작은 숫자에요!"
    else:
        messagebox.showinfo("✨ 정답!", f"🎉 {시도수}번 만에 맞췄어요!\n다시 해볼까요?")
        새게임()
        return

    결과["text"] += f"\n➡️ 현재 범위: {최소값} 이상 {최대값} 이하"

화면 = tk.Tk()
화면.title("🎲 숫자 추측 게임")
화면.geometry("400x300")
화면.configure(bg="#fef9f4")

tk.Label(화면, text="숫자 맞춰볼래요?", font=("Helvetica", 18, "bold"), bg="#fef9f4", fg="#333").pack(pady=(20, 10))
tk.Label(화면, text="1부터 100 사이의 숫자를 입력해 주세요 🎯", font=("Helvetica", 12), bg="#fef9f4", fg="#555").pack(pady=(0, 10))

입력창 = tk.Entry(화면, font=("Helvetica", 14), justify='center')
입력창.pack(pady=5)

tk.Button(화면, text="확인!", command=확인, font=("Helvetica", 12), bg="#ffd966", activebackground="#ffe599").pack(pady=10)

결과 = tk.Label(화면, text="", font=("Helvetica", 12), bg="#fef9f4", fg="#d35400")
결과.pack(pady=10)

새게임()
화면.mainloop()
