from sington import *
import unittest


class SingletonTests(unittest.TestCase):
    def test_is_single_object(self):
        db_singleton_1 = Database()
        db_singleton_2 = Database()

        self.assertEqual(db_singleton_1, db_singleton_2)
        self.assertNotEqual(db_singleton_1, 2)

    def test_connection(self):
        db_singleton_1 = Database()

        self.assertTrue(db_singleton_1.connect())
        self.assertFalse(db_singleton_1.connect())

    def test_insert_select(self):
        db_singleton = Database()
        self.assertTrue(db_singleton.insert('INSERT INTO table1 2'))

        result = False
        if 'INSERT INTO table1 2' in db_singleton.connection.DB:
            result = True
        self.assertTrue(result)

    def test_select(self):
        requsts = ['INSERT INTO table1 2', 'requst2', 'requst3', 'requst4']
        db_singleton = Database()
        db_singleton.insert('requst2')
        db_singleton.insert('requst3')
        db_singleton.insert('requst4')

        self.assertEqual(requsts, db_singleton.select('requst'))


if __name__ == '__main__':
    unittest.main()