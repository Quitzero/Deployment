# ---------------------------------------------------------------------------------
# Напишите функцию, которая конвертирует заданное булевое значение в строку.
# Например: True => ’True’
# ---------------------------------------------------------------------------------


def main(value):
    """
    Конвертирует заданное булевое значение в строку.
    >>> main(False)
    "Теперь значение False имеет тип <class 'str'>"
    >>> main(True)
    "Теперь значение True имеет тип <class 'str'>"

    :param value: Булевое значение
    :return: Результат выполнения
    """
    if type(value) == bool:
        value = str(value)
        return f'Теперь значение {value} имеет тип {type(value)}'
    else:
        return f'Ошибка, {value} не является булевым значением!'

