import random
from scipy.stats import beta
from person import Person

"""beta generator for picking people"""
class BetaGenerator:
    def __init__(self,hiddenGoal,startTime,endTime,floorSelector,a=1,b=1):
        self.__hiddenGoal=hiddenGoal
        self.__startTime=startTime
        self.__endTime=endTime
        self.__floorSelector=floorSelector
        self.__a=a
        self.__b=b

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self,floor):
        self.__floor=floor

    def tick(self,time):
        bt=beta(self.__a,self.__b)
        #if random.random()*3600*24<(numpy.random.beta(self.__a,self.__b)*(time-self.__startTime)+self.__startTime):
        p=bt.pdf((time-self.__startTime)/(self.__endTime-self.__startTime))
        if random.random()<p:
            targetFloor=self.__floorSelector.pickFloor()
            return Person(self.__floor,targetFloor,time,self.__hiddenGoal)
