class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self, discount_rate):
        if 0 <= discount_rate <= 1:
            self.price -= self.price * discount_rate
            self.price = round(self.price, 2) 
        else:
            print("Discount rate must be between 0 and 1.")

    def display_details(self):
        print(f"Title: \"{self.title}\", Author: \"{self.author}\", Price: {self.price}")


book = Book(title="Python 101", author="John Doe", price=29.99)

book.discount(0.1)  
book.display_details()  
