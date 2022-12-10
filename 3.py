# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# count=int(input("Введите количество чисел в последовательности: "))
# from random import randint
# numbers=[]
# for i in range(count):
#     numbers.append(randint(0,5))
# print(numbers)
# numbers.sort()
# print(numbers)
# b=[]
# x=1
# for i in range(0,len(numbers)):
#     for j in range(0,len(numbers)):
#         if numbers[i]==numbers[j]:
#             x+=1
#     if x==2:
#         b.append(numbers[i])
#     x=1
# print(b)

# другое решение
digits = [1, 2, 4, 5, 3, 2, 1, 1, 2, 4, 5, 7, 8]
dct = {}
for k in set(digits):
    dct.setdefault(k, digits.count(k))
print(f'Неповторяющиеся элементы:', end=' ')
for k, v in dct.items():
    if int(v) == 1:
        print(k, end=' ')