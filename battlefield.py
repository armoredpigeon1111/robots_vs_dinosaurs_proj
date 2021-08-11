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

        for robo in self.fleet.robots_list:
            index = int(input("Select a weapon for " + robo.name + ". Enter 1 for sword, 2 for laser, 3 for gun: ")) -1
            robo.weapon = robo.get_a_weapon(index)
        
        while len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0:

            firstAttack = input("Who do you want to attack first robots or dinos?").lower()
            
            if(firstAttack == "dinos"):
                Battlefield.dino_turn(self)
                if(len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0):
                    Battlefield.robo_turn(self)

            else:
                Battlefield.robo_turn(self)
                if(len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0):
                    Battlefield.dino_turn(self)


        if len(self.herd.dino_list) == 0:
            self.display_winners("Robots")
        elif len(self.fleet.robots_list) == 0:
            self.display_winners("Dinosaurs")

       


    def dino_turn(self):

        index = int(input("Select a weapon for " + self.herd.dino_list[0].name + ". Enter 1 for chomp, 2 for stomp, 3 for romp: ")) -1
        self.herd.dino_list[0].get_attack(index)

        self.herd.dino_list[0].attack(self.fleet.robots_list[0], index)
        print(self.herd.dino_list[0].name + " attacked " + self.fleet.robots_list[0].name + "!")
        print(self.fleet.robots_list[0].name + " has " + str(self.fleet.robots_list[0].health) + " health left.")
        if(self.fleet.robots_list[0].health <= 0):
            print(self.fleet.robots_list[0].name + " is dead.")
            self.fleet.robots_list.pop(0)


                
        
    
    def robo_turn(self):
        self.fleet.robots_list[0].attack(self.herd.dino_list[0])
        print(self.fleet.robots_list[0].name + " attacked " + self.herd.dino_list[0].name + "!")
        print(self.herd.dino_list[0].name + " has " + str(self.herd.dino_list[0].health) + " health left.")
        if(self.herd.dino_list[0].health <= 0):
            print(self.herd.dino_list[0].name + " is dead.")
            self.herd.dino_list.pop(0)


    def display_winners(self, winner):
        print(winner + " are the winners!")