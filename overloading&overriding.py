# Overloading example
def add(*args):
    if len(args) == 2:
        return args[0] + args[1]
    elif len(args) == 3:
        return args[0] + args[1] + args[2]

# Overriding example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Overloading example
print("Overloading example:")
print(add(2, 3))
print(add(2, 3, 4))

# Overriding example
print("\nOverriding example:")
animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()

