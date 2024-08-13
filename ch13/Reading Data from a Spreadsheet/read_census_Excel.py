#! python3
# read_census_Excel.py - Tabulates population and number of census tracts for
# each county.


import openpyxl, pprint

print('Opening Workbook...')

wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.active
country_data = {}

#  Fill in countyData with each county's population and tracts.
print('Reading rows...')

for row in range(2, sheet.max_row+1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    country_data.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    country_data[state].setdefault(country, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    country_data[state][country]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    country_data[state][country]['pop'] += int(pop)

#  Open a new text file and write the contents of countyData to it.
print('Writing results...')
result_file = open("census2010.py", 'w')
result_file.write('allData = ' + pprint.pformat(country_data))
result_file.close()
print('Done.')
