from abc import ABC, abstractmethod
from enum import Enum

# Staff -------------------------------------------------------------------

class Role(Enum):
    Waiter = "Waiter"
    Chef = "Chef"
    Bartender = "Bartender"

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
        print("Waiter: listening what customers want")

     
    def getOrderItems(self):
        print("Waiter: write all in order")
        return self.orderItems
    
     
    def deliverOrder(self, order):
        print("Waiter: serve the order")

     
    def receivePayment(self, order):
        print("Waiter: get payment")

class Chef(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Chef)
    
     
    def prepareOerder(self, orderItems):
        print("Chef: I'm cooking dishes now")

class Bartender(Staff):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName, role = Role.Bartender)
    
     
    def prepareOerder(self, orderItems):
        print("Bartender: I'm mixing cocktails now")
