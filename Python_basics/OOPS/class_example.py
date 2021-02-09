#/usr/bin/venv python

class Person:
    def __init__(self, first_name, last_name, age):
        # Instance Variable
        print('Init Method Initialize')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Saby', 'Kar', 30)
p2 = Person('Arin', 'Kar', 4)


print(p1.first_name)
print(p2.first_name, p2.last_name, p2.age)
