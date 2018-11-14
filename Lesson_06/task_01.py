#!/usr/bin/python3

"""
Disclaimer:
    Используя всякие dir()/locals()/globals() можно бы было вычленить переменные, по признаку именования,
    например. Что-нибудь типо [var for var in globals() if not var.startswith("__")]. Но тут и функции подбираются, а я
    не знаю, хотели бы вы видеть функции в оценке размеров или нет. Поэтому выбрал самый прозрачный для пользователя
    способ, указать какие именно переменные нужно "померить".

Нужно вставить эту функцию в код оцениваемого скрипта. Через импорт работает не так как хотелось бы, в связи с тем, что
globals() импортированной функции отображает не то что нужно.

#Пример использования:
    count_and_show_variables_size([a, b, c, d, sum_, mul_, smth_strings_list])
    или
    count_and_show_variables_size([a, b, c, d, sum_, mul_, smth_strings_list], include_varlist_size=True)

    Флаг include_varlist_size=True можно выставить, если хотите так же померить сколько весит собранный список указанных
    переменных
"""


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
