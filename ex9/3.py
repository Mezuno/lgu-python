# При уч. Анастасии Самуйловой

def f(x):
    k=2
    deliteli=set()
    while k * k <= x:
        if x % k==0:
            deliteli.add(k)
            if x // k < x:
                deliteli.add(x // k)
        k = k + 1
    return sorted(deliteli)
start = 174457
end = 174505
for i in range(start, end + 1):
    if len(f(i)) == 2:
        print(f(i))
