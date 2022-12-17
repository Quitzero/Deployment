# Переписать программу из задания 10 с использованием модуля argparse. Считать аргументы a, b и c позиционными.
# Добавить опциональный аргумент -с или --complex, при наличии этого аргумента результаты выводить в виде комплексных чисел.
import argparse
import math
import cmath

parser = argparse.ArgumentParser()
parser.add_argument('a', type=int)
parser.add_argument('b', type=int)
parser.add_argument('c', type=int)
parser.add_argument("-c", "--complex", action="store_true")
args = parser.parse_args()


def main(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0 and args.complex:
        x1 = (-b + cmath.sqrt(discr)) / (2 * a)
        x2 = (-b - cmath.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2

    elif discr == 0 and args.complex:
        x1 = -(b / 2 * a)
        return complex(x1)
    elif discr == 0:
        x1 = -(b / 2 * a)
        return x1

    elif discr < 0 and args.complex:
        x1 = (-b + cmath.sqrt(discr)) / (2 * a)
        x2 = (-b - cmath.sqrt(discr)) / (2 * a)
        return x1, x2
    else:
        return 'Корней нет!'

# complex(int(


if args.complex:
    print(main(args.a, args.b, args.c))
else:
    print(main(args.a, args.b, args.c))
