from tkinter import *
import pandas as pnd
import random as rnd

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
# ------------------------ Data input ----------------------------------------------#
try:
    data = pnd.read_csv("data/words_to_learn.csv")


except FileNotFoundError:
    data = pnd.read_csv("data/french_words.csv")
    data_dict = data.to_dict('records')
except pnd.errors.EmptyDataError:
    data = pnd.read_csv("data/french_words.csv")
    data_dict = data.to_dict('records')
else:
    data_dict = data.to_dict('records')

# ------------------------ Functions----------------------------------------------#


def next_word():
    global list_position
    if len(data_dict) > 0:
        list_position = rnd.randint(0, len(data_dict) - 1)
        new_french_word = data_dict[list_position]["French"]
        canvas.itemconfig(language_text, text="French")
        canvas.itemconfig(canvas_image, image=CARD_FRONT_IMAGE)
        canvas.itemconfig(word_text, text=new_french_word)

        def change_background(list_position):
            canvas.itemconfig(canvas_image, image=CARD_BACK_IMAGE)
            new_english_word = data_dict[list_position]["English"]
            canvas.itemconfig(language_text, text="English")
            canvas.itemconfig(word_text, text=new_english_word)

        window.after(3000, lambda: change_background(list_position))
    else:
        canvas.itemconfig(word_text, text="No more words!")

def update_file():
    words = pnd.DataFrame.from_dict(data_dict)
    words.to_csv('data/words_to_learn.csv', index=False)


def right_answer():
    del data_dict[list_position]
    update_file()
    next_word()


def wrong_answer():
    next_word()






# ------------------------ UI Definitions----------------------------------------------#


window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

next_word()

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=wrong_answer)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

window.mainloop()
