def func(a=None, b=None, c=None):
    print(f'a = {a} b= {b} c={c}')


func(a=1, c=3)

a = [1, 2, 4]
b = [*a, 'text', True]
print(b)


def printScores(a, b, c, *args, **kwargs):
    print(f'args = {args} kwargs= {kwargs}')


printScores(1, 2, 4, True, False, 'rwer', ",,,", key='ключик')


def outer_func():
    def inner_func1():
        print("вызов inner_func1")

    def inner_func2():
        print("вызов inner_func2")

    def inner_func3():
        print("вызов inner_func3")

    # func1, func2, func3 = inner_func1, inner_func2, inner_func3
    # func1(), func2(), func3()
    return inner_func1(), inner_func2(), inner_func3


outer_func()
