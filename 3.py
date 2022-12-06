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
x=True

for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[j]==numbers[i]:
            x=False
    if x==True:
        b.append(numbers[i])
    x=True
print(b)
