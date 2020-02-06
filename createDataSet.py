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

tweetsWithStocks = allTweets.merge(allStockData)

differenceStocks = pd.DataFrame(columns=allStockData.columns)


for dayIndex in range(allStockData.shape[0] - 1):

    newRow = allStockData.values[dayIndex]

    # loop through the stocks and for day n set value of stock on day n + 1 - value on n
    for subIndex in range(3, allStockData.shape[1], 1):
        percentageValue = 100*((allStockData.values[dayIndex + 1][subIndex] - allStockData.values[dayIndex]
                                [subIndex])/allStockData.values[dayIndex][subIndex])
        newRow[subIndex] = round(percentageValue, 5)   # change in percentages
    differenceStocks.loc[differenceStocks.shape[0]] = newRow

differencesWithTweets = differenceStocks.merge(allTweets)

print(differencesWithTweets.head(10))

differencesWithTweets.to_csv(
    'dataSet_differences.csv', header=True, mode='w', index=False)
