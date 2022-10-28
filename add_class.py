from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, *args):
        self.name = name
        self.phones = []
        for arg in args:
            self.phones.append(arg)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record.phones
        # if record.name.value in self.data:
        #     record = self.data[record.name.value]

    def get_all_record(self):
        return self.data
