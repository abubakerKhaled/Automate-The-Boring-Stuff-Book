# Update Produce - Corrects Costs in Produce Sales Spreadsheet

## Overview

The `update_produce` script is designed to update the prices of certain produce items in an Excel spreadsheet named `produceSales.xlsx`. It loads the workbook, updates the prices for specific produce types, and saves the modified workbook as `updatedProduceSales.xlsx`.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **openpyxl**: This script uses the `openpyxl` library to manipulate Excel files. You can install it via pip:

  ```bash
  pip install openpyxl
  ```

## Script Explanation

1. **Loading the Workbook**

   ```python
   import openpyxl

   print('Loading Workbook...')
   wb = openpyxl.load_workbook("produceSales.xlsx")
   ```

   The script begins by loading the Excel workbook named `produceSales.xlsx`.

2. **Renaming and Accessing the Sheet**

   ```python
   wb['Sheet'].title = "ProduceSales" 
   sheet = wb['ProduceSales']
   ```

   It renames the default sheet to "ProduceSales" and accesses it for updating.

3. **Defining Price Updates**

   ```python
   PRICE_UPDATES = {"Garlic": 3.07, "Celery": 1.19, "Lemon": 1.27}
   ```

   The script defines a dictionary with the produce types and their updated prices.

4. **Updating Prices**

   ```python
   for row_num in range(2, sheet.max_row):
       produce_name = sheet.cell(row=row_num, column=1).value
       if produce_name in PRICE_UPDATES:
           sheet.cell(row=row_num, column=2).value = PRICE_UPDATES[produce_name]
   ```

   It loops through the rows of the sheet, updates the prices based on the dictionary, and saves the changes.

5. **Saving the Updated Workbook**

   ```python
   wb.save("updatedProduceSales.xlsx")
   ```

   Finally, the modified workbook is saved with the filename `updatedProduceSales.xlsx`.

## Suggestions for Improvement

1. **Error Handling**: Add error handling to manage cases where the file `produceSales.xlsx` does not exist or cannot be read.

2. **Dynamic Sheet Selection**: Instead of hardcoding the sheet name, make the script capable of selecting a sheet dynamically based on user input or configuration.

3. **File Path Flexibility**: Allow the input and output file paths to be specified as command-line arguments or through configuration files, enhancing the script’s flexibility.

4. **Validation Checks**: Implement validation checks to ensure that the sheet has the expected structure and data types before attempting to update prices.

5. **Logging**: Add logging functionality to track the script’s progress and any issues encountered during execution.

6. **User Feedback**: Provide more detailed user feedback, such as which prices were updated and which produce types were not found in the spreadsheet.

By incorporating these suggestions, the script can become more robust, flexible, and user-friendly.