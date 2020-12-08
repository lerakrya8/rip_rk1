def print_result(func):
    def func_decorated(*args, **kwards):
        print(func.__name__)
        result = func(*args, **kwards)
        if type(result) == list:
            for key in result:
                print(key)
        if type(result) == dict:
            for key, value in result.items():
                print(str(key) + '=' + str(value))
        else:
            print(result)
        return result
    return func_decorated


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
