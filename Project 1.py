class Book :
	def __init__(self, title, author, ):
		self.title = title
		self.author = author 
		self.is_issued = False 
		
	def display(self):
		print(f"Title of book : {self.title}.")
		print(f"Author of {self.title} : {self.author}.")
		status = "Issued" if self.is_issued else "Available"
		print(f"Status : {status}\n")
	
	def issue_book(self):
		if not self.is_issued  :
			self.is_issued = True 
			print("Book issued successfully")			
		else :
			print("Book issued already ")
						
	def return_book(self):
		if self.is_issued  :
			self.is_issued = False 
			print("Book returned successfully")			
		else :
			print("Book wasn't issued, can't return")
			
class Library :
	def __init__(self):
		self.books = [ ]
			
	def add_book(self, book):			
		self.books.append(book)
			
	def show_books(self):
		for b in self.books :
			b.display( )
	
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
			
		def borrow_book (self, book):
			if len(self.borrowed_books) >= self.borrow_limit( ):
				print(f"{self.name} has reached borrow limit!\n")
				return 
			if book.is_issued:
				print(f"{book.title} is already issued.")
				return 
				
			book.issue_book()
			self.borrowed_books.append(book)
			print(f"{self.name} borrowed {book.title}\n")
			
		def return_book(self, book):
			if book in self.borrowed_books :
				book.return_book()
				self.borrowed_books.remove(book)
				print(f"{self.name} returned {book.title}")
			else :
				print(f"{self.name} did not borrow  {book.title}")
				
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
			
b1 = Book("Atomic Habits ", "James Clear")
s1 = StudentMember("Aadi", "S001")
b2 = Book("Deep Work", "Cal Newport")
b3 = Book("Think and Grow Rich", "Napoleon Hill")

s1.borrow_book(b2)
s1.borrow_book(b3)

s1.borrow_book(b1)

s1.display_info()
s1.show_borrowed_books()
b1.display()


s1.return_book(b2)
s1.display_info()
s1.show_borrowed_books()
