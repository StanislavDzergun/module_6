class Human:
    def __int__(self, name):
        self.name = name

    def info(self):
        print(f'Привет, меня зовут {self.name}')


class Student(Human):
    def __init__(self, name, place):
        super().__init__(name)
        self.place = place
        super().info()

human = Human('Денис')
print(human.name)
student = Student('Макс', 'Урбан')
