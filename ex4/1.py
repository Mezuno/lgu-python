# При уч. Анастасии Самуйловой

f = open('1.txt').readline()
k = 1
m = 0
for i in range(1, len(f)):
    if f[i] != f[i-1]:
        k += 1
    else:
        m = max(m, k)
        k = 1
m = max(m, k)
print(m)
