class MarketEvent:
    def __init__(self, date, ohlcv_impact):
        self.ohlcv_impact = ohlcv_impact
    
class SignalEvent:
    def __init__(self, symbol, strength, direction):
        self.symbol = symbol
        self.strength = strength
        self.direction = direction


class OrderEvent:
    def __init__(self, symbol, quantity, order_type):
        self.symbol = symbol
        self.quantity = quantity
        self.order_type = order_type
    
    def __repr__(self):
        return f"OrderEvent(symbol={self.symbol}, quantity={self.quantity}, order_type={self.order_type})"
