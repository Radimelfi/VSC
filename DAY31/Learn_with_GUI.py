from tkinter import *
import random
import pandas as pd

data = pd.read_csv("french_words.csv")
to_learn = data.to_dict(orient="records")
random_choice ={}

def next_card():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.choice(to_learn)
    # print(random_choice["french"])
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= random_choice["French"], fill= "black")
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= random_choice["English"], fill= "white")
    canvas.itemconfig(card_background, image =card_back_png)

def is_known():
    to_learn.remove(random_choice)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.cvs")
    next_card()


bg = "#B1DDC6" # background
window =Tk()    
window.title("Learn with me")
window.config(padx=50, pady=50, bg= bg)

flip_timer= window.after(3000, func=flip_card) #3000 mean 3 second

canvas = Canvas(width=800, height=526)
card_front_png = PhotoImage(file="card_front.png")
card_back_png = PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263, image=card_front_png)
card_title=canvas.create_text(400,150,text= "Title", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400,263, text="Word", font=("Ariel",60, "bold"))
canvas.config(bg =bg, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

buttonr_png= PhotoImage(file="right.png")
Known_button= Button(image=buttonr_png, command=is_known)
Known_button.grid(row=1, column=0)

buttonw_png= PhotoImage(file="wrong.png")
Unknown_button= Button(image=buttonw_png, command=next_card)
Unknown_button.grid(row=1, column=1)
next_card() # necesary to show the next card intead of word and title 



window.mainloop() 