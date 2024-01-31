class Book:
    """ Базовый класс книги.
        We can create a book, which safe its name and author. In this class, we use a property for an attribute of our class.
        For instance: book = Book("Martin Eden", "Jack London"). name - "Martin Eden" , author - "Jack London".
        And we have methods that show information about the class.
    """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    """Creating properties to protect our name and author. The result of the call( in our example) : Martin Eden (for 
    name)"""

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    """Creating setters to protect our name and author. And added checks.
    For instants: book.name = "New" """
    @name.setter
    def name(self, new_name) -> None:
        if not isinstance(new_name, str):
            raise TypeError("A name must be a string")
        else:
            self._name = new_name

    @author.setter
    def author(self, author_name: str) -> None:
        if not isinstance(author_name, str):
            raise TypeError("A name must be a string")
        else:
            self._author = author_name

    """ A magic method, which shows information about class for users. The result in our example will be 
    Книга Martin Eden. Автор Jack London"""

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    """A magic method, which shows information about class for programmers. The result in our example will be 
    Book(name='Martin Eden', author='Jack London')  """

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ An inherited class. Has the same as the class 'Book', except for the attribute 'pages' """
    def __init__(self, name: str, author: str, pages: int = 0):
        super().__init__(name, author)
        self.pages = pages
    """ A getter for pages """
    @property
    def pages(self) -> int:
        return self._pages
    """ A setter for safe a pages. The setter has check ( that the number of pages is more than zero and that type is int)
    """
    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int) or new_pages < 0:
            raise TypeError("The number of pages must be an integer and more than zero")
        else:
            self._pages = new_pages
    """ In the methods 'str' and 'repr' added the number of pages """
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author} . Кол-во страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ An inherited class.Has the same as the class 'Book', except for the attribute 'duration'  """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    """ A getter for duration"""
    @property
    def duration(self) -> float:
        return self._duration
    """ A setter safe a new time. The setter has checks ( time > 0 and time is float) """
    @duration.setter
    def duration(self, new_time: float) -> None:
        if not isinstance(new_time, float) or new_time < 0.0:
            raise TypeError("The time must be a float and greater than zero")
        else:
            self._duration = new_time

    """ In the methods 'str' and 'repr' added the duration """
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


book = Book("Martin Eden", "Jack London")
print(book.name)
print(book.author)
book.name = "New"
print(book.__str__())
print(book.__repr__())
print("_________________________________________", '\n')
paperbook = PaperBook("Martin Eden", "Jack London", 100)
print(paperbook.name)
print(paperbook.author)
print(paperbook.pages)
print(paperbook.__str__())
print(paperbook.__repr__())
print("_________________________________________", '\n')
audiobook = AudioBook("Martin Eden", "Jack London", 25.6)
print(audiobook.name)
print(audiobook.author)
print(audiobook.duration)
print(audiobook.__str__())
print(audiobook.__repr__())
