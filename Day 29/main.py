from tkinter import * # * imports just  classes
from tkinter import messagebox
from functions import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#

def password_button_clicked():
    newPassword = password_generator()
    password_entry.insert(0, newPassword)
    pyperclip.copy(newPassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    info = info_entry.get()
    password = password_entry.get()
    result = website + " | " + info + " | " + password + "\n"
    if len(website)*len(password) == 0:
        messagebox.showerror(title="Invalid Input", message="One of the inputs has no text")
    else:
        answer = messagebox.askyesnocancel(title=website, message=f"Would you like to add {result} to the file ?")
        if answer:
            with open("result.txt", 'a') as file:
                file.write(result)
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

info_label = Label(text="Email/Username:")
info_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

info_entry = Entry(width=35)
info_entry.grid(column=1, row=2, columnspan=2)
info_entry.insert(0, "niklas@usp.br")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_generator_button = Button(text="Generate Password", command=password_button_clicked)
password_generator_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data )
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
