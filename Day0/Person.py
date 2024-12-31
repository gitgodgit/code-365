class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name}, {self.age})"
    
    def sayHello(self):
        print(f"Hello my name is {self.name}")