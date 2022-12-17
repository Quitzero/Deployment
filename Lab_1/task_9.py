# С помощью модуля os создайте директорию lab_1. В данной директории создайте для каждого из заданий выше
# текстовые файлы: 1.txt, 2.txt, 3.txt и т.д..
# В данные файлы выведите результаты выполнения функций по каждому заданию (по 2-3 случая).
import os
import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
import task_8

os.mkdir("lab_1")
os.chdir("lab_1")


def lab_1(a, b):
    text_file = open("1.txt", "w")
    text_file.write(f"Ввод:\n{a} {type(a)}\n{b} {type(b)}\nВывод:\n{task_1.main(a)}\n{task_1.main(b)}")
    text_file.close()


def lab_2(a, b):
    text_file = open("2.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{a}\nВывод:\n{task_2.main(a)}\n{task_2.main(b)}")
    text_file.close()


def lab_3(a, b):
    text_file = open("3.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_3.main(a)}\n{task_3.main(b)}")
    text_file.close()


def lab_4(a, b):
    text_file = open("4.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_4.main(a)}\n{task_4.main(b)}")
    text_file.close()


def lab_5(a, b):
    text_file = open("5.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_5.main(a)}\n{task_5.main(b)}")
    text_file.close()


def lab_6(a, b):
    text_file = open("6.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_6.main(a)}\n{task_6.main(b)}")
    text_file.close()


def lab_7(a, b):
    text_file = open("7.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_7.main(a)}\n{task_7.main(b)}")
    text_file.close()


def lab_8(a, b):
    text_file = open("8.txt", "w")
    text_file.write(f"Ввод:\n{a}\n{b}\nВывод:\n{task_8.main(a)}\n{task_8.main(b)}")
    text_file.close()


if __name__ == '__main__':
    lab_1(True, False)
    lab_2('Hello, world!', 'Gotta go fast')
    lab_3([2, -4, 5, 1, 0, -10], [1, 2, 3, -1, -2, -3])
    lab_4(3, 5)
    lab_4('aabBcde', 'indivisibilities')
    lab_6('camelsHaveThreeHumps', 'gottaGoFast')
    lab_7(9000, 222222222222)
    lab_8([5, 8, 6, 3, 4], [7, 8, 1])
