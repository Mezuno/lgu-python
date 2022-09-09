from tkinter import *

app = Tk()
app.geometry("350x400+700+300")
app.title('App')
app['background'] = '#2f3030'

def switchCurrency():

    if currentCurrency.get() == 'dol':
        exchangeRateLabel.config(text=f'Валютный курс (рубли)')
        amountAvailableLabel.config(text=f'Имеющаяся сумма (доллары)')

    if currentCurrency.get() == 'rub':
        exchangeRateLabel.config(text=f'Валютный курс (доллары)')
        amountAvailableLabel.config(text=f'Имеющаяся сумма (рубли)')


def calculate():
    exchangeRate = exchangeRateInput.get()
    amountAvailable = amountAvailableInput.get()
    isCommission.get()
    if currentCurrency.get() == 'rub': currencyToResult = '$'
    if currentCurrency.get() == 'dol': currencyToResult = 'руб.'
    if amountAvailable != '' and exchangeRate != '' and amountAvailable.isdigit() and exchangeRate.isdigit():
        if isCommission.get():
            result.config(text=f"Результат: вы сможете "
                               f"купить {str(round(float(amountAvailable) / float(exchangeRate)*0.9, 2))} {currencyToResult}")
        else:
            result.config(text=f"Результат: вы сможете "
                               f"купить {str(round(float(amountAvailable) / float(exchangeRate), 2))} {currencyToResult}")
    else:
        result.config(text=f"Результат: введены неверные данные")

standartPadding = 10
standartBackground = '#2f3030'
standartTextColor = 'white'
app.columnconfigure(1, minsize=300)

Label(text="Валютный калькулятор", bg=standartBackground, fg=standartTextColor, font=("Tahoma", 16), anchor='w', justify=LEFT)\
    .grid(pady=standartPadding, padx=standartPadding, column=1, row=1, columnspan=10, sticky='we')

currentCurrency = StringVar()
currentCurrency.set('rub')

exchangeRateLabel = Label(text=f"Валютный курс (доллары)", bg=standartBackground, fg=standartTextColor, anchor='w')
exchangeRateLabel.grid(pady=(standartPadding, 0), padx=standartPadding, column=1, row=2, columnspan=2, sticky='we')
exchangeRateInput = Entry()
exchangeRateInput.grid(pady=(0, standartPadding), padx=standartPadding, column=1, row=3, columnspan=2, sticky='we')

amountAvailableLabel = Label(text=f"Имеющаяся сумма (рубли)", bg=standartBackground, fg=standartTextColor, anchor='w')
amountAvailableLabel.grid(pady=(standartPadding, 0), padx=standartPadding, column=1, row=4, columnspan=2, sticky='we')
amountAvailableInput = Entry()
amountAvailableInput.grid(pady=(0, standartPadding), padx=standartPadding, column=1, row=5, columnspan=2, sticky='we')

isCommission = BooleanVar()
Label(text="Комиссия (10%)", bg=standartBackground, fg=standartTextColor, anchor='w', width=14)\
    .grid(pady=standartPadding, padx=(standartPadding, 0), column=1, row=6, sticky='e')
commission = Checkbutton(bg=standartBackground, anchor='w', variable=isCommission)
commission.grid(pady=standartPadding, padx=standartPadding, column=2, row=6, sticky='e')

Label(text="Покупаю рубли", bg=standartBackground, fg=standartTextColor, anchor="w")\
    .grid(column=1, row=7, sticky='e')
changeCurrentCurenctyButton = Radiobutton(variable=currentCurrency, value="dol", bg=standartBackground, command=switchCurrency)
changeCurrentCurenctyButton.grid(column=2, row=7)

Label(text="Покупаю доллары", bg=standartBackground, fg=standartTextColor, anchor="w")\
    .grid(column=1, row=8, sticky='e')
changeCurrentCurenctyButton2 = Radiobutton(variable=currentCurrency, value="rub", bg=standartBackground, command=switchCurrency)
changeCurrentCurenctyButton2.grid(column=2, row=8)

btn = Button(app, text=f"Рассчитать", bd=0, bg=standartBackground, fg=standartTextColor, width=10, height=1, command=calculate)
btn.grid(column=1, row=9, columnspan=2, padx=standartPadding, pady=standartPadding, sticky='we')

result = Label(bg=standartBackground, fg=standartTextColor, justify=LEFT, anchor='n')
result.grid(pady=standartPadding, padx=standartPadding, column=1, columnspan=2, row=10, sticky='we')

app.mainloop()
