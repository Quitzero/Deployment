# ---------------------------------------------------------------------------------
# Дан массив целых чисел. Напишите функцию, которая возвращает сумму всех положительных значений.
# Если массив пустой, то сумма равна 0. Например: [2, -4, 5, 1, 0, -10] => 2 + 5 + 1 = 8
# ---------------------------------------------------------------------------------


def main(value):
    """
    :param value: Массив целых чисел
    :return: Результат выполнения

    Возвращает сумму всех положительных значений массива.
    >>> main([1, 2, 3, -1, -2, -3])
    6
    >>> main([2, -4, 5, 1, 0, -10])
    8
    """
    if type(value) == list:
        result = 0
        for i in value:
            if i > 0:
                result += i
        return result
    else:
        return f'Ошибка, {value} не является массивом целых чисел!'

