from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)
# window.minsize(width=300, height=300)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.grid(column = 1, row= 0)
# entry.config(padx=5, pady=5)

#Labels
label = Label(text="Miles")
label.grid(column = 2, row= 0)

label2 = Label(text="is equal to")
label2.grid(column = 0, row= 1)


result_label = Label(text="0")
result_label.grid(column = 1, row= 1)

label3 = Label(text="Km")
label3.grid(column = 2, row= 1)


def converter():
    user_input = float(entry.get())
    result = round(user_input * 1.60934, 2)
    result_label.config(text= f"{result}")

button = Button(text="Calculate", command=converter)
button.grid(column = 1, row= 2)








window.mainloop()

