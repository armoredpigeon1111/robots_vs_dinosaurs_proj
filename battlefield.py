#CLASS: Battlefield
#Author: Richard Fleming
#Create Date: August 10, 2021

from dinosaur import Dinosaur
from robot import Robot
from herd import Herd
from fleet import Fleet

class Battlefield():
    #Constructor
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    #Methods
    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle(self)

    def display_welcome(self):
        print("Welcome to Robots Vs. Dinosaurs!")

    def battle(self):
        Battlefield.dino_turn(self)
        Battlefield.robo_turn(self)
       


    def dino_turn(self):

        print(self.fleet.robots_list[0].name)
        print(self.herd.dino_list[0].name)
        
        print("dino turn")
        #self.herd.dino_list[0].attack(self, self.fleet.robots_list[0])
        
        
    
    def robo_turn(self):
        print("robo turn")

