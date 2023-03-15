from tkinter import *
from tkinter import messagebox

# ------------------------------ PASSWORD GENERATOR ------------------------------ #
import random
from random import randint, shuffle
import json 

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [random.choice(letters) for _ in range(randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    input_password.focus()
    input_password.insert(0, password)
   


# ---------------------------- SAVE PASSWORD ------------------------------------ #
def save():
    website= input_webside.get()
    email= input_Email_user.get()
    password= input_password.get()
    new_json= {website:{"email": email,
                        "password": password,
                        }}


    if len(website)==0 or len(email)==0:
        messagebox.showinfo("Place do not leave fields empty!")

    else:
         is_ok = messagebox.askokcancel(title="confimation", message=f" these are the details entered: \nEmail: {email}" f"\nPasswor: {password} \n Is it ok to save")

         if is_ok:
            try:
                with open("data_password.json", "r") as data_file: 
                    #reading data
                    data= json.load(data_file)
            except FileNotFoundError:
                 with open("data_password.json", "w") as data_file: 
                    #saving update data
                    json.dump(new_json, data_file, indent=4 )
            else: 
                #update data
                data.update(new_json)

                with open("data_password.json", "w") as data_file: 
                    #saving update data
                    json.dump(data, data_file, indent=4 )
            finally:
                input_webside.delete(0,END)
                input_Email_user.delete(0,END)
                input_password.delete(0,END)
# -------------------------------------UI SETUP ----------------------------------------- #
def find_password():
    webside= input_webside.get() 
    try:
        with open("data_password.json", "r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found.")
    else:
        if webside in data:
            email = data[webside]["email"]
            password= data[webside]["password"]
            messagebox.showinfo(title=webside, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {webside} exists.")
            
# ---------------------------------- UI SETUP ----------------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_png)
canvas.grid(row=0,column=1)

webside_label = Label(text="Webside:")
webside_label.grid(row=1, column=0)
email_Username_label= Label(text="Email/Username:")
email_Username_label.grid(row=2, column=0)
password_label= Label(text="Password:")
password_label.grid(row= 3, column=0)

search_button = Button(text="Search",width=13, command= find_password)
search_button.grid(row=1, column=2)
add_button =Button(text="Add",width=35, command= save)
add_button.grid(row=4,column=1, columnspan=2)
gene_password_button = Button(text="Generate Password", command=generate_password)
gene_password_button.grid(row=3, column=2)

input_webside= Entry(width=21)
input_webside.grid(row=1,column=1)
input_webside.focus()
input_Email_user= Entry(width=35)
input_Email_user.grid(row=2, column=1, columnspan=2)
input_Email_user.insert(0,"Radimelfi@gmail.com")
input_password= Entry(width=21)
input_password.grid(row=3, column=1)

window.mainloop()

