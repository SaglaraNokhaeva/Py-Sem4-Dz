# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data1 = open('многочлен1.txt','r',encoding='UTF-8')
s1=data1.readline()
data2 = open('многочлен2.txt','r',encoding='UTF-8')
s2=data2.readline()
data1.close
data2.close

