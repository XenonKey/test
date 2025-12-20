from .my_decorator import *


@timing
def mult_num(x):
    return x*2


# @timing
def division(x, y):
    return x / y


@timing
def say_hi():
    return 'Hello!'


@timing
def multiply(a, b) -> int:
    return a * b


@timing
def mult_by_10(a) -> int:
    return a * 10


@timing
def add_my_mail(mail):
    return f'This is my mail {mail}'


@timing
def mult_my_list(lst, x):
    """Умножает итерируемый объект на введенный аргумент"""
    new_list = []

    for i in lst:
        new_list.append(i * x)

    print(new_list)

