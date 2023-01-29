# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print()

num = float(input("Введите число: "))
num = str(num)

count = 0
numSum = 0

for i in num:
    if i != ".":
        numSum += int(i)
        count += 1

print()
print("Сумма цифр числа", num, "равна: ", numSum)
