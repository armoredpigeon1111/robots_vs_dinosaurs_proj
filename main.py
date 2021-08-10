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



#Herd
herd = Herd()
herd.create_herd(trex)
herd.create_herd(stegosaurus)
herd.create_herd(triceratops)


battlefield = Battlefield()
battlefield.run_game()
