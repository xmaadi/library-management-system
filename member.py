from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_info(self):
        pass


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed_books = []

    @abstractmethod
    def borrow_limit(self):
        pass

    def display_info(self):
        print(f"Name : {self.name}.")
        print(f"Member Id : {self.member_id}")
        print(f"Books borrow count : {len(self.borrowed_books)}\n")

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit():
            print(f"{self.name} has reached borrow limit!\n")
            return
        if book.is_issued:
            print(f"{book.title} is already issued.")
            return

        book.issue_book()
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}\n")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
            return

        print("Borrowed books:")
        for book in self.borrowed_books:
            print(f"- {book.title}\n")


class StudentMember(Member):
    def borrow_limit(self):
        return 2


class TeacherMember(Member):
    def borrow_limit(self):
        return 5