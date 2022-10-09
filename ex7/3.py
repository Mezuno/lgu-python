# При уч. Анастасии Самуйловой

import time
from tkinter import *
from tkinter import filedialog as fd

app = Tk()

app.title('Занятие 7 задание 3')
app.geometry('500x900')

def openFile():
    global fileName
    fileName = fd.askopenfilename()
    file = open(fileName, 'r')
    index = 1
    sum = 0
    tmp = ''
    warmDays = 0
    warmDaysTempSum = 0
    frozenDays = 0
    frozenDaysTempSum = 0

    for line in file:
        if (index == 1):
            mostFrozenDayTemp = float(line)
            mostFrozenDay = index

        if (index == 1):
            mostWarmDayTemp = float(line)
            mostWarmDay = index

        line = line.replace('\n', ' ')
        sum += float(line)

        if (float(line) > 0):
            warmDays += 1
            warmDaysTempSum += float(line)

        if (float(line) <= 0):
            frozenDays += 1
            frozenDaysTempSum += float(line)

        if (mostFrozenDayTemp > float(line)):
            mostFrozenDayTemp = float(line)
            mostFrozenDay = index

        if (mostWarmDayTemp < float(line)):
            mostWarmDayTemp = float(line)
            mostWarmDay = index

        line = str(index)+' января: '+line+'°C\n'
        tmp += line
        index += 1


    average = sum / index
    warmAverage = warmDaysTempSum / warmDays
    frozenAverage = frozenDaysTempSum / frozenDays

    global stat
    stat = 'средняя темп за мес: '+str(round(average, 1))+'\n'\
           'кол-во дней когда > 0°C: '+str(warmDays)+'\n'\
           'самый холодный день: '+str(mostFrozenDay)+' января ('+str(mostFrozenDayTemp)+'°C)'+'\n'\
           'самый теплый день: '+str(mostWarmDay)+' января ('+str(mostWarmDayTemp)+'°C)'+'\n'\
           'средняя положительная темп воздуха: '+str(round(warmAverage, 1))+'°C)'+'\n'\
           'средняя отрицательная темп воздуха: '+str(round(frozenAverage, 1))+'°C)'+'\n'\

    listFromFile.set(stat+tmp)

    btnOpen["state"] = DISABLED
    btnClose["state"] = ACTIVE
    btnSave["state"] = ACTIVE

def closeFile():
    title.config(text='Вы успешно закрыли файл')
    listFromFile.set('')
    fileName = ''

    btnOpen["state"] = ACTIVE
    btnSave["state"] = DISABLED
    btnClose["state"] = DISABLED

def saveStat():
    file = open(fileName+' '+time.asctime(), 'w')
    file.write(stat)


btnOpen = Button(text='Открыть файл', command=openFile)
btnOpen.pack()
btnClose = Button(text='Закрыть файл', command=closeFile, state=DISABLED)
btnClose.pack()
btnSave = Button(text='Сохранить статистику в файл', command=saveStat, state=DISABLED)
btnSave.pack()

title = Label()
title.pack()

listFromFile = StringVar()

list = Label(textvariable=listFromFile, width=80)
list.pack()

app.mainloop()
