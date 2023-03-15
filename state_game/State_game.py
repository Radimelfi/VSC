import turtle 
import pandas 

screen = turtle.Screen()
screen.title("States Game")
imagen = ("blank_states_img.gif")
screen.addshape(imagen)
turtle.shape(imagen)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_answer = []

while len(guessed_answer) < 50:
    question = screen.textinput(title= (f"your currenly score is {len(guessed_answer)}/50"), prompt= " what's another states you know ?").title()
   
    if question == "Exist":
        missing_state = []
        for state in states_list:
            if state  not in guessed_answer:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_lear.csv")
        break
    if question in states_list:
        guessed_answer.append(question)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == question]
        t.goto(int (state_data["x"]), int(state_data["y"]))
        t.write(question)



# def get_mouse_click(x,y):
# print(x,y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
# screen.exitonclick()