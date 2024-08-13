# Excel Workbook Manipulation Script

## Overview

This Python script demonstrates how to work with Excel files using the `openpyxl` library. It covers various operations, including loading workbooks, accessing sheets and cells, retrieving and modifying data, and saving changes to a new file.

## Requirements

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **openpyxl**: The script uses the `openpyxl` library for Excel file manipulation. You can install it via pip:

  ```bash
  pip install openpyxl
  ```

## Script Explanation

### 1. Loading the Workbook

```python
import openpyxl

# Load the workbook from the file 'example.xlsx'
wb = openpyxl.load_workbook('example.xlsx')
```

The script begins by loading an Excel workbook (`example.xlsx`) using the `openpyxl` library.

### 2. Sheet Operations

```python
# Print all sheet names in the workbook
print("Sheet names in the workbook:", wb.sheetnames)

# Access a specific sheet by its name
sheet = wb['Sheet3']
print("Selected sheet title:", sheet.title)

# Access the active sheet (the sheet that was last opened)
another_sheet = wb.active
print("Active sheet title:", another_sheet.title)
```

- **Sheet Names:** The script prints all the sheet names in the workbook.
- **Accessing Sheets:** It accesses a specific sheet by name and the active sheet (the last opened sheet).

### 3. Row and Column Information

```python
# Print the minimum and maximum row and column indices
print("Minimum row:", another_sheet.min_row)
print("Maximum row:", another_sheet.max_row)
print("Minimum column:", another_sheet.min_column)
print("Maximum column:", another_sheet.max_column)
```

The script prints the minimum and maximum row and column indices in the active sheet.

### 4. Accessing Cell Values

```python
# Access and print the value of specific cells in the active sheet
print("Value of cell A1:", another_sheet['A1'].value)
print("Value of cell B1:", another_sheet['B1'].value)

# Access and print cell values using row and column indices
print("Value in row 1, column 1 (A1):", another_sheet.cell(row=1, column=1).value)
```

- **Specific Cells:** The script retrieves and prints the value of specific cells (`A1`, `B1`).
- **Using Indices:** It accesses cell values using row and column indices.

### 5. Column Letters and Indices

```python
from openpyxl.utils import get_column_letter, column_index_from_string

# Get and print the column letter corresponding to a column index
print("Column letter for column 1:", get_column_letter(1))

# Convert column letters to indices and vice versa
print("Column index for letter 'B':", column_index_from_string('B'))
```

The script converts column indices to letters and vice versa using `get_column_letter` and `column_index_from_string` functions.

### 6. Iterating Over Ranges

```python
# Print the values in a range of cells (A1 to C3)
print("Values in the range A1:C3:")
for row_of_cell_objects in another_sheet['A1':'C3']:
    for cell_object in row_of_cell_objects:
        print(f"Cell {cell_object.coordinate}: {cell_object.value}")
    print('--- END OF ROW ---')
```

The script iterates over a range of cells (`A1:C3`) and prints each cell's coordinates and values.

### 7. Additional Features

- **Total Rows and Columns:** The script calculates and prints the total number of rows and columns in the sheet.
- **Column and Row Values:** It prints all values in a specific column (`B`) and row (`2`).
- **Merged Cells:** The script checks if specific cells are merged and demonstrates merging and unmerging cells.
- **Writing Data:** It writes data to a cell (`C1`) and saves the changes to a new file (`modified_example.xlsx`).

```python
# Save changes to a new workbook
wb.save('modified_example.xlsx')
```

### 8. Saving the Workbook

Finally, the modified workbook is saved as `modified_example.xlsx`.

## Documentation

For more details on using the `openpyxl` library, refer to the official documentation: [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/tutorial.html).
