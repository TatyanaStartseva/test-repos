from typing import Optional

from typing import List

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


class Book:
    """It's a class that remembers an id ,a name and the number of pages of books.
    For instance:
    book = ( '1','1984','450')
    """

    def __init__(self, id_: int, name: str, pages: int):
        """A constructor that accepts a name, pages and an id book"""
        self.__id = id_
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
        return self.__id

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
        return f"Book(id_={self.__id!r}, name={self.__name!r}, pages={self.__pages!r})"


# TODO написать класс Book


# TODO написать класс Library
class Library:
    """ A class Library which has a list with books ( an id, a name, a pages)
    For instance:
    books = [ { '1','1984','450'}, {'2',' Jack London','550'}]
    """
    books = List[Book]

    def __init__(self, books: List[Book] = []):
        """Initializing our list """
        self.books = books.copy()

    @property
    def get_next_book_id(self) -> int:
        """We create the id of the next book, if we don't have a book, when we'll return 1
        For instance:
        an id = 0 -> return 1
        an id = 3 -> return 4
        """
        if len(self.books) == 0:
            return 1
        else:
            count = self.books[len(self.books) - 1].get_id_()
            return count + 1
    def get_index_by_book_id(self, book_id: int) -> int:
        """We are creating an index book in the list with certain id
        For example:
        we have this books in our library
        books = [ { '1','1984','450'}, {'2',' Jack London','550'}]
        we want to know index book with id = 1. Result = 0
        """
        for index, book in enumerate(self.books):
            if book.get_id_() == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id)  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id)  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
