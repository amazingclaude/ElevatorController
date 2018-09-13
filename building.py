


class Building:
    createdPeople=0
    servedPeople=0

    def __init__(self,floors,lifts,controller,time=0):
        self.__floors=floors
        self.__lifts=lifts
        for l in lifts:
            l.building=self
        self.__controller=controller
        self.__controller.building(self)
        self.__time=time

    def tick(self):
        for f in self.__floors:
            f.tick(self.__time)
        for l in self.__lifts:
            l.tick()
        self.__controller.tick(self.__time)
        self.__time+=1
        #print(self.__time,Building.createdPeople,Building.servedPeople)

    @property
    def floors(self):
        return self.__floors

    @property
    def lifts(self):
        return self.__lifts

    @property
    def time(self):
        return self.__time

