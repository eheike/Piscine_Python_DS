import timeit
import random
from collections import Counter

def list_gener():
    big_list = [random.randint(0,100) for i in range(10 ** 6)]
    return (big_list)

def my_counter(lisst):
    d = {}
    for i in lisst:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    return (d)

def my_counter_top(lisst):
	my_dict = my_counter(lisst)
	sort_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
	top_list = sort_list[:10]
	top_dict = dict((x, y) for x, y in top_list)
	return (top_dict)

def your_counter(lst):
	return dict(Counter(lst))

def your_counter_top(lst):
	return Counter(lst).most_common(10)

def how_long(func_name, lst):
	times = timeit.timeit(lambda: func_name(lst), number = 1)
	return times


if __name__ == '__main__':
    try:
        print('my function:', how_long(my_counter, list_gener()))
        print('Counter:', how_long(your_counter, list_gener()))
        print('my top:', how_long(my_counter_top, list_gener()))
        print('Counter\'s top:', how_long(your_counter_top, list_gener()))
    except Exception:
	    print('Error')