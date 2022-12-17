from pydantic import BaseModel
from fastapi import FastAPI
import re
import math


class Equation(BaseModel):
    a: int
    b: int
    c: int
    argument: str = None


arg = ['-c', '--complex']
app = FastAPI()


@app.get("/task_1")
def task_1(value: bool):
    value = str(value)
    return f'Теперь значение {value} имеет тип {type(value)}'


@app.get("/task_2")
def task_2(value: str):
    return value[::-1]


@app.post("/task_3")
def task_3(value: list[int]):
    result = 0
    for i in value:
        if i > 0:
            result += i
    return result


@app.get("/task_4")
def task_4(value: int):
    triangle = []
    for i in range(1, value * 2, 2):
        triangle.append(('*' * i).center(value * 2 - 1))
    return '\n'.join(triangle)


@app.get("/task_5")
def task_5(value: str):
    value = value.lower()
    count = 0
    for i in value:
        if value.count(i) >= 2:
            value = value.replace(i, '')
            count += 1
    return count


@app.get("/task_6")
def task_6(value: str):
    value = re.sub(r'(?=[A-Z])', '-', value).lower()
    return value


@app.get("/task_7")
def task_7(value: int):
    result = []
    value = list(map(int, str(value)))
    li = [i for n, i in enumerate(value) if i not in value[:n]]
    for i in li:
        if i in value:
            result.append(f'{value.count(i)}{i}')
    return ''.join(result)


@app.post("/task_8")
def task_8(value: list[int]):
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


@app.post("/task_11")
def task_11(value: Equation):
    discr = value.b ** 2 - 4 * value.a * value.c

    if discr > 0 and value.argument in arg:
        x1 = (-value.b + math.sqrt(abs(discr))) / (2 * value.a)
        x2 = (-value.b - math.sqrt(abs(discr))) / (2 * value.a)
        return f'{x1}j, {x2}j'
    elif discr > 0:
        x1 = (-value.b + math.sqrt(discr)) / (2 * value.a)
        x2 = (-value.b - math.sqrt(discr)) / (2 * value.a)
        return x1, x2

    elif discr == 0 and value.argument in arg:
        x1 = -(value.b / 2 * value.a)
        return f'{x1}j'
    elif discr == 0:
        x1 = -(value.b / 2 * value.a)
        return x1

    elif discr < 0 and value.argument in arg:
        x1 = (-value.b + math.sqrt(abs(discr))) / (2 * value.a)
        x2 = (-value.b - math.sqrt(abs(discr))) / (2 * value.a)
        return f'{x1}j, {x2}j'
    else:
        return 'Корней нет!'
