#/usr/bin/venv python 

class Person:
    def __init__(self, first_name, last_name, age):
        print(" INIT METHOD")
        self.first_name = first_name
        print("Search for last_name")
        self.last_name = last_name
        print("Searching for age")
        self.age = age

    def full_name(self):
        print("SECOND FUNCTION EXECUTE")
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        print("Print Details")
        return self.age>18



p1 = Person('Saby', 'Kar', 24)
#p2 = Person('Arin', 'Kar', 4)


## print(p2.full_name())
#print(Person.full_name(p2))
print(p1.is_above_18())


