from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.nam = name # self.nam --> self.name

    @abstractmethod
    def speak(self): pass
    
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        # should be used super().__init__(name)

    def speaks(self): return "woof" # speaks --> speak

def intro(a: Animal):
    print(a.name.upper(), "says", a.speak())

buddy = Dog("Buddy", "beagle")
intro(buddy)