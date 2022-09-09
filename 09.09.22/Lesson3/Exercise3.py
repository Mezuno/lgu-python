# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

f = open('text3.txt', 'r')

winterCount = 0
springCount = 0
summerCount = 0
autumnCount = 0

for line in f:
    parsedLine = line.split('.')
    if parsedLine[1] == '01' or parsedLine[1] == '02' or parsedLine[1] == '12': winterCount += 1
    if parsedLine[1] == '03' or parsedLine[1] == '04' or parsedLine[1] == '05': springCount += 1
    if parsedLine[1] == '06' or parsedLine[1] == '07' or parsedLine[1] == '08': summerCount += 1
    if parsedLine[1] == '09' or parsedLine[1] == '10' or parsedLine[1] == '11': autumnCount += 1

print('Дат зимы: '+str(winterCount))
print('Дат весны: '+str(springCount))
print('Дат лета: '+str(summerCount))
print('Дат осени: '+str(autumnCount))
