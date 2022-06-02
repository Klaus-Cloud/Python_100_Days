from tkinter import *


def buttonClicked():
    milesValue = float(input.get())
    kmValue = 1.6 * milesValue
    answer_label.config(text=f"{kmValue}")


# Window definition
window = Tk()
window.title("Mile to km converter")
window.wm_minsize(width=200, height=100)
window.config(padx=10, pady=10)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label()
answer_label.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=buttonClicked)
button.grid(column=1, row=2)


window.mainloop()
