from tkinter import *
from numbers import Number

app = Tk()


def getprice():
    exchange = float(exchangeInput.get())
    amount = float(amountInput.get())

    if exchange != '' and amount != '':
        if isinstance(exchange, Number) and isinstance(exchange, Number):
            if (float(exchange) > 0) and (float(amount) > 0):
                result.config(text='Вы сможете купить '
                                   + str(round(float(amount) / float(exchange), 2))
                                   + '$')
            else:
                result.config(text='Не все значения положительны ;с')
        else:
           result.config(text='Буквы не подойдут ;с')
    else:
        result.config(text='Заполните все поля..')


app.title('Calculate app')
app.geometry('400x300+700+350')
app.resizable(width=False, height=False)

canvas = Canvas(app, height=300, width=400)
canvas.pack()

frameTop = Frame(app, bg='#484952')
frameTop.place(relwidth=1, relheight=1)
frameBottom = Frame(app, bg='blue')

exchangeLabel = Label(frameTop, text='Курс доллара')
exchangeLabel.pack()
exchangeInput = Entry(frameTop, bg='white')
exchangeInput.pack()

amountLabel = Label(frameTop, text='Рубли')
amountLabel.pack()
amountInput = Entry(frameTop, bg='white')
amountInput.pack()

btn = Button(frameTop, text='Button', bg='#ccc', command=getprice)
btn.pack()

result = Label(frameTop, bg='white', text='Тут появится стоимость или уведомление об ошибке')
result.pack()

app.mainloop()
