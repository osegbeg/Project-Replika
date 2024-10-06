from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42)
add_button.grid(column=1, row=4, columnspan=2)

















window.mainloop()
