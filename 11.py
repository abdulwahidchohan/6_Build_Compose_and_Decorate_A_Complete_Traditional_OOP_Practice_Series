class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.tool_book += 1
        