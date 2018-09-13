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

class Controller:
    exit_person=0
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
                     for p in l.people:
                             td=p.targetLocation
                             if abs(curFloor-td)<abs(curFloor-d):
                                     d=td
                     if len(l.people)==0:
                             for f in b.floors:
                                     if len(f.waitingPeople)>0 and abs(curFloor-f.number)<d:
                                             d=f.number

                     if d!=999999999:
                         l.destination=d 
                     print("moving to ",d)
                     self.liftStatus[l]="MOVING"
             elif self.liftStatus[l]=="MOVING" and l.destination==curFloor:
                     print("arrived at ",curFloor)
                     self.liftStatus[l]="ARRIVED"       
                             

