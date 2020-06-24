class IntersectionAndUnionOfLists:
    def __init__(self):
        return


if __name__ == '__main__':
    list_one = [1, 2, 3, 4, 5]
    list_two = [3, 4, 5, 6, 7]
    union_set = set()

    for i in range(len(list_one)):
        union_set.add(list_one[i])
    for i in range(len(list_two)):
        union_set.add(list_two[i])
    print(f'Union elements of lists are {union_set}')

    common_set = set()
    for i in range(len(list_one)):
        if list_one[i] in list_two:
            common_set.add(list_one[i])

    print(f'Common elements of lists are {common_set}')
