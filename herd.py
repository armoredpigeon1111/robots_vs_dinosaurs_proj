#CLASS: Herd
#Author: Richard Fleming
#Create Date: August 10, 2021

from dinosaur import Dinosaur

class Herd:
    #Constructor
    def __init__(self):
        self.dino_list = []
        self.create_herd()

    #methods
    def create_herd(self):
        trex = Dinosaur("T-Rex", 30)
        stegosaurus = Dinosaur("Stegosaurus", 20)
        triceratops = Dinosaur("Triceratops", 20)
        self.dino_list.append(trex)
        self.dino_list.append(stegosaurus)
        self.dino_list.append(triceratops)