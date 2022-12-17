# Дана строка. Напишите функцию, которая будет возвращать количество символов,
# которые встречаются в строке более одного раза. Регистр символов не учитывается. Например:
# ’abcde’ => 0
# ’aabcde’ => 1
# ’aabBcde’ => 2
# ’aabbccde’ => 3
# ’indivisibilities’ => 2

def main(value):
    if type(value) == str:
        value = value.lower()
        count = 0
        for i in value:
            if value.count(i) >= 2:
                value = value.replace(i, '')
                count += 1
        return count
    else:
        return f'Ошибка, {value} не является строкой!'


if __name__ == '__main__':
    print(main('aabBcde'))
