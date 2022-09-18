import sys
def names_ex():
    with open(sys.argv[1], "r") as mails:
        list_of_mails = mails.readlines()
    with open("employees.tsv", "w") as output:
        output.write('Name\tSurname\tE-mail\n')
        for line in range(len(list_of_mails)):
            name = list_of_mails[line].split("@")[0].split(".")[0]
            surname = list_of_mails[line].split("@")[0].split(".")[1]
            output.write(f'{name.capitalize()}\t{surname.capitalize()}\t{list_of_mails[line]}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_ex()
    else:
        raise Exception ("Wrong arg")
