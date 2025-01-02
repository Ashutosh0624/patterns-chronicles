from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def animal_type(self):
        pass

class Dog(Animal):
    ''' A simple dog class '''
    def __init__(self, name):
        self._name = name 

    def speak(self):
        return "woof"

    def animal_type(self):
        return "Dog"

class Cat(Animal):
    def __init__(self, name):
        self._name = name 

    def animal_type(self):
        return "Cat"
    
class AnimalFactory:
    @staticmethod
    def animal_type(species_type):
        if species_type == "dog":
            return Dog('sheru')
        elif species_type == "cat":
            return Cat('willi')
        else:
            raise ValueError("Invalid species type")

if __name__ == "__main__":
    animal = AnimalFactory()
    pet_type = animal.animal_type('dog')
    print(pet_type.animal_type())
    print(pet_type._name)