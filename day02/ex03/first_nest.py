import sys

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
        def counts(ret_list):
            heads = 0
            tails = 0
            for i in range(len(ret_list)):
                if ret_list[i][0] == 1:
                    heads += 1
                else:
                    tails += 1
            return([heads, tails])

        def fractions(heads, tails):
            return(heads / (heads+tails) * 100, tails / (heads+tails) * 100)


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
        list_of_lists = (Research(sys.argv[1]).file_reader())
        print(list_of_lists)
        list_c = Research.Calculations.counts(list_of_lists)
        print(*list_c)
        list_f = Research.Calculations.fractions(list_c[0], list_c[1])
        print(*list_f)