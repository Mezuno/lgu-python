# При уч. Анастасии Самуйловой

count = m = 0
f = open('3.txt')
l = [int(i) for i in f]
for i in range(len(l) - 2):
    l1 = sorted([l[i], l[i + 1], l[i + 2]])
    if l1[2]**2 < (l1[1]**2 + l1[0]**2):
        count += 1
        m = max(m, sum(l1))
print(count, m)