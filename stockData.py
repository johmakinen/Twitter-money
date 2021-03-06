#{
#   stockData.py
# 
#   Execution will read all .csv files from 'StocksnShit folder and create one .csv file
#   with stock information. The output format will be : Month, Day, Year, 'name of stock 0',    'name of stock 1', ...
#                                                        ... , ...,  ..., 'closing value 0',    'closing value 0', ...
# }                                                                             ...                     ...
import pandas as pd
import numpy as np
import os

# Function declarations

def verifyFolder(folder):
    fileNames = os.listdir(folder)
    nofFiles = len(fileNames)
    nofRows = np.zeros(nofFiles)

    for index in range(nofFiles):
        contents = pd.read_csv(folder + fileNames[index])
        contents_date = contents['Date']
        nofRows[index] = len(contents_date)
        print(fileNames[index])

    temp = nofRows[0]

    for lenIndex in range(nofFiles):
        currentLength = nofRows[lenIndex]
        if(temp != currentLength):
            print("ERROR, length was : " + str(currentLength) + ", temp was : " + str(temp))
            print("Filename was : " + fileNames[lenIndex])
            return -1
        else:
            print("OK")
    return 1


def appendData(nameOfDataFile, appendTo):
    
    input = pd.read_csv(nameOfDataFile)
    oldData = pd.read_csv(appendTo)
    #Find the index where the filename starts
    csvIndex = 0
    for charIndex in range(len(nameOfDataFile)):
        char = nameOfDataFile[charIndex]
        if(char == '/'):
            lastSlashIndex = charIndex
        if(char == '.' and charIndex > csvIndex):
            csvIndex = charIndex

    sliceObj = slice(lastSlashIndex + 1, csvIndex)

    stockName = nameOfDataFile[sliceObj]
    newClosingValues = pd.DataFrame(data = input['Close'])
    newClosingValues.columns = [stockName]
    
    allClosingValues = pd.DataFrame(data = oldData) 

    if stockName in allClosingValues:
        allClosingValues[stockName] = newClosingValues[stockName]
    else:
        allClosingValues = allClosingValues.join(newClosingValues)
    
    allClosingValues.to_csv(appendTo, header = True, mode = 'w', index = False)

    return

def parseDate(dateString):
    yearSlice = slice(0, 4)
    monthSlice = slice(5, 7)
    daySlice = slice(8, 10)

    year = int(dateString[yearSlice])

    monthString = dateString[monthSlice]
    if(monthString[0] == '0'):
        monthString = monthString[1]
    month = int(monthString)

    dayString = dateString[daySlice]
    if(dayString[0] == '0'):
        dayString = dayString[1]
    day = int(dayString)

    return (month, day, year)


def setDates(nameOfDataFile, appendTo):
    
    input = pd.read_csv(nameOfDataFile)

    dates = pd.DataFrame(data = input['Date'])

    newDates = np.zeros((len(dates['Date']), 3))

    for dateIndex in range(len(dates['Date'])):
        currDate = dates['Date'][dateIndex]
        month, day, year = parseDate(currDate)
        newDates[dateIndex][0] = month
        newDates[dateIndex][1] = day
        newDates[dateIndex][2] = year
    
    newDatesDataFrame = pd.DataFrame(data = newDates, columns = ['Month', 'Day', 'Year'])
    
    newDatesDataFrame.to_csv(appendTo, header = True, mode = 'w', index = False)

    return


def createData():
    outputFile = 'stockData_clean.csv'
    folder = './StocksnShit/'
    #testFile = 'AAL.csv'

    if(verifyFolder(folder) == -1):
        print("Error in verifying folder.")
        exit
    else:
        print("Folder row lengths ok")


    fileNames = os.listdir(folder)
    nofFiles = len(fileNames)

    setDates(folder + fileNames[0], outputFile)

    for fileIndex in range(nofFiles):
        currentFile = fileNames[fileIndex]
        fullPath = folder + currentFile
        appendData(fullPath, outputFile)
    
    return



#{
#   Script begins here
# }

createData()
