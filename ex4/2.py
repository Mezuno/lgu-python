# При уч. Анастасии Самуйловой

f = open('2.txt')
s = f.readline()
mx = 1
cnt = 1
for i in range(len(s)-1):
    if s[i] == 'X' and s[i+1] == 'X':
        cnt += 1
        if cnt > mx:
            mx = cnt
    else:
        cnt = 1

mx = max(cnt, mx)
print(mx)