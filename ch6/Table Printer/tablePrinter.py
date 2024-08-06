tableData = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
]


def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))

    # assuming all columns have the same number of items
    numRows = len(tableData[0])
    
    for row in range(numRows):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end= ' ')
        print()


printTable(tableData)
