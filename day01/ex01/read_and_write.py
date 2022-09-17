def read_and_write():
    with open ("ds.csv", "r") as input_file:
        with open ("ds.tsv", "w") as output_file:
            data = input_file.read()
            data = data.replace('\",\"', '\"\t\"')
            data = data.replace('false,', 'false\t').replace('true,', 'true\t')
            data = data.replace(',false', '\tfalse').replace(',true', '\ttrue')
            output_file.write(data)
if __name__ == '__main__':
    read_and_write()