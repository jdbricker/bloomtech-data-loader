import pandas as pd
import os
import sys

class DataLoader():
    
    def __init__(self, web_path, data_file, local_path='./data'):
        
        self.web_path = web_path
        self.local_path = local_path
        self.data_file = data_file
        
        self.ext = os.path.splitext(data_file)[1]
        
        if self.ext == '.csv':
            self.reader = pd.read_csv
            self.writer = pd.DataFrame.to_csv
        elif self.ext == '.xlsx':
            self.reader = pd.read_excel
            self.writer = pd.DataFrame.to_excel
            
    def read_web_data(self):
        
        self.data = self.reader(os.path.join(self.web_path, self.data_file))
    
    def read_local_data(self):
        
        self.data = self.reader(os.path.join(self.web_path, self.data_file))
    
    def cache_local_data(self):
        
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)
        
        self.writer(self.data, os.path.join(self.local_path, self.data_file))
    
    def read_and_cache_data(self):
        
        if 'google.colab' in sys.modules:
            self.read_web_data()
        elif os.path.exists(os.path.join(self.local_path, self.data_file)):
            self.read_local_data()
        else:
            #not on colab, don't have data already stored
            self.read_web_data()
            self.cache_local_data()
        
        return self.data