from collections import UserDict

class PhoneError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


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
        return (
            f"Contact name: {self.name.value}, " 
            f"phones: {'; '.join(p.value for p in self.phones)}"
                )
    
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


def name_error_check(func):
    def inner(*args):
        try:
            return func(*args)
        except:
            return "Not found record with the name {name}!"
    return inner


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    @name_error_check
    def find(self, name):
        return self.data[name]
        
    @name_error_check
    def delete(self, name):
        self.data.pop(name)
    
    def __str__(self):
        book = ''
        for name, record in self.data.items():
            book += str(record) + "\n"
        return book


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)

# phone1 = '5555555555'
# phone2 = '4444444444'
# phone3 = '1111111111'
# john = Record('John')
# john.add_phone(phone1)
# john.add_phone(phone2)
# print(john)
# john.edit_phone(phone1, phone3)
# print(john)
# john.remove_phone(phone2)
# print(john)
# found = john.find_phone(phone3)
# print(found)