import csv

def getCSVData(filename):
    #create an empty list to store rows
    rows = []
    #open the csv file
    datafile = open(filename,'r')
    #create a CSV reader from CSV file
    reader = csv.reader(datafile)
    #skip the headers
    next(reader)
    #add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows