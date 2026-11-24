# Адресна книга

Реалізація на Python 3.7+ із використанням стандартної бібліотеки.

## Приклад використання

```python
from address_book import AddressBook, Record

book = AddressBook()
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")
book.add_record(john)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
print(john.find_phone("5555555555"))

book.delete("John")
```
