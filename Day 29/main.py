from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.wm_minsize(width=240, height=240)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage("Day 29/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=0, row=0)

window.mainloop()