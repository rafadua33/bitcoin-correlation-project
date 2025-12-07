





class CrossMovingStrat:

    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
    def short_moving_average(self, data):
        for i in range(self.short_window):
            

        return 
    def long_moving_average(self, data):
        for i in range(self.long_window):

        return
    def generate_signals(self, data):
        if short_moving_average(data) > long_moving_average(data):
            return "BUY"
        else:
            return "HOLD"
        
