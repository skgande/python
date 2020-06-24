class FileOperations:
    def __init__(self):
        return


if __name__ == '__main__':
    with open('C:\\Users\\gande\\PycharmProjects\\pythoncoding\\com\sunil\\resources\\test_file.txt') as file:
        file_content = file.readlines()
        for i in range(len(file_content)):
            file_name = 'C:\\Users\\gande\\PycharmProjects\\pythoncoding\\com\sunil\\resources\\out_' + str(i) + '.txt'
            with open(file_name, mode='w+') as out:
                out.write(file_content[i])
