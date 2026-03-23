class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book '{self.title}' by {self.author} added to library.")

    def __del__(self):
        print(f"Book '{self.title}' removed from library.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        print(f"Member {self.name} (ID: {self.member_id}) registered.")


b1 = Book("1984", "George Orwell")
m1 = Member("Alice", 101)

del b1  