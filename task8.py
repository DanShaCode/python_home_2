# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

print()
print("Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.") 
print("Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.") 
print("Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.") 
print()
print("Помогите Кате отгадать задуманные Петей числа.")
print()
sum = int(input("Введите сумму чисел: ")) 
print()
prod = int(input("Введите произведение чисел: "))


res = int(sum/2)

if sum - (res*2) == 1:
    a = res
    b = res + 1
else:
    a = res
    b = res
if (a+b == sum and a*b == prod) and a > 0 and b > 0 and a < 1000 and b < 1000:
    print()
    print("Числа, которые загадал Петя: ", a, "и", b)
else:
    print()
    print("Найти такие целые натуральные числа, которые бы являлись решением данной задачи не представляется возможным.")