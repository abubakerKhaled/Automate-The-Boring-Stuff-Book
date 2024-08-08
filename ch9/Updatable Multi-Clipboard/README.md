# Multi-Clipboard (mcb.pyw)

This Python script allows you to save and load pieces of text to and from the clipboard using keywords. It provides a simple command-line interface for managing multiple clipboard entries.

## Features

- Save clipboard content with a keyword.
- Load saved clipboard content using a keyword.
- List all saved keywords.
- Delete specific or all saved keywords.

## Requirements

- Python 3.x
- `pyperclip` library

## Installation

1. Ensure you have Python 3 installed on your machine.
2. Install the `pyperclip` library:

   ```sh
   pip install pyperclip
   ```

## Usage

### Saving Clipboard Content

To save the current clipboard content with a keyword:

```sh
python mcb.pyw save <keyword>
```

### Loading Clipboard Content

To load the content saved with a specific keyword to the clipboard:

```sh
python mcb.pyw <keyword>
```

### Listing All Keywords

To copy a list of all saved keywords to the clipboard:

```sh
python mcb.pyw list
```

### Deleting Clipboard Content

To delete the content saved with a specific keyword:

```sh
python mcb.pyw delete <keyword>
```

To delete all saved clipboard content:

```sh
python mcb.pyw delete
```

## Code Explanation

### Importing Libraries

```python
import shelve, pyperclip, sys
```

- `shelve`: Used for persistent storage of clipboard content.
- `pyperclip`: Used to interact with the clipboard.
- `sys`: Used to handle command-line arguments.

### Main Logic

1. **Open Shelve**: Opens a shelve file named `mbc` for storing clipboard content.
   
   ```python
   mbcshelve = shelve.open('mbc')
   ```

2. **Saving Clipboard Content**: Checks if the first argument is `save` and saves the current clipboard content under the provided keyword.
   
   ```python
   if len(sys.argv) > 3:
       if sys.argv[1].lower() == 'save':
           mbcshelve[sys.argv[2]] = pyperclip.paste()
       elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mbcshelve:
           del mbcshelve[sys.argv[2]]
   ```

3. **Loading and Listing**: If only one argument is provided, it either lists all keywords, deletes all content, or loads the content for the provided keyword.
   
   ```python
   elif len(sys.argv) == 2:
       if sys.argv[1].lower() == 'list':
           pyperclip.copy(str(list(mbcshelve.keys())))
       elif sys.argv[1].lower() == 'delete':
           mbcshelve.clear()
       elif sys.argv[1] in mbcshelve:
           pyperclip.copy(mbcshelve[sys.argv[1]])
   ```

4. **Close Shelve**: Closes the shelve file.
   
   ```python
   mbcshelve.close()
   ```

## Areas for Improvement

1. **Error Handling**: Improve error handling for invalid commands or missing arguments.
2. **Case Insensitivity**: Ensure all commands and keywords are case-insensitive.
3. **GUI**: Create a graphical user interface for easier use.
4. **Security**: Encrypt stored clipboard content for added security.
5. **Documentation**: Add more detailed comments and documentation within the code.