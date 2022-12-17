from Labs import *
from unittest.mock import patch

# region task_1 test
def test_1_0():
    assert task_1.main(False) == "Теперь значение False имеет тип <class 'str'>"


def test_1_1():
    assert task_1.main(True) == "Теперь значение True имеет тип <class 'str'>"
# endregion


# region task_2 test
def test_2_0():
    assert task_2.main('Hello, world!') == '!dlrow ,olleH'


def test_2_1():
    assert task_2.main('Gotta go fast') == 'tsaf og attoG'
# endregion


# region task_3 test
def test_3_0():
    assert task_3.main([1, 2, 3, -1, -2, -3]) == 6


def test_3_1():
    assert task_3.main([2, -4, 5, 1, 0, -10]) == 8
# endregion


# region task_4 test
def test_4_0():
    assert task_4.main(3) == '  *  \n *** \n*****'


def test_4_1():
    assert task_4.main(4) == '   *   \n  ***  \n ***** \n*******'
# endregion


# region task_5 test
def test_5_0():
    assert task_5.main('aabBcCde') == 3


def test_5_1():
    assert task_5.main('indivisibilities') == 2
# endregion


# region task_6 test
def test_6_0():
    assert task_6.main('camelsHaveThreeHumps') == 'camels-have-three-humps'


def test_6_1():
    assert task_6.main('gottaGoFast') == 'gotta-go-fast'
# endregion


# region task_7 test
def test_7_0():
    assert task_7.main(9000) == '1930'


def test_7_1():
    assert task_7.main(222222222222) == '122'
# endregion


# region task_8 test
def test_8_0():
    assert task_8.main([5, 8, 6, 3, 4]) == [3, 8, 6, 5, 4]


def test_8_1():
    assert task_8.main([7, 8, 1]) == [1, 8, 7]
# endregion


# region task_9 test
def test_9_0():
    assert task_9.lab_1(True, False) == 'Ввод:\n' "True <class 'bool'>\n" "False <class 'bool'>\n" 'Вывод:\n' "Теперь значение True имеет тип <class 'str'>\n" "Теперь значение False имеет тип <class 'str'>"
    assert task_9.lab_2('Hello, world!', 'Gotta go fast') == 'Ввод:\nHello, world!\nGotta go fast\nВывод:\n!dlrow ,olleH\ntsaf og attoG'
    assert task_9.lab_3([2, -4, 5, 1, 0, -10], [1, 2, 3, -1, -2, -3]) == 'Ввод:\n[2, -4, 5, 1, 0, -10]\n[1, 2, 3, -1, -2, -3]\nВывод:\n8\n6'
    assert task_9.lab_4(3, 5) == 'Ввод:\n3\n5\nВывод:\n  *  \n *** \n*****\n    *    \n   ***   \n  *****  \n ******* \n*********'
    assert task_9.lab_5('aabBcde', 'indivisibilities') == 'Ввод:\naabBcde\nindivisibilities\nВывод:\n2\n2'
    assert task_9.lab_6('camelsHaveThreeHumps', 'gottaGoFast') == 'Ввод:\ncamelsHaveThreeHumps\ngottaGoFast\nВывод:\ncamels-have-three-humps\ngotta-go-fast'
    assert task_9.lab_7(9000, 222222222222) == 'Ввод:\n9000\n222222222222\nВывод:\n1930\n122'
    assert task_9.lab_8([5, 8, 6, 3, 4], [7, 8, 1]) == 'Ввод:\n[5, 8, 6, 3, 4]\n[7, 8, 1]\nВывод:\n[3, 8, 6, 5, 4]\n[1, 8, 7]'

# endregion


# region task_10 test
def test_10_0():
    assert task_10.main(['1', '2', '3']) == 'Корней нет'


def test_10_1():
    assert task_10.main(['1', '21', '5']) == 'x1 = -0.24\nx2 = -20.76'
# endregion

# region task_11 test
def test_11():
    assert task_11.main(1, 4, 3, False) == 'Корни уравнения: -1.0 -3.0'
# endregion
