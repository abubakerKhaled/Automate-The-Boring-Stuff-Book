# Multiplication Table Generator

## Overview

The `multiplication_table` script generates a multiplication table in an Excel file using Python. The script creates or updates an Excel file named `multiplication_table.xlsx` with a multiplication table based on a user-provided number.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **openpyxl**: This script uses the `openpyxl` library for creating and manipulating Excel files. Install it using pip:

  ```bash
  pip install openpyxl
  ```

## Script Explanation

1. **User Input for Multiplication Number**

   ```python
   num = None

   while True:
       if len(sys.argv) == 2:
           num = int(sys.argv[1])
           break
       else:
           print("Enter a multiplication number: python file_name.py number")
   ```

   The script checks if a multiplication number is provided via command-line arguments. If not, it prompts the user for input.

2. **Loading or Creating the Workbook**

   ```python
   if os.path.exists("multiplication_table.xlsx"):
       wb = openpyxl.load_workbook("multiplication_table.xlsx")
   else:
       wb = openpyxl.Workbook()
   ```

   It loads an existing workbook named `multiplication_table.xlsx` if it exists; otherwise, it creates a new workbook.

3. **Accessing and Renaming the Sheet**

   ```python
   sheet = wb.active

   if sheet.title == "Sheet":
       sheet.title = "Multiplication Table"
   ```

   The script accesses the active sheet and renames it to "Multiplication Table" if it still has the default title.

4. **Formatting and Populating the Table**

   ```python
   from openpyxl.styles import Font

   head_font = Font(size=12, bold=True)
   sheet['A1'] = 'Multiplication Table'
   sheet['A1'].font = head_font
   ```

   It sets up the header with bold formatting and populates the table with the multiplication values.

   ```python
   i = 1
   for no in range(2, num + 2):
       sheet.cell(row=no, column=1).value = i
       sheet.cell(row=no, column=1).font = head_font
       sheet.cell(row=1, column=no).value = i
       sheet.cell(row=1, column=no).font = head_font
       for colNum in range(2, num + 2):
           sheet.cell(row=no, column=colNum).value = i * (colNum-1)
       i+=1
   ```

   The script populates the table with multiplication results and applies formatting to headers.

5. **Saving the Workbook**

   ```python
   wb.save("multiplication_table.xlsx")
   ```

   The workbook is saved with the filename `multiplication_table.xlsx`.

## Usage

To run the script and generate the multiplication table, use the following command:

```bash
python multiplication_table.py <number>
```

Replace `<number>` with the desired size of the multiplication table. For example, to generate a 10x10 multiplication table, use:

```bash
python multiplication_table.py 10
```

## Suggestions for Improvement

1. **Error Handling**: Add error handling to ensure the user input is a valid integer and handle cases where the file cannot be saved.

2. **Dynamic File Naming**: Allow the user to specify a filename for the output Excel file via command-line arguments or configuration.

3. **Custom Formatting**: Provide options for customizing the formatting of the table, such as font size, color, and cell borders.

4. **Additional Features**: Include options to generate different types of tables, such as addition or subtraction tables.

5. **User Feedback**: Implement user feedback to confirm successful creation and saving of the Excel file.

For more details on using `openpyxl`, refer to the [official documentation](https://openpyxl.readthedocs.io/en/stable/tutorial.html).