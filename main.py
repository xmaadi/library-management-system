from book import Book
from library import Library
from member import StudentMember, TeacherMember

# Library setup
lib = Library()

b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Deep Work", "Cal Newport")
b3 = Book("Think and Grow Rich", "Napoleon Hill")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.show_books()

# Member setup
s1 = StudentMember("Aadi", "S001")

s1.borrow_book(b2)
s1.borrow_book(b3)
s1.borrow_book(b1)   # should hit limit (StudentMember = 2)

s1.display_info()
s1.show_borrowed_books()

s1.return_book(b2)
s1.display_info()
s1.show_borrowed_books()

lib.show_books()