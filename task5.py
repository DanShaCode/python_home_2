# Реализуйте алгоритм перемешивания списка.

import random

print()
user_data = int(input("Введите размер списка: "))
print()

count = 0
arr = []

while count < user_data:
    i = arr.append(random.randint(1, 6))
    count += 1

print()
print("Сгенерированный список: ", arr)
print()

arrLen = len(arr)
rng = int(arrLen/2)

for i in arr:
    rand1 = random.randint(0, rng)
    rand2 = random.randint(rng, arrLen - 1)
    temp = arr[rand1]
    arr[rand1] = arr[rand2]
    arr[rand2] = temp

print()
print("Перемешанный список: ", arr)
print()