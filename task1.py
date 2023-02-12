import doctest

class Pills:
    """
        Создание и подготовка к работе базового класса "Таблетки"
    :param brand: производитель таблеток
    :param quantity: количество таблеток в коробке
    :param weight: вес пациента
    """
    def __init__(self, brand: str, quantity: int, weight: float):
        self.brand = brand
        self.quantity = quantity
        self.weight = weight

    def __str__(self)->str:
        return f"Производитель {self.brand}. Количествотаблеток {self.quantity}. Вес пациента{self.weight}"

    def __repr__(self) ->str:
        return f"{self.__class__.__name__} brand={self.brand!r}, quantity={self.quantity!r},weight={self.weight}"

    def quantity_suitable(self, quantity: int):
        """
        Функция, которая проверяет, что количество таблеток типа int
        :param quantity: количество таблеток в коробке
        :raise ValueError: Если количество таблеток указана не int, то вызываем ошибку
        Примеры:
        >>> pill = Pills("Стрепсилс",20, 40)
        >>> pill.quantity_suitable(20)
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество таблеток должно быть типа int")

    def weight_suitable(self, weight: float):
        """
        Функция, которая проверяет вес пациента
        :param weight: вес пациента
        :raise ValueError: Если вес пациента меньше 20 , то вызываем ошибку
        Примеры:
        >>> pill = Pills("Стрепсилс",20, 40)
        >>> pill.weight_suitable(40)
        """
        if weight < 20 :
            raise ValueError("Вес пациента должен быть больше 20")

    def dose_total(self) -> int:
        """
        Функция dose_total считает суточную дозу для взрослого человека
        """
        return self.weight // 20

class WaterSolublePills(Pills):
    """
    Создание дочернего класса "Водоростворимые таблетки".
    :param brand: производитель таблеток
    :param quantity: количество таблеток в коробке
    :param weight: вес пациента
    :param volume: объём воды для растворения таблетки
     """
    def __init__(self, brand: str, quantity: int, weight: float, volume: int):
        """
        Расширяем конструктор базового класса, так как у водорастворимых таблеток есть дополнительный атрибут - обьём требуемой воды (volume).
        """
        super().__init__(brand, quantity, weight)
        self.volume = volume

    def __str__(self)->str:
        """
        Перегружаем str, так как у водорастворимых таблеток есть дополнительный атрибут - обьём требуемой воды, и это надо отобразить в str
        """
        return f"Производитель {self.brand}. Количествотаблеток {self.quantity}. Вес пациента{self.weight}. Обьём требуемой воды {self.volume}"

    def __repr__(self) -> str:
        """
        Перегружаем repr так как у водорастворимых таблеток есть дополнительный атрибут - обьём требуемой воды, и это надо отобразить в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, quantity={self.quantity!r},weight={self.weight}, volume={self.volume!r}"

    def dose_total(self):
        """
        Перегружаем функцию dose_total, так как у водорастворимых таблеток другая формула подсчета дозы
        """
        return self.weight // 10


    @property
    def volume(self):
        """Возвращает объем требуемой воды"""
        return self._volume

    @volume.setter
    def volume(self, new_volume: int) -> None:
        """Устанавливает объем требуемой воды."""
        if not isinstance(new_volume, int):
            raise TypeError ("объем требуемой воды должен быть типа int")
        if not new_volume >= 1:
            raise ValueError ("объем требуемой воды должен быть положительным числом")
        self._volume = new_volume

print(WaterSolublePills("vitaminC", 40, 80, 200))
print(repr(WaterSolublePills("vitaminC", 40, 80, 200)))


byba = WaterSolublePills("vitaminC", 40, 80, 200)
print(byba.volume)  # вызываем как атрибут, но срабатывает метод
byba.volume = 100  # присваиваем значение атрибуту, но срабатывает метод
print(byba.volume)

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации