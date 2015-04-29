import csv
from itertools import zip_longest, groupby, chain
import time

name = lambda d: d[0][0]
size = lambda d: d[0][2]


def get_data():

    with open("pypy.csv") as pypy_inp, open("scala.csv") as scala_inp:
        data = chain(csv.reader(pypy_inp, delimiter=","), csv.reader(scala_inp, delimiter=","))
        data = sorted(data, key=lambda item: item[0])
        scala_data = list()
        pypy_data = list()
        for k, v in groupby(data, key=lambda item: item[0]):
            args = [iter(v)]*10
            groups = zip_longest(*args, fillvalue=None)
            for _ in groups:
                if k == "scala":
                    scala_data.append((k, sum(map(lambda item: float(item[4]), _)) / 10**10))
                elif k == "pypy":
                    pypy_data.append((k,  sum(map(lambda item: float(item[4]), _)) / 10))
        
        lazy_scala_val = list(map(lambda item: item[1], scala_data[:6]))
        filter_strict_scala_val = list(map(lambda item: item[1], scala_data[7:13]))
        fib1_scala_val = list(map(lambda item: item[1], scala_data[8:11]))
        fib3_scala_val = list(map(lambda item: item[1], scala_data[12:15]))

        lazy_pypy_val = list(map(lambda item: item[1], pypy_data[:6]))
        filter_strict_pypy_val = list(map(lambda item: item[1], pypy_data[7:13]))
        fib1_pypy_val = list(map(lambda item: item[1], pypy_data[8:11]))
        fib3_pypy_val = list(map(lambda item: item[1], pypy_data[12:15]))

def start_eval():
        print("Computing lazy function")
        res_1 = evaluate_measure(lazy, sizes=(10, 100, 1000, 10000, 100000, 1000000))

        print("Computing filter_strict function")
        res_2 = evaluate_measure(filter_strict, sizes=(10, 100, 1000, 10000, 100000, 1000000))

        print("Computing factorial function")
        res_3 = evaluate_measure(factorial, sizes=(10, 20, 40))

        print("Computing factorial_tc function")
        res_4 = evaluate_measure(factorial_tc, sizes=(10, 20, 40))

        data = chain(res_1, res_2, res_3, res_4)
        with open("py.csv", "a") as out:
            wr = csv.writer(out, delimiter=",")
            for d in data:
                for a in list(d):
                    wr.writerow(["py", a[0], a[1], a[2], a[3]])


def evaluate_measure(func, sizes):
    res = list()
    for __ in sizes:
        def handle_exec(size):
            for _ in range(1, 11):
                start = time.clock()
                func(size)
                yield (func.__name__, _, size, time.clock() - start)
        res.append(handle_exec(__))
    return res


def lazy(size):
    (i for i in range(1, size+1))


def filter_strict(size):
    list(filter(lambda item: not item % 2, (i for i in range(1, size+1))))


def factorial(n):
    if not n:
        return 1
    return n * factorial(n-1)


def factorial_tc(n, acc=1):
    if not n:
        return acc
    return factorial_tc(n-1, acc*n)

start_eval()
