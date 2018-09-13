from building import Building

class Floor:
    def __init__(self,number,generators,vanishers,maxPeople=20):
        self.__number=number
        self.__waitingPeople=set()
        self.__generators=generators
        self.__vanishers=vanishers
        self.__maxPeople=maxPeople
        for g in self.__generators: g.floor=self
        for v in self.__vanishers: v.floor=self

    def addPerson(self,person):
        if person.targetLocation!=self.number:
                self.__waitingPeople.add(person)
                Building.createdPeople+=1
        else:
                Building.servedPeople+=1

    def tick(self,time):
        if len(self.__waitingPeople)<self.__maxPeople:
            for g in self.__generators:
                toAdd=g.tick(time)
                if toAdd!=None:
                    self.addPerson(toAdd)
        for v in self.__vanishers:
            self.__waitingPeople=self.__waitingPeople - v.tick(time,self.__waitingPeople)

    @property
    def number(self):
        return self.__number

    @property
    def waitingPeople(self):
        return self.__waitingPeople
