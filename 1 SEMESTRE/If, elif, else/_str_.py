class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)