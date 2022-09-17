def dict_print(new_dict):
    for key, value in new_dict.items():
        for i in range(len(value)):
            print (f"'{key}' :", f"'{new_dict[key][i]}'")
def to_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    my_dict = dict(list_of_tuples)
    new_dict = {}
    for value in my_dict.values(): new_dict[value] = list() 
    for key in my_dict.keys():
        new_dict.setdefault(my_dict[key], []).append(key)
    dict_print(new_dict)

if __name__ == '__main__':
    to_dict()