#!/usr/bin/python3

"""
По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

"""

print("Введите координату #1:")
X_coord1 = float(input('\tВведите x: '))
Y_coord1 = float(input('\tВведите y: '))

print("Введите координату #2:")
X_coord2 = float(input('\tВведите x: '))
Y_coord2 = float(input('\tВведите y: '))

X_vec1 = X_coord2 - X_coord1
Y_vec1 = Y_coord2 - Y_coord1

X_vec2 = Y_vec1
Y_vec2 = -X_vec1

C = -(X_vec2 * X_coord1 + Y_vec2 * Y_coord1)

print("Уравнение прямой:")
print("\tОбщее уравнение прямой:")
print("\t\t%.3f*X + %.3f*Y + %.3f = 0" % (X_vec2, Y_vec2, C))

"""
Вид 'y = kx + b' невозможен для прямых параллельных оси ординат.
"""

if Y_vec2 != 0:
    k = X_vec2 / Y_vec2
    b = C / Y_vec2
    print("\tВ виде 'y = kx + b':")
    print("\t\tY = %.3f*X + %.3f" % (k, b))
else:
    print("\tПрямая параллельна оси ординат, запись вида 'y = kx + b' невозможна")
