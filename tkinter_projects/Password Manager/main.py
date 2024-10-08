# ---------------------------- PASSWORD MANAGER PROJECT ------------------------------- #

import random
import pyperclip
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a random password
def generate_password():
    # Define character sets

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly select character counts

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Generate password components
    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    # Combine and shuffle password components
    password_list = password_letter + password_symbol + password_num
    random.shuffle(password_list)

    # Join password components into a single string
    password = "".join(password_list)

    # Insert generated password into password entry field
    password_entry.insert(0, password)

    # Copy generated password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function to save password to file
def save_to_file():
    website_value = website_entry.get()
    username_value = username_entry.get()
    password_value = password_entry.get()

    # Validate input fields
    if len(website_value) == 0 or len(username_value) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Missing fields",
                                           message="please enter a value in the missing field")

    else:
        confirmed = messagebox.askokcancel(title="Please confirm your details",
                               message=f"\n website: {website_value} \n "
                          f"username: {username_value} \n "
                          f"password: {password_value} \n "
                                       f"Do you want to proceed?")
        # Save password to file if confirmed
        if confirmed:
            data = open("pw_docs.txt", "a")
            data.write(f"\n website: {website_value} \n "
                              f"username: {username_value} \n "
                              f"password: {password_value} \n ")
            data.close()
            clear_screen()

# Function to clear input fields
def clear_screen():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

# Create canvas for logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Create input field labels
website_label = Label(text="website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create input fields
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "osegbegoldenjoe1@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Create buttons
generate_password_button = Button(text="Generate Password", width=14, command= generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
