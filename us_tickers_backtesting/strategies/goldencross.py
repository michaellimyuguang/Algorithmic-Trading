import math as m
import backtrader as bt

class GoldenCross(bt.Strategy):
    params = (('fast', 20), ('slow', 40), ('order_percentage', 0.95), ('ticker', 'ORGO'))

    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(self.data.close, period=self.params.fast, plotname='50 day moving average')
        self.slow_moving_average = bt.indicators.SMA(self.data.close, period=self.params.slow, plotname='200 day moving average')
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                # amount_to_invest = (self.params.order_percentage * self.broker.cash)
                # self.size = m.floor(amount_to_invest / self.data.close)
                self.size = m.floor(3000/self.data.close)
                print("{} Buy {} shares of {} at {}".format(self.datas[0].datetime.date(0), self.size, self.params.ticker, self.datas[0].close))
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                print("{} Sell {} shares of {} at {}".format(self.datas[0].datetime.date(0), self.size, self.params.ticker, self.datas[0].close))
                self.close()