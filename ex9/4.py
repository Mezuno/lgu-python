# При уч. Анастасии Самуйловой

for i in range(312614, 312652):
    cnt = 0
    v = []
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    v.append(j)
    if cnt == 6:
        print(v)