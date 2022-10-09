# При уч. Анастасии Самуйловой

import time
from tkinter import *
from tkinter import filedialog as fd

app = Tk()

app.title('Занятие 7 задание 2')
app.geometry('500x800')

def openFile():
    global fileName
    fileName = fd.askopenfilename()
    file = open(fileName, 'r')

    title.config(text='Список учащихся('+str(len(file.readlines()))+'):')
    file = open(fileName, 'r')

    for line in file:
        tmp = listFromFile.get()
        tmp += line
        listFromFile.set(tmp)

    btnOpen["state"] = DISABLED
    btnClose["state"] = ACTIVE
    btnSave1["state"] = ACTIVE
    btnSave2["state"] = ACTIVE
    btnSave3["state"] = ACTIVE


def closeFile():
    title.config(text='Вы успешно закрыли файл')
    listFromFile.set('')
    fileName = ''
    btnOpen["state"] = ACTIVE
    btnClose["state"] = DISABLED
    btnSave1["state"] = DISABLED
    btnSave2["state"] = DISABLED
    btnSave3["state"] = DISABLED

def save1():
    file = open(fileName, 'r')
    dataToSave = ''
    for line in file:
        tmpResultLine = line.split(' ')
        surname = tmpResultLine[0]
        name = tmpResultLine[1]
        patronymic = tmpResultLine[2].split('\n')

        dataToSave += name+' '+patronymic[0]+' '+surname+'\n'

    fileToSave = open(fileName+' '+str(time.asctime()), 'w')

    fileToSave.write(dataToSave)


def save2():
    file = open(fileName, 'r')
    dataToSave = ''
    for line in file:
        tmpResultLine = line.split(' ')
        surname = tmpResultLine[0]
        name = tmpResultLine[1]
        patronymic = tmpResultLine[2].split('\n')

        dataToSave += surname+' '+name[0]+'. '+patronymic[0][0]+'.\n'

    fileToSave = open(fileName+' '+str(time.asctime()), 'w')

    fileToSave.write(dataToSave)

def save3():
    file = open(fileName, 'r')
    dataToSave = ''
    for line in file:
        tmpResultLine = line.split(' ')
        surname = tmpResultLine[0]
        name = tmpResultLine[1]
        patronymic = tmpResultLine[2].split('\n')

        dataToSave += name[0]+'. '+patronymic[0][0]+'. '+surname+'\n'

    fileToSave = open(fileName+' '+str(time.asctime()), 'w')

    fileToSave.write(dataToSave)


btnOpen = Button(text='Открыть файл', command=openFile)
btnOpen.pack()
btnClose = Button(text='Закрыть файл', command=closeFile, state=DISABLED)
btnClose.pack()

btnSave1 = Button(text='Сохранить в формате (имя отчество фамилия)', command=save1, state=DISABLED)
btnSave1.pack()
btnSave2 = Button(text='Сохранить в формате (фамилия и.о.)', command=save2, state=DISABLED)
btnSave2.pack()
btnSave3 = Button(text='Сохранить в формате (и.о. фамлиия)', command=save3, state=DISABLED)
btnSave3.pack()


title = Label()
title.pack()

listFromFile = StringVar()

list = Label(textvariable=listFromFile)
list.pack()

app.mainloop()
