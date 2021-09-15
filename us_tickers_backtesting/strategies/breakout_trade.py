import backtrader as bt

class BreakoutTrade(bt.Strategy):
    #long using built in indicators
    # def __init__(self):
    #     self.bt_sma = bt.indicators.MovingAverageSimple(self.data, period=20)
    # def next(self):
    #     if not self.position and self.data.close[0] > self.bt_sma[0] and self.data.close[-1] < self.bt_sma[-1]:
    #         self.order = self.buy(size=100)
    #         print('bought on', self.data.datetime.date())
    #     if self.data.close[0] < self.bt_sma[0] and self.data.close[-1] > self.bt_sma[-1]:
    #         self.order = self.close()

    #long using own written indicators
    # def next(self):
    #     ma_value = sum([self.data.close[-cnt] for cnt in range(20)]) / 20
    #     pre_ma_value = sum([self.data.close[-cnt-1] for cnt in range(20)]) / 20
    #     if self.data.close[0] > ma_value and self.data.close[-1] < pre_ma_value:
    #         self.order = self.buy(size=100)
    #         print('long', self.data.datetime.date())
    #     if self.data.close[0] < ma_value and self.data.close[-1] > pre_ma_value:
    #         self.order = self.sell(size=100)
    #
    #     print(self.data.datetime.date())
    #     print(self.data.close[0])

    #cross over buy or close
    # def __init__(self):
    #     self.buysignal = bt.indicators.CrossOver(self.data.close, self.data.r1)
    #
    # def next(self):
    #     if not self.position and self.buysignal[0] == 1:
    #         self.order = self.buy(size=100)
    #     if self.position and self.buysignal[0] == -1:
    #         self.order = self.close()

    #get the closing price from past 3 days
    # def next(self):
    #     price = self.data.close.get(ago=-1, size=3)
    #     print(price)



