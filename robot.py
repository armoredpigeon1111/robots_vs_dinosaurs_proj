#CLASS: Robot
#Author: Richard Fleming
#Create Date: August 10, 2021

class Robot:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = "" # Todo find out how to use weapon class

    #Methods
    def attack(self, dinosaur):
        