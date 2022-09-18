import sys

def caesar(code, my_string, n):
    if code == 'decode':
        n *= -1
    new_string = ''
    alph_low = 'abcdefghijklmnopqrstuvwxyz'
    alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(my_string)):
        if my_string[i] in alph_low:
            m = alph_low.find(my_string[i])
            new_string += alph_low[(n + m) % len(alph_low)]
        elif my_string[i] in alph_up:
            m = alph_up.find(my_string[i])
            new_string += alph_up[(n + m) % len(alph_up)]
        else:
            new_string += my_string[i]

    print(new_string)

if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception("Error argument")
    if not sys.argv[2].isascii():
        raise Exception("Error of string")
    try:
        n_shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Error of shift")
    caesar(sys.argv[1], sys.argv[2], n_shift)