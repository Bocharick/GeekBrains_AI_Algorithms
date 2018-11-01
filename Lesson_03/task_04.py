#!/usr/bin/python3

"""
Определить, какое число в массиве встречается чаще всего.

"""

import random
import time

random.seed(time.time())

RANDRANGE_MIN_VAL = -10
RANDRANGE_MAX_VAL = 10

VAL_ARR_SIZE = 25

val_arr = [random.randint(RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL) for _ in range(VAL_ARR_SIZE)]
print("Массив случайных целых чисел:\n", val_arr)

range_len = RANDRANGE_MAX_VAL - RANDRANGE_MIN_VAL + 1
print("Количество возможных целых значений в диапазоне [%d;%d]: %d" % (RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL, range_len))


def cast_val_to_range_pos(val):
    return val - RANDRANGE_MIN_VAL


def cast_range_pos_to_val(range_pos):
    return RANDRANGE_MIN_VAL + range_pos


cntr_arr = [0] * range_len
for val in val_arr:
    cntr_arr[cast_val_to_range_pos(val)] += 1

max_count = 0
max_idx = 0
for i in range(len(cntr_arr)):
    count = cntr_arr[i]
    if count > max_count:
        max_count = count
        max_idx = i

print("Самое большое количество повторений у числа %d, оно встречается %d раз" % (
cast_range_pos_to_val(max_idx), max_count))

# print("Можно проверить глазками (отсортированный массив):")
# val_arr.sort()
# print(val_arr)
