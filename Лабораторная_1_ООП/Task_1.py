import datetime
from abc import ABC, abstractclassmethod
import datetime as dt


class Human:
    """
    Класс 'Человек' у него можно задать такие параметры как : возраст, имя, гендер. И с помощью методов добавить дополнительные параметры, такие как : вес,рост, профессию.
    При необходимости получить значение параметров, т.к. класс тут не публичный, а приватный.
    """

    def __init__(self, name: str, date_burn: int, gender: str, current_year=datetime.datetime.now().year):
        self.__weight = None
        self.__height = None
        if type(name) != str or type(date_burn) != int or type(gender) != str:
            raise TypeError("invalid data type")
        self.__gender = gender
        self.__name = name
        self.__age = current_year - date_burn
        self.__profession = None

    def change_profession(self, prof: str) -> None:
        if not isinstance(prof, str):
            raise TypeError("This is not the name of the profession. Please write the name of your profession")
        self.__profession = str

    def add_parameters(self, weight: float, height: float) -> None:
        if not isinstance(weight, float) or not isinstance(height, float):
            raise TypeError("Please, write the weight and the height as floating numbers")
        if weight < 0 or height < 0:
            raise TypeError("Weight and height cannot be negative ")
        self.__weight = weight
        self.__height = height

    def get_parameters(self, attrib):
        attributes = {'age': self.__age, 'name': self.__name, 'profession': self.__profession, 'gender': self.__gender,
                      'height': self.__height, 'weight': self.__weight}
        return attributes[attrib]


class Monster(ABC):
    def __init__(self, mons_type: str, power: int, attack: str, attack_part_of_body: str, x: int, y: int):
        if type(mons_type) != str or type(power) != int or type(attack) != str or attack_part_of_body != str or type(
                x) != int or type(y) != int:
            raise TypeError("invalid types")
        self.attack = attack
        self.type_mons = mons_type
        self.power = power
        self.x = x
        self.y = y
        self.attack_part_of_body = attack_part_of_body
        self.time = None  # time when someone improve his power. If someone improved his power and don't go more that
        # 12 hours, we cannot develop his power. (limit)

    def attack(self) -> None:
        print('vzhuh' + self.attack)

    def improve_power(self) -> int:
        temp_time = self.time;
        temp_time += dt.datetime.hour(12);
        self.time = dt.time.hour();
        if self.time <= temp_time:
            print('Wait, when you can again improve your power', temp_time - self.time)
            return
        self.power += self.power
        return self.power


class Bat(Monster):
    def __init__(self, type_mons: str, power: int, attack: str, attack_part_of_body: str, x: int, y: int, z: int):
        self.y = y
        if z < 0 or type(z) != int:
            raise TypeError("invalid types")
        self.z = z

    def attack(self) -> None:
        print('Кусь')

    def fly(self, x: int, y: int, z: int) -> None:
        if (self.z - z) < 0:
            print(' Our bat is not able to fly in the hole')
            return
        self.x += x
        self.y += y
        self.z += z


class Werewolves(Monster):
    def attack(self) -> None:
        print('rrrr')

    def jump(self, x: int, y: int, z: int) -> None:
        if (self.z - z) < 0:
            print(' Our werewolves is not able to go down')
            return
        self.x += x
        self.y += y
        self.z += z


b = Bat('black', 100, 'k', 'theeth', 0, 0, 0)
p = Human('Dima', 1999, 'M')
y = Human('nnnn', 2000, 'M')
print(p.get_parameters('name'))
print(y.get_parameters('name'))
