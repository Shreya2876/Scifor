from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    def print_message(self):
        print("This is a shape.")

class Circle(Shape):

    def draw(self):
        print("circle")

class Square(Shape):

    def draw(self):
        print("square")

def main():
    shape1 = Circle()
    shape2 = Square()

    shape1.draw()
    shape1.print_message()
    shape2.draw()
    shape2.print_message()

if __name__ == "__main__":
    main()


apple.peel()
banana.peel()
orange.peel()

