
from controller import Controller
import logging
from vanisher import Vanisher
from betaGenerator import BetaGenerator
from betaFloorSelector import BetaFloorSelector
from floor import Floor
from lift import Lift
from building import Building

from mycontroller import MyController
##################### VERSION 1.1, 20/11/2017 ###########################

"""---------------------------------------------------------------------------------------------"""
HG=False #Don't hide goals from the controller


########## START FLOOR DEFINITIONS ####################
morningGroundFloorSelector=BetaFloorSelector(1,10) 
morningGFGenerator=BetaGenerator(HG,7*3600,9*3600,morningGroundFloorSelector,5,5)
lunchGFGenerator=BetaGenerator(HG,12.5*3600,14*3600,morningGroundFloorSelector,5,5)

dayOtherFloorSelector=BetaFloorSelector(0,10)
dayOtherFloorGenerator=BetaGenerator(HG,8*3600,17*3600,dayOtherFloorSelector,2,2)

vanisher=Vanisher()

floors=[]
groundFloor=Floor(0,[morningGFGenerator,lunchGFGenerator,dayOtherFloorGenerator],[vanisher])

floors.append(groundFloor)
for i in range(1,11):
    vanisher=Vanisher()
    dayOtherFloorSelector=BetaFloorSelector(0,10)
    dayOtherFloorGenerator=BetaGenerator(HG,8*3600,17*3600,dayOtherFloorSelector,2,2)
    lunchOtherFloorSelector=BetaFloorSelector(0,0)
    lunchOtherFloorGenerator=BetaGenerator(HG,12*3600,13.5*3600,lunchOtherFloorSelector)
    eveningOtherFloorSelector=BetaFloorSelector(0,0)
    eveningOtherFloorGenerator=BetaGenerator(HG,16.5*3600,18*3600,eveningOtherFloorSelector)

    #f=Floor(i,[dayOtherFloorGenerator,lunchOtherFloorGenerator,eveningOtherFloorGenerator],[vanisher])
    #Test floor
    testSelector=BetaFloorSelector(0,10)
    testGenerator=BetaGenerator(HG,0,3000,testSelector,2,2)

    f=Floor(i,[testGenerator],[vanisher])
    floors.append(f)

########## END FLOOR DEFINITIONS ####################
########## START LIFT DEFINITIONS ####################
l1=Lift(0,10,0,10,False,None) #this lift goes across all floors
l2=Lift(0,10,0,10,False,None) #this lift goes across all floors
l3=Lift(0,10,0,10,False,None) #this lift goes across all floors
#l2=Lift(0,20,0,5,False,None)  #services the first 6 floors, more capacity
#l3=Lift(0,5,3,10,False,None)  #services floor 4 - 10, less capacity
########## END LIFT DEFINITIONS ####################

########## REPLACE WITH OWN CONTROLLER####################
#controller=MyController()
controller=Controller()
########## BUILDING DEFINITION ####################
startTime=0#int(7.5*3600)
#building=Building(floors,[l1,l2,l3],controller,startTime)
building=Building(floors,[l1],controller,startTime)


########## RUN OVER A SINGLE 24 HOUR PERIOD####################
for i in range(startTime,3000):
#    logging.debug("TOTAL PEOPLE: %d",TOTPEOPLE)
#    logging.debug("SERVED PEOPLE: %d",PEOPLESERVED)
    building.tick()

