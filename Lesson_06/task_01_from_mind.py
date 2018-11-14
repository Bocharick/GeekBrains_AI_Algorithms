#!/usr/bin/python3
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


a = 23456
b = "Hello, World!"
c = "If two witches were watching two watches which witch would watch which watch"

d = ["Red lorry, yellow lorry.", "I wish to wash my Irish wristwatch.", "How can a clam cram in a clean cream can?",
     ["Send toast to ten tense stout saints’ ten tall tents.",
      "Six sick hicks nick six slick bricks with picks and sticks."]]

e = {"e_a": 1234, "e_b": 4356,
     "e_c": {"in_e_a": "we are in deep", "in_e_b": "very very deep", "in_e_c": True, "in_e_d": 0}, "e_d": False,
     "e_e": 1}

count_and_show_variables_size([a, b, c, d, e])

"""
/usr/bin/python3.5 /home/bocharick/HDD/UbuntuFiles/PycharmProjects/GeekBrains_AI_Algorithms/Lesson_06/task_01_from_mind.py
================================================================================
Данные о переменных:
	 Имя переменной = ['a']; тип = <class 'int'>; размер = 28; содержимое =  23456
	 Имя переменной = ['b']; тип = <class 'str'>; размер = 62; содержимое =  Hello, World!
	 Имя переменной = ['c']; тип = <class 'str'>; размер = 125; содержимое =  If two witches were watching two watches which witch would watch which watch
	 Имя переменной = ['d']; тип = <class 'list'>; размер = 96; содержимое =  ['Red lorry, yellow lorry.', 'I wish to wash my Irish wristwatch.', 'How can a clam cram in a clean cream can?', ['Send toast to ten tense stout saints’ ten tall tents.', 'Six sick hicks nick six slick bricks with picks and sticks.']]
		 Имя переменной = []; тип = <class 'str'>; размер = 73; содержимое =  Red lorry, yellow lorry.
		 Имя переменной = []; тип = <class 'str'>; размер = 84; содержимое =  I wish to wash my Irish wristwatch.
		 Имя переменной = []; тип = <class 'str'>; размер = 90; содержимое =  How can a clam cram in a clean cream can?
		 Имя переменной = []; тип = <class 'list'>; размер = 80; содержимое =  ['Send toast to ten tense stout saints’ ten tall tents.', 'Six sick hicks nick six slick bricks with picks and sticks.']
			 Имя переменной = []; тип = <class 'str'>; размер = 180; содержимое =  Send toast to ten tense stout saints’ ten tall tents.
			 Имя переменной = []; тип = <class 'str'>; размер = 108; содержимое =  Six sick hicks nick six slick bricks with picks and sticks.
	 Имя переменной = ['e']; тип = <class 'dict'>; размер = 288; содержимое =  {'e_c': {'in_e_c': True, 'in_e_b': 'very very deep', 'in_e_a': 'we are in deep', 'in_e_d': 0}, 'e_e': 1, 'e_a': 1234, 'e_b': 4356, 'e_d': False}
		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_c
		 Имя переменной = []; тип = <class 'dict'>; размер = 288; содержимое =  {'in_e_c': True, 'in_e_b': 'very very deep', 'in_e_a': 'we are in deep', 'in_e_d': 0}
			 Имя переменной = []; тип = <class 'str'>; размер = 55; содержимое =  in_e_c
			 Имя переменной = []; тип = <class 'bool'>; размер = 28; содержимое =  True
			 Имя переменной = []; тип = <class 'str'>; размер = 55; содержимое =  in_e_b
			 Имя переменной = []; тип = <class 'str'>; размер = 63; содержимое =  very very deep
			 Имя переменной = []; тип = <class 'str'>; размер = 55; содержимое =  in_e_a
			 Имя переменной = []; тип = <class 'str'>; размер = 63; содержимое =  we are in deep
			 Имя переменной = []; тип = <class 'str'>; размер = 55; содержимое =  in_e_d
			 Имя переменной = []; тип = <class 'int'>; размер = 24; содержимое =  0
		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_e
		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  1
		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_a
		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  1234
		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_b
		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  4356
		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_d
		 Имя переменной = []; тип = <class 'bool'>; размер = 24; содержимое =  False
================================================================================
Суммарный размер всех переменных из списка: 2268
"""
