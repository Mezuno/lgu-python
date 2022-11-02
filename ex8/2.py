# При уч. Анастасии Самуйловой

array = [
    [1,2,23],
    [4,5,6],
    [7,8,9],
]
maxLine = 0

for line in array:
    lineSum = 0
    
    for e in line:
        lineSum += e
        
    if maxLine < lineSum:
        maxLine = lineSum

print(maxLine)