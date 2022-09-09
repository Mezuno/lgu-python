from tkinter import *

root = Tk()
root.title('03.09.22 Lesson2 ExerciseOne')
root.geometry('400x500+600+350')
root.resizable(width=True, height=True)

def calculate():
    exp = experience.get()
    lngCount = languageCount.get()
    edu = education.get()
    wage = 0
    result = 'Не принимаем'

    if exp == '' or lngCount == '' or exp == '':
        return resultLabel.config(text='заполните все поля')

    if exp == '<3': return resultLabel.config(text=result)
    if lngCount == '0': return resultLabel.config(text=result)
    if edu == 'начальное' or edu == 'среднее': return resultLabel.config(text=result)

    if (exp == '3-5'): wage += 3000
    if (exp == '5+'): wage += 7000
    if (lngCount == '1'): wage += 1500
    if (lngCount == '2'): wage += 2000
    if (lngCount == '3+'): wage += 3000
    if (edu == 'среднее специальное'): wage += 1200
    if (edu == 'высшее'): wage += 5000

    return resultLabel.config(text='итоговая зп: '+str(wage))

experience = StringVar()
languageCount = StringVar()
education = StringVar()

Label(root, text='Какой у Вас рабочий стаж?').pack()

Radiobutton(root, variable=experience, value='<3', text='< 3').pack()
Radiobutton(root, variable=experience, value='3-5', text='3-5').pack()
Radiobutton(root, variable=experience, value='5+', text='5+').pack()

Label(root, text='Сколько иностранных языков вы знаете?').pack()

Radiobutton(root, variable=languageCount, value='0', text='0').pack()
Radiobutton(root, variable=languageCount, value='1', text='1').pack()
Radiobutton(root, variable=languageCount, value='2', text='2').pack()
Radiobutton(root, variable=languageCount, value='3+', text='3+').pack()

Label(root, text='Образование: ').pack()

Radiobutton(root, variable=education, value='начальное', text='начальное').pack()
Radiobutton(root, variable=education, value='среднее', text='среднее').pack()
Radiobutton(root, variable=education, value='среднее специальное', text='среднее специальное').pack()
Radiobutton(root, variable=education, value='высшее', text='высшее').pack()

Button(root, text="отправить заявку", command=calculate).pack()

resultLabel = Label(root, text='')
resultLabel.pack()

root.mainloop()
