class SearchInList:
    def __init__(self):
        return


if __name__ == '__main__':
    given_list = [1, 2, 3, 4, 5]
    element = 3
    is_found = False

    for i in range(len(given_list)):
        if given_list[i] == element:
            is_found = True
            break

    if is_found:
        print(f'Element {element} found in the {given_list}')
    else:
        print(f'Element {element} not found in the {given_list}')
