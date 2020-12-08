
class Unique(object):
    def __init__(self, items, **kwargs):
        self.current_elem = set()
        self.data = iter(items)
        self.case = False
        for key in kwargs:
            if key is "ignore_case":
                if kwargs[key] is True:
                    self.case = True

    def __next__(self):
        while True:
            current = self.data.__next__()
            if self.case:
                current = current.lower()
            if current not in self.current_elem:
                self.current_elem.add(current)
                return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = ['c', 'a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    # data = gen_random(6, 3, 10)
    for i in Unique(data, ignore_case=True):
        print(i)

    print('new')
    data_new = ['c', 'a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    # data = gen_random(6, 3, 10)
    for i in Unique(data_new):
        print(i)
