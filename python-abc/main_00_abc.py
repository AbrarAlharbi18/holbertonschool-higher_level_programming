#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# This will raise an error as Animal is abstract
try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(f"Error: {e}")
