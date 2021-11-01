import random


class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f" Машина {self.name} едет")

    def stop(self):
        print(f" Машина {self.name} остановилась")

    direction = ["вправо", "влево", "вперед", "назад"]

    def turn(self):
        print(f"Машина {self.name} {random.choice(self.direction)}")

    def show_speed(self):
        print(f" Скорость машины {self.name} {self.speed}")


class TownCar(Car):
    def show_speed(self):
        return f"Машина превысила скорость" if int(self.speed) > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f"Машина превысила скорость" if int(self.speed) > 40 else super().show_speed()


class SportCar(Car):
    """ Спортивная машина """


class PoliceCar(Car):
    """ Полицейская машина """


police_car = PoliceCar("Полицейская", "белая", 80, True)
work_car = WorkCar("Грузовик", "черная", 45, False)
sport_car = SportCar("Спортиная", "красная", 110, False)
town_car = TownCar("Городская", "серая", 70, False)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

