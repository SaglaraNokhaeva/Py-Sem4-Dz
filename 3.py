# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

count=int(input("Введите количество чисел в последовательности: "))
from random import randint
numbers=[]
for i in range(count):
    numbers.append(randint(0,5))
print(numbers)
numbers.sort()
print(numbers)
b=[]
x=1
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        if numbers[i]==numbers[j]:
            x+=1
    if x==2:
        b.append(numbers[i])
    x=1
print(b)