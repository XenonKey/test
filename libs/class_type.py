class Building:
    def __init__(self, id_num, address=None, square=None, company=None):
        self.id_num = id_num
        self.address = address
        self.square = square
        self.company = company

    def set_info(self, address=None, square=None, company=None):
        if address is not None:
            self.address = address
        if square is not None:
            self.square = square
        if company is not None:
            self.company = company

    def get_info(self):
        lst = [self.id_num, self.address, self.square, self.company]
        print(lst)


class School(Building):
    def __init__(self, id_num, address=None, square=None, company=None, students=None):
        super().__init__(id_num, address, square, company)
        self.students = students


    def set_info(self, address=None, square=None, company=None, students=None):
        super().set_info(address, square, company)
        if students is not None:
            self.students = students

    def get_info(self):
        lst = [self.id_num,
               self.address,
               self.square,
               self.company,
               self.students]
        print(lst)


class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, my name is {self.name}')


class LoggingMixin:
    def log(self, user_id, password):
        print(f'Entered {user_id}, password {password}')
        print(f'Successful')


class UserLogging(User, LoggingMixin):
    pass




















