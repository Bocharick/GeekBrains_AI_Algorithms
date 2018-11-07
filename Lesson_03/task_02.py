#!/usr/bin/python3

"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается
с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

"""

import random
import time

random.seed(time.time())

val_arr = [random.randint(0, 100) for _ in range(100)]
print("Массив случайных целых чисел:")
print(val_arr)

print("Массив индексов четных элементов первого массива:")
idx_arr = [idx for idx, val in enumerate(val_arr) if val % 2 == 0]
print(idx_arr)