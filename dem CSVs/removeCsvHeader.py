#! python3

# removeCsvHeader - remove headers from every csv file in the current directory
# p. 384-387

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# L oop through every file in the current working directory.

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row.)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
    csvFileObj.close()
    # Write out the CSV file.
    csvFileObj = open(os.path.join(
        'headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
