# Дано целое число. Напишите функцию, которая преобразует число в другое по следующему принципу:
# 1 -> 11 , т.е. одна еденица;
# 0 -> 10, т.е. один нуль;
# 21 -> 1211, т.е. одна двойка и одна еденица;
# 9000 -> 1930, т.е. одна девятка и три нуля;
# 222222222222 -> 122, т.е. двенадцать двоек.
# 7 зад.
def main(value):
    result = []
    value = list(map(int, str(value)))
    li = [i for n, i in enumerate(value) if i not in value[:n]]
    for i in li:
        if i in value:
            result.append(f'{value.count(i)}{i}')
    return ''.join(result)


if __name__ == '__main__':
    print(main(11))
