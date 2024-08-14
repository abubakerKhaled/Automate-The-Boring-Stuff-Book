import ezsheets

# Load an existing Google Spreadsheet using its unique ID
spreadsheet_id = "1mRtgJkgJog5_j8bW_h68XtBo6Ujo3bfdtUITa2tFlHY"
ss = ezsheets.Spreadsheet(spreadsheet_id)

# Print the title of the loaded spreadsheet
print("Spreadsheet Title:", ss.title)

# Create a new Google Spreadsheet
new_ss = ezsheets.createSpreadsheet("Created Using Ezsheets")
print("New Spreadsheet Created:", new_ss.title)

# Upload an existing Excel file to Google Sheets
uploaded_ss = ezsheets.upload("multiplication_table.xlsx")
print("Uploaded Spreadsheet Title:", uploaded_ss.title)

# (Uncomment to list all spreadsheet titles in your Google Account)
# print(ezsheets.listSpreadsheets())

"""
listSpreadsheets()
    This function returns a dictionary where the keys are spreadsheet IDs 
    and the values are the titles of each spreadsheet.
"""

# Print the unique ID of the spreadsheet (this is read-only)
print("Spreadsheet ID:", ss.spreadsheetId)

# Print the original URL of the spreadsheet (this is read-only)
print("Spreadsheet URL:", ss.url)

# Print the titles of all sheets within the spreadsheet
print("Sheet Titles:", ss.sheetTitles)

# Print the list of all Sheet objects in the spreadsheet
print("Sheets:", ss.sheets)

# Access the first sheet in the spreadsheet by its index (uncomment to use)
# first_sheet = ss[0]

# Access a sheet by its title (uncomment to use)
# students_sheet = ss["Students"]

# Delete the first sheet in the spreadsheet (uncomment to use)
# del ss[0]

# (Uncomment to check the titles of sheets after deletion)
# print("Sheet Titles After Deletion:", ss.sheetTitles)

# Refresh the spreadsheet object to match any online changes
ss.refresh()

"""
refresh()
    If the spreadsheet is modified through the Google Sheets website, 
    this function updates the Spreadsheet object to reflect those changes.
    It refreshes the Spreadsheet object's attributes and the data in the 
    Sheet objects it contains. Changes made in your script will be 
    synchronized with the online spreadsheet in real-time.
"""

# Download the spreadsheet in various formats
ss.downloadAsExcel()  # Download as Excel (.xlsx)
ss.downloadAsODS()  # Download as OpenOffice (.ods)
ss.downloadAsCSV()  # Download only the first sheet as CSV (.csv)
ss.downloadAsTSV()  # Download only the first sheet as TSV (.tsv)
ss.downloadAsPDF()  # Download as PDF (.pdf)
ss.downloadAsHTML()  # Download as a ZIP of HTML files

# Delete the spreadsheet (move it to the Trash folder)
ss.delete()

"""
delete()
    Moves the spreadsheet to the Trash folder in Google Drive.
"""

# Permanently delete the spreadsheet (use with caution)
ss.delete(permanent=True)

"""
permanent=True
    Permanently deletes the spreadsheet from Google Drive.
    Be cautious with permanent deletion, as it cannot be undone. 
    It's generally safer to avoid permanent deletion in case a bug in your 
    script accidentally deletes important spreadsheets.
"""
