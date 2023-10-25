
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(first_group, second_group, separator=","):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    intersection_set = set(first_group).intersection(second_group)
    intersection_list = list(intersection_set)
    if intersection_list is not None:
        intersection_list.sort()
        return intersection_list
    else:
        return None


fi = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(fi)

