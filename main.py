from add_class import AddressBook, Record

contacts_dict = AddressBook()


def input_error(function):
    """
    Створюємо декоратор для обробки помилок, котрі можуть виникнути через
    ввід користувача.
    :param function: Функція вводу від користувача.
    :return: Або роботу функції або текст з помилкою, для повторного вводу.
    """

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return wrapper


@input_error
def hello_func():
    """
    При отриманні команди привіт- маємо зреагувати правильно.
    :return:
    """
    return 'How can I help you?'


@input_error
def exit_func():
    """
    При отриманні слів про вихід з боту- маємо його закрити.
    :return:
    """
    return 'good bye'


@input_error
def add_func(data):
    """
    Додавання нового контакту. Обробка строки и створення контакту.
    :param data: Строка з ім'ям та телефоном.
    :return: Відповідь, що контакт створено.
    """
    name, phones = create_data(data)

    if name in contacts_dict:
        raise ValueError('This contact already exist.')
    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    contacts_dict.add_record(record)

    return f'You added new contact: {name} with this {phones}.'


@input_error
def change_phones_func(data):
    """
    Зміна вже існуючого контактного номера.
    :param data: Строка з ім'ям та телефоном.
    :return: Відповідь про зміни.
    """
    name, phones = create_data(data)

    if contacts_dict.has_record(name):
        record = contacts_dict.get_record(name)
        record.clear_phones()

        for phone in phones:
            record.add_phone(phone)

        return f'You changed numbers to {phones} for {name}.'
    return 'Use add command plz.'


@input_error
def search_func(value):
    """
    Коли користувач шукає конкретний контакт за ім'ям.
    :param value: Контакт котрий шукаємо.
    :return: Номер контакту.
    """
    return contacts_dict.search(value.strip()).get_info()


@input_error
def show_func():
    """
    Показуємо всю книгу контактів створену раніше.
    :return: Список контактів.
    """
    contacts = ''

    for key, record in contacts_dict.get_all_records().items():
        contacts += f'{record.get_info()}\n'

    return contacts


@input_error
def del_func(name):
    name = name.strip()

    if contacts_dict.has_record(name):
        contacts_dict.remove_record(name)

        return f'The record with name: {name} is deleted'

    raise ValueError(f'The record with name: {name} is not found')


COMMANDS_DICT = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change phones': change_phones_func,
    'show all': show_func,
    'phone': search_func,
    'delete': del_func
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)


def create_data(data):
    """
    Розділяє вхідні дані на дві частини - номер і телефон.
    Також ці данні проходять валідацію.
    Для подальшої роботи з ними.
    :param data: Строка з номером і ім'ям.
    :return: Вже розділені ім'я і номер
    """
    new_data = data.strip().split(" ")
    name = new_data[0]
    phones = new_data[1:]

    if name.isnumeric():
        raise ValueError('Wrong name.')

    for phone in phones:
        if not phone.isnumeric():
            raise ValueError('Wrong phone.')
    return name, phones


def break_func():
    """
    Якщо користувач ввів якусь тарабарщину- повертаємо відповідну відповідь
    :return: Неправильна команда
    """
    return 'Wrong enter.'


def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    while True:
        """
        Просимо користувача ввести команду для нашого бота
        Також тут же вимикаємо бота якщо було введено відповідну команду
        """

        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break


if __name__ == '__main__':
    main()
