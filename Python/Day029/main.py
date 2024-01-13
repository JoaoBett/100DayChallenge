import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
cur_card = {}
to_learn = {}

try :
    data = pandas.read_csv("Day029/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day029/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=cur_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=cur_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(cur_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day029/data/words_to_learn.csv", index=False)
    next_card()

#------------------------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)
 
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Day029/images/card_front.png")
card_back_img = PhotoImage(file="Day029/images/card_back.png")
card_bg = canvas.create_image(400,263, image=card_front_img)
canvas.grid(column=0, row=0)
card_title = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


cross_image = PhotoImage(file="Day029/images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unkown_button.grid(column=0,row=1)

check_image = PhotoImage(file="Day029/images/right.png")
unkown_button = Button(image=check_image, highlightthickness=0,command=next_card)
unkown_button.grid(column=1,row=1)

next_card()


window.mainloop()