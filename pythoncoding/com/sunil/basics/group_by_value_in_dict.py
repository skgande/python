class GroupByValueInDict:
    def __init__(self):
        return


if __name__ == '__main__':
    student_marks = {'sunil': 35, 'shravya' : 90, 'sahasra': 95, 'saharsh': 95, 'test': 90}
    result_dict = {}

    for key in student_marks:
        if student_marks[key] in result_dict:
            result_dict[student_marks[key]].append(key)
            result_dict[student_marks[key]] = result_dict[student_marks[key]]
        else:
            result_dict[student_marks[key]] = [key]

    print(f'{result_dict}')
