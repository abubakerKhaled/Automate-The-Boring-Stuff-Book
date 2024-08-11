#! python3
# walk_a_directory_tree.py - Walks through files and subdirectories in a directory and performs actions on them.

import os
import sys


def walk_directory_tree(path):
    for folder_name, subfolders, filenames in os.walk(path):
        print(f"The current folder is: {folder_name}")
        ## Perform some functions if needed

        for subfolder in subfolders:
            print(f"SUBFOLDER OF {folder_name}: {subfolder}")
            ## Perform some functions if needed

        for filename in filenames:
            print(f"FILE INSIDE {folder_name}: {filename}")
            ## Perform some functions if needed

        print("")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python walk_a_directory_tree.py <path>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.isdir(path):
        print(f"The path '{path}' is not a valid directory.")
        sys.exit(1)

    walk_directory_tree(path)
