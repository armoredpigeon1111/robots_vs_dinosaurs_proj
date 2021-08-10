#CLASS: Robot
#Author: Richard Fleming
#Create Date: August 10, 2021

from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 100)

    #Methods
    def attack(self, dinosaur):
        dinosaur.health -= 10