# ---------------------------------------------------------------------------------
# С помощью модуля os создайте директорию lab_1. В данной директории создайте для каждого из заданий выше
# текстовые файлы: 1.txt, 2.txt, 3.txt и т.д..
# В данные файлы выведите результаты выполнения функций по каждому заданию (по 2-3 случая).
# ---------------------------------------------------------------------------------
import os
from Labs import *


def lab_1(a, b):
    r"""
    >>> lab_1(True, False)
    "Ввод:\nTrue <class 'bool'>\nFalse <class 'bool'>\nВывод:\nТеперь значение True имеет тип <class 'str'>\nТеперь значение False имеет тип <class 'str'>"
    """
    text_file = open("../TXT/1.txt", "w")
    text_file.write(f"Ввод:\n{a} {type(a)}\n{b} {type(b)}\nВывод:\n{task_1.main(a)}\n{task_1.main(b)}")
    text_file.close()
    text_file = open("../TXT/1.txt", "r")
    return text_file.read()
    text_file.close()


def lab_2(a, b):
    r"""
    >>> lab_2('Hello, world!', 'Gotta go fast')
    'Ввод:\nHello, world!\nGotta go fast\nВывод:\n!dlrow ,olleH\ntsaf og attoG'
    """
    text_file = open("../TXT/2.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_2.main(a)}\n{task_2.main(b)}")
    text_file.close()
    text_file = open("../TXT/2.txt", "r")
    return text_file.read()
    text_file.close()


def lab_3(a, b):
    r"""
    >>> lab_3([2, -4, 5, 1, 0, -10], [1, 2, 3, -1, -2, -3])
    'Ввод:\n[2, -4, 5, 1, 0, -10]\n[1, 2, 3, -1, -2, -3]\nВывод:\n8\n6'
    """
    text_file = open("../TXT/3.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_3.main(a)}\n{task_3.main(b)}")
    text_file.close()
    text_file = open("../TXT/3.txt", "r")
    return text_file.read()
    text_file.close()


def lab_4(a, b):
    r"""
    >>> lab_4(3, 5)
    'Ввод:\n3\n5\nВывод:\n  *  \n *** \n*****\n    *    \n   ***   \n  *****  \n ******* \n*********'
    """
    text_file = open("../TXT/4.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_4.main(a)}\n{task_4.main(b)}")
    text_file.close()
    text_file = open("../TXT/4.txt", "r")
    return text_file.read()
    text_file.close()


def lab_5(a, b):
    r"""
    >>> lab_5('aabBcde', 'indivisibilities')
    'Ввод:\naabBcde\nindivisibilities\nВывод:\n2\n2'
    """
    text_file = open("../TXT/5.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_5.main(a)}\n{task_5.main(b)}")
    text_file.close()
    text_file = open("../TXT/5.txt", "r")
    return text_file.read()
    text_file.close()


def lab_6(a, b):
    r"""
    >>> lab_6('camelsHaveThreeHumps', 'gottaGoFast')
    'Ввод:\ncamelsHaveThreeHumps\ngottaGoFast\nВывод:\ncamels-have-three-humps\ngotta-go-fast'
    """
    text_file = open("../TXT/6.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_6.main(a)}\n{task_6.main(b)}")
    text_file.close()
    text_file = open("../TXT/6.txt", "r")
    return text_file.read()
    text_file.close()


def lab_7(a, b):
    r"""
    >>> lab_7(9000, 222222222222)
    'Ввод:\n9000\n222222222222\nВывод:\n1930\n122'
    """
    text_file = open("../TXT/7.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_7.main(a)}\n{task_7.main(b)}")
    text_file.close()
    text_file = open("../TXT/7.txt", "r")
    return text_file.read()
    text_file.close()


def lab_8(a, b):
    r"""
    >>> lab_8([5, 8, 6, 3, 4], [7, 8, 1])
    'Ввод:\n[5, 8, 6, 3, 4]\n[7, 8, 1]\nВывод:\n[3, 8, 6, 5, 4]\n[1, 8, 7]'
    """
    text_file = open("../TXT/8.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_8.main(a)}\n{task_8.main(b)}")
    text_file.close()
    text_file = open("../TXT/8.txt", "r")
    return text_file.read()
    text_file.close()


