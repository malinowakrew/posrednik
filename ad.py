import PySimpleGUI as sg
import pandas as pd
import numpy as np


def zeros():
    print("Zmiej niż zero")


def main():
    animal = Animal(3, "black", "Rysiek")
    animal.say_your_color_not_self()
    animal.say_your_color()
    animal.class_method()

    el = Elephant(4, "nicpoń")
    el.words()
    print("{} słowa {}".format(el.name, el.age))
    print(f"{el.name} cokolweik {80999999} {animal.age} el.name")

    b = Bear("88", 9, 9191)
    b.say_your_color()


class Animal:
    def __init__(self, age, color, name):
        self.age = age
        self.color = color
        self.name = name

    def say_your_color(self):
        print(self.color)

    @staticmethod
    def say_your_color_not_self():
        print("nie wiem nic o sobie")

    @classmethod
    def class_method(cls):
        print(cls.__name__)


class Elephant:
    def __init__(self, age, name):
        age = age + 10
        self.name = "Mr." + name
        self.age = age

    def words(self):
        print(f"MY name is {self.name}")


class Bear(Animal):
    def __init__(self, age, name, weigh):
        super().__init__(age=age, name=name, color="brown")
        self.weigh = weigh


if __name__ == "__main__":
    main()