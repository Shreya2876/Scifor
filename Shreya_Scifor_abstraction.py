from abc import ABC, abstractmethod

class Fruit(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def peel(self):
        pass
        
class Apple(Fruit):

    def peel(self):
        print(f"Peeling the skin of {self.name}.")


class Banana(Fruit):

    def peel(self):
        print(f"Peeling the skin of {self.name}.")

class Orange(Fruit):

    def peel(self):
        print(f"Peeling the skin of {self.name}.")

 
apple = Apple("Red Apple")
banana = Banana("Yellow Banana")
orange = Orange("Orange")

apple.peel()
banana.peel()
orange.peel()

