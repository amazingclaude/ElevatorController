from enum import Enum

class Lift:
    """This class represents the lift."""
    __FLOORTICKS=10 #number of ticks to wait between floors
    __DOORTICKS=5

    class Action(Enum):
        NONE = 0
        MOVE = 1
        DOOR = 2


    def __init__(self,location,capacity,minFloor,maxFloor,doorOpen,building):
        self.__location=location
        self.__capacity=capacity
        self.__minFloor=minFloor
        self.__maxFloor=maxFloor
        self.__building=building
        self.__doorOpen=doorOpen
        self.__destination=location

        self.__load=set() #people on the lift
        self.__waitingtime=0 #waiting time stores how many ticks will happen until something occurs
        self.__instruction=self.Action.NONE

    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self,b):
        self.__building=b

    @property
    def people(self):
        return self.__load

    @property
    def location(self):
        if self.__waitingtime==0:
            return self.__location
        return -1

    @property
    def capacity(self):
        return self.__capacity

    @property
    def minFloor(self):
        return self.__minFloor

    @property
    def maxFloor(self):
        return self.__maxFloor

    @property
    def doorOpen(self):
        if self.__waitingtime>0 and self.__instruction==self.Action.DOOR:
            return False
        return self.__doorOpen

    @property
    def doorClosed(self):
        if self.__waitingtime>0 and self.__instruction==self.Action.DOOR:
            return False
        return not self.__doorOpen


    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self,floor):
        if self.__minFloor>floor or self.__maxFloor<floor:
            raise ValueError("floor outside legal range",floor)
        if self.__doorOpen:
            raise Exception("door still open")
        self.__destination=floor
        self.__instruction=self.Action.MOVE
        if self.__waitingtime<=0: #TODO: handle case where we are between floors better
            self.__waitingtime=0+self.__FLOORTICKS

    def openDoor(self):
        if not self.__location==self.__destination:
            raise Exception("lift is moving")
        if not self.__doorOpen:
            self.__instruction=self.Action.DOOR
            if self.__waitingtime==0:
                self.__waitingtime=0+self.__DOORTICKS
        else:
            self.__instruction=self.NONE

    def closeDoor(self):
        if self.__location!=self.__destination:
            raise Exception("lift is moving")
        if self.__doorOpen:
            self.__instruction = self.Action.DOOR
            if self.__waitingtime==0:
                self.__waitingtime = 0+self.__DOORTICKS
        else:
            self.__instruction=self.NONE

    def tick(self):
        if self.__waitingtime>0:
            self.__waitingtime-=1
        if self.__instruction==self.Action.NONE or self.__waitingtime>0:
            return

        if self.__instruction==self.Action.DOOR and self.__location==self.destination:
            self.__doorOpen=not self.__doorOpen
            self.instruction=self.Action.NONE
        elif self.__instruction==self.Action.MOVE:
            if self.__location==self.__destination:
                self.instruction=self.Action.NONE
                self.__waittime=0
            else:
                self.__location+=int((self.__destination-self.__location)/abs(self.__destination-self.__location))
                self.__waitingtime=0+self.__FLOORTICKS

#TODO: check that the person is on the right floor to be added
    def enterLift(self,person):
        if self.__waitingtime>0:
            return
        if not self.__doorOpen:
            raise Exception("door is not open")
        if len(self.__load)>=self.__capacity:
            raise Exception("lift full")
        if person.location!=self.__building.floors[self.__location]:
            raise Exception("Trying to load a person from a different floor:",person.location,self.__building.floors[self.__location],self.__location,self.__building.floors[self.__location].number)
        self.__load.add(person)
        person.location.waitingPeople.remove(person)
        person.location=self

    def exitLift(self,person):
        if self.__waitingtime>0:
            return
        if not self.__doorOpen:
            raise Exception("door is not open")
        self.__load.remove(person)
        person.location = self.__building.floors[self.__location]
        person.location.addPerson(person)
