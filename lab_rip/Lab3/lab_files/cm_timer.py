import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)


@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print(time.time() - start)


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(2)

    with cm_timer_2():
        time.sleep(3)
