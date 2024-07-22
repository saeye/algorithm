class Person:
    age = 19
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def hello(cls):
        print("안녕", cls.age)

    def eat(self):
        print('good')


p1 = Person('새에', 22)
p1.eat()
Person.hello()
