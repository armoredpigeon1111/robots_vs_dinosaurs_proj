#CLASS: Dinosaur
#Author: Richard Fleming
#Create Date: August 10, 2021



from attacks import Attacks


class Dinosaur:
    #Constructor
    def __init__(self, name): #, attack_power):
        self.name = name
        #self.attack_power = attack_power
        self.health = 100
        self.attack_types = []

    #Methods
    def attack(self, robot, index):
        robot.health -= self.attack_types[index].attack_power

    def add_attack(self):
        chomp = Attacks("Chomp", 30)
        stomp = Attacks("Stomp", 25)
        romp = Attacks("Romp", 15)
        self.attack_types.append(chomp)
        self.attack_types.append(stomp)
        self.attack_types.append(romp)

    def get_attack(self, index):
        print("You selected " + self.attack_types[index].name)
        return self.attack_types[index]
        