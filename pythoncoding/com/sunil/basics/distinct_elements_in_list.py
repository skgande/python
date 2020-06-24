class DistinctElementsInList:
    def __init__(self):
        return


if __name__ == '__main__':
    given_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 3, 3, 4, 5]
    distinct_ele = set()

    for i in given_list:
        distinct_ele.add(i)

    print(distinct_ele)
