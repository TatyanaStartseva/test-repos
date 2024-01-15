BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """It's a class that remembers an id ,a name and the number of pages of books.
    For instance:
    book = ( '1','1984','450')
    """
    def __init__(self, id_: int, name: str, pages: int):
        """A constructor that accepts a name, pages and an id book"""
        self.__id_ = id_
        self.__name = name
        if not isinstance(pages, int) or pages < 0:
            raise Exception("Number pages cannot be low that 0")
        else:
            self.__pages = pages

    def get_name(self) -> str:
        """ a method that return the name book"""
        return self.__name

    def get_id_(self) -> int:
        """ a method that return the id book"""
        return self.__id_

    def get_pages(self) -> int:
        """ a method that return the pages book"""
        return self.__pages

    def add_pages(self, count_new_pages: int):
        """ a method that return the id book"""
        if not isinstance(count_new_pages, int) or count_new_pages < 0:
            raise Exception("Number pages cannot be low that 0")
        else:
            self.__pages += count_new_pages

    def __str__(self) -> str:
        """a method that writes the name of a certain book"""
        return f'Книга "{self.__name}"'

    def __repr__(self) -> str:
        """a method that shows how we can make a book """
        return f"Book(id_={self.__id_!r}, name={self.__name!r}, pages={self.__pages!r})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
