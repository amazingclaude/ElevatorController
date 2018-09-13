
class Vanisher:
    WAITINGTHRESHOLD=600

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self,floor):
        self.__floor=floor

    def tick(self,time,people):
        toRemove=set()
        for p in people:
            if time-p.creationTime>self.WAITINGTHRESHOLD:
                toRemove.add(p)
            if p.targetLocation==self.__floor:
                toRemove.append(p)
                global PEOPLESERVED
                PEOPLESERVED+=1
        return toRemove
