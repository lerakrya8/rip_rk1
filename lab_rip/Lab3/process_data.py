import json
from lab_files.gen_random import gen_random
from lab_files.cm_timer import cm_timer_1
from lab_files.print_result import print_result
from lab_files.field import field
from lab_files.unique import Unique

path = 'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
