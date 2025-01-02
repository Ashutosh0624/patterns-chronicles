from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def animal_type(self):
        pass

class Dog(Animal):
    def animal_type(self):
        return "Dog"

class Cat(Animal):
    def animal_type(self):
        return "Cat"
    
class AnimalFactory:
    @staticmethod
    def animal_type(species_type):
        if species_type == "dog":
            return Dog()
        elif species_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid species type")

if __name__ == "__main__":
    animal = AnimalFactory()
    pet_type = animal.animal_type('dog')
    print(pet_type.animal_type())