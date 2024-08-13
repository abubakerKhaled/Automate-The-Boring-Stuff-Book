# Census Data Tabulator

## Overview

`read_census_Excel.py` is a Python script that processes census data from an Excel file (`censuspopdata.xlsx`) and generates a summary of the population and the number of census tracts for each county in the United States. The processed data is then saved as a Python dictionary in a new file (`census2010.py`).

## Features

- **Excel File Processing:** The script reads and processes data from an Excel spreadsheet containing census information.
- **Population and Tract Counting:** It calculates the total population and the number of census tracts for each county within a state.
- **Data Output:** The resulting data is formatted and written to a Python file (`census2010.py`) as a dictionary for further analysis or usage.

## Requirements

- **Python 3.x**: Ensure that Python 3.x is installed on your system.
- **openpyxl**: This package is required to read and process Excel files. You can install it using pip:
  ```bash
  pip install openpyxl
  ```

## Usage

### Command-Line Execution

1. Place the `censuspopdata.xlsx` file in the same directory as the script.
2. Run the script using the following command:

```bash
python read_census_Excel.py
```

### Output

- The script will process the Excel file and generate a summary of the population and census tracts for each county.
- The results will be saved in a file named `census2010.py` as a dictionary called `allData`.

### Example Output Structure

The `census2010.py` file will contain a dictionary with the following structure:

```python
allData = {
    'State1': {
        'County1': {'tracts': number_of_tracts, 'pop': population},
        'County2': {'tracts': number_of_tracts, 'pop': population},
        # ...
    },
    'State2': {
        'County3': {'tracts': number_of_tracts, 'pop': population},
        # ...
    },
    # ...
}
```

### Sample Data

For example, after running the script, `census2010.py` might contain data like:

```python
allData = {
    'California': {
        'Los Angeles': {'tracts': 234, 'pop': 9818605},
        'San Francisco': {'tracts': 45, 'pop': 805235},
    },
    'Texas': {
        'Harris': {'tracts': 130, 'pop': 4092459},
        'Dallas': {'tracts': 93, 'pop': 2368139},
    }
}
```

## Error Handling

- The script assumes that the `censuspopdata.xlsx` file exists and is formatted correctly with specific columns:
  - Column B: State
  - Column C: County
  - Column D: Population
- If the file is missing or the structure is incorrect, the script will raise an error.

## Customization

- **Input File:** You can modify the script to read from a different Excel file by changing the file name in the script.
- **Output File:** You can change the name of the output file by modifying the `result_file = open("census2010.py", 'w')` line.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the script as needed.
