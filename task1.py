print()
print("Данная программа принимает на вход вещественное число и показывает сумму его цифр.")
print()

num = float(input("Введите число: "))

count = 0
numSum = 0

if num < 0:
    num = num * -1

num = str(num)

for i in num:
    if i != ".":
        numSum += int(i)
        count += 1

print()
print("Сумма цифр модуля числа", "|", num, "|", "равна: ", numSum)
