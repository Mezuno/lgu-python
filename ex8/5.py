# При уч. Анастасии Самуйловой

array = [
    [1.3, 2.4, 5.6],
    [3.2, 4.1, 1.1],
    [6.5, 3.2, 7.6],
]
indexI = 0
result = 0

k = 3

for line in array:
    indexJ = 0
    
    for e in line:
        if indexI + indexJ == k:
            result += e
        indexJ += 1
            
    indexI += 1
        
print(round(result, 2))