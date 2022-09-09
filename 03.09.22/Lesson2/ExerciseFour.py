from tkinter import *
from tkinter import ttk

root = Tk()
root.title('03.09.22 Lesson2 ExerciseOne')
root.geometry('400x500+600+350')
root.resizable(width=True, height=True)

def calculate():
    isToy = toy.get()
    isKnife = knife.get()
    isCigarettes = cigarettes.get()
    isOffprice = offprice.get()
    price = 0

    if isToy: price += prices.get('toy')
    if isKnife: price += prices.get('knife')
    if isCigarettes: price += prices.get('cigarettes')

    if isOffprice: price *= 0.97
    priceLabel.config(text=price)

values = ['toy', 'knife', 'cigarettes']
prices = {
    'toy': 1000,
    'knife': 500,
    'cigarettes': 100,
}
toy = BooleanVar()
knife = BooleanVar()
cigarettes = BooleanVar()
offprice = BooleanVar()


Label(root, text=values[0] + str(prices[values[0]])).grid(row=0, column=0)
Checkbutton(root, variable=toy).grid(row=0, column=1)

Label(root, text=values[1] + str(prices[values[1]])).grid(row=1, column=0)
Checkbutton(root, variable=knife).grid(row=1, column=1)

Label(root, text=values[2] + str(prices[values[2]])).grid(row=2, column=0)
Checkbutton(root, variable=cigarettes).grid(row=2, column=1)

Label(root, text='скидка').grid(row=3, column=0)
Checkbutton(root, variable=offprice).grid(row=3, column=1)

Button(root, text="Buy", command=calculate).grid(row=4, column=0)

priceLabel = Label(root, text="")
priceLabel.grid(row=5, column=0)

root.mainloop()
