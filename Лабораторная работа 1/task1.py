import doctest

class Flashlight:
    def __init__(self, power: int, mode: bool):
        """
        Создание оздание и подготовка к работе обьекта "Фонарик"
        :param power: Заряд (1-0% заряда, 2-25%,3-50% ,4-75%,5 -100%)
        :param mode: Режим работы (True-включен, False-выключен)

        Пример:
        >>> torch_1 = Flashlight(1,True) # инициализация экземпляра класса
        """
        if not isinstance(power, int):
            raise TypeError("Заряд батарии фонарика должен быть типа int")
        if (power < 1) and (power > 5):
            raise ValueError("Зачение заряда может менять только от 1 до 5")
        self.power = power
        if not isinstance(mode, bool):
            raise TypeError("Используется только тип bool")
        self.mode = mode
    def what_is_mode(self) -> bool:
        """
        Функиця которая проверяем включен ли фонарь

        :return: Является ли фонарь включенным

        Пример:
        >>> torch_1 = Flashlight(1,False)
        >>> torch_1.what_is_mode()
        """
        ...

    def change_power(self, zarad: int) -> str:
        """
        Функция которая меняет процент заряда фонаря

        :param zarad: Заряд фонарика после зарядки
        :raise ValueError: Если фонарь уже заряжен на 100%, возвращяется ошибка

        :return: Заряд фонаря после зарядки

        Пример:
        >>> torch_1 = Flashlight(1,True)
        >>> torch_1.change_power(5)
        """
        if not isinstance(zarad, int):
            raise TypeError("Зарядо должен быть типа int")
        if (zarad < 2) and (zarad > 5):
            raise ValueError("минимальный процент зарядки 25% и максимум зарядить можно на 100%")
        ...

class TV:
    def __init__(self, mode: bool, current_chanel: str, current_volume: int):
        """
        Создание и подготовка к работе обьекта "Телевизор"
        :param mode: Состояние телевизора (True-включен , False-выключен)
        :param current_chanel: Телеканал который сейчас включен
        :param current_volume: Громкость звука

        Пример:
        >>> tv_at_bedroom = TV(True,"CTC",80) #инициализация экземпляра класса
        """
        if not isinstance(mode, bool):
            raise TypeError("Состояние телевизора должно быть типа bool")
        self.mode = mode
        if not isinstance(current_chanel, str):
            raise TypeError("Название канала должно быть типа str")
        self.current_chanel = current_chanel
        if not isinstance(current_volume, int):
            raise TypeError("Громкость звука должнабыть типа int")
        if (current_volume < 1) and (current_volume > 100):
            raise ValueError("Громкость звука не должна быть меньше 1 и больше 100%")
        self.current_volume = current_volume

    def change_current_chanel(self, new_chanel: str) -> str:
        """
        Функиця меняет текуший канал на новый

        :param new_chanel: Название нового канала
        :raise TypeError: Если канал не пренадлежит типу str, то возвращяется ошибка

        :return: Название канала на который переключили телевизор

        Пример:
        >>> tv_at_room = TV(True, "НТВ", 50)
        >>> tv_at_room.change_current_chanel("ТВ3")
        """
        if not isinstance(new_chanel,str):
            raise TypeError("Название канала должно быть типа str")

        ...
    def change_current_volume(self, new_volume: int) -> str:
        """
        Функция меняет текущий показатель звука на новый

        :param new_voulme: Новая громкость звука
        :raise TypeError: Если новая громкость звука не пренадлежит типу int, то возвращяется ошибка
        :raise ValueError: Если новая громкость звука меньше 1 или больше 100 , то возвращяется ошибка

        :return: Новую громкость звука

        Пример:
        >>> tv_at_room = TV(True, "2x2",20)
        >>> tv_at_room.change_current_volume(50)
        """
        if not isinstance(new_volume,int):
            raise TypeError("Новая громкость звука Должно быть типа int")
        if (new_volume < 1) and (new_volume > 100):
            raise ValueError("Громкость звука не должна быть меньше 1 и больше 100%")
        ...

class Bottle:
    def __init__(self, liquid: str, volume: int, temperatyre: int):
        """
        Создание и подготовка к работе обьекта "Бутылка"

        :param liquid: Тип Жидкости
        :param volume: Объём бутылки в мл
        :param temperatyre: Температура (1-холодная, 2-теплая)

        Пример:
        >>> bottle_1 = Bottle("Кока-кола",50, 2) #инициализация экземпляра класса
        """
        if not isinstance(liquid, str):
            raise TypeError("Тип жидкости должен быть типа str")
        self.liquid=liquid
        if not isinstance(volume, int):
            raise TypeError("Обьём бутылки должен быть типа int")
        if volume <= 0:
            raise ValueError("Обьём бутылки не может быть отрицательным или равным 0")
        self.volume = volume
        if not isinstance(temperatyre, int):
            raise TypeError("Температура должен быть типа int")
        if (temperatyre < 1) and (temperatyre > 2):
            raise ValueError("Температура может принимать только значение 1 и 2")
        self.temperatyre = temperatyre

    def chill_the_bottle(self) -> None:
        """
        Функция которая меняет температуру бутылки на холодную

        Пример:
        >>> bottle_1 = Bottle("Квас", 10, 2)
        >>> bottle_1.chill_the_bottle()
        """
        ...
    def change_type_liquid(self, new_liquid: str) -> str:
        """
        Функция меняет тип жидкости в бутылке

        :param new_liquid: Новая жидкость
        :raise TypeError: Если новая жидкость не пренадлежит типу str, то возвращяется ошибка

        :return: Название новой жидкости в бутылке

        Пример:
        >>> bottle_1 = Bottle("Квас", 50, 2)
        >>> bottle_1.change_type_liquid("Сидр")
        """
        if not isinstance(new_liquid, str):
            raise TypeError("Новая жидкость должна быть типа str")
        ...

if __name__ == "__main__":
    bottle_3 = Bottle("Спрайт", 22, 2)
    print(bottle_3.volume, bottle_3.temperatyre)
    doctest.testmod()
    pass
