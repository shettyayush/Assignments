from person import Person

class Member(Person):
    MAX_BOOKS = 3

    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if not book.is_available():
            print(f"Book '{book.title}' is currently not available.")
            return

        if len(self.__borrowed_books) >= Member.MAX_BOOKS:
            print(f"{self.name} cannot borrow more than {Member.MAX_BOOKS} books.")
            return

        self.__borrowed_books.append(book)
        book.set_availability(False)

        print(f"{self.name} borrowed '{book.title}' successfully.")

    def return_book(self, book):
        if book not in self.__borrowed_books:
            print(f"{self.name} has not borrowed '{book.title}'.")
            return

        self.__borrowed_books.remove(book)
        book.set_availability(True)

        print(f"{self.name} returned '{book.title}' successfully.")

    def display_member_details(self):
        print(f"\nMember Name : {self.name}")
        print(f"Member ID   : {self.member_id}")

        if self.__borrowed_books:
            print("Borrowed Books:")
            for book in self.__borrowed_books:
                print(f"- {book.title}")
        else:
            print("Borrowed Books: None")

        print("-" * 35)

    def get_borrowed_books(self):
        return self.__borrowed_books