def data_types():
    a_int = 1
    b_char = 'a'
    c_float = 3.14
    d_bool = False
    e_list = [1, 2, 3]
    f_dict = {'a': 1, 'b': 2}
    g_tuple = (1, 2, 3)
    h_set = {1, 2, 3}
    print ('[%s, %s, %s, %s, %s, %s, %s, %s]' % (type(a_int).__name__, type(b_char).__name__, type(c_float).__name__, \
    type(d_bool).__name__, type(e_list).__name__, type(f_dict).__name__, type(g_tuple).__name__, type(h_set).__name__))


if __name__ == '__main__':
    data_types()