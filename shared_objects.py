class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def greeting(self):
        print(self.first + " " + self.last + " is " + str(self.age) + " years old!")

# instantiate our class, and try it out
test = Person("Jon", "Doe", 34)
test.greeting()