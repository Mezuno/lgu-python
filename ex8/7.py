# При уч. Анастасии Самуйловой

array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,2,3],
]
result = False

num = 15

for line in array:
    lineSum = 0
    for e in line:
        lineSum += e
    
    if lineSum == num:
        result = True
        break



if result:
    print("Есть")
else: 
    print("Нету")