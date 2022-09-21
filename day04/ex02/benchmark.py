import timeit
import sys

def with_loop():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails *= 5
    gm_emails = []
    for em in emails:
        if em.split("@")[1] == "gmail.com":
            gm_emails.append(em)
    return(gm_emails)

def with_compr():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails *= 5
    gm_emails = [em for em in emails if em.split("@")[1] == "gmail.com"]
    return(gm_emails)

def with_map():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails *= 5
    gm_emails = list(map(lambda em: em if (em.split("@")[1] == "gmail.com") else None, emails))
    return (gm_emails)

def with_filter():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails *= 5
    gm_emails = filter(lambda em: em if (em.split("@")[1] == "gmail.com") else None, emails)
    return (gm_emails)

def how_long(func, num):
    time = timeit.timeit(func, number = num)
    return (time)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            if sys.argv[2].isdigit() == False:
                raise Exception("Need number")
            if sys.argv[1] == "loop":
                time = how_long(with_loop, int(sys.argv[2]))
            elif sys.argv[1] == "list_comprehension":
                time = how_long(with_compr, int(sys.argv[2]))
            elif sys.argv[1] == "map":
                time = how_long(with_map, int(sys.argv[2]))
            elif sys.argv[1] == "filter":
                time = how_long(with_filter, int(sys.argv[2]))
            else:
                raise Exception("Wrong args")
            print(time)
    except Exception as err:
        print(err)