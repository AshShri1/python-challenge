import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empFiles = ['1','2']

empId  = []
empFirstName =[]
empLastName = []
empDOB = []
empSSN = []
empState = []
empNameSplit = []

# Loop through the employee files
for filesToCheck in empFiles:

    # Grab employee CSV
    employeeCSV = os.path.join('raw_data', 'employee_data' + filesToCheck + '.csv')

    # Open current employee CSV
    with open(employeeCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)

        for row in csvReader:
            # Append data from the row
            empId.append(row[0])

            # Split employee full name to first name and last name
            empNameSplit = row[1].split()
            empFirstName.append(empNameSplit[0])
            empLastName.append(empNameSplit[-1])

            # format DOB to mm/dd/yyyy format
            empdateformat = row[2]
            empDOB.append(empdateformat[5:7]+'/' + empdateformat[8:] + '/' + empdateformat[:4])

            # for SSN to only display last 4 digit and other digits to *
            empSSNformat = row[3]
            empSSN.append('***' + '-' + '**' + '-' + empSSNformat[7:11])

            #lookup state name to get the state code
            empStateformat = row[4]

            if empStateformat in us_state_abbrev:
                empState.append(us_state_abbrev[empStateformat])

    # Zip lists together
    cleanCSV = zip(empId, empFirstName, empLastName, empDOB, empSSN, empState)


combinedEmployeeCSV = os.path.join('raw_data', 'combined_employee_data.csv')

with open(combinedEmployeeCSV, 'w', newline="") as csvFile:

    csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file
    csvWriter.writerow(["Emp Id", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write the zipped lists to a csv
    csvWriter.writerows(cleanCSV)
