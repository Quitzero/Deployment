# С помощью модуля sys напишите программу, которая принимает три параметра (a, b, c) и выводит
# результат решения квардратного уравнения. ax^2 + bx + c = 0
# Например:
# $ ./solve.py 1 4 3
# -1 -3
import sys
import math


def main(value):
    value = list(map(int, value))
    discr = value[1] ** 2 - 4 * value[0] * value[2]

    if discr > 0:
        x1 = (-value[1] + math.sqrt(discr)) / (2 * value[0])
        x2 = (-value[1] - math.sqrt(discr)) / (2 * value[0])
        print(f'x1 = {x1}, \nx2 = {x2}')
    elif discr == 0:
        x1 = -(value[1] / 2 * value[0])
        print(f'x1 = {x1}')
    else:
        print('Корней нет')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        main(sys.argv)
    else:
        print("Ошибка, не были введены параметры!")




