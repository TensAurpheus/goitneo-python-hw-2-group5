from collections import UserDict

class PhoneError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10:
            self.value = value
        else:
            raise PhoneError
   
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, phone_from, phone_to):
        for p in self.phones:
            if p.value == phone_from:
                p.value = phone_to
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return "Not found"


class AddressBook(UserDict):
    # реалізація класу
    pass

phone1 = '5555555555'
phone2 = '4444444444'
phone3 = '1111111111'
john = Record('John')
john.add_phone(phone1)
john.add_phone(phone2)
print(john)
john.edit_phone(phone1, phone3)
print(john)
john.remove_phone(phone2)
print(john)
found = john.find_phone(phone1)
print(found)