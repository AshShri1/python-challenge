import os
import csv

# List of files

budgetFiles = ['1', '2']

# Set empty list variables
budgetDate = []
budgetRevenue = []



# Loop through the files
for filesToCheck in budgetFiles:

    # Grab budget CSV
    budgetCSV = os.path.join('raw_data', 'budget_data_' + filesToCheck + '.csv')

    # Open current wrestling CSV
    with open(budgetCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)

        for row in csvReader:
            # Append data from the row
            budgetDate.append(row[0])
            budgetRevenue.append(row[1])

    # Zip lists together
    cleanCSV = zip(budgetDate, budgetRevenue)



newbudgetCSV = os.path.join('raw_data', 'combined_budget_data.csv')

with open(newbudgetCSV, 'w', newline="") as csvFile:

    csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file
    csvWriter.writerow(["Date", "Revenue"])

    # Write the zipped lists to a csv
    csvWriter.writerows(cleanCSV)


