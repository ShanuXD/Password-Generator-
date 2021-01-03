from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# --------------------------Find_Password---------------------------#


def find_password():
    check_website_input = website_input.get()

    try:
        with open('website_data.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message="No data file is present")

    else:
        if check_website_input in data:
            user_email = data[check_website_input]['email']
            user_password = data[check_website_input]['password']

            messagebox.showinfo(title=f'{check_website_input}', message=f"Email:{user_email} \n Password:{user_password}")
        else:
            messagebox.showinfo(title='Oops', message="No id present")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_input_data():
    password_data = password_input.get()
    email_data = email_input.get()
    website_data = website_input.get()

    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }
    
    if not website_data or not password_data:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty. ")
    else:
        try:
            with open('website_data.json', 'r') as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open('website_data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating data
            data.update(new_data)

            with open('website_data.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text='Website:', font=('Courier', 15, 'bold'))
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=('Courier', 15, 'bold'))
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('Courier', 15, 'bold'))
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=21)
website_input.grid(row=1, column=1)

email_input = Entry(width=35)
email_input.insert(0, 'shanu09@gmail.com')
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Button
generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(row=3, column=2)
                       
add_button = Button(text='Add', width=36, command=save_input_data)
add_button.grid(row=4, column=1, columnspan=2)

website_search = Button(text='Search', width=14, command=find_password)
website_search.grid(row=1, column=2, columnspan=1)


window.mainloop()
