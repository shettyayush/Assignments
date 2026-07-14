class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def display_books(self):
        print("\n========== Library Books ==========")

        for book in self.books:
            book.display_details()

    def display_members(self):
        print("\n========== Library Members ==========")

        for member in self.members:
            member.display_member_details()