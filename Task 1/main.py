# TBD -- To Be Done
# it means it need to be implemented in some time in future :)


from abc import ABC, abstractmethod
from enum import Enum
from Staff import *
from Stations import *
from MenuItems import *

class OrderStatus(Enum):
    NEW = "New" # waiter create list of menu items, and transmit it to Chef and Bartender
    PREPARING = "Preparing" # Chef and Bartender check that all ingredients are present and prepare item
    READY = "Ready" # Waiter took dishes and baverages 
    SERVED = "Served" # dishes and baverages  are deliveder
    CLOSED = "Closed" # paied

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
        print(f">>>>> Ored status: {self.status}")
        print()
    
     
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
            print(f">>>>> Ored status: {self.status}")
            print()
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

            print("The order is ready")

            self.status = OrderStatus.READY
            print(f">>>>> Ored status: {self.status}")
            print()
        else:
            raise Exception("The order isn't in status PREPARING!") 
     
    def serveOrder(self):
        if self.status == OrderStatus.READY:
            self.calcTotalPrice()
            self.CreateBill()
            self.waiter.deliverOrder(self)
            self.status = OrderStatus.SERVED
            print(f">>>>> Ored status: {self.status}")
            print()
        else:
            raise Exception("The order isn't in status READY!")   
     
    def payOrder(self):
        if self.status == OrderStatus.SERVED:
            self.waiter.receivePayment(self)
            self.status = OrderStatus.CLOSED
            print(f">>>>> Ored status: {self.status}")
            print()
        else:
            raise Exception("The order isn't in status SERVED!")

if __name__ == "__main__":
    # init a restourant
    print("Initialization")
    kitchenStaff = [Chef("Jhone", "Doe"), Chef("Tom", "Doe")]
    # barStaff = [Chef("Ana", "Boe"), Chef("Bob", "Boe")]   ----------  test: should raise an exception 
    barStaff = [Bartender("Ana", "Boe"), Bartender("Bob", "Boe")]
    restaurant = Restaurant(kitchenStaff, barStaff)
    waiter1 = Waiter("Robert", "Polson")
    
    print("Initialization finished")

    print()
    print("Creating new order")
    order1 = Order(waiter1, restaurant)
    order1.createAnOrder()
    order1.prepareOrder()
    order1.serveOrder()
    order1.payOrder()


