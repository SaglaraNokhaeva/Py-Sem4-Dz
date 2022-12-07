# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
data1 = open('многочлен1.txt','r',encoding='UTF-8')
s1=data1.readline()
data2 = open('многочлен2.txt','r',encoding='UTF-8')
s2=data2.readline()
print("s1=",s1)
print("s2=",s2)
for i in range(len(s1)):
    step1=s1.find("^")
    step2=s1.find("+")
stepen1=int(s1[step1+1:step2])
print(stepen1)
for i in range(len(s2)):
    step1=s2.find("^")
    step2=s2.find("+")
stepen2=int(s2[step1+1:step2])
print(stepen2)

if stepen1>stepen2: 
    rezult=s1
    s=s2
else:
    rezult=s2
    s=s1
data3 = open('сумма.txt','a',encoding='UTF-8')
data3.write(rezult[:-2])
data3.write('+')
data3.write(s)
data1.close
data2.close
data3.close