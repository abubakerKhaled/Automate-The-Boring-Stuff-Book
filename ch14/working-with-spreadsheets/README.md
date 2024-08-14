# Google Sheets Automation with EZSheets

## Overview

This Python script demonstrates how to interact with Google Sheets using the EZSheets library. It covers basic operations such as loading existing spreadsheets, creating new ones, uploading Excel files, accessing and modifying sheets, and downloading spreadsheets in various formats. The script also includes functionality to delete spreadsheets, both temporarily (moving to Trash) and permanently.

## Prerequisites

Before running this script, ensure that you have the following:

1. **Python 3.x**: Make sure you have Python installed on your machine.
2. **EZSheets Library**: Install the EZSheets library using pip if you haven't already:
   ```bash
   pip install ezsheets
   ```
3. **Google API Credentials**: Obtain the necessary credentials for accessing Google Sheets via EZSheets. Refer to the [Setting Up Google Sheets and Drive API for EZSheets](README.md) guide.

## Script Features

### 1. Load an Existing Google Spreadsheet

The script begins by loading an existing Google Spreadsheet using its unique spreadsheet ID:
```python
spreadsheet_id = "1mRtgJkgJog5_j8bW_h68XtBo6Ujo3bfdtUITa2tFlHY"
ss = ezsheets.Spreadsheet(spreadsheet_id)
print("Spreadsheet Title:", ss.title)
```

### 2. Create a New Google Spreadsheet

A new Google Spreadsheet is created with a specified title:
```python
new_ss = ezsheets.createSpreadsheet('Created Using Ezsheets')
print("New Spreadsheet Created:", new_ss.title)
```

### 3. Upload an Existing Excel File to Google Sheets

The script demonstrates how to upload an existing Excel file (`multiplication_table.xlsx`) to Google Sheets:
```python
uploaded_ss = ezsheets.upload("multiplication_table.xlsx")
print("Uploaded Spreadsheet Title:", uploaded_ss.title)
```

### 4. Accessing Spreadsheet Properties

The script prints various properties of the spreadsheet:
- **Spreadsheet ID**: The unique identifier for the spreadsheet.
- **Spreadsheet URL**: The original URL to access the spreadsheet online.
- **Sheet Titles**: Titles of all sheets within the spreadsheet.
- **Sheets**: List of all `Sheet` objects in the spreadsheet.

### 5. Working with Sheets

The script includes commented-out sections demonstrating how to:
- Access a sheet by its index or title.
- Delete a sheet by its index.

### 6. Refresh the Spreadsheet Object

The `refresh()` method is used to synchronize the Spreadsheet object with any changes made online through the Google Sheets website:
```python
ss.refresh()
```

### 7. Download the Spreadsheet in Various Formats

The script provides options to download the spreadsheet in multiple formats:
- Excel (`.xlsx`)
- OpenOffice (`.ods`)
- CSV (`.csv`)
- TSV (`.tsv`)
- PDF (`.pdf`)
- HTML (as a ZIP of HTML files)

### 8. Delete the Spreadsheet

The script includes two options for deleting the spreadsheet:
- **Move to Trash**: Temporarily deletes the spreadsheet by moving it to the Trash folder in Google Drive.
- **Permanent Deletion**: Permanently deletes the spreadsheet from Google Drive. Use with caution as this action is irreversible.

## Usage

1. **Run the Script**: Execute the script in your Python environment:
   ```bash
   python your_script_name.py
   ```
2. **Modify as Needed**: Uncomment and modify sections as per your use case.

## Caution

- **Permanent Deletion**: Be extremely careful when using the `permanent=True` flag with the `delete()` method. This will permanently delete the spreadsheet from your Google Drive, and the action cannot be undone.

## Conclusion

This script serves as a comprehensive guide to managing Google Sheets using the EZSheets library. Customize it to fit your specific needs and be mindful of the permanent deletion feature to avoid accidental loss of important data.
