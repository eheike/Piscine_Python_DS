import sys
import os

class Research:
    def __init__(self, path_file):
        self.path_file = path_file

    def file_reader(self):
            with open(self.path_file, "r") as read_file:   
                return(read_file.read())  

def check_file():
    if len(sys.argv) != 2:
        raise Exception("Wrong number of args")
    try:
        with open(sys.argv[1], "r") as read_file:
            line = read_file.readlines()
    except FileNotFoundError:
        raise Exception("File not found")
    except Exception:
        raise Exception("Read error")
    else:
        if len(line) < 2 or len(line[0].split(',')) !=2:
            raise Exception("Error argument")
        for i in range(1, len(line) - 1):
            if line[i] != '0,1\n' and line[i] != '1,0\n':
                raise Exception("Error argument")


if __name__ == '__main__':
    try:
        check_file()
    except Exception as err:
        print(err)
    else:
        print(Research(sys.argv[1]).file_reader())