from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals"""
    
    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented by subclasses to return the animal's sound"""
        pass

class Dog(Animal):
    """Dog subclass of Animal"""
    
    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """Cat subclass of Animal"""
    
    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
