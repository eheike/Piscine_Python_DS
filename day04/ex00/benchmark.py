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

if __name__ == '__main__':
    try:
        time_l = timeit.timeit(with_loop, number = 9 * 10 ** 6)
        time_c = timeit.timeit(with_compr, number = 9 * 10 ** 6)
    except Exception:
        print("Error")

    if time_l < time_c:
        print("it is better to use a loop")
    else:
        print("it is better to use a list comprehension")
    print(f"{min(time_l, time_c)} vs {max(time_l, time_c)}")
    
