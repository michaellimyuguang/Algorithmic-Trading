from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt # Import the backtrader platform
import backtrader.feeds as btfeeds

class MyCSV(btfeeds.GenericCSVData):
    params = (
        ('nullvalue', 0.0),
        ('dtformat', ('%Y-%m-%d')),
        ('datetime', 0),
        ('high', 1),
        ('low', 2),
        ('open', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1)
    )

# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)

        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close # Keep a reference to the "close" line in the data[0] dataseries
        self.order = None # To keep track of pending orders

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None # Write down: no pending order


    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:
            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] < self.dataclose[-1]:
                    if self.dataclose[-1] < self.dataclose[-2]:
                        # BUY, BUY, BUY!!! (with default parameters)
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])
                        # Keep track of the created order to avoid a 2nd order
                        self.order = self.buy()
        else:
            # Already in the market ... we might sell
            if len(self) >= (self.bar_executed + 5):
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()

if __name__ == '__main__':
    cerebro = bt.Cerebro() # Create a cerebro entity
    cerebro.addstrategy(TestStrategy) # Add a strategy
    data = MyCSV(dataname=r'C:\Users\yu guang\Desktop\backtrader_tutorial\ticker_files\AAPL.csv') # Create a Data Feed
    cerebro.adddata(data) # Add the Data Feed to Cerebro
    cerebro.broker.setcash(100000.0) # Set our desired cash start
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run() #this is to loop over data
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())