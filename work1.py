#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |
n = input("Введите трехзначное число: ")
n = int(n)
n1 = n
#n = int(423)
sum = 0
while n > 0:
    x = n % 10
    sum = sum + x
    n = n//10
print("Сумма цифр числа:", sum, "рассчитано циклом")

d1 = n1 % 10
d2 = n1 % 100 // 10
d3 = n1 // 100
print("Сумма цифр числа:", d1 + d2 + d3, "рассчитано сложением цифр числа")

