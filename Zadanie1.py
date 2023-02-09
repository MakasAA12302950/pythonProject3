"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
"""
my_list = ['зима','весна','лето','осень']
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
    print(my_list[0])
if month ==3 or month == 4 or month == 5:
    print(my_list[1])
if month ==6 or month == 7 or month == 8:
    print(my_list[2])
if month ==9 or month == 10 or month == 11:
    print(my_list[3])
"""

my_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
    print(my_dict.get(1))
if month ==3 or month == 4 or month == 5:
    print(my_dict.get(2))
if month ==6 or month == 7 or month == 8:
    print(my_dict.get(3))
if month ==9 or month == 10 or month == 11:
    print(my_dict.get(4))
