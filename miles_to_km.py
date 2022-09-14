from tkinter import *

window = Tk()
window.title("mile to km converter")
window.config(padx=20, pady=20)

# labels
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)
label_4.config(padx=30)


# text entry
entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# button
def calc():
    label_4.config(text=round(float(entry.get()) * 1.609, 2))


button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)


window.mainloop()