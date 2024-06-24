#Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

class Product():
    def __init__(self, name, product_id, price):
        self.name = name
        self.product_id = product_id
        self.price = price

    def get_product_id(self):
        print(f"{self.product_id}, with the ID: {self.name}, retails at the value of ${self.price}.")


class Book(Product):
    def __init__(self, name, product_id, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def book_display(self):
        print(f"{self.product_id} written by {self.author}, retails at {self.price}. For more information on {self.name}, use product ID: {self.name} to search the database.")


book1 = Book('Dune', 426578, 17.95, 'Frank Herbert')
book2 = Book("Bone Silence", 789450, 19.95, 'Alistair Reynolds')
book3 = Book('The Hobbit', 124658, 14.95, 'J.R.R. Tolkien')


book1.book_display()