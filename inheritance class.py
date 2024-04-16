from abc import ABC,abstractmethod
class publication(ABC):
    org = 'ABC pvt'
    CEO = 'sam'
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def show(self):
        print(self.title)
        print(self.price)

    def discount(self):
        self.price = self.price - (self.price *0.5)
        
    @abstractmethod
    def address():
        pass    
    
class periodic(publication):
    def __init__(self,title, publisher, price, period):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher

    def show(self):
        super().show()
        print(self.period)
        print(self.publisher)

class Book(publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages

    def show(self):
        super().show()
        print(self.pages)
        print(self.author)
        
    @staticmethod
    def address():
        print('chennai')

class Magazine(periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

    def show(self):
        super().show()
    
    @staticmethod
    def address():
        print('chennai')

class Newspaper(periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

    def show(self):
        super().show()
        
    # @staticmethod
    # def address():
    #     print('velachery')



b1 = Book("wings of f", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")
# p1 = publication('kanna',25)
# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)
# print(n1.CEO)
# print(m1.CEO)
m1.show()
b1.address()
