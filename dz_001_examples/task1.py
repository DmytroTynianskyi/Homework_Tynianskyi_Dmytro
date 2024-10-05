# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву,
# рік видання та жанр. Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_..

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Book(author='{self.author}', title='{self.title}', year={self.year}, genre='{self.genre}')"

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year}, Genre: {self.genre}"

book1 = Book("George Orwell", "1984", 1949, "Dystopia")
book2 = Book("J.K. Rowling","Harry Potter and the Philosopher's Stone", 1997, "Fantasy")
book3 = Book("Harper Lee", "To Kill a Mockingbird", 1960, "Fiction")

print(book1)  
print(repr(book2)) 
print(book3) 
