#CLASS: Battlefield
#Author: Richard Fleming
#Create Date: August 10, 2021

from herd import Herd
from fleet import Fleet

class Battlefield():
    #Constructor
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd()


    #Methods
    def run_game(self):
        Battlefield.display_welcome()
        Battlefield.battle()

    def display_welcome(self):
        print("Welcome to Robots Vs. Dinosaurs!")

    def battle(self):
        pass


    def dino_turn(self):
        pass
    
    def robo_turn(self):
        pass

