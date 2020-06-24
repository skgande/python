class ReverseOfList:
    def __init__(self):
        return


if __name__ == '__main__':
    given_list = [1, 2, 3, 4, 5]
    start = 0
    end = len(given_list)-1
    while start < end:
        temp = given_list[start]
        given_list[start] = given_list[end]
        given_list[end] = temp
        start = start+1
        end = end-1

    print(f'Reverse of list id {given_list}')
