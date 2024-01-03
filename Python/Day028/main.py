from tkinter import *
from tkinter import messagebox
import random
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any field empty.")
    else:
        isOk = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                                    f"\nPassword {password} \nIs it ok to save?")

        if isOk:
            with open("Day028/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_button.delete(0,END)
                email_user_input.delete(0,END)
                password_input.delete(0,END)

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

website_button = Entry(width=35)
website_button.grid(column=1, row=1, columnspan=2)
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

password_input = Entry(width=30)
password_input.grid(column=1, row=3, sticky=W)


generate_password = Button(text="Generate Password", command=pass_gen)
generate_password.grid(column=1, row=3, sticky=E)
#falta colocar o command

#Add
add = Button(text="Add", width=30, command=save)
add.grid(row=4,column=1, columnspan=2)


window.mainloop()