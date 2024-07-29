"""Task - Address Book"""


from collections import UserDict


class Field:
    """
    Base class for record fields
    """
    def __init__(self, value):
        """
        Initializes the instance based on type of field.

        Args:
          value: The value of the field
        """
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    A class for storing a contact name.
    """
    pass


class Phone(Field):
    """
    A class for storing a phone number.
    """
    def __init__(self, value):
        """
        Initializes the phone number field.

        Args:
          value: The phone number
        
        Raises:
          ValueError if phone number doesn't have 10 digits
        """
        if not self.validate(value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

    def validate(self, phone):
        """
        Validates if phone number has 10 digits.
        """
        return phone.isdigit() and len(phone) == 10


class Record:
    """
    A class for storing information about a contact, 
    including name and phone list.
    """
    def __init__(self, name):
        """
        Initializes the instance based on record.

        Args:
          name: The contact name.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Adds phone number to the record.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """
        Removes specific phone number from the record.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Replaces old phone number with new phone number
        in the record.
        """
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        """
        Finds specific phone number in the record.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    A class for storing and managing records.
    """
    def add_record(self, record):
        """
        Adds the record to the address book.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Finds the record by the name.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Removes the record from address 
        book by the name.
        """
        if name in self.data:
            del self.data[name]


# Code testing
if __name__ == "__main__":
    # Creating the new address book
    book = AddressBook()

    # Creating new record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding record for John to the address book
    book.add_record(john_record)

    # Creating and adding new record fof Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Outputing all records of address book
    for name, record in book.data.items():
        print(record)

    # Finding and editing phone number for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    # Finding specific phone number in record for John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Deleting record for Jane
    book.delete("Jane")

    # Outputing all records of address book
    for name, record in book.data.items():
        print(record)
