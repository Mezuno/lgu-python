# При уч. Анастасии Самуйловой

def DigitCountSum(K):
    arr = [int(x) for x in str(K)]
    print(arr)
    
    sum = 0
    
    for i in arr:
        sum = sum + i
    print(sum)
    
    
DigitCountSum(1113)