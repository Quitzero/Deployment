# ---------------------------------------------------------------------------------
# Дана строка. Напишите фунцию, которая возвращает строку в обратном порядке. Например:
# ’Hello, world!’ => ’!dlrow ,oolleH’
# ---------------------------------------------------------------------------------
def main(value):
    """
    :param value: Строка
    :return: Результат выполнения

    Конвертирует заданное булевое значение в строку.
    >>> main('Hello, world!')
    '!dlrow ,olleH'
    >>> main('Gotta go fast')
    'tsaf og attoG'
    """
    if type(value) == str:
        return value[::-1]
    else:
        return f'Ошибка, {value} не является строкой!'

