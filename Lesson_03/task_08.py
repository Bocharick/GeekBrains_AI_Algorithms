#!/usr/bin/python3

"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

"""

"""
Предполагаю, что в вебинаре вы ошиблись, сказав "пятый столбик посчитал компьютер". Обычно в размерах матрицы указывают
количество строк X количество столбцов. То есть в данном случае 5 строк по 4 столбца. Значит вводится с клавиатуры 5 раз
по 3 числа, затем в каждой из 5 строк считается 4-ое значение как сумма трех первых значений данной строки. Может это и
не принципиально, но я привык рассматривать размерности матриц именно в таком порядке. Да и 'a = numpy.zeros([5,4])' 
пораждает матрицу 'a' из 5 строк * 4 столбцов.
Тут не указано какие числа вводятся, целые или дробные. Предположил, что целые.
"""

matrx = [[0] * 4 for _ in range(5)]

for i in range(5):
    for j in range(3):
        matrx[i][j] = int(input("Введите matrx[%d][%d] элемент: " % (i, j)))

for i in range(5):
    for j in range(3):
        matrx[i][3] += matrx[i][j]

print("Полученная матрица:")
for line in matrx:
    print(line)