# Напишите функцию, которая конвертирует заданное булевое значение в строку. Например:
# True => ’True’


def main(value):
    if type(value) == bool:
        value = str(value)
        return f'Теперь значение {value} имеет тип {type(value)}'
    else:
        return f'Ошибка, {value} не является булевым значением!'


if __name__ == '__main__':
    print(main(False))

