from tkinter import *
from tkinter import ttk

root = Tk()
root.title('03.09.22 Lesson2 ExerciseOne')
root.geometry('1000x600+600+350')
root.resizable(width=True, height=True)

tasksCount = 6

points = [0, 1, 2, 3]

def get_result():
    taskRates = [0] * 6
    taskRatesSum = 0
    threePointCount = twoPointCount = onePointCount = zeroPointCount = 0

    for i in range(tasksCount):

        if combo1.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo1.get().isdigit() == False or int(combo1.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 0: taskRates[i] = combo1.get()

        if combo2.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo2.get().isdigit() == False or int(combo2.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 1: taskRates[i] = combo2.get()

        if combo3.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo3.get().isdigit() == False or int(combo3.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 2: taskRates[i] = combo3.get()

        if combo4.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo4.get().isdigit() == False or int(combo4.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 3: taskRates[i] = combo4.get()

        if combo5.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo5.get().isdigit() == False or int(combo5.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 4: taskRates[i] = combo5.get()

        if combo6.get() == '':
            result.set('Заполните все поля')
            return 1
        elif combo6.get().isdigit() == False or int(combo6.get()) not in points:
            result.set('Ошибка, неверные данные')
            return 1
        elif i == 5: taskRates[i] = combo6.get()

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

combo1 = ttk.Combobox(root, values=values)
combo1.grid(row=1, column=8, padx=30)
combo2 = ttk.Combobox(root, values=values)
combo2.grid(row=2, column=8, padx=30)
combo3 = ttk.Combobox(root, values=values)
combo3.grid(row=3, column=8, padx=30)
combo4 = ttk.Combobox(root, values=values)
combo4.grid(row=4, column=8, padx=30)
combo5 = ttk.Combobox(root, values=values)
combo5.grid(row=5, column=8, padx=30)
combo6 = ttk.Combobox(root, values=values)
combo6.grid(row=6, column=8, padx=30)


result = StringVar()
sumPoints = StringVar()

Label(textvariable=sumPoints).grid(row=14, column=1)
Label(textvariable=result).grid(row=15, column=1)

button = Button(text="Отправить", command=get_result)
button.grid(row=20, column=1, pady=30)

root.mainloop()
