from random import randint
class Map:
    def __init__(self, distance):
        self.movement_strategy = OnFootStrategy(-1)
        self.distance = distance

    def chek_strategy(self):
        if self.distance <= 5:
            self.movement_strategy = OnFootStrategy(self.distance)
        elif 5 < self.distance <= 20:
            self.movement_strategy = ByBikeStrategy(self.distance)
        elif self.distance > 20:
            self.movement_strategy = ByCarStrategy(self.distance)


    def go(self):
        self.chek_strategy()
        self.movement_strategy.go()


class MovementStrategy:
    def __init__(self, distance, way, speed):
        self.way = way
        self.speed = speed
        self.distance = distance

    def go(self):
        pass


class OnFootStrategy(MovementStrategy):
    def __init__(self, distance, way='Пешком', speed=5):
        super().__init__(distance, way, speed)

    def go(self):
        print(f'Путь построен, вам следует отправится {self.way}, со средней скоростью {self.speed} км\\ч вы '
              f'преодолеете путь в {self.distance}км за {round(self.distance / self.speed, 1)} часа')


class ByBikeStrategy(MovementStrategy):
    def __init__(self, distance, way='На велосипеде', speed=randint(5, 25)):
        super().__init__(distance, way, speed)

    def go(self):
        print(f'Путь построен, вам следует отправится {self.way}, со средней скоростью {self.speed} км\\ч  вы '
              f'преодолеете '
              f'путь в {self.distance}км за {round(self.distance / self.speed, 1)} часа ')


class ByCarStrategy(MovementStrategy):
    def __init__(self, distance, way='На машине', speed=randint(35,110)):
        super().__init__(distance, way, speed)

    def go(self):
        print(f'Путь построен, вам следует отправится {self.way}, со средней скоростью {self.speed} км\\ч  вы '
              f'преодолеете '
              f'путь в {self.distance}км за {round(self.distance / self.speed, 1)} часа')


def main():

    goto = Map(4)
    goto.go()

    goto = Map(7)
    goto.go()

    goto = Map(1000)
    goto.go()

if __name__ == '__main__':
    main()