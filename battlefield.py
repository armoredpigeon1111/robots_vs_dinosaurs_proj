#CLASS: Battlefield
#Author: Richard Fleming
#Create Date: August 10, 2021

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
        self.select_robot_weapon()

        self.select_turn()

        self.check_winners()


    def select_turn(self):
        while len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0:
                Battlefield.dino_turn(self)
                if(len(self.herd.dino_list) > 0 and len(self.fleet.robots_list) > 0):
                    Battlefield.robo_turn(self)


    def check_winners(self):
        if len(self.herd.dino_list) == 0:
            self.display_winners("Robots")
        elif len(self.fleet.robots_list) == 0:
            self.display_winners("Dinosaurs")



#=======Dino turn section======
    def dino_turn(self):

        index = int(input("Select an attack for " + self.herd.dino_list[0].name + ". Enter 1 for chomp, 2 for stomp, 3 for romp: ")) -1
        self.herd.dino_list[0].get_attack(index)

        self.herd.dino_list[0].attack(self.fleet.robots_list[0], index)

        self.dino_turn_print()

        self.dino_turn_health()

        self.dino_turn_energy()

    def dino_turn_print(self):
        print(self.herd.dino_list[0].name + " attacked " + self.fleet.robots_list[0].name + "!")
        print(self.fleet.robots_list[0].name + " has " + str(self.fleet.robots_list[0].health) + " health left.")      
        
    
    def dino_turn_health(self):
        if(self.fleet.robots_list[0].health <= 0):
            print(self.fleet.robots_list[0].name + " is dead.")
            self.fleet.robots_list.pop(0)

    def dino_turn_energy(self):
        if(self.herd.dino_list[0].energy <= 0):
            print(self.herd.dino_list[0].name + " is out of energy.")
            self.herd.dino_list.pop(0)
        else:
            print(self.herd.dino_list[0].name + " has " + str(self.herd.dino_list[0].energy) + " energy left.")    
        



#======Robot turn section=======
    def select_robot_weapon(self):
        for robo in self.fleet.robots_list:
            index = int(input("Select a weapon for " + robo.name + ". Enter 1 for sword, 2 for laser, 3 for gun: ")) -1
            robo.weapon = robo.get_a_weapon(index)


    def robo_turn(self):
        self.fleet.robots_list[0].attack(self.herd.dino_list[0])
        
        self.print_robo_turn()
       
        self.robo_turn_health()

        self.robo_turn_energy()


    def print_robo_turn(self):
        print(self.fleet.robots_list[0].name + " attacked " + self.herd.dino_list[0].name + "!")
        print(self.herd.dino_list[0].name + " has " + str(self.herd.dino_list[0].health) + " health left.")

   
    def robo_turn_health(self):
        if(self.herd.dino_list[0].health <= 0):
            print(self.herd.dino_list[0].name + " is dead.")
            self.herd.dino_list.pop(0)

  
    def robo_turn_energy(self):
        if(self.fleet.robots_list[0].energy <= 0):
            print(self.fleet.robots_list[0].name + " is out of energy.")
            self.fleet.robots_list.pop(0)
        else:
            print(self.fleet.robots_list[0].name + " has " + str(self.fleet.robots_list[0].energy) + " energy left.")  
  
  #Display the winner
    def display_winners(self, winner):
        print(winner + " are the winners!")