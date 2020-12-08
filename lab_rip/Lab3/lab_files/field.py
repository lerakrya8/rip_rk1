# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for key in items:
            if args[0] in key:
                yield key[args[0]]
    elif len(args) > 1:
        for key in items:
            result = dict()
            for key_arg in args:
                if key_arg in key:
                    result[key_arg] = key[key_arg]
            if result is not None:
                yield result


if __name__ == "__main__":
    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    for i in field(goods, 'title', 'price'):
        print(i)
