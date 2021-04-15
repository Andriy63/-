# Задание-2:
'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''


def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)


my_func(name='andriy', surname='sles', byear=1963, city='Dudinka', email='email', phone='007')
