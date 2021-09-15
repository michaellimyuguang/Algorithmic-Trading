# from strategies.goldencross import GoldenCross
import backtrader as bt
from strategies.breakout_trade import BreakoutTrade
from backtrader.feeds import GenericCSVData

class MyCSV(GenericCSVData):
    pass
    # lines = ('vma60',
    #          'r1',
    #          'r2',
    #          'r3',
    #          )
    #
    # params = (('vma60', 13),
    #           ('r1', 14),
    #           ('r2', 15),
    #           ('r3', 16),
    #           )

path1 = r"C:\Users\yu guang\Desktop\AAPL.csv"

# Create a data feed
data = MyCSV(
    dataname=path1,
    dtformat=('%Y-%m-%d'),
    datetime=0,
    high=1,
    low=2,
    open=3,
    close=4,
    volume=5,
    openinterest=-1,
)

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add data feed to cerebro
cerebro.adddata(data)

# Add strategy to cerebro
# cerebro.addstrategy(GoldenCross)
cerebro.addstrategy(BreakoutTrade)

cerebro.broker.setcommission(commission=0.001)

# Set our desired cash start
cerebro.broker.setcash(10000.0)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot(style='candlestick', barup='green', bardown='red')