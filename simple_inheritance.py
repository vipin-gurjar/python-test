class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Parent:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Child:", self.name, ", Age:", self.age)

parent = Parent("vipin")
child = Child("test", 10)

parent.display()
child.display()

    
