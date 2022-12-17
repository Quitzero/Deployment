# Дана строка которая представлена в стиле camelCase.
# Напишите функцию которая преобразует данную строку в стиль kebab-case.
# Возвращаемая строка должна содержать только символы в нижнем регистре. Например:
# ’camelsHaveThreeHumps’ => ’camels-have-three-humps’
import re


def main(value):
    if type(value) == str:
        value = re.sub(r'(?=[A-Z])', '-', value).lower()
        return value
    else:
        return f'Ошибка, {value} не является строкой!'


if __name__ == '__main__':
    print(main('camelsHaveThreeHumps'))

