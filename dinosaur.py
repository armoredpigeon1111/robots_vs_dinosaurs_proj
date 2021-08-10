#CLASS: Dinosaur
#Author: Richard Fleming
#Create Date: August 10, 2021

from robot import Robot

class Dinosaur:
    #Constructor
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    #Methods
    def attack(self, robot):
        robot.health -= self.attack_power
        print("dino attacked")