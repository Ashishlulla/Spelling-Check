import tkinter as tk
from tkinter import ttk, PhotoImage
from textblob import TextBlob

root = tk.Tk()
root.title("Spell Check")
root.geometry("400x300")
root.resizable(0, 0)
root.config(bg="#ffabe0")


# ------------------------------------- Functionality ------------------------------

def spell_check():
    word = spelling_var.get()
    a = TextBlob(word)
    right = str(a.correct())

    correct_spelling_var.set(right)


# -------------------------- Icon -------------------------------

icon = PhotoImage(file="download.png")
root.iconphoto(False, icon)

# -------------------------- Heading ----------------------------

heading = tk.Label(root, text="Spelling Check", font="arial 22 bold", fg="#ad4e8a", bg="#ffabe0")
heading.place(x=90, y=50)

# --------------------------- Entry -------------------------------

spelling_var = tk.StringVar()
spelling = tk.Entry(root, width=40, border=0, font="arial 12 bold", textvariable=spelling_var)
spelling.pack(pady=100, ipady=10)

# -------------------------- Check Button --------------------------

check = tk.Button(root, text="Check", font="arial 18 bold", fg="black", bg="#0dba10", command=spell_check)
check.place(x=150, y=160)

# ----------------------------- Correct Spelling LAbel --------------

heading = tk.Label(root, text="Correct Spelling:- ", font="arial 12 bold", fg="#ad4e8a", bg="#ffabe0")
heading.place(x=135, y=220)

# ---------------------------- Correct Spelling label --------------

correct_spelling_var = tk.StringVar()
correct_spelling = tk.Entry(root, width=20, border=0, font="arial 18 bold", textvariable=correct_spelling_var)
correct_spelling.place(x=70, y=250)

root.mainloop()
