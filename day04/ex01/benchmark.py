import timeit

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

if __name__ == '__main__':
    try:
        time_l = timeit.timeit(with_loop, number = 9 * 10 ** 7)
        time_c = timeit.timeit(with_compr, number = 9 * 10 ** 7)
        time_m = timeit.timeit(with_map, number = 9 * 10 ** 7)
    except Exception:
        print("Error")
    else:
        if time_l < time_c and time_l < time_m:
            print("it is better to use a loop")
            print(f"{time_l} vs {min(time_m, time_c)} vs {max(time_m, time_c)}")
        elif time_c < time_l and time_c < time_m:
            print("it is better to use a list comprehension")
            print(f"{time_c} vs {min(time_m, time_l)} vs {max(time_m, time_l)}")
        else:
            print("it is better to use a map")
            print(f"{time_m} vs {min(time_c, time_l)} vs {max(time_c, time_l)}")