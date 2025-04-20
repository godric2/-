import tkinter as tk
import random

def play(choice):
    user_label.config(text=choice)
    comp = random.choice(['가위', '바위', '보'])
    comp_label.config(text=comp)
    if choice == comp:
        result_label.config(text='비겼습니다')
    elif (choice == '가위' and comp == '보') or (choice == '바위' and comp == '가위') or (choice == '보' and comp == '바위'):
        result_label.config(text='당신이 이겼습니다!')
    else:
        result_label.config(text='당신이 졌습니다!')

root = tk.Tk()
root.title("가위바위보")
root.geometry("300x250")
root.configure(bg="white")

title = tk.Label(root, text="가위 바위 보", font=("Arial", 20), bg="white")
title.pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack(pady=5)

tk.Button(frame, text="가위", width=8, command=lambda: play("가위")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="바위", width=8, command=lambda: play("바위")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="보", width=8, command=lambda: play("보")).grid(row=0, column=2, padx=5)

tk.Label(root, text="내 선택:", font=("Arial", 12), bg="white").pack(pady=(15, 0))
user_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="blue")
user_label.pack()

tk.Label(root, text="컴퓨터:", font=("Arial", 12), bg="white").pack()
comp_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="red")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="white", fg="green")
result_label.pack(pady=10)

root.mainloop()
