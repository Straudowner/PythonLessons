
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.speed = '150 km/h'
        self.is_police = False
    def go(self):
        print('Поехала')
    def stop(self):
        print('Остановилась')
    def turn(direction):
        print('Повернула(куда)')

class WorkCar(Car):
    pass
class TownCar(WorkCar):
    pass
class SportCar(TownCar):
    def __init__(self, name):
        super().__init__(self)
        self.color = 'red'
        self.speed = '300 km/h'
class PoliceCar(SportCar):
    def __init__(self, name):
        super().__init__(self)
        self.color = 'White&Black'
        self.is_police = True

workcar = WorkCar('VW Transporter')
towncar = TownCar('Kia Rio')
sportcar = SportCar('Porsche 911')
policecar = PoliceCar('Ford Police Interceptor')




