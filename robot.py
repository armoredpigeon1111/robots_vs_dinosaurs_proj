#CLASS: Robot
#Author: Richard Fleming
#Create Date: August 10, 2021

from weapon import Weapon



class Robot:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = []

    #Methods
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        
    def add_weapons(self):
        sword = Weapon("Sword", 30)
        laser = Weapon("Laser", 25)
        gun = Weapon("Gun", 15)
        self.weapon.append(sword)
        self.weapon.append(laser)
        self.weapon.append(gun)
    
    def get_a_weapon(self, index):
        print("You selected " + self.weapon[index].name)
        return self.weapon[int(index)]
