#CLASS: Fleet
#Author: Richard Fleming
#Create Date: August 10, 2021

from robot import Robot

class Fleet:
    #Constructor
    def __init__(self):
        self.robots_list = []

    #methods
    def create_fleet(self, robot):
        self.robots_list.append(robot)
