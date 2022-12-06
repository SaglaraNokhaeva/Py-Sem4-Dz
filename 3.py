# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

count=int(input("Введите количество последовательности чисел: "))
from random import randint
numbers=[]
for i in range(count):
    numbers.append(randint(0,5))
print(numbers)
numbers.sort()
print(numbers)
numbers1=[]
x=False

length=len(numbers)

for i in range(1,length):
    if numbers[i]==numbers[i-1]:
        numbers.remove(numbers[i-1])
        length-=1
        print(length)
print(numbers)


#         if numbers[j]==numbers[i]:
#             numbers.remove(numbers[j])
#     print(x)
#     if x==False:
#         numbers1.append(numbers[i])
#     x=False
# print(numbers)