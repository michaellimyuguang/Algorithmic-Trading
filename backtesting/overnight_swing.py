import pandas as pd
import datetime as dt

'''order execution'''
class OrderExecution:
    def __init__(self):
        self.position = None

    def buy(self, price):
        self.position = True
        self.entry = price

    def sell(self, price):
        self.position = False
        self.exit = price

    def stop(self, price):
        self.position = False
        self.exit = price

# a = OrderExecution()
# a.buy(50)
# print(a.position)
# print(a.entry)
# a.sell(55)
# print(a.position)
# print(a.exit)
# p_l = ((a.exit - a.entry) / a.entry) * 100
# print(p_l)

'''signal'''
class Signal:
    pass

'''data'''
#data shall inherit from signal and order execution
