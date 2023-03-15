import tkinter

def miles_to_km():
    calculate = int(input.get())   
    km = calculate * 1.609344
    equal_text.config(text= f" {km}")

window = tkinter.Tk()
window.title("Calculator Mile to KM Converter")
window.minsize(width= 500, height = 300)
window.config(padx= 20 , pady=20)

millas = tkinter.Label(text="Miles").grid(column=2,row=0)
km = tkinter.Label(text="KM").grid(column=2,row=1)
equal = tkinter.Label(text= "Is equal to").grid(column=0,row=1)
equal_text = tkinter.Label(text= "0").grid(column=1,row=1)
botton = tkinter.Button(text="calculate", command= miles_to_km).grid(column=1,row=2)
input = tkinter.Entry().grid(column=1,row=0)

 
window.mainloop()


