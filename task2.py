# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

limit = int(input('Введите число для ограничения -> '))
print(limit, end=' -> ')
degree = 0
resalt = 0
number = 2
while resalt <= limit:
    resalt = number**degree
    degree += 1
    if resalt > limit:
        break
    print(resalt, end=' ')

