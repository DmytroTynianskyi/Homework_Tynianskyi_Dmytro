# Завдання 2
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Review:
    def __init__(self, reviewer, rating, text):
        self.reviewer = reviewer
        self.rating = rating
        self.text = text

    def __str__(self):
        return f"{self.reviewer} rated {self.rating}/5: {self.text}"


class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []  

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        book_info = f"'{self.title}' by {self.author}, {
            self.year}, Genre: {self.genre}\nReviews:"
        if not self.reviews:
            book_info += "\n  No reviews yet."
        else:
            for review in self.reviews:
                book_info += f"\n  {review}"
        return book_info


book1 = Book("George Orwell", "1984", 1949, "Dystopia")
book2 = Book("J.K. Rowling",
             "Harry Potter and the Philosopher's Stone", 1997, "Fantasy")

review1 = Review("Alice", 5, "A thought-provoking masterpiece.")
review2 = Review("Bob", 4, "Great book but a bit heavy in themes.")
review3 = Review("Charlie", 5, "A timeless classic.")

book1.add_review(review1)
book1.add_review(review2)
book2.add_review(review3)

print(book1)
print(book2)
