#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
print(FlyingFish.mro())
