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
        self.name = Name(name)
        self.phones = []

        for arg in args:
            self.phones.append(Phone(arg))

    def get_info(self):
        phones_info = ''

        for phone in self.phones:
            phones_info += f"{phone.value}, "

        return f'{self.name.value} : {phones_info[:-2]}'


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        # if record.name.value in self.data:
        #     record = self.data[record.name.value]

    def get_all_records(self):
        return self.data
