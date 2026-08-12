import os

FILE_PATH = os.path.join("Day4", "text.txt")

def create_file():
    with open(FILE_PATH, "w") as file:
        file.write("Hello World!\nWelcome to File Handling in Python.\n")
    print(" File created and initial data written.")

def read_file():
    print("\nReading File Contents")
    with open(FILE_PATH, "r") as file:
        contents = file.read()
        print(contents.strip())

def append_to_file():
    with open(FILE_PATH, "a") as file:
        file.write("So, how you doin'?\nHave fun practicing Python!\n")
    print("\nAppended new data to file.")

def line_count():
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        print(f"\n Total line count: {len(lines)}")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
    line_count()
