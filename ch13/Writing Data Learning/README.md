# Excel Workbook Creation and Manipulation Script

## Overview

This Python script demonstrates how to create and manipulate Excel workbooks using the `openpyxl` library. It covers tasks such as creating and renaming sheets, adding and deleting sheets, writing data to cells, and advanced features like changing tab colors and freezing panes.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **openpyxl**: The script uses the `openpyxl` library. You can install it via pip:

  ```bash
  pip install openpyxl
  ```

## Script Explanation

### 1. Creating and Initializing the Workbook

```python
import openpyxl

# Creating a new Excel workbook
wb = openpyxl.Workbook()

# Print the default sheet names in the workbook (usually, there's one default sheet)
print("Initial sheet names:", wb.sheetnames)
```

The script begins by creating a new Excel workbook and printing the default sheet names. Initially, the workbook contains one default sheet.

### 2. Accessing and Renaming the Active Sheet

```python
# Access the active sheet (the sheet that is currently open)
sheet = wb.active
print("Active sheet title:", sheet.title)

# Rename the active sheet
sheet.title = "Spam Bacon Eggs Sheet"
print("Renamed active sheet title:", sheet.title)
```

It accesses the active sheet and renames it to "Spam Bacon Eggs Sheet."

### 3. Adding and Deleting Sheets

```python
# Create a new sheet at the first index (position 0) with a custom title
wb.create_sheet(title="First Index", index=0)
print("Sheet names after adding a new sheet at index 0:", wb.sheetnames)

# Create a new sheet at the end (default behavior when no index is specified)
wb.create_sheet()
print("Sheet names after adding a new sheet at the end:", wb.sheetnames)

# Delete the sheet named 'Sheet' (the default sheet if it still exists)
del wb["Sheet"]
print("Sheet names after deleting the default 'Sheet':", wb.sheetnames)
```

The script demonstrates how to create new sheets at specific positions and delete a sheet by name.

### 4. Writing Data to Cells

```python
# Create a new sheet again with the default name 'Sheet'
wb.create_sheet()
sheet = wb["Sheet"]

# Write a value to cell A1 in the newly created sheet
sheet["A1"] = "Hello, Excel"
print("Value in cell A1 of the new 'Sheet':", sheet["A1"].value)
```

It writes a value ("Hello, Excel") to cell `A1` in the newly created sheet named "Sheet."

### 5. Additional Features

#### Changing the Tab Color

```python
# 1. Changing the tab color of a sheet
sheet.title = "Colored Tab Sheet"
sheet.sheet_properties.tabColor = "1072BA"  # Set tab color to a shade of blue
print(f"The tab color of '{sheet.title}' sheet has been changed.")
```

The script changes the tab color of the sheet to a shade of blue.

#### Adding a Formula

```python
# 2. Adding a formula to a cell
sheet["B1"] = "=SUM(A1:A10)"
print(f"Formula in cell B1: {sheet['B1'].value}")
```

It adds a formula (`=SUM(A1:A10)`) to cell `B1`.

#### Merging and Unmerging Cells

```python
# 3. Merging and unmerging cells
sheet.merge_cells('C1:D1')  # Merge cells from C1 to D1
sheet["C1"] = "Merged Cells"
print(f"Value in merged cells C1:D1: {sheet['C1'].value}")

sheet.unmerge_cells('C1:D1')  # Unmerge the cells
print("Cells C1:D1 have been unmerged.")
```

The script demonstrates merging cells from `C1` to `D1` and then unmerging them.

#### Adjusting Column Width and Row Height

```python
# 4. Adjusting column width and row height
sheet.column_dimensions['A'].width = 20  # Set the width of column A
sheet.row_dimensions[1].height = 40  # Set the height of row 1
print("Column width and row height adjusted for column A and row 1.")
```

It adjusts the width of column `A` and the height of row `1`.

#### Freezing Panes

```python
# 5. Freezing panes
sheet.freeze_panes = 'B2'  # Freeze the pane at B2 (top row and first column will be frozen)
print(f"Pane frozen at {sheet.freeze_panes}.")
```

The script freezes the pane at cell `B2`, keeping the top row and first column visible while scrolling.

### 6. Saving the Workbook

```python
# Save the workbook to a file named 'writing_learning.xlsx'
wb.save('writing_learning.xlsx')

# Save changes to a new workbook
wb.save('writing_learning_extended.xlsx')
```

Finally, the workbook is saved to two different files: `writing_learning.xlsx` and `writing_learning_extended.xlsx` to preserve the modifications made during the script execution.

## Documentation

For more information on using the `openpyxl` library, refer to the official documentation: [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/tutorial.html).