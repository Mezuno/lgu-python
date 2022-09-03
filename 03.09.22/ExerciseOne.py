from tkinter import *
from tkinter.messagebox import askokcancel

app = Tk()

def getPrice():
    electricityConsumption = electricityConsumptionaInput.get()
    electricityRate = electricityRateInput.get()

    if electricityConsumption != '' and electricityRate != '':
        if electricityConsumption.isdigit() and electricityRate.isdigit():
            if (float(electricityConsumption) > 0) and (float(electricityRate) > 0):
                result.config(text='Размер оплаты равен '
                                   + str(float(electricityConsumption) * float(electricityRate))
                                   + ' руб.')
            else:
                result.config(text='Не все значения положительны ;с')
        else:
            result.config(text='Буквы не подойдут ;с')
    else:
        result.config(text='Заполните все поля..')

app.title('Calculate app')
app.geometry('400x300')
app.resizable(width=False, height=False)

canvas = Canvas(app, height=300, width=400)
canvas.pack()

frameTop = Frame(app, bg='#484952')
frameTop.place(relwidth=1, relheight=1)
frameBottom = Frame(app, bg='blue')

electricityConsumptionaLabel = Label(frameTop, text='Электроэнергия (положительное целое, кВт)')
electricityConsumptionaLabel.pack()
electricityConsumptionaInput = Entry(frameTop, bg='white')
electricityConsumptionaInput.pack()

electricityRateLabel = Label(frameTop, text='Тариф (положительное целое)')
electricityRateLabel.pack()
electricityRateInput = Entry(frameTop, bg='white')
electricityRateInput.insert(0, '')

electricityRateInput.pack()

btn = Button(frameTop, text='Button', bg='#ccc', command=getPrice)
btn.pack()

result = Label(frameTop, bg='white', text='Тут появится стоимость или уведомление об ошибке')
result.pack()

app.mainloop()