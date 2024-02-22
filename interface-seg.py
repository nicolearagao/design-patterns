"""
Interface seggregation: an interface shouldn't be forced to implement methods it doesn't use.
 abstract classes -> "if it walks like a duck, it must be a duck", methods will determine what its objects will be,
 not the type fo class. Cohesion -> it must do one thing
"""
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_chicken(self):
        pass

class MeatPizza(Pizza):
    def add_cheese(self):
        print("Cheese being added...")

    def add_chicken(self):
        print("Chicken being added...")


class VegPizza(Pizza):
    def add_cheese(self):
        print("Cheese being added...")

    def add_chicken(self):
        raise Exception('There is no chicken in veg pizzas.')
