# Дана строка. Напишите фунцию, которая возвращает строку в обратном порядке. Например:
# ’Hello, world!’ => ’!dlrow ,oolleH’
def main(value):
    if type(value) == str:
        return value[::-1]
    else:
        return f'Ошибка, {value} не является строкой!'


if __name__ == '__main__':
    print(main('Hello, world!'))
