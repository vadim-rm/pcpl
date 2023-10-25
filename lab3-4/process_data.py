import json

from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique

path = "./data_light.json"


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(field(arg, "job-name")))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda s: f"{s} с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with open(path) as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))

    # Вывод в файле process_data.output.txt
