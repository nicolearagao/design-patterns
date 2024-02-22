"""
One and only object of a given type, provides a global access.
Solves: Avoid conflicting requests
Problem: Violates Single responsability principle
Steps: 
    - private constructor, stop other objects to use dunder now
    - static creation method that act out as a constructor, 
    calls private constructor under the hood, return cached object.
"""

# 1- non-thread safe, not using lazy instantiation
# creates the instance as soon as the class is imported or accessed, even if it’s not immediately needed.
# In a multi-threaded environment, two threads attempting to access the Singleton simultaneously might end up
# creating two separate instances.

#explicitly specifies the class and its superclass from which to inherit the __new__ method
 # multiple parent classes(mixin)  
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
 # relies on Python's method resolution order (MRO) to determine the appropriate superclass to call. 
 
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()


# non-thread safe, using lazy instantiation
class Singleton:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Example usage
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()


import threading

# thread-safe
# python isn't multi-threaded, it uses processes. Processes might share memory, but it might become over problematic.
class Singleton:
    _instance = None
    _lock = threading.Lock()  # Add a lock for thread safety
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# decorator approach Singleton
def Singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@Singleton
class Wizard:
    def __init__(self, name):
        self.name = name
    
# Singleton through meta classes for separation of concerns    
class SingletonMeta(type):
    _instances = {} #why not _instances = None ?
    # this keeps tracks of all singletons, that might share the same meta class
    # if None, one would replace the other

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Wizard(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

