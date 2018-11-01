#!/usr/bin/python3

"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

"""

diap = [i for i in range(2, 100)]
kratnost = [0] * 10

for val in diap:
    for divider in range(2, 10):
        if val % divider == 0:
            kratnost[divider] += 1

for divider in range(2, 10):
    print("В диапазоне натуральных чисел [2;99] количество чисел кратных %d = %d" % (divider, kratnost[divider]))
