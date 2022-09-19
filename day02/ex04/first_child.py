import sys
from random import randint

class Research:
    def __init__(self, path_file):
        self.path_file = path_file

    def file_reader(self, has_header = True):
        with open(self.path_file, "r") as read_file:
            lines = read_file.readlines()
        if lines[0] == '0,1\n' or lines[0] == '1,0\n':
            has_header = False
        start = int(has_header)
        if has_header == True:
            start = 1
        else:
            start = 0
        ret_list = []
        for line in range(start, len(lines)):
            ret_list.append([int(lines[line].split(",")[0]), int(lines[line].split(",")[1])])
        return (ret_list) 
    class  Calculations:
        def __init__(self, data):
            self.data = data 
            self.count = self.counts()
            self.frac = self.fractions()

        def counts(self):
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(self):
            return [(self.count[0] / (self.count[0] + self.count[1])) * 100,
                    (self.count[1] / (self.count[0] + self.count[1])) * 100]
    class Analytics(Calculations):
        def __init__(self, n_steps):
            self.n_steps = n_steps
            self.predict = self.predict_random()
            self.predict_l = self.predict_last()

        def predict_random(self):
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(self.n_steps)]

        def predict_last(self):
            return self.predict[-1]

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
        rcrch = Research(sys.argv[1])
        output = rcrch.file_reader()
        # the data from file_reader()
        print(output)
        # the counts from counts()
        elem = rcrch.Calculations(output)
        print(*elem.count)
        # the fractions from fractions()
        print(*elem.frac)
        #the list of lists from predict_random() for the 3 steps
        analyt = rcrch.Analytics(3)
        print(analyt.predict)
        # the list from predict_last()
        print(analyt.predict_l)