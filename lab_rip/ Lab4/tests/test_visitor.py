from visitor import *
import unittest
from time import sleep


class VisitorTests(unittest.TestCase):
    def test_working(self):
        window1 = Window(1, 2, 'red')
        thread = ThreadForWindow(window1)
        thread.start()
        self.assertFalse(window1.is_ready())
        sleep(7)
        self.assertTrue(window1.is_ready())

if __name__ == '__main__':
    unittest.main()