from tkinter import *
from tkinter import ttk

root = Tk()
root.title('03.09.22 LessonTwo ExerciseOne')
root.geometry('1000x600+600+350')
root.resizable(width=True, height=True)

tasksCount = 6

points = [0, 1, 2, 3]

def get_result():
    taskRates = [0] * 6
    taskRatesSum = 0
    threePointCount = twoPointCount = onePointCount = zeroPointCount = 0

    taskRatesList1 = list.curselection()
    taskRatesList2 = list2.curselection()
    taskRatesList3 = list3.curselection()
    taskRatesList4 = list4.curselection()
    taskRatesList5 = list5.curselection()
    taskRatesList6 = list6.curselection()

    for i in range(tasksCount):

        if taskRatesList1[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList1[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 0: taskRates[i] = taskRatesList1[0]

        if taskRatesList2[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList2[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 1: taskRates[i] = taskRatesList2[0]

        if taskRatesList3[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList3[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 2: taskRates[i] = taskRatesList3[0]

        if taskRatesList4[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList4[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 3: taskRates[i] = taskRatesList4[0]

        if taskRatesList5[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList5[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 4: taskRates[i] = taskRatesList5[0]

        if taskRatesList6[0] == '':
            result.set('Заполните все поля')
            return 1
        elif taskRatesList6[0] not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 5: taskRates[i] = taskRatesList6[0]

        taskRatesSum += int(taskRates[i])

        if int(taskRates[i]) == 3: threePointCount += 1
        if int(taskRates[i]) == 2: twoPointCount += 1
        if int(taskRates[i]) == 1: onePointCount += 1
        if int(taskRates[i]) == 0: zeroPointCount += 1

    if threePointCount == 6:
        category = 1
    elif onePointCount == 0 and zeroPointCount == 0 and threePointCount != 0 and twoPointCount != 0:
        category = 2
    elif twoPointCount == 6:
        category = 3
    else:
        category = 4

    result.set(f'Ваша категория: {category}, Сумма баллов: {taskRatesSum}')


Label(text="Фамилия: ").grid(row=1, column=1)
surnameInput = Entry()
surnameInput.grid(row=1, column=2)

Label(text="Имя: ").grid(row=2, column=1)
nameInput = Entry()
nameInput.grid(row=2, column=2)

Label(text="Отчество: ").grid(row=3, column=1)
patronymicInput = Entry()
patronymicInput.grid(row=3, column=2)

Label(text="Номер школы: ").grid(row=4, column=1)
schoolNumberInput = Entry()
schoolNumberInput.grid(row=4, column=2)

for i in range(tasksCount):
    Label(text='Кол-во баллов за ' + str(i+1) + ' задачу').grid(row=i+1, column=3, padx=30)


values = [0, 1, 2, 3]

list = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list.insert(END, value)
list.grid(row=1, column=9, padx=30)

list2 = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list2.insert(END, value)
list2.grid(row=2, column=9, padx=30)

list3 = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list3.insert(END, value)
list3.grid(row=3, column=9, padx=30)

list4 = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list4.insert(END, value)
list4.grid(row=4, column=9, padx=30)

list5 = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list5.insert(END, value)
list5.grid(row=5, column=9, padx=30)

list6 = Listbox(root, height=4, selectmode=SINGLE, exportselection=0)
for value in values:
    list6.insert(END, value)
list6.grid(row=6, column=9, padx=30)

result = StringVar()
sumPoints = StringVar()

Label(textvariable=sumPoints).grid(row=14, column=1)
Label(textvariable=result).grid(row=15, column=1)

button = Button(text="Отправить", command=get_result)
button.grid(row=20, column=1, pady=30)

root.mainloop()
