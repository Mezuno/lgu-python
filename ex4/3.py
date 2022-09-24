# При уч. Анастасии Самуйловой

f = open('3.txt').readline()
k = 1
m = 1
for i in range(len(f)-1):
    if f[i] == 'Y' and f[i+1] == 'Y':
        k += 1
        m = max(m, k)
    else: k = 1

print(m)
