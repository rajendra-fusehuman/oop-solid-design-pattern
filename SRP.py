class Book:
    def __init__(self, title, author, ISBN, genre, availability):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.availability = availability

    def get_details(self):
        print("\nThe details of the book are as follows:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Genre: {self.genre}")
        print(f"availability: {self.availability}")


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        print(f"\nList of all available books:")
        for book in self.books:
            print(book.title)

    def get_book_details(self, book):
        book.get_details()


def main():
    book1 = Book("Outlier", "Malcolm Gladwell", 12345, "Non-Fiction", True)
    book2 = Book("Pride and Prejudice", "Jane Auster", 67890, "Classical Fiction", False)
    library = LibraryCatalog()

    library.add_book(book1)
    library.add_book(book2)
    library.get_all_books()

    library.get_book_details(book1)

if __name__ == '__main__':
    main()
