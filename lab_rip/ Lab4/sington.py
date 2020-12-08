class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DbConnection:
    DB = list()

    def select(self, request):
        print('Произведен такой запрос к базе данных:' + request)
        print('Получены какие-то данные...')
        print(self.DB)
        return self.DB

    def insert(self, request):
        self.DB.append(request)
        print('Произведен такой запрос к базе данных:' + request)
        print('Данные:' + ' В BD вставлены такие-то данные...')


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = DbConnection()
            print('Соединение BD установленно')
            return True
        else:
            print('Соединение с BD уже установленно')
            return False

    def select(self, request):
        if self.connection is not None:
            return self.connection.select(request)
        else:
            print('Соединение с базой данных отсутствует')
            return False

    def insert(self, request):
        if self.connection is not None:
            self.connection.insert(request)
            return True
        else:
            print('Соединение с базой данных отсутствует')
            return False


if __name__ == '__main__':
    db_singleton_1 = Database()
    print(db_singleton_1)
    db_singleton_2 = Database()
    print(db_singleton_2)

    db_singleton_1.insert('INSERT INTO table1 2')
    db_singleton_2.connect()
    db_singleton_1.insert('INSERT INTO table1 2')