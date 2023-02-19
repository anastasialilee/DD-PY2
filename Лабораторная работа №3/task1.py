class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
        super().__init__(name, author)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages:int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError('Страницы должны быть типа int')
        if new_pages <= 0:
            raise ValueError('Страницы должны быть положительным числом')
        self._pages = new_pages

class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    def __repr__(self):
        return f"{self.__class__.name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError('Длительность должна быть типа float')
        if new_duration <= 0:
            raise ValueError('Длительность должна быть положительным числом')
        self._duration = new_duration

