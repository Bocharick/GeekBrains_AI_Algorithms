#!/usr/bin/python3

"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""

a = int(input('Введите трехзначное число: '))

b = a // 100
c = a // 10 % 10
d = a % 10

sum_ = b + c + d
mul_ = b * c * d

"""
ЗЫ: Да, я старовер :)
На самом деле просто по работе использую python 3.5, в котором еще нету f-строк
"""
print('Cумма цифр = %d; Произведение цифр = %d' % (sum_, mul_))


def count_and_show_variables_size(variables_list, include_varlist_size=False):
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def show_size(x, level=0, include_level_0=False):
        import sys
        # Если НЕ хотите учитывать размер списка переменных для оценки то:
        if include_level_0 is False:
            if level != 0:
                size_count = sys.getsizeof(x)
                print("\t" * level,
                      "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()),
                                                                                     type(x), sys.getsizeof(x)),
                      x)
            else:
                size_count = 0
        # Иначе, если хотите учитывать размер списка переменных для оценки то:
        else:
            size_count = sys.getsizeof(x)
            print("\t" * level,
                  "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()), type(x),
                                                                                 sys.getsizeof(x)), x)
        if hasattr(x, "__iter__") and not isinstance(x, str):
            if hasattr(x, "items"):
                for key, value in x.items():
                    size_count += show_size(key, level + 1)
                    size_count += show_size(value, level + 1)
            else:
                for item in x:
                    size_count += show_size(item, level + 1)
        return size_count

    size_of_border_line_ = 80
    print("=" * size_of_border_line_)
    print("Данные о переменных:")
    total_size = show_size(variables_list, include_level_0=include_varlist_size)
    print("=" * size_of_border_line_)
    print("Суммарный размер всех переменных из списка:", total_size)


count_and_show_variables_size([a, b, c, d, sum_, mul_])

"""
/usr/bin/python3.5 /home/bocharick/HDD/UbuntuFiles/PycharmProjects/GeekBrains_AI_Algorithms/Lesson_06/task_01_lesson_01_task_01.py
Введите трехзначное число: 479
Cумма цифр = 20; Произведение цифр = 252
================================================================================
Данные о переменных:
	 Имя переменной = ['a']; тип = <class 'int'>; размер = 28; содержимое =  479
	 Имя переменной = ['b']; тип = <class 'int'>; размер = 28; содержимое =  4
	 Имя переменной = ['c']; тип = <class 'int'>; размер = 28; содержимое =  7
	 Имя переменной = ['d']; тип = <class 'int'>; размер = 28; содержимое =  9
	 Имя переменной = ['sum_']; тип = <class 'int'>; размер = 28; содержимое =  20
	 Имя переменной = ['mul_']; тип = <class 'int'>; размер = 28; содержимое =  252
================================================================================
Суммарный размер всех переменных из списка: 168
"""
