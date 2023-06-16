"""
 implement a program that expects exactly one command-line argument, 
 the name (or path) of a Python file, and outputs the number of lines 
 of code in that file, excluding comments and blank lines. If the user 
 does not specify exactly one command-line argument, or if the specified 
 file’s name does not end in .py, or if the specified file does not exist, 
 the program should instead exit via sys.exit.
"""
import sys

def count_lines_of_code(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1

    return count

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        print("Error: Please specify a valid Python file.")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        num_lines = count_lines_of_code(file_path)
        print(f"The number of lines of code in '{file_path}' is: {num_lines}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
