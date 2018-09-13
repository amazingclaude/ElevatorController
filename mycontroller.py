"""
class Controller:
    def building(self,building):
        pass
    def tick(self,time):
        pass

"""
from person import Person
from building import Building
from floor import Floor
import random

class MyController:
    exit_person=0
    stored_d=0
    def building(self,b):
      self.b=b
      self.liftStatus={}
      for l in self.b.lifts:
              self.liftStatus[l]="ARRIVED"

#"""implement a simple loop: if a lift is at a floor (ARRIVED), open the door (DOOROPENING). Once the door is open, load and unload people and close the door (DOORCLOSING). Once door is closed, work out where to move to based first on people in the lift, and second on whether there are people waiting. Finally, start moving until at the destination."""
    def tick(self,time):

      b=self.b
      for l in b.lifts:
             curFloor=l.location
             f=self.b.floors[curFloor]
             if curFloor!=-1:
               print("current floor of lift ",l," is ",curFloor)

             if self.liftStatus[l]=="ARRIVED":
                     print("opening door")
                     l.openDoor()
                     self.liftStatus[l]="DOOROPENING"
             elif self.liftStatus[l]=="DOOROPENING" and l.doorOpen:
                     toExit=set()
                     for p in l.people:
                             if p.targetLocation==curFloor:
                                     toExit.add(p)
                     for p in toExit:
                             print("person exiting",p.targetLocation,curFloor)
                             self.exit_person+=1
                             p.exitLift()
                     print("lift has served",self.exit_person,"person")
                     while len(f.waitingPeople)>0 and len(l.people)<l.capacity:
                             for p in f.waitingPeople:
                                     print("person entering",p.targetLocation)
                                     p.enterLift(l)
                                     break
                     l.closeDoor()
                     self.liftStatus[l]="DOORCLOSING"
             elif self.liftStatus[l]=="DOORCLOSING" and l.doorClosed:
                     d=999999999
                     up=0
                     down=0
                     EU_up=0
                     EU_down=0
                     hall_call=[]
                     utility_up=set()
                     utility_down=set()
                     down_requirement=[]
                     up_requirement=[]
                     both_requirement=[]
                     #Identify the direction of the lift, whether going up or going down
                     #==============================================================================================
                     if l.location>self.stored_d:
                                 elevator_direction="up"
                     if l.location<self.stored_d:
                                 elevator_direction="down"
                     #====================================================================================================

                    # Scenario 1:When there are passengers inside the lift, their target will be considered firstly
                    #===============================================================================================
                     for p in l.people:
                             td=p.targetLocation
                             if (elevator_direction=="up")&(l.location<p.targetLocation): #when lift is movign upwards, consider people'starget who drives the lift to go up
                                 if abs(curFloor-td)<abs(curFloor-d):
                                     d=td
                             if (elevator_direction=="down")&(l.location>p.targetLocation): #when lift is movign downwards, consider people'starget who drives the lift to go down
                                 if abs(curFloor-td)<abs(curFloor-d):
                                     d=td
                             else:
                                 if abs(curFloor-td)<abs(curFloor-d):
                                     d=td
                    #=================================================================================================

                    #Scenerio 2: When there are no passengers inside the lift
                    #================================================================================================
                     if len(l.people)==0:
                             for f in b.floors:
                                     if len(f.waitingPeople)>0:
                                             direction_up=0
                                             direction_down=0

                                             for p in f.waitingPeople:
                                                 if curFloor>p.targetLocation: #passenter wants to go down
                                                     direction_down+=1
                                                 if curFloor<p.targetLocation: #passenger wants to go up
                                                     direction_up+=1
                                             if (direction_down>0)&(direction_up==0):#hall calling only for down direction
                                                 direction=1  #Mark the button-on for up-hall-call
                                             if (direction_down==0)&(direction_up>0):#hall calling only for up direction
                                                 direction=2 #Mark the button-on for down-hall-call
                                             else:
                                                 direction=3 #hall calling for both directions

                                             hall_call.append([f.number,direction])
                            #Utility Function Kernal
                            #######################################################################
                                             if f.number>l.location:
                                                 up+=1
                                                 utility_up.add(11-abs(f.number-l.location))
                                             if f.number<l.location:
                                                 down+=1
                                                 utility_down.add(11-abs(f.number-l.location))

                             for u in utility_up:
                                 EU_up=(1/up)*u
                             for u in utility_down:
                                 EU_down=(1/down)*u
                            #########################################################################
                             for calling_direction in hall_call:
                                    if calling_direction[1]==1:
                                        down_requirement.append(calling_direction)
                                    if calling_direction[1]==2:
                                        up_requirement.append(calling_direction)
                                    if calling_direction[1]==3:
                                        both_requirement.append(calling_direction)
                            #Using Expected Utility to identify the direction to go (for the lift)
                             if EU_up>EU_down: #elevator should go up
                                if(up_requirement):
                                    temp=[]
                                    for item in up_requirement:
                                        if item[0]>curFloor:
                                            temp.append(item)
                                    for item in both_requirement:
                                        if item[0]>curFloor:
                                            temp.append(item)

                                    max_calling=min(temp) #Choosing the nearst floor which has a up-hall-call
                                    d=max_calling[0]
                                else:
                                    max_calling=max(hall_call)
                                    d=max_calling[0]

                             if EU_up<EU_down: #elevator should go down
                                 if(down_requirement):
                                     temp=[]
                                     for item in down_requirement:
                                         if item[0]<curFloor:
                                             temp.append(item)
                                     for item in both_requirement:
                                        if item[0]>curFloor:
                                            temp.append(item)
                                     min_calling=max(temp) #Choosing the nearesr flor which has a down-hall-call
                                     d=min_calling[0]
                                 else:
                                    min_calling=min(hall_call)
                                    d=min(min_calling)
                             if not (hall_call):
                                 for f in b.floors:
                                     if len(f.waitingPeople)>0 and abs(curFloor-f.number)<d:
                                             d=f.number


                     self.stored_d=l.location #variable to help identify the direction of the elevator.



                     if d!=999999999:
                         l.destination=d
                     print("moving to ",d)
                     self.liftStatus[l]="MOVING"
             elif self.liftStatus[l]=="MOVING" and l.destination==curFloor:
                     print("arrived at ",curFloor)
                     self.liftStatus[l]="ARRIVED"

