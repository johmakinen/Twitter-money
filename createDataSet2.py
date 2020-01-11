# {
#   With Twitter data and Stock data set up, build a dataset that matches Twitter data with corresponding stock value changes
#   during the next day. (Timeframe can be changed later.)
#
# }


import pandas as pd
import numpy as np
import os

# Gather all data
allStockData = pd.read_csv('stockData_clean.csv')
allTweets = pd.read_csv('x_all.csv')

headers = ['Month', 'Day', 'Year']

for i in range(allTweets.shape[1] - 3):
    headers.append(i)
allTweets = pd.read_csv('x_all.csv', names=headers)

print(allTweets.head(5))


# tweetsWithStocks = allTweets.merge(allStockData, left_on = )

# print(allTweets['Month'].head(5))

# print(tweetsWithStocks.head(5))
print(allTweets.shape)
print(allStockData.shape)
# print(tweetsWithStocks.shape)
