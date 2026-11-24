from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ім’я контакту має бути непорожнім рядком.")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if (
            not isinstance(value, str)
            or len(value) != 10
            or not value.isascii()
            or not value.isdigit()
        ):
            raise ValueError("Номер телефону має містити рівно 10 цифр від 0 до 9.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for saved_phone in self.phones:
            if saved_phone.value == phone:
                return saved_phone
        return None

    def remove_phone(self, phone):
        saved_phone = self.find_phone(phone)
        if saved_phone is not None:
            self.phones.remove(saved_phone)

    def edit_phone(self, old_phone, new_phone):
        saved_phone = self.find_phone(old_phone)
        if saved_phone is None:
            raise ValueError(f"Номер {old_phone} не знайдено.")
        index = self.phones.index(saved_phone)
        self.phones[index] = Phone(new_phone)

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)
