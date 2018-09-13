import numpy

"""there is a beta distribution regarding the selected floor"""
class BetaFloorSelector:
    def __init__(self,minFloor,maxFloor,a=1,b=1):
        self.__minFloor=minFloor
        self.__maxFloor=maxFloor
        self.__a=a
        self.__b=b

    def pickFloor(self):
        if self.__maxFloor==self.__minFloor:
            return self.__maxFloor
        return int(round((numpy.random.beta(self.__a,self.__b)*(self.__maxFloor-self.__minFloor)+self.__minFloor),0))
