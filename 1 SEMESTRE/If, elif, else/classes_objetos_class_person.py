class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello My name is " + self.name)
        print(f"I am {self.age} years old")

p1 = Person("John", 36)
p1.myfunc()
