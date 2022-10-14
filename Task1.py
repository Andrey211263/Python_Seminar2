# 1 – Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11


def f(num):
    summ = 0
    if num < 0:
        num = num * -1
    while num != 0:
        summ = summ + num % 10
        num //= 10
    return summ
number = input('Введите число ').split('.')
length = len(number)
match length:
    case 1:
        num1 = int(number[0])
        print(num1)
        print('Сумма цифр =', f(num1))
        
    case 2:
        num1 = int(number[0])
        num2 = int(number[1])
        print('Сумма цифр =', f(num1) + f(num2))
    
    case _:
       print('лишняя точка')
# except ValueError:
# print('error')
