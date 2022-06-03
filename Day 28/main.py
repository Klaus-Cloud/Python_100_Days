from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_round = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_check_marks():
    global work_round
    work_round = ""
    check_marks.config(text=work_round)


def reset_timer():
    global timer,reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    reset_check_marks()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def increase_check_marks():
    global work_round
    work_round += " ✔"
    check_marks.config(text=work_round)


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:  # Work out
        timer_label.config(text="Work", fg=RED)
        count_down(WORK_MIN*60)
    elif reps % 8 == 0:  # Long break
        timer_label.config(text="Long Break", fg=GREEN)
        count_down(LONG_BREAK_MIN*60)
        reset_check_marks()
    elif reps % 2 == 0:  # Short Break
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    if count >= 0:
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        if minutes < 10:
            minutes = f"0{minutes}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            increase_check_marks()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
