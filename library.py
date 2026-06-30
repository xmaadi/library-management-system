class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            b.display()

    def issue_book(self, title):
        for b in self.books:
            if b.title == title:
                b.issue_book()
                return
        print("Book not found.")

    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.return_book()
                return
        print("Book not found.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None