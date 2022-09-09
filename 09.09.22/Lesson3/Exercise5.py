# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись
import re

f = open('text5.txt', 'r')

surnameArr = []
exists = False

for line in f:
    parsedLine = line.split(' ')
    parsedClass = re.split('А|Б|В|Г', parsedLine[2])
    parsedClass = parsedClass[0]

    if parsedLine[0]+parsedClass in surnameArr:
        exists = True
        existsWhere = parsedLine[0]+'ы в '+parsedClass+' классе'

    surnameArr.append(parsedLine[0]+parsedClass)


if (exists):
    print('Найдено следующее совпадение: '+existsWhere)
else:
    print('Нету')