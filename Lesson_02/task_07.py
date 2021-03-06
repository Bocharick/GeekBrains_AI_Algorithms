#!/usr/bin/python3

"""
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n – любое натуральное число.

"""

n = int(input("Введите натуральное число n: "))

left = 0
right = n * (n + 1) // 2

for i in range(n+1):
    left += i

if left == right:
    print(True)
else:
    print(False)
