# При уч. Анастасии Самуйловой

f = open('5.txt').readline()
k = 1
m = 0
for i in range(len(f) - 1):
    if f[i] == 'Z' and f[i + 1] == 'Z':
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)