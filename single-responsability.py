"""
Single responsability: one reason to change, one job.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    Person.save(p)

# two jobs = manage person's property, save person to database

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')

# separating responsabilities, the downside of this solution is that the clients of the this code have to deal
# with two classes.
        
class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)

# using facade DP for conveniency
        
