# Дано целое положительное число. Напишите функцию, которая выводит треугольник из символов *.
# Высота треугольника равна данному числу. Например: если число равно 5, то в консоль выводится:
#     *
#    ***
#   *****
#  *******
# *********

def main(value):
    triangle = []
    if type(value) == int and value > 0:
        for i in range(1, value * 2, 2):
            triangle.append(('*' * i).center(value * 2-1))
        return '\n'.join(triangle)
    else:
        return f'Ошибка, {value} не является положительным числом!'


if __name__ == '__main__':
    print(main(5))


