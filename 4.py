# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# k=int(input("Введите степень многочлена: "))
# koeff=[]
# for i in range(k+1):
#     koeff.append(randint(0,101))
# # koeff=[0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
# print(koeff)
# data = open('многочлен.txt','a',encoding='UTF-8')
# x=0 # счётчик нулевых коэффициентов в хвосте
# s=''
# for j in range(len(koeff)):
#     if koeff[len(koeff)-1-j]==0:
#         x+=1
#     else:
#         break
# # print(x)
# for i in range(k+1):
#     if (k-i)!=0:#если это не нулевая степень, то
#         if koeff[i]==1:#если коэффициент=1, то не печатаем его
#              s=s+"x^"
#              s=s+str(k-i)
#              s=s+"+"
#         elif koeff[i]!=0:  #только если коэффициент не ноль, то печатаем его
#             s=s+str(koeff[i])
#             s=s+"*x^"
#             s=s+str(k-i)
#             s=s+"+"
#     else:
#         if koeff[i]!=0:
#             s=s+str(koeff[i])
# # print(s)
# if x!=0:
#     s=s[:-1]
# data.write(s)
# data.write("=0"+'\n')
# data.close()

# другое решение
from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(0, 2))

ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()
