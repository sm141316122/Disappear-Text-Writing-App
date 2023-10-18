from tkinter import *


timer = None
count_num = 5


def count(num):
    global timer, count_num

    time_label.config(text=f"Timer: {num}", fg="#8B7E74")
    count_num = num

    if num < 3:
        time_label.config(fg="red")

    if num == 0:
        window.after_cancel(timer)
        text.delete(1.0, END)
        time_label.config(text="Delete")
        count_num = 5
    else:
        timer = window.after(1000, count, count_num - 1)


def keep_typing(event):
    global timer, count_num

    if timer:
        window.after_cancel(timer)
        count_num = 5

    count(count_num)


window = Tk()
window.geometry("800x600")
window.title("Disappearing Text Writing App")
window.config(bg="#F3EFE0")

title_label = Label(text="Keep Writing !", bg="#F3EFE0", font=("Arial", 28), fg="#434242")
title_label.pack(pady=50)

text = Text(width=40, height=10, font=("Arial", 20))
text.pack(pady=15)

time_label = Label(text="Hi", bg="#F3EFE0", font=("Arial", 28), fg="#8B7E74")
time_label.pack()

text.bind("<KeyPress>", keep_typing)

window.mainloop()
