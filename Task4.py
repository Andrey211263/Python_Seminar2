# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

from random import randint


number = int(input('Введите число '))
lst = []
for i in range(-number, number+1):
    lst.append(randint(-number, number))
print(lst)
# exit()
path = 'Seminar002/file.txt'
data = open(path, 'r')
result = 1
index = 0
for line in data:
    if int(line) <= (len(lst) - 1):
        result *= lst[int(line)]
data.close()
print(f'Произведение = {result}')
