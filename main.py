#MAIN: Controller/Initiator of Application
#Author: Richard Fleming
#Create Date: August 10, 2021

from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield

#======Instation of Objects=======

#Weapons
sword = Weapon("Sword", 10)
laser = Weapon("Laser", 20)
grenade = Weapon("Grenade", 30)

#Robots
robobob = Robot("Robo Bob")
robotom = Robot("Robo Tom")
robocarl = Robot("Robo Carl")

#Dinosaurs
trex = Dinosaur("T-Rex", 20)
stegosaurus = Dinosaur("Stegosaurus", 20)
triceratops = Dinosaur("Triceratops", 20)

#Fleet
fleet = Fleet()
fleet.create_fleet(robobob)
fleet.create_fleet(robotom)
fleet.create_fleet(robocarl)

#Herd
herd = Herd()
herd.create_herd(trex)
herd.create_herd(stegosaurus)
herd.create_herd(triceratops)

