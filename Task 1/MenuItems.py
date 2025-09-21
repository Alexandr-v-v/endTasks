
from abc import ABC, abstractmethod
from enum import Enum
from Staff import Chef, Bartender
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
