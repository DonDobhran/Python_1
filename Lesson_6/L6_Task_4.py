"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import time


class Car:

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = bool(is_police)


    def go(self):
        print("The car is start driving")

    def stop(self):
        print("The car is stopping")

    def turn_direction(self):
        print("Car had turned ")

    def show_speed(self, speed):
        print(speed)
        time.sleep(3)


class TownCar(Car):

    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self, speed, max_allowed=60):
        Car.show_speed(speed, max_allowed)
        max_allowed = 60
        if speed > max_allowed:
            print("Stop, stop, stop!!! Скорость превышена, нужно снижать")


class WorkCar(Car):

    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self, speed, max_allowed=40):

        if speed > max_allowed:
            print("Stop, stop, stop!!! Скорость превышена, нужно снижать")


class SportCar(Car):

    def sport_car(self):
        print("This is sport car... vrum, vrummmm")


class PoliceCar(Car):

    def police_car(self):
        print("This is Police Car, be careful with it!")


# print(TownCar)
# name = input("Введите название машины из представленного списка: ")

start_speed = speed = int(input("Введите начальное значение скорости больше 1: "))
Car_Town_1 = TownCar(speed, "Yellow", "Jaguar", True)
Car_2 = TownCar(speed, "Black", "VW", False)
Car_Police = PoliceCar
Car_3 = Car(speed, "Yellow", "Jaguar", True)

while speed > 1:
    if speed % 2 == 0:
        speed /= 2
    else:
        speed *= 3
        speed += 1
    Car_Town_1.show_speed(speed)
