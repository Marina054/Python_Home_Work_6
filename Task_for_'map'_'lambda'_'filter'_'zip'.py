# 
n = int(input('Введите значение n:'))    
a = int(input('Введите начало диапозона:'))
b = int(input('Введите конец диапозона:'))

import random
arr = []
for i in range(n):
    arr.append(random.randint(a,b))
print(arr)

  
arr2 = map(lambda x: x ** 2, arr)
arr3 = list(arr2)
print(arr3)

def odd(x): 
    return x % 2
arr4 = list(filter (odd, arr3)) # отфильтруем не четные числа
print(arr4)

result = zip (arr, arr3, arr4)
print(list(result))

