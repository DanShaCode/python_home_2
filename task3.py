# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

print()
n = int(input("Введите число N: "))

num = 1
count = 0
resultSum = 0

while count < n:
    resultSum += (1+1/num)**num
    num += 1
    count += 1

print()
print("Сумма чисел заданной последовательности: ", round(resultSum, 2))