class Road:

    __lenght = None
    __width = None
    weight = None
    thickness = None
    def __init__ (self, length, width):
        self.lenght = length
        self.width = width
        print('Данные получены')

    def calculate(self):
        self.weight = 25
        self.thickness = 0.05
        calc = self.lenght * self.width * self.weight * self.thickness / 1000
        print(f'Необходимо {calc} тонн для строительства')

my_road = Road(20000, 6)
my_road.calculate()