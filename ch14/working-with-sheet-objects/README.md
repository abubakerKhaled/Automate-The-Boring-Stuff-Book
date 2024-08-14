# Google Sheets Operations with EZSheets

## Overview

This Python script demonstrates various operations you can perform on Google Sheets using the EZSheets library. The script covers tasks such as loading existing spreadsheets, uploading Excel files, manipulating rows and columns, creating and deleting sheets, and copying sheets between spreadsheets.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x**: Ensure Python is installed on your machine.
2. **EZSheets Library**: Install the EZSheets library using pip:
   ```bash
   pip install ezsheets
   ```
3. **Google API Credentials**: Set up the necessary credentials for accessing Google Sheets. Refer to the [Setting Up Google Sheets and Drive API for EZSheets] guide if needed.

## Script Features

### 1. Load an Existing Google Spreadsheet

The script begins by loading an existing Google Spreadsheet using its unique ID:
```python
spreadsheet_id = "1mRtgJkgJog5_j8bW_h68XtBo6Ujo3bfdtUITa2tFlHY"
ss = ezsheets.Spreadsheet(spreadsheet_id)
```

### 2. List Sheets and Titles

It then prints out all the Sheet objects and their titles:
```python
print("Sheets in Spreadsheet:", ss.sheets)
print("Sheet Titles:", ss.sheetTitles)
```

### 3. Cell Address and Column Conversion

The script demonstrates how to convert between cell addresses and row/column formats, as well as between column letters and numbers:
```python
print(ezsheets.convertAddress('A2'))  # Converts 'A2' to (1, 2)
print(ezsheets.getColumnLetterOf(2))  # Converts column number 2 to 'B'
```

### 4. Upload an Excel File to Google Sheets

The script uploads an Excel file (`produceSales.xlsx`) to Google Sheets and accesses the first sheet:
```python
ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
```

### 5. Retrieve and Update Data

The script shows how to retrieve data from rows and columns, as well as how to update them:
```python
print("First Row:", sheet.getRow(1))
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
```

### 6. Modify Columns

The first column's values are converted to uppercase and updated:
```python
columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    columnOne[i] = value.upper()
sheet.updateColumn(1, columnOne)
```

### 7. Adjust Row and Column Counts

The number of columns is modified, and the script demonstrates how to change the column count:
```python
sheet.columnCount = 4
print("New Number of Columns:", sheet.columnCount)
```

### 8. Create and Delete Sheets

The script adds new sheets at specific positions, then deletes sheets by index and title:
```python
ss.createSheet('Spam')  # Adds 'Spam' at the end
ss.createSheet('Bacon', 0)  # Adds 'Bacon' at index 0
ss[0].delete()  # Deletes the first sheet ('Bacon')
```

### 9. Clear a Sheet

The first sheet's data is cleared without deleting the sheet:
```python
ss[0].clear()
```

### 10. Copy Sheets Between Spreadsheets

The script demonstrates copying a sheet from one spreadsheet to another:
```python
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
ss1[0].copyTo(ss2)
```

## Usage

1. **Run the Script**: Execute the script in your Python environment:
   ```bash
   python your_script_name.py
   ```
2. **Modify as Needed**: Customize the script by uncommenting or editing sections based on your specific use case.

## Caution

- **Data Manipulation**: Be cautious when using functions like `delete()` and `clear()`, as they can remove data from your sheets.

## Conclusion

This script provides a comprehensive guide to performing various operations on Google Sheets using the EZSheets library. It’s a useful tool for automating tasks and managing data within your Google Spreadsheets efficiently.
