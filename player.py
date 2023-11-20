# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)
