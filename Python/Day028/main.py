from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['+','-','/','*','~','^','<','>','&','%','@','!','|']

def pass_gen():
    password_input.delete(0,END)
    
    password_letters = [random.choice(letters) for _ in range(random.randint(4,6))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(map(str, password_list))
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_button.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":email,
            "password": password
        }
    }


    if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Error", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("Day028/data.json", "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
             with open("Day028/data.json", "w") as data_file:
                  json.dump(data, data_file, indent=4)

        else: 
            data.update(new_data)
            with open("Day028/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_button.delete(0,END)
            email_user_input.delete(0,END)
            password_input.delete(0,END)
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website = website_button.get()

    if len(website) == 0:
            messagebox.showinfo(title="Error", message="Please make sure you haven't left any field empty.")
    try:
        with open("Day028/data.json", "r") as data_file:
             data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("No Data File found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Credentials", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showerror("That website doesn't have any credentials.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="Day028/logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1, row=0)

#Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_button = Entry(width=28)
website_button.grid(column=1, row=1, columnspan=2, sticky=W)
website_button.focus()
#User or Email
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

email_user_input = Entry(width=35)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "myemail@gmail.com")

#Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=35)
password_input.grid(column=1, row=3, sticky=W)

generate_password = Button(text="Generate Password", command=pass_gen)
generate_password.grid(column=1, row=3, sticky=E)

#Add
add = Button(text="Add", width=30, command=save)
add.grid(row=4,column=1, columnspan=2)

#search
search = Button(text="Search", command=search)
search.grid(row=1, column=3, sticky=W)


window.mainloop()



# with open("Day028/data.json", "r") as data_file:
#                 #adds on a json
#                 #need to change the way we use the function with open("asdad", "")
#                 #json.dump(new_data, data_file, indent=4)

#                 #read from the file
#                 #need to change the way we use the function with open("asdad", "r")
#                 #json.load(data_file)

#                 #reading old data
#                 data = json.load(data_file)
#                 #updating the old data with new data
#                 data.update(new_data)

#         with open("Day028/data.json", "w") as data_file:
#             #saving updated data
#             json.dump(data, data_file, indent=4)

#             website_button.delete(0,END)
#             email_user_input.delete(0,END)
#             password_input.delete(0,END)