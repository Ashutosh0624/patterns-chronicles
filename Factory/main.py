'''
Factory method 

'''

from abc import ABC, abstractmethod

# Abstract factory ( Base class)
class AnimalFactory(ABC):
    @staticmethod
    def create_animal(self):
        pass 

# Concrete Factories
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal():
        return Cat()

# Product classes
class Animal(ABC):
    @staticmethod
    def speak(self):
        pass 

class Dog(Animal):   # Dog factory
    def speak(self):
        return "wooooof"
 
class Cat(Animal):    # Cat factory
    def speak(self):
        return "meiuuuuuuuuuuu"
    

if __name__ == "__main__":
    factory = DogFactory()     # Calling factory for dog
    dog = factory.create_animal()   
    print(dog.speak())

    factory = CatFactory()    # Calling factory for cat
    cat = factory.create_animal()
    print(cat.speak())

"""
                                                        Abstract factory
In Abstract factory, we create related objects of a family.

Creating multiple objects belonging to same family , for example family: Window , objects created : buttons, checkbox
"""

# Abstract products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete products for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows checkbox"

# Concrete products for mac 
class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"
    
class MacChceckbox(Checkbox):
    def render(self):
        return "Rendering Mac checkbox"

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factories
class WindowFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckbox()
    
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacChceckbox()

# Client Code
if __name__ == "__main__":
    factory = WindowFactory()  # Windows ke liye factory
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())  # Output: Rendering Windows Button
    print(checkbox.render())  # Output: Rendering Windows Checkbox

    factory = MacFactory()  # Mac ke liye factory
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())  # Output: Rendering Mac Button
    print(checkbox.render())  # Output: Rendering Mac Checkbox



"""

Factory Method: Jab ek hi cheez banani ho, lekin subclasses ko decision lena ho ki kaunsa object banana hai.

        Example: Dog ya Cat factory.

Abstract Factory: Jab ek family ke multiple objects banane ho jo ek saath compatible ho.

        Example: Windows ke Button aur Checkbox.

Factory Class: Jab aapko sirf ek centralized jagah chahiye jo objects banaye.

        Example: Dog aur Cat ek hi Factory class se banenge.



"""