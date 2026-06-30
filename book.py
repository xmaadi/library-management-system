class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        print(f"Title of book : {self.title}.")
        print(f"Author of {self.title} : {self.author}.")
        status = "Issued" if self.is_issued else "Available"
        print(f"Status : {status}\n")

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued successfully")
        else:
            print("Book issued already")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book returned successfully")
        else:
            print("Book wasn't issued, can't return")