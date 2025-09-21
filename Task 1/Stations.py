from abc import ABC, abstractmethod
from enum import Enum
from Staff import Staff, Bartender, Chef

# Station -------------------------------------------------------------------

class Ingredient():
    def __init__(self, name, count):
        self.name = name
        self.count = count

class Station(ABC):
    def __init__(self, staffList : list[Staff]):
        self.storageItems = []
        self.staffList = staffList
        # self.orders = []

    @abstractmethod
    def addStorageItems(self, items: list[Ingredient]):
        pass

    @abstractmethod
    def useStorageItems(self, items: list[Ingredient]):
        pass

    @abstractmethod
    def getStaffWaitingForOrders():
        pass

class Bar(Station):
    def __init__(self, staffList : list[Staff]):
        for employe in staffList:
            if isinstance(employe, Chef): raise Exception("No chefs in the Bar!!!")
        super().__init__(staffList)
        self.showCase = []
    
    def addStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation

    def useStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation
    
    def addShowcaseItem(self, items: list[Ingredient]):
        pass # TBD implementation

    def useShowcaseItem(self, items: list[Ingredient]):
        pass # TBD implementation

    def getStaffWaitingForOrders(self):
        return self.staffList[0]

class Kitchen(Station):
    def __init__(self, staffList : list[Staff]):
        for employe in staffList:
            if isinstance(employe, Bartender): raise Exception("No bartender in the Bar!!!")
        super().__init__(staffList)
    
    def addStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation

    def useStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation

    def getStaffWaitingForOrders(self):
        return self.staffList[0]

    