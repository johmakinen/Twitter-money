# {
#   With Twitter data and Stock data set up, build a dataset that matches Twitter data with corresponding stock value changes
#   during the next day. (Timeframe can be changed later.)
#
# }


import pandas as pd
import numpy as np
import os


allStockData = pd.read_csv('stockData_clean.csv')
allTweets = pd.read_csv('x_all.csv')





