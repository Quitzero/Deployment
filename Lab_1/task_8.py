# Дан массив целых чисел. Напишите функцию, которая сортирует все нечетные числа в массиве по возрастанию,
# при этом четные числа должны остаться на своих местах. Например:
# [7, 8, 1] => [1, 8, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

def main(value):
    if type(value) == list:
        before = []
        after = []
        for i in value:
            if i % 2:
                before.append(i)
        before = sorted(before)
        index = 0
        for i in value:
            if i % 2:
                i = value[value.index(i)] = before[index]
                index += 1

            after.append(i)
        return after
    else:
        return f'Ошибка, {value} не является массивом!'


if __name__ == '__main__':
    print(main([5, 8,1, 6, 3, 4]))

