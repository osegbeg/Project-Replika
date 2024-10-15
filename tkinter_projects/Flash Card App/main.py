import random
import pandas
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_dict = {}
# ---------------------------- FUNCTIONALITIES ------------------------------- #

try:
    words_file = pandas.read_csv("/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = words_file.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    clear_word()
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(title_label, text="French", fill= "black")
    canvas.itemconfig(bg_image, image=image_front)
    flip_timer = window.after(4000, flip_card)

def is_known():
    words_dict.remove(current_card)
    words = pandas.DataFrame(words_dict)
    words.to_csv("./words_to_learn.csv", index=False)
    next_card()

def clear_word():
    canvas.itemconfig(word_label, text="")


def flip_card():
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(bg_image, image=image_back)





# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = Tk()
window.title("My Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(4000, flip_card)


# Create canvas for flash card front
canvas = Canvas(width=800, height=526)
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400, 263, image=image_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
title_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()

window.mainloop()





