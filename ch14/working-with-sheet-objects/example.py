import ezsheets

# Load an existing Google Spreadsheet using its unique ID
spreadsheet_id = "1mRtgJkgJog5_j8bW_h68XtBo6Ujo3bfdtUITa2tFlHY"
ss = ezsheets.Spreadsheet(spreadsheet_id)

# Print all the Sheet objects in the spreadsheet as a tuple
print("Sheets in Spreadsheet:", ss.sheets)

"""
The `sheets` attribute returns a tuple of Sheet objects in the order 
they appear in the spreadsheet. Each Sheet object represents an individual 
sheet within the Google Spreadsheet.
"""

# Print a tuple of all sheet titles in the spreadsheet
print("Sheet Titles:", ss.sheetTitles)

# Convert a cell address from 'A2' to (row, column) format and back
print(ezsheets.convertAddress("A2"))  # Converts 'A2' to (1, 2)
print(ezsheets.convertAddress(1, 2))  # Converts (1, 2) back to 'A2'

# Convert between column letters and numbers
print(ezsheets.getColumnLetterOf(2))  # Converts column number 2 to 'B'
print(ezsheets.getColumnNumberOf("B"))  # Converts column letter 'B' to 2
print(ezsheets.getColumnLetterOf(999))  # Converts column number 999 to 'ALK'
print(ezsheets.getColumnNumberOf("ZZZ"))  # Converts column letter 'ZZZ' to number

# Upload an Excel file to Google Sheets and get the first sheet
ss = ezsheets.upload("produceSales.xlsx")
sheet = ss[0]

# Print the first row and first column of the sheet
print("First Row:", sheet.getRow(1))
print("First Column:", sheet.getColumn(1))

# Retrieve and display data from the second row
print("Second Row:", sheet.getRow(2))

# Retrieve and display data from the third row
print("Third Row:", sheet.getRow(3))

# Update the third row with new data
sheet.updateRow(3, ["Pumpkin", "11.50", "20", "230"])
print("Updated Third Row:", sheet.getRow(3))

# Convert the first column to uppercase and update the sheet
columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    columnOne[i] = value.upper()
sheet.updateColumn(1, columnOne)

"""
The updateColumn() method updates the entire column in one request.
It's more efficient than updating cells individually, especially when
modifying large amounts of data.
"""

# Display the number of rows and columns in the sheet
print("Number of Rows:", sheet.rowCount)
print("Number of Columns:", sheet.columnCount)

# Change the number of columns to 4
sheet.columnCount = 4
print("New Number of Columns:", sheet.columnCount)

# Create new sheets at different positions within the spreadsheet
ss.createSheet("Spam")  # Adds 'Spam' at the end
ss.createSheet("Eggs")  # Adds 'Eggs' at the end
print("Sheet Titles After Adding 'Spam' and 'Eggs':", ss.sheetTitles)

ss.createSheet("Bacon", 0)  # Adds 'Bacon' at index 0
print("Sheet Titles After Adding 'Bacon':", ss.sheetTitles)

# Delete sheets by index and title
ss[0].delete()  # Deletes the first sheet ('Bacon')
print("Sheet Titles After Deleting 'Bacon':", ss.sheetTitles)

ss["Spam"].delete()  # Deletes the 'Spam' sheet
print("Sheet Titles After Deleting 'Spam':", ss.sheetTitles)

# Assign a variable to the 'Eggs' sheet and delete it
sheet = ss["Eggs"]
sheet.delete()
print("Sheet Titles After Deleting 'Eggs':", ss.sheetTitles)

# Clear all cells on the first sheet (Sheet1)
ss[0].clear()
print("Sheet Titles After Clearing 'Sheet1':", ss.sheetTitles)
"""
The clear() method removes all data from the sheet but leaves the sheet intact.
This is useful when you want to reset the sheet's contents without deleting it.
"""

# Create two new spreadsheets and copy a sheet from one to the other
ss1 = ezsheets.createSpreadsheet("First Spreadsheet")
ss2 = ezsheets.createSpreadsheet("Second Spreadsheet")

# Update the first row in the first sheet of the first spreadsheet
ss1[0].updateRow(1, ["Some", "data", "in", "the", "first", "row"])

# Copy the first sheet from ss1 to ss2
ss1[0].copyTo(ss2)
print("Sheet Titles in 'Second Spreadsheet' After Copy:", ss2.sheetTitles)

"""
The copyTo() method copies a sheet from one spreadsheet to another.
This is useful for duplicating data or templates across different spreadsheets.
"""
