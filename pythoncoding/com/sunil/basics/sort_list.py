class SortList:
    def __init__(self):
        return


if __name__ == '__main__':
    given_list = [3, 8, 1, 6, 2, 5]
    for i in range(len(given_list)):
        for j in range(i+1, len(given_list)):
            if given_list[i] > given_list[j]:
                temp = given_list[i]
                given_list[i] = given_list[j]
                given_list[j] = temp

    print(f'Sorted list is {given_list}')
