# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d=input("Введите точность вычисления корня из 2: ")
# sqrt2=2**(1/2)
# d=d[2::]
# print(sqrt2)
# sqrt2=round(sqrt2,len(d))
# print(sqrt2)


# решение другое
a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
    pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi_target)[:a + 2])