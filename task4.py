print()
print("Данная программа принимает число N,затем создает и заполняет список числами из промежутка от -N до N.") 
print("Затем находит произведение элементов на указанных позициях.") 
print()
print("Ответ будет храниться в файле file.txt в одной строке в одно число.")
print()

user_list = []

n = int(input("Введите, пожалуйста, число N: "))

count = n
num = -count - 1
i = 0

while i < n*2 + 1:
    num += 1
    user_list.append(num)
    i += 1

print()
print("Созданный список: ", user_list)

productElements = 1

for i in user_list:
    if i == 0:
        continue
    else:
        productElements *= i

productElements = str(productElements)

file = open("file.txt", "w")
file.write("Произведение элементов списка равна: ")
file.write("[")
file.write(productElements)
file.write("]")
file.close()