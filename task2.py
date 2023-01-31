print()
print("Данная программа принимает на вход число N и выдает набор произведений чисел от 1 до N.")
print()

n = int(input("Введите, пожалуйста, число N: "))

count = 1
multiplier = 1
result = 1

print()

while count <= n:
    result = result * multiplier
    multiplier += 1
    count += 1
    print(result, end = " ")

print()



