# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной.
#   Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2

import random
coins = int(input('Введите количество монеток -> '))
print (coins, end='->')
tails = 0
heads = 0
for i in range(coins):
    coin_value = random.randint(0, 1)
    print (coin_value, end=' ')
    if coin_value == 0:
        tails += 1
    if coin_value == 1:
        heads += 1 
if  tails <= heads:
    print(f'\nМинимальное количество -> {tails}')
else:
    print(f'\nМинимальное количество -> {heads}')    
