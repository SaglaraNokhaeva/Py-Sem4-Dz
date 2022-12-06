# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k=int(input("Введите степень многочлена: "))
koeff=[]
for i in range(k+1):
    koeff.append(randint(0,3))
print(koeff)
data = open('многочлен.txt','a',encoding='UTF-8')
x=0
s=''

for j in range(len(koeff)):
    if koeff[len(koeff)-1-j]==0:
        x+=1
    else:
        break
print(x)

for i in range(k+1-x):
    if koeff[i]==1:#если коэффицинет=1, то не печатаем его
        s=s+"x^"
        s=s+str(k-i)
        s=s+"+"
    elif koeff[i]!=0:  #только если коэффициент не ноль, то печатаем его
        if (k-i)!=0:  #проверка равен ли свободный член нулю
            s=s+str(koeff[i])
            s=s+"*x^"
            s=s+str(k-i)
            s=s+"+"
        else:
            s=s+str(koeff[i])
print(s)
if x!=0:
    s=s[:-1]
data.write(s)
data.write("=0")
data.close()