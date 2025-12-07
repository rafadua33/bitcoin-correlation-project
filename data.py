import pandas as pd

class CSVDataLoader:
    """ Loads historical bar data from a CSV file. """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath, parse_dates=['timestamp'])
        self.data.set_index('timestamp', inplace=True)
        self.current_index = 0

    def get_close(self):
        return self.data['close']
    
    def get_next_bar(self):
        for index, row in self.data.iterrows():
            yield row

    def get_next_bar_dict(self):
        for index, row in self.data.iterrows():
            yield row.to_dict()
    
    

    