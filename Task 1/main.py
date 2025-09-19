from abc import ABC, abstractmethod
from enum import Enum

# class Station(Enum):
#     Kitchen = "Kitchen"
#     Bar = "Bar"  

class Role(Enum):
    Waiter = "Waiter"
    Chef = "Chef"
    Bartender = "Bartender"

class OrderStatus(Enum):
    NEW = "New" # waiter create list of menu items, and transmit it to Chef and Bartender
    PREPARING = "Preparing" # Chef and Bartender check that all ingredients are present and prepare item
    READY = "Ready" # Waiter took dishes and baverages 
    SERVED = "Served" # dishes and baverages  are deliveder
    CLOSED = "Closed" # paied

class Ingredient():
    def __init__(self, name, count):
        self.name = name
        self.count = count

# Staff -------------------------------------------------------------------

class Staff(ABC):
    def __init__(self, firstName, lastName, role: Role):
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
    
    def takeOrder(order):


class Waiter(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Waiter)

    @classmethod
    def takeOrder():
        pass

class Chef(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Chef)

class Bartender(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Bartender)


# Station -------------------------------------------------------------------

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

    # @abstractmethod
    # def getStaffWaitingForOrders():
    #     pass

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

    # def getStaffWaitingForOrders(self):
    #     pass # TBD implementation

class Kitchen(Station):
    def __init__(self, staffList : list[Staff]):
        for employe in staffList:
            if isinstance(employe, Bartender): raise Exception("No bartender in the Bar!!!")
        super().__init__(staffList)
    
    def addStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation

    def useStorageItems(self, items: list[Ingredient]):
        pass # TBD implementation

    # def getStaffWaitingForOrders(self):
    #     pass # TBD implementation

    
# Menu items --------------------------------------------------------------

class MenuItem(ABC):
    def __init__(self, name, price, ingredients):
        self.price = price
        self.name = name
        self.ingredients = ingredients

class OrderItem(MenuItem): # it is better to use MenuItem as parameter for constructor then inheret it, but let it be so
    def __init__(self, name, price, ingredients, amount, notes):
        super().__init__(name, price, ingredients)
        self.amount = amount
        self.notes = notes

class Dish(OrderItem):
    def __init__(self, name, price, ingredients, amount, notes, prepared_by: Chef):
        super().__init__(name, price, ingredients, amount, notes, prepared_by)
        self.prepared_by = prepared_by

class Beverage(OrderItem):
    def __init__(self, name, price, ingredients, amount, notes, prepared_by: Bartender):
        super().__init__(name, price, ingredients, amount, notes, prepared_by)
        self.prepared_by = prepared_by

class Order:
    def __init__(self, orderItems: list[OrderItem]):
        self.status = OrderStatus.NEW
        self.orderItems = orderItems
        self.totalPrice = sum(item.price * item.amount for item in self.orderItems)

# class OrderStateMachine():

if __name__ == "__main__":
    # init a restourant
    tables = set([item for item in range(10)])


    cher1= Chef("Jhone", "Doe")
    print(type(cher1))

