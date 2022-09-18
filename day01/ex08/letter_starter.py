import sys
def let_start():
    with open("employees.tsv", "r") as names_read:
        names = names_read.readlines()
        need_name = ""
        for i in range(len(names)):
            if names[i].split('\t')[2] == sys.argv[1]+"\n":
                need_name = names[i].split('\t')[0]
        if need_name == "":
            raise Exception("Email not found")
        print(f"Dear {need_name}, welcome to our team. We are sure that it will be a pleasure to work with you. That's a precondition for the professionals that our company hires.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        let_start()
    else:
        raise Exception("Arg error")