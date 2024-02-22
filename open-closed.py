"""
Open/Closed principle. Open for extension, closed for modications.
"""
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())
