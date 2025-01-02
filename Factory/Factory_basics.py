from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"
    
class Rectangle(Shape):
    def draw(self):
        return "Drawing a rectangle"
    

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return circle()
        elif shape_type == "square":
            return Square
        elif shape_type =="rectangle":
            return Rectangle()
        else:
            raise ValueError("invalid shape type")
        

if __name__=="__main__":
    factory = ShapeFactory()
    shape = factory.create_shape("circle")
    print(shape.draw())