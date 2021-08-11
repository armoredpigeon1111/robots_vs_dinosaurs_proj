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
        while len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0:
            Battlefield.dino_turn(self)
            Battlefield.robo_turn(self)
       


    def dino_turn(self):

        for dino in self.herd.dino_list:
            if(dino.health == 0):
                print(dino.name + "is dead.")
                self.herd.dino_list.remove(dino)

            if(len(self.herd.dino_list) == 0):
                self.display_winners("Robots")
        
        
        robo = 0
        for dino in self.herd.dino_list:
            

            if (dino.health > 0):
                print("dino turn")

                dino.attack(self.fleet.robots_list[robo])

                print(self.fleet.robots_list[robo].name + " now has " + str(self.fleet.robots_list[robo].health) + " health.")

            while robo < len(self.fleet.robots_list):
                robo += 1
        
    
    def robo_turn(self):

        for robo in self.fleet.robots_list:
            if(robo.health == 0):
                print(robo.name + "is dead.")
                self.fleet.robots_list.remove(robo)

            if(len(self.fleet.robots_list) == 0):
                self.display_winners("Dinosaurs")
        
        
        dino = 0
        for robo in self.fleet.robots_list:
            

            if (robo.health > 0):
                print("robot turn")

                robo.attack(self.herd.dino_list[dino])

                print(self.herd.dino_list[dino].name + " now has " + str(self.herd.dino_list[dino].health) + " health.")

            while dino < len(self.herd.dino_list):
                dino += 1


    def display_winners(self, winner):
        print(winner + "are the winners!")