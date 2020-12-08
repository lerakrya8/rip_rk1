from time import sleep
from threading import *
from termcolor import colored

# Поведенческий шаблон Наблюдатель


class InformationBoard:
    def __init__(self):
        self.objects = list()

    def add(self, new_obj):
        self.objects.append(new_obj)

    def start_watching(self):
        i = 0
        while True:
            if i >= len(self.objects):
                i = 0
            thread = ThreadForWindow(self.objects[i])
            if self.objects[i].is_ready():
                print(colored('Окно номер ' + str(self.objects[i].number()) + ' свободно', self.objects[i].color))
                thread.start()
            # sleep(2)
            i += 1


class Window:
    def __init__(self, number, time_for_sleeping, color='white'):
        self.number_ = number
        self.is_ready_ = True
        self.time_for_sleeping_ = time_for_sleeping
        self.color = color

    def number(self):
        return self.number_

    def start_working(self):
        self.is_ready_ = False
        sleep(self.time_for_sleeping_)
        self.is_ready_ = True

    def is_ready(self):
        return self.is_ready_


class ThreadForWindow(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        self.window.start_working()


if __name__ == '__main__':
    inform_board = InformationBoard()
    window1 = Window(1, 3, 'red')
    window2 = Window(2, 4, 'white')
    window3 = Window(3, 5, 'yellow')
    window4 = Window(4, 10, 'blue')

    inform_board.add(window1)
    inform_board.add(window2)
    inform_board.add(window3)
    inform_board.add(window4)

    inform_board.start_watching()