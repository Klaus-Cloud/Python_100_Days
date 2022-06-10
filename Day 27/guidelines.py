import tkinter

window = tkinter.Tk()
window.title("My GUI")
window.wm_minsize(width=700, height=500)
window.config(padx=200, pady=200)
# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 25, "bold"))
my_label["text"] = "New text"
my_label.config(text="Really?")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=20)

# Buttons
def buttonClicked():
    print("I got clicked")
    text = input.get()
    my_label.config(text=text)


button = tkinter.Button(text="Press me", command=buttonClicked)
button.grid(column=1, row=1)

newButton = tkinter.Button(text="I am a special button", command=buttonClicked)
newButton.grid(column=2, row=0)
# Entry
input = tkinter.Entry(width=10)
input.insert(1, string="Type here.")
input.grid(column=3, row=2)
# Text

# Start the program
window.mainloop()
