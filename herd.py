#CLASS: Herd
#Author: Richard Fleming
#Create Date: August 10, 2021

from dinosaur import Dinosaur

class Herd:
    #Constructor
    def __init__(self):
        self.dino_list = []

    #methods
    def create_herd(self, dinosaur):
        self.dino_list.append(dinosaur)