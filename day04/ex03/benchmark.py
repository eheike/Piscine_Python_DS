import timeit
import sys
from functools import reduce

class My_class:
    def __init__(self, number, num_of_calls):
        self.number = number
        self.num_of_calls = num_of_calls

    def with_loop(self):
        sum = 0
        for i in range(1, self.number + 1):
            sum = sum + i*i
        return (sum)

    def with_reduce(self):
        sum_square = reduce(lambda x, y: x + y**2, range(1, self.number + 1))
        return (sum_square)

    def how_long(self, func):
        time = timeit.timeit(func, number = self.num_of_calls)
        return (time)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 4:
            if sys.argv[2].isdigit() == False or sys.argv[3].isdigit() == False:
                raise Exception("Need numbers")
            times = My_class(int(sys.argv[3]), int(sys.argv[2]))
            if sys.argv[1] == "loop":
                time = times.how_long(times.with_loop)
            elif sys.argv[1] == "reduce":
                time = times.how_long(times.with_reduce)
            else:
                raise Exception("Wrong args")
            print(time)
    except Exception as err:
        print(err)