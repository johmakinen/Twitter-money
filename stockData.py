#{
#   stockData.py
# 
#   Execution will read all .csv files from 'StocksnShit folder and create one .csv file
#   with stock information. The output format will be : 'name of stock 0'     'name of stock 1' ...
#                                                       'closing value 0'     'closing value 0' ...
# }                                                         ...                     ...
import pandas as pd


def appendData(nameOfDataFile, appendTo):
    
    input = pd.read_csv(nameOfDataFile)


    #writeTo = pd.to_csv(appendTo, mode='a', header=False)


    return

outputFile = 'stockData_clean.csv'
folder = './StocksnShit'
testFile = 'LMT.csv'

fullPath = folder + "/" + testFile

appendData(fullPath, outputFile)