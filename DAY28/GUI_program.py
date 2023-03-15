from tkinter import * 
# ---------------------------- CONSTANTS ------------------------------- #
# web palette of color: color Hunt 
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------------- # 

# ---------------------------- TIMER MECHANISM ---------------------------------- # 
def Start_time():
    count_down(5*60)
    
   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time 
import math 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec==0:
        count_sec="00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        window.after(1000,count_down, count -1)

# ----------------------------------- UI SETUP -------------------------------------- #

window = Tk()
window.title("The thecnique of pomodoro")
window.config(padx=100, pady=50)
# window.configure(background='white')
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background= YELLOW, highlightthickness=0)
canvas.create_image(103,112, image= tomato_img)
timer_text = canvas.create_text(103,130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1) 
timer_label = Label(text="Timer", foreground= GREEN, font=(FONT_NAME, 50), background= YELLOW).grid(column=1, row=0)
check_mark = Label(text="✔️").grid(column=1, row=3)
star_button= Button(text="Start",  highlightthickness=0, command=Start_time).grid(column=0 ,row=2)
reset_button = Button(text="Reset" , highlightthickness=0).grid(column=2, row=2)

window.mainloop()
