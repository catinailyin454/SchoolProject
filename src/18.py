import sys
from os import path

def find_file(directory, filename):
    if not path.isfile(directory + '/' + filename):
        raise FileNotFoundError(f"File '{filename}' not found in directory: {directory}")
    print(f"Found file: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py [directory] [filename]")
    else:
        try:
            directory = sys.argv[1]
            filename = sys.argv[2]
            find_file(directory, filename)
        except FileNotFoundError as e:
            print(e)
