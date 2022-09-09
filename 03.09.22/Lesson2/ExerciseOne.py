from tkinter import *

root = Tk()
root.title('03.09.22 Lesson2 ExerciseOne')
root.geometry('750x300+600+350')

root.columnconfigure(1, minsize=150)

tasksCount = 6

points = [0, 1, 2, 3]

def get_result():
    taskRates = [0] * 6
    taskRatesSum = 0
    threePointCount = twoPointCount = onePointCount = zeroPointCount = 0

    for i in range(tasksCount):
        taskRates[i] = taskRateVars[i].get()
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

    result.set(f'''Ваша категория: {category}
    Сумма баллов: {taskRatesSum}''')


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
    Label(text='''Кол-во баллов за ''' + str(i+1) + ''' задачу''').grid(row=i+1, column=3, padx=30)

taskOneRateVar = IntVar()
taskTwoRateVar = IntVar()
taskThreeRateVar = IntVar()
taskFourRateVar = IntVar()
taskFiveRateVar = IntVar()
taskSixRateVar = IntVar()

taskRateVars = [
    taskOneRateVar,
    taskTwoRateVar,
    taskThreeRateVar,
    taskFourRateVar,
    taskFiveRateVar,
    taskSixRateVar,
]

for i in range(tasksCount):
    for j in range(4):
        Radiobutton(root, variable=taskRateVars[i], value=j, text=str(j)).grid(row=i+1, column=j+4, pady=10)


button = Button(text="Отправить", command=get_result)
button.grid(row=5, column=1, sticky='wesn',  columnspan=2)

result = StringVar()
Label(textvariable=result, justify=LEFT).grid(row=6, column=1, columnspan=2, rowspan=2)

root.mainloop()
