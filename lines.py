import sys

def main():
    check_args()

    try:
        read_file = sys.argv[1]
        with open(read_file, "r") as file:
            lines = file.readlines()

        print(count(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")

def check(line):
    if line.strip().startswith("#"):
        return True
    if line.isspace():
        return True
    return False

def count(lines):
    count = 0
    for line in lines:
        if check(line) == False:
            count += 1
    return count

def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

main()
