# При уч. Анастасии Самуйловой
# Скачанный файл не открывается, просмотр без скачивания недоступен

f = open('7.txt')

s = f.readline()\
    .replace('ad', 'a d')\
    .replace('da', 'd a')

w = list(map(len, s.split()))

print(max(w))