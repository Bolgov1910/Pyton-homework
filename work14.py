#Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# Пример:             Ввод: 13 -> 1, 2, 4, 8


num = int(input("Ведите число: "))
base = 2
degBase = 1
while degBase <= num:
    degBase = degBase * base
    if degBase > num:      # чтобы не выскакивало за границы условия в последнем цикле
        degBase = degBase/base
        break
    else: 
        print (degBase)

