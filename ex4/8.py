# При уч. Анастасии Самуйловой
# Скачанный файл не открывается, просмотр без скачивания недоступен

with open('24.txt')as f:
    l = f.readline()
    count, mak = 0, 0
    k = 0
    for i in range(0, len(l)):
        if l[i] != 'A':
            count += 1
        if l[i] == 'A':
            if count >= 3:
                t = l[i - count: i]
                u = 0
                while "E" in t:
                    u += 1
                    t = t.replace('E', 'K', 1)
                if u >= 3:
                    mak = max(mak, count)
            count = 0
print(mak)