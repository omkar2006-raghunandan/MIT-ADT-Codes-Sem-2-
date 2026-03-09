# class Book:
#     def __init__(self, book_name, author):
#         self.book_name = book_name
#         self.author = author
#         self.available = True

#     def checkout(self):
#         if self.available:
#             self.available = False
#             print(f'"{self.book_name}" has been checked out.')
#         else:
#             print(f'"{self.book_name}" is currently unavailable.')

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print(f'"{self.book_name}" has been returned.')
#         else:
#             print(f'"{self.book_name}" was not checked out.')


class library:
    def __init__(self, book_name, author, available = True):
        self.book_name = book_name
        self.author  = author
        self.available = available

    def check_out(self):
        if self.available:
           self.available = False
           print(f"{self.book_name} has been checked out.")
        else:
            print(f"{self.book_name} is currently not available. ")

    def return_book(self):
        self.available = True
        print(f"{self.book_name} has been returned and is now available")

    def display_book(self):
        status = "Available" if self.available else "not Available"
        print(f"Book name: {self.book_name}, Author: {self.author}, Status: {status}")
    book1 = library("Python Programming", "guido van Rossum")
    book2 = library("Data Structure", "Mark Allen Weiss")

    book1.display_book()
    book1.check_out()
    book1.display_book()