class Flashlight:
    def __init__(self,power :int,mode: bool,):
        """
        Создание оздание и подготовка к работе обьекта "Фонарик"
        :param power: Заряд (1-0% заряда, 2-25%,3-50% ,4-75%,5 -100%)
        :param mode: Режим работы (True-включен, False-выключен)

        Пример:
        >>> torch_1 = Flashlight(1,True)
        """
        if not isinstance(power, int):
            raise TypeError
        self.power = power
        if power < 1 and power>5:
            raise ValueError
        self.power = power
        if not isinstance(mode, bool):
            raise TypeError
        self.mode = mode
    def change_mode(self):
        ...# Изменить режим работы
    def change_power(self):
        ...# Зарядить батарейку в фонаре

if __name__ == "__main__":
    flashlight1 = Flashlight(0,False)
    print(flashlight1.power, flashlight1.mode)
    doctest.testmod()
    pass


class TV:
    def __init__(self,mode: bool, current_chanel: str,current_volume: int):
        """
        Создание и подготовка к работе обьекта "Телевизор"
        :param mode: Состояние телевизора (True-включен , False-выключен)
        :param current_chanel: Телеканал который сейчас включен
        :param current_volume: Громкость звука

        Пример:
        >>> tv_at_bedroom = TV(True,"CTC",80) #инициализация экземпляра класса
        """
        if not isinstance(mode, bool):
            raise TypeError
        self.mode = mode
        if not isinstance(current_chanel, str):
            raise TypeError
        self.current_chanel = current_chanel
        if current_volume < 1 and current_volume > 100:
            raise ValueError
        self.current_volume = current_volume
    def change_current_chanel(self):
        ...# Изменить канал
    def change_current_volume(self):
        ...# Изменить громкость

if __name__ == "__main__":
    televizor = TV(False,"ТНТ",30)
    print(televizor.current_chanel, televizor.current_volume)
    doctest.testmod()
    pass

class Bottle:
    def __init__(self, liquid:str,volume: int,temperatyre:int):
        """
        Создание и подготовка к работе обьекта "Бутылка"
        :param liquid: Тип Жидкости
        :param volume: Объём бутылки в мл
        :param temperatyre: Температура (1-холодная, 2-теплая)

        Пример:
        >>> bottle_1 = Bottle("Кока-кола",500, 2) #инициализация экземпляра класса
        """
        if not isinstance(liquid, str):
            raise TypeError
        self.liquid=liquid
        if volume < 0:
            raise ValueError
        self.volume = volume
        if temperatyre <1 and temperatyre>2:
            raise ValueError
        self.temperatyre = temperatyre
    def chill_the_bottle(self):
        ...# Изменить темпетаруту бутылки
    def change_type_liquid(self):
        ... # Вылить предыдущую жидкость, налить новую

if __name__ == "__main__":
    bottle_1 = Bottle("Спрайт",220,2)
    print(bottle_1.volume, bottle_1.temperatyre)
    doctest.testmod()
    pass
