#!/usr/bin/python3

"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random
import time

random.seed(time.time())

RANDRANGE_MIN_VAL = -100
RANDRANGE_MAX_VAL = 100

VAL_ARR_SIZE = 100

val_arr = [random.randint(RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL) for _ in range(VAL_ARR_SIZE)]
print("Массив случайных целых чисел:\n", val_arr)

min_val = RANDRANGE_MAX_VAL + 1
min_idx = 0

max_val = RANDRANGE_MIN_VAL - 1
max_idx = 0

for i in range(len(val_arr)):
    val = val_arr[i]
    if val < min_val:
        min_val = val
        min_idx = i
    if val > max_val:
        max_val = val
        max_idx = i

print("Минимальное значение: %d; Индекс минимального: %d" % (min_val, min_idx))
print("Максимальное значение: %d; Индекс максимального: %d" % (max_val, max_idx))

val_arr[min_idx], val_arr[max_idx] = val_arr[max_idx], val_arr[min_idx]

print("Измененный массив:\n", val_arr)
