# important concepts

#__init__ (welcoming host of an object)
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

#__new__ (customize object creation)
class Dog:
    def __new__(cls, model):
        dog_instance = super(Dog, cls).__new__(cls)
        dog_instance.model = model
        return dog_instance

# __call__ metaclasses creation (invoked whenever a new instance of a class is created) 

class DogMeta(type):
    def __call__(cls, name, breed):
        print("Creating a new dog...")
        instance = super().__call__(name, breed)
        return instance

class Dog(metaclass=DogMeta):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed