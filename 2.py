# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n=int(input("Введите натуральное число: "))
for i in range(2,n-1):
    while (n%i)==0:
        n=n/i
        print(i,end=" ")
if n!=1:
    print(n)
