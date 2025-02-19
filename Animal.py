class Animal:
    def __init__(self, name):
        self.__name = name
        print("Hello, I am", self.__name)

    def talk(self):
        print("Hi")

    def eat(self, food):
        print(self.__name, "is eating", food)

    def sleep(self):
        print(self.__name, "is sleeping")

    def move(self):
        print(self.__name, "is moving around")

    def play(self):
        print(self.__name, "is playing")



   
