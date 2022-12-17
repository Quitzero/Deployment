# ---------------------------------------------------------------------------------
# Дана строка которая представлена в стиле camelCase.
# Напишите функцию которая преобразует данную строку в стиль kebab-case.
# Возвращаемая строка должна содержать только символы в нижнем регистре. Например:
# ’camelsHaveThreeHumps’ => ’camels-have-three-humps’
# ---------------------------------------------------------------------------------
import re


def main(value):
    """
    :param value: Строка
    :return:  Результат выполнения

    Преобразует данную строку в стиль kebab-case
    >>> main('camelsHaveThreeHumps')
    'camels-have-three-humps'
    >>> main('gottaGoFast')
    'gotta-go-fast'
    """
    if type(value) == str:
        value = re.sub(r'(?=[A-Z])', '-', value).lower()
        return value
    else:
        return f'Ошибка, {value} не является строкой!'

