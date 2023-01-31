# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

print()
print("Данная программа выводит все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
print()

print()
user_num = int(input("Введите число N: "))
print()

temp = 2
i = 1
result = 0

print("Ответ:", end = " ")
while result < user_num:
    if i == 1:
        print(int(1), end=" ")
        result = temp * i
        temp = result
        print(result, end=" ")
        i += 1
    else:
        result = temp * i
        if result > user_num:
            break
        else:
            temp = result
            print(result, end=" ")

print()