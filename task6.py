import random

print()
n = int(input("Введите количество монет: "))

coins = []
count = 0

while count < n:
    i = coins.append(random.randint(0, 1))
    count +=1  

heads = 0
tails = 0

for i in coins:
    if i == 1:
        heads += 1
    if i == 0:
        tails += 1

print()
print("Орел: ", heads)
print("Решка: ", tails)
print()
print("Монеты на столе", coins)
print()

if heads < tails:
    print("Минимальное количество монет, которые надо перевернуть: ", heads)
if heads > tails:
    print("Минимальное количество монет, которые надо перевернуть: ", tails)
if heads == tails:
    print("Минимальное количество монет, которые надо перевернуть: ", heads)