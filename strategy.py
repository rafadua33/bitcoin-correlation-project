class WindowList:
    def __init__(self, window_size=200):
        self.window_size = window_size
        self.data = []
    
    def add(self, value):
        self.data.append(value)
        if len(self.data) > self.window_size:
            self.data.pop(0)

class CrossMovingStrat:

    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
        self.data = WindowList(window_size=long_window)
    def short_moving_average(self):
        sum = 0
        for i in range(self.short_window):
            sum += self.data[-i]
        return sum / self.short_window
    def long_moving_average(self):
        sum = 0
        for i in range(self.long_window):
            sum += self.data[-i]
        return sum / self.long_window
    def generate_signals(self):
        if self.short_moving_average() > self.long_moving_average():
            return "BUY"
        else:
            return "HOLD"
        
class BollingerBandsStrat:

    def __init__(self, window_size=20, num_std_dev=2):
        self.window_size = window_size
        self.num_std_dev = num_std_dev
        self.data = WindowList(window_size=window_size)
    
    def moving_average(self):
        sum = 0
        for i in range(self.window_size):
            sum += self.data[-i]
        return sum / self.window_size
    
    def standard_deviation(self):
        mean = self.moving_average()
        sum_squared_diff = 0
        for i in range(self.window_size):
            sum_squared_diff += (self.data[-i] - mean) ** 2
        variance = sum_squared_diff / self.window_size
        return variance ** 0.5
    
    def upper_band(self):
        return self.moving_average() + (self.num_std_dev * self.standard_deviation())
    
    def lower_band(self):
        return self.moving_average() - (self.num_std_dev * self.standard_deviation())
    
    def generate_signals(self):
        if self.data[-1] > self.upper_band():
            return "SELL"
        elif self.data[-1] < self.lower_band():
            return "BUY"
        else:
            return "HOLD"
   
