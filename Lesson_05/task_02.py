#!/usr/bin/python3

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого это цифры числа.

Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import deque


def hex_sum(val1, val2):
    


def hex_list_sum(list1, list2):
        deq1 = deque(list1)
        deq2 = deque(list2)
        print(deq1)
        print(deq2)

a = [i for i in str(input("Введите HEX число a = "))]
b = [i for i in str(input("Введите HEX число b = "))]


hex_list_sum(a, b)

