import os

def chech_env():
    if os.environ['VIRTUAL_ENV'].split("/")[-1] != "eheike":
        raise Exception("Uncorrect env")

if __name__ == '__main__':
    try:
        chech_env()
    except KeyError:
        print("Virtual env is not running")
    except Exception as err:
        print(err)
    else:
        os.system("pip install bs4 PyTest")   
        os.system("pip3 freeze > requirements.txt")
        os.system("pip3 freeze")

# ZIP
# tar -cf eheike.tgz eheike 

# UNZIP
# tar -xf eheike.tgz