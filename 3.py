# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

count=int(input("Введите количество последовательности чисел: "))
from random import randint
numbers=[]
for i in range(count):
    numbers.append(randint(0,10))
print(numbers)
numbers.sort()
print(numbers)

for i in range(0,len(numbers)):
    x=0
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            x=1
    if x==0:
        print(numbers[i])    

