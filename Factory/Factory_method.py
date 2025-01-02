from abc import ABC, abstractmethod

# Abstract creator 
class Animal(ABC):
    @staticmethod
    def speak(self):
        pass 

# Concrete  Implementation

class Dog(Animal):
    def __init__(self, name):
        self._name = name 

    def speak(self):
        return "wooof"

class Cat(Animal):
    def __init__(self, name):
        self._name = name 
    
    def speak(self):
        return "meiuuuu"
    
# Abstract creator

class AnimalFactory(ABC):
    @staticmethod
    def create_animal(self, name):
        pass 

# concrete factories

class DogFactory(AnimalFactory):
    def create_animal(self, name):
        return Dog(name)
    
class CatFactory(AnimalFactory):
    def create_animal(self, name):
        return Cat(name)
    

# Client Code
if __name__ == "__main__":
    # Create a Dog using the DogFactory
    dog_factory = DogFactory()
    dog = dog_factory.create_animal("Sheru")
    print(dog.speak())  # Output: Sheru says: Woof!

    # Create a Cat using the CatFactory
    cat_factory = CatFactory()
    cat = cat_factory.create_animal("Whiskers")
    print(cat.speak())  # Output: Whiskers says: Meow!