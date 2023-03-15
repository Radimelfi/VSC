import tkinter
# creating windows and Labels with Tkinter 

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width= 500, height = 300)

# Label 
my_label = tkinter.Label(text= "GUI PROGRAM", font= ("Arial", 10))
my_label.pack() # pack necesarry to reflect the component 

# making changes to the privios label
my_label["text"]= "THE FIRST GUI PROGRAM"
#My_label.config(text = "FIRST GUI PROGRAM") another way to do it 


# Botton
botton = tkinter.Button(text="Save")
botton.place(x= 10 ,y= 10)

# Entry 

input_text = tkinter.Entry()
input_text.pack()

window.mainloop() # necesarry to go at the end.


