# TBD -- To Be Done
# it means it need to be implemented in some time in future :)


from abc import ABC, abstractmethod
from enum import Enum

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
    
class Waiter(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Waiter)
        self.orderItems = []

     
    def takeOrder(self):
        pass # TBD fill self.orderItems

     
    def getOrderItems(self):
        return self.orderItems
    
     
    def deliverOrder(self, order):
        pass # TBD

     
    def receivePayment(self, order):
        pass # TBD

class Chef(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Chef)
    
     
    def prepareOerder(self, orderItems):
        pass # TBD

class Bartender(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Bartender)
    
     
    def prepareOerder(self, orderItems):
        pass # TBD


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

# other -------------------------------------

class Restaurant():
    def __init__(self, kitchenStaff: list[Chef], barStaff: list[Bartender]):
        self.kitchen = Kitchen(kitchenStaff)
        self.bar = Bar(barStaff)

class Order:
    def __init__(self, waiter: Waiter, restaurant: Restaurant):
        self.status = OrderStatus.NEW
        self.orderItems = list()
        self.totalPrice = 0
        self.waiter = waiter
        self.restaurant = restaurant
    
     
    def addOrderItems(self, orderItems: list[OrderItem]):
        self.orderItems.extend(orderItems)

     
    def calcTotalPrice(self):
        self.totalPrice = sum(item.price * item.amount for item in self.orderItems)

     
    def CreateBill(self):
        pass # TBD

    # state handlers -------------------------------------------------------------------
     
    def createAnOrder(self):
        if self.status == OrderStatus.NEW:
            self.waiter.takeOrder()
            self.addOrderItems(self.waiter.getOrderItems())
            self.status = OrderStatus.PREPARING
        else:
            raise Exception("The order isn't in status NEW!")
        
     
    def prepareOrder(self):
        if self.status == OrderStatus.PREPARING:
            # split order between bar and kitchen 
            orderItemsForKitchen = [item for item in self.orderItems if isinstance(item, Dish)]
            orderItemsForBar     = [item for item in self.orderItems if isinstance(item, Beverage)]
            chef = self.restaurant.kitchen.getStaffWaitingForOrders()
            chef.prepareOerder(orderItemsForKitchen) 
            bartender = self.restaurant.bar.getStaffWaitingForOrders()
            bartender.prepareOerder(orderItemsForBar)

            self.status = OrderStatus.READY
        else:
            raise Exception("The order isn't in status PREPARING!")
        
     
    def serveOrder(self):
        if self.status == OrderStatus.READY:
            self.calcTotalPrice()
            self.CreateBill()
            self.waiter.deliverOrder(self)
            self.status = OrderStatus.SERVED
        else:
            raise Exception("The order isn't in status READY!")
        
     
    def payOrder(self):
        if self.status == OrderStatus.SERVED:
            self.waiter.receivePayment(self)
            self.status = OrderStatus.CLOSED
        else:
            raise Exception("The order isn't in status SERVED!")


if __name__ == "__main__":
    # init a restourant
    kitchenStaff = [Chef("Jhone", "Doe"), Chef("Tom", "Doe")]
    # barStaff = [Chef("Ana", "Boe"), Chef("Bob", "Boe")]   ----------  test: should raise an exception 
    barStaff = [Bartender("Ana", "Boe"), Bartender("Bob", "Boe")]
    restaurant = Restaurant(kitchenStaff, barStaff)

    waiter1 = Waiter("Robert", "Polson")
    order1 = Order(waiter1, restaurant)

    order1.createAnOrder()
    order1.prepareOrder()
    order1.serveOrder()
    order1.payOrder()


