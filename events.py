class MarketEvent:
    def __init__(self, name, date, ohlcv_impact):
        self.name = name
        self.date = date
        self.ohlcv_impact = ohlcv_impact

    def __repr__(self):
        return f"MarketEvent(name={self.name}, date={self.date}, ohlcv_impact={self.ohlcv_impact})"
    
class SignalEvent:
    def __init__(self, symbol, strength, direction):
        self.symbol = symbol
        self.strength = strength
        self.direction = direction


class OrderEvent:

