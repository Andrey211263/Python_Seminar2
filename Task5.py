# 5 – Реализуйте алгоритм перемешивания списка.

from random import randint

number = int(input('Задайте длину списка '))
lst = []
for i in range(0, number):
    lst.append(randint(0, 999))
print(lst)
for i in range(0, number):
    buf_i = lst[i]
    j = randint(0, number-1)
    buf_j = lst[j]
    lst[j] = buf_i
    lst[i] = buf_j
    
print(lst)