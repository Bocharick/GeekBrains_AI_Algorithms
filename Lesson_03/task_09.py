#!/usr/bin/python3

"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""

import random
import time

random.seed(time.time())

RANDRANGE_MIN_VAL = -100
RANDRANGE_MAX_VAL = 100

# Ширина = количество столбцов
MATRX_WIDTH = 10
# Высота = количество строк
MATRX_HEIGHT = 6

matrx = [[0] * MATRX_WIDTH for _ in range(MATRX_HEIGHT)]

for row in range(MATRX_HEIGHT):
    for column in range(MATRX_WIDTH):
        matrx[row][column] = random.randint(RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL)

print("Матрица случайных элементов размером [%d;%d]:" % (MATRX_WIDTH, MATRX_HEIGHT))
for line in matrx:
    print(line)

min_col_vals = [RANDRANGE_MAX_VAL + 1] * MATRX_WIDTH
for column in range(MATRX_WIDTH):
    for row in range(MATRX_HEIGHT):
        if matrx[row][column] < min_col_vals[column]:
            min_col_vals[column] = matrx[row][column]

print("Минимальные значения столбцов:\n", min_col_vals)
spam_max = min_col_vals[0]
for i in range(1, len(min_col_vals)):
    if min_col_vals[i] > spam_max:
        spam_max = min_col_vals[i]
print("Максимальный элемент среди минимальных элементов столбцов матрицы:", spam_max)
