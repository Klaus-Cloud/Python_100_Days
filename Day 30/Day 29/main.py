from tkinter import *  # * imports just  classes
from tkinter import messagebox
from functions import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_button_clicked():
    newPassword = password_generator()
    password_entry.insert(0, newPassword)
    pyperclip.copy(newPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    info = info_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "Email": info,
        "Password": password,
    }}
    if len(website) * len(password) == 0:
        messagebox.showerror(title="Invalid Input", message="One of the inputs has no text")
    else:
        try:
            with open("result.json", 'r') as file:
                # Reading old Data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("result.json", 'w') as file:
                # Writing New file
                json.dump(new_data, file, indent=4)
        else:
            with open("result.json", 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- Look for password ------------------------------- #


def look_for_info():
    website = website_entry.get()
    try:
        with open("result.json", 'r') as file:
            # Reading old Data
            data = json.load(file)
            stored_email = data[website]["Email"]
            stored_password = data[website]["Password"]
    except FileNotFoundError:
        messagebox.showerror(title="FileNotFound", message="There is no file with data")
    except KeyError:
        messagebox.showerror(title="KeyError", message="There is no website data")
    else:
        messagebox.showinfo(title="Info", message=f"Email: {stored_email}\n Password: {stored_password}")


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

info_entry = Entry(width=35)
info_entry.grid(column=1, row=2, columnspan=2)
info_entry.insert(0, "niklas@usp.br")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_generator_button = Button(text="Generate Password", command=password_button_clicked)
password_generator_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=12, command=look_for_info)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()
