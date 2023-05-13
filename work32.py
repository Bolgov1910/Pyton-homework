# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)
# Input: 1, 3, 7, 10, 5, 8 - рассматриваемый список 4 - начало диапазона 8 - конец
# Output:
# 2(7), 4(5), 5(8)

num = int(input("Введите длину списка): "))
aMin = int(input("Введите начало диапазона (от 0 до 100): "))
aMax = int(input("Введите конец диапазона (от 0 до 100): "))  
if aMin > aMax:      # меняем местами границы диапазона, если введены в неправильном порядке
    [aMin,aMax] = [aMax,aMin]
A = []              # создаем пустой список
import random       # обращение к генератору случайных чисел
for i in range(num):                   # заполняем список случайными числами
    A.append(random.randint(0,101))    # от 0 до 100 

listInd = []              # создаем пустой список для индексов
listValue = []            # создаем пустой список для значений
for i in range(num-1):          # заполняем оба списка по условию
    if aMin <= A[i] <= aMax:
        listInd.append(i)
        listValue.append(A[i])

print  ("В списке", A, sep='\n')
print  (f"В диапазоне {aMin} - {aMax} находятся значения с индексами: ")
for i in range(len(listInd)):      # печать циклом из обоих спписков: индекс-значение
    print (listInd[i],"(значение" ,listValue[i],")") 
