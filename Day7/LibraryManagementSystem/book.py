class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True

    def is_available(self):
        return self.__available


    def set_availability(self, status):
        self.__available = status


    def display_details(self):
        status = "Available" if self.__available else "Borrowed"

        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN  : {self.isbn}")
        print(f"Status: {status}")
        print("-" * 35)