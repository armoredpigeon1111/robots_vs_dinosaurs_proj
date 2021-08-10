#CLASS: Fleet
#Author: Richard Fleming
#Create Date: August 10, 2021

from robot import Robot

class Fleet:
    #Constructor
    def __init__(self):
        self.robots_list = []
        self.create_fleet()

    #methods
    def create_fleet(self):
        robobob = Robot("Robo Bob")
        robotom = Robot("Robo Tom")
        robocarl = Robot("Robo Carl")
        self.robots_list.append(robobob)
        self.robots_list.append(robotom)
        self.robots_list.append(robocarl)
        
