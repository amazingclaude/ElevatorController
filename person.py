from lift import Lift


class Person:
    def __init__(self,currentLocation,goal,creationTime,hiddenGoal):
        self.__currentLocation=currentLocation
        self.__goal=goal
        self.__creationTime=creationTime
        self.__hiddenGoal=hiddenGoal

    def enterLift(self,lift):
        lift.enterLift(self)

    def exitLift(self):
        if type(self.__currentLocation)!=Lift:
            raise Exception("not in lift")
        self.location.exitLift(self)

    @property
    def location(self):
        return self.__currentLocation

    @location.setter
    def location(self,location):
        self.__currentLocation=location

    @property
    def targetLocation(self):
        if self.__hiddenGoal and not type(self.__currentLocation)==Lift:
            return -1
        return self.__goal

    @property
    def creationTime(self):
        return self.__creationTime