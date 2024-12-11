class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book_title):
        if book_title not in self.books:
            self.books.append(book_title)
        else:
            print(f"The book '{book_title}' is already in the library.")

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
        else:
            print(f"The book '{book_title}' is not found in the library.")

    def __str__(self):
        return f"Name: \"{self.name}\", Address: \"{self.address}\", Books: {self.books}"


library = Library(name="City Library", address="123 Main St")

library.add_book("Book1")
library.add_book("Book2")
library.remove_book("Book1")

print(library) 